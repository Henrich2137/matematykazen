/* Test odtwarzacza „rozwiązanie krok po kroku" — losowe okładanie sterowania
 * plus niezmienniki, których okiem nie da się upilnować.
 *
 * PO CO TO JEST. Odtwarzacz ma stan (który krok, w przód czy wstecz, czy przy
 * końcu) rozłożony na kropki, licznik, pasek postępu i film w kadrze. Objawy
 * rozjazdu tego stanu są niepozorne — kropka o jedną za daleko, pasek z innego
 * filmu — i przy szybkim łączu w ogóle nie występują, bo podmiana kroku trwa
 * milisekundy. Ten skrypt klika losowo, po każdym ruchu sprawdza, czy plik
 * FAKTYCZNIE w kadrze zgadza się z licznikiem, i powtarza to przy trzech
 * prędkościach łącza.
 *
 * WYMAGA URUCHOMIONEGO tools/serwer.js (obsługa Range + dławienie):
 *
 *   node tools/serwer.js 8000 &
 *   node tools/serwer.js 8001 --wolno=1200 --bps=60000 &
 *   NODE_PATH=/usr/local/share/npm-global/lib/node_modules node tools/test-krokow.js
 *
 * NODE_PATH jest OBOWIĄZKOWE — playwright siedzi w globalnym prefiksie
 * (patrz nagłówek tools/zrzuty.js i issues/playwright-podglad.md).
 *
 * PRZEŁĄCZNIKI:
 *   --port=<n>       serwer (domyślnie 8000)
 *   --arkusz=<id>    domyślnie 2024-grudzien
 *   --zadania=0,1,2  indeksy zadań z krokami (domyślnie 0,1,2)
 *   --ruchy=<n>      kliknięć na przebieg (domyślnie 25)
 *   --ziarna=1,7     ziarna losowania — powtarzalne przebiegi (domyślnie 3,11,29)
 *
 * Kod wyjścia 1, gdy któryś niezmiennik padł albo strona rzuciła błędem.
 *
 * PUŁAPKA: pierwszy `.exercise-container` w DOM to pusty szablon — zadanie
 * o indeksie i to `.nth(i + 1)`.
 */

const { chromium } = require('playwright');

const args = process.argv.slice(2);
const flaga = (nazwa, dom) => {
    const t = args.find(a => a.startsWith(`--${nazwa}=`));
    return t ? t.slice(nazwa.length + 3) : dom;
};

const PORT = flaga('port', '8000');
const ARKUSZ = flaga('arkusz', '2024-grudzien');
const ZADANIA = flaga('zadania', '0,1,2').split(',').map(Number);
const RUCHY = Number(flaga('ruchy', 25));
const ZIARNA = flaga('ziarna', '3,11,29').split(',').map(Number);

const spij = ms => new Promise(r => setTimeout(r, ms));

// Własny generator, żeby przebieg dało się powtórzyć po numerze ziarna.
function losowanie(ziarno) {
    let s = ziarno;
    return () => (s = (s * 1103515245 + 12345) % 2147483648) / 2147483648;
}

// Cały stan odtwarzacza czytany z DOM — `ctx` z app/steps.js jest per-zadanie
// i z zewnątrz nieosiągalny, więc jedyne dostępne źródło prawdy to to, co widać.
const czytajStan = zad => zad.evaluate(el => {
    const video = el.querySelector('.steps-content video');
    const tresc = el.querySelector('.steps-content');
    return {
        licznik: el.querySelector('.step-counter').textContent.trim(),
        plik: video ? (video.currentSrc || '').split('/').pop() : '',
        wstecz: /reverse/.test(video ? video.currentSrc : ''),
        laduje: tresc.classList.contains('laduje') || tresc.classList.contains('podmiana'),
        pusty: tresc.childElementCount === 0,
    };
});

async function przebieg(browser, zadanie, ziarno) {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
    const bledy = [];
    page.on('pageerror', e => bledy.push('pageerror: ' + e.message));
    page.on('console', m => {
        // gc.zgo.at (statystyki) jest odcięty firewallem kontenera — to nie usterka strony.
        if (m.type() === 'error' && !/gc\.zgo\.at|ERR_ADDRESS_UNREACHABLE/.test(m.text())) bledy.push('console: ' + m.text());
    });
    await page.goto(`http://127.0.0.1:${PORT}/template.html?arkusz=${ARKUSZ}`);
    await page.waitForSelector('.exercise-container', { state: 'attached' });

    const zad = page.locator('.exercise-container').nth(zadanie + 1);
    await zad.locator('.solution-button').click();
    await zad.locator('.steps-content video').waitFor({ timeout: 15000 });

    const kropek = await zad.locator('.step-dot').count();
    const los = losowanie(ziarno);
    const naruszenia = [];

    // Plik w kadrze musi należeć do kroku, który pokazuje licznik. Sprawdzamy
    // tylko poza trwającą podmianą — w jej trakcie stary kadr jest z założenia
    // „nie ten" i widz ma to zasygnalizowane przygaszeniem obrazu.
    const sprawdz = (st, gdzie) => {
        if (st.laduje || !st.plik) return;
        const nr = Number(st.licznik.split('/')[0].trim());
        if (!new RegExp(`^step${nr}(reverse)?\\.mp4$`).test(st.plik)) {
            naruszenia.push(`${gdzie}: licznik ${st.licznik}, a w kadrze ${st.plik}`);
        }
        if (st.wstecz !== st.plik.includes('reverse')) {
            naruszenia.push(`${gdzie}: kierunek nie zgadza się z plikiem (${st.plik})`);
        }
    };

    for (let i = 1; i <= RUCHY; i++) {
        const r = los();
        let co;
        if (r < 0.4) { co = '◄'; await zad.locator('.step-prev').click({ force: true }); }
        else if (r < 0.7) { co = '►'; await zad.locator('.step-next').click({ force: true }); }
        else if (r < 0.85) { co = 'play'; await zad.locator('.step-play').click({ force: true }); }
        else { const k = Math.floor(los() * kropek); co = 'kropka ' + k; await zad.locator('.step-dot').nth(k).click({ force: true }); }
        await spij(Math.floor(los() * 900) + 60);
        sprawdz(await czytajStan(zad), `ruch ${i} (${co})`);
    }

    // Po ustaniu klikania odtwarzacz musi dojść do stanu spoczynku: film w kadrze,
    // zgodny z licznikiem, i żadnego wiecznego „ładuję".
    await spij(6000);
    const koniec = await czytajStan(zad);
    if (koniec.laduje) naruszenia.push('po 6 s spokoju odtwarzacz nadal się ładuje');
    if (koniec.pusty || !koniec.plik) naruszenia.push('po 6 s spokoju kadr jest pusty');
    sprawdz(koniec, 'stan spoczynku');

    await page.close();
    return { naruszenia, bledy };
}

(async () => {
    const browser = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
    let padlo = 0;
    for (const zadanie of ZADANIA) {
        for (const ziarno of ZIARNA) {
            const { naruszenia, bledy } = await przebieg(browser, zadanie, ziarno);
            const zle = naruszenia.length + bledy.length;
            padlo += zle;
            console.log(`zad ${zadanie + 1}, ziarno ${ziarno}: ${zle ? 'ŹLE' : 'ok'}`);
            [...naruszenia, ...bledy].forEach(w => console.log('    ' + w));
        }
    }
    await browser.close();
    console.log(padlo ? `\nRAZEM: ${padlo} problemów` : '\nRAZEM: bez zastrzeżeń');
    process.exit(padlo ? 1 : 0);
})();
