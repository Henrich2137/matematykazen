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
    const kadr = el.querySelector('.steps-kadr');
    const kropki = [...el.querySelectorAll('.step-dot')];
    // Nazwę pliku czytamy z data-plik, NIE z currentSrc: film wzięty z pobrania
    // w tle ma src w postaci „blob:…", z którego nie wynika, który to krok
    // (app/steps.js, sekcja „POBIERANIE FILMÓW W TLE").
    const plik = video ? (video.dataset.plik || video.currentSrc || '') : '';
    return {
        licznik: el.querySelector('.step-counter').textContent.trim(),
        plik: plik.split('/').pop(),
        wstecz: /reverse/.test(plik),
        laduje: kadr.classList.contains('laduje'),
        koniec: video ? video.ended : false,
        pauza: video ? video.paused : true,
        pusty: tresc.childElementCount === 0,
        kropka: kropki.findIndex(k => k.classList.contains('biezaca')),
        czas: video ? video.currentTime : 0,
        dlugosc: video && isFinite(video.duration) ? video.duration : 0,
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
        // Duża kropka pokazuje POCZĄTEK filmu, który jest w kadrze, czyli kropkę
        // o numerze (krok - 1) w liczeniu od zera. Wyjątek tylko na ostatnim
        // kroku, gdzie po dobiegnięciu filmu głowica przechodzi na ostatnią
        // kropkę (Henrich po testach v27).
        const ostatni = nr === kropek - 1;
        if (st.kropka !== nr - 1 && !(ostatni && st.kropka === nr)) {
            naruszenia.push(`${gdzie}: licznik ${st.licznik}, a duża kropka na ${st.kropka}`);
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

// Konkretne zachowania, których losowe klikanie nie sprawdzi, bo trzeba trafić
// w dokładny stan. Wszystkie dotyczą jednej zasady: KONIEC REWERSU to ten sam
// stan co PIERWSZA KLATKA zwykłego filmu i przyciski mają reagować tak samo.
async function zachowania(browser, zadanie) {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
    await page.goto(`http://127.0.0.1:${PORT}/template.html?arkusz=${ARKUSZ}`);
    await page.waitForSelector('.exercise-container', { state: 'attached' });
    const zad = page.locator('.exercise-container').nth(zadanie + 1);
    await zad.locator('.solution-button').click();
    await zad.locator('.steps-content video').waitFor({ timeout: 15000 });

    const czekajAz = async (warunek, limit = 15000) => {
        const t0 = Date.now();
        let s = await czytajStan(zad);
        while (Date.now() - t0 < limit && !warunek(s)) { await spij(100); s = await czytajStan(zad); }
        return s;
    };
    const doKoncaCofki = () => czekajAz((s) => s.wstecz && s.plik && !s.laduje && s.koniec);
    const doSpoczynku = () => czekajAz((s) => !s.laduje);

    const zle = [];
    // Ustaw się na początku kroku 4 i cofnij cały krok 3 — na końcu cofki stoimy
    // na pierwszej klatce kroku 3.
    const ustawSie = async () => {
        await zad.locator('.step-dot').nth(3).click({ force: true });
        await doSpoczynku();
        await zad.locator('.step-prev').click({ force: true });
        return doKoncaCofki();
    };

    if (!(await ustawSie()).koniec) {
        zle.push('nie udało się doprowadzić cofki do końca — reszta zachowań niesprawdzona');
    } else {
        await zad.locator('.step-prev').click({ force: true });
        let s = await doSpoczynku();
        if (!(s.plik === 'step2reverse.mp4' && !s.pauza)) {
            zle.push(`◄ po dobiegnięciu cofki: oczekiwano cofania POPRZEDNIEGO kroku (step2reverse.mp4, gra), jest ${s.plik}${s.pauza ? ' (pauza)' : ''}`);
        }
        await ustawSie();
        await zad.locator('.step-next').click({ force: true });
        s = await doSpoczynku();
        if (!(s.plik === 'step3.mp4' && !s.wstecz && !s.pauza)) {
            zle.push(`► po dobiegnięciu cofki: oczekiwano TEGO SAMEGO kroku w przód (step3.mp4, gra), jest ${s.plik}${s.pauza ? ' (pauza)' : ''}`);
        }
    }

    // Duża kropka po obejrzeniu filmu do przodu zostaje na POCZĄTKU tego filmu,
    // a nie przeskakuje na jego koniec (Henrich po testach v27).
    await zad.locator('.step-dot').first().click({ force: true });
    await doSpoczynku();
    await zad.locator('.step-play').click({ force: true });
    const poFilmie = await czekajAz((s) => !s.laduje && !s.wstecz && s.koniec, 30000);
    if (!poFilmie.koniec) {
        zle.push('nie udało się dograć kroku 1 do końca — położenie kropki niesprawdzone');
    } else if (poFilmie.kropka !== 0) {
        zle.push(`po obejrzeniu kroku 1 duża kropka jest na ${poFilmie.kropka}, a ma zostać na 0`);
    }

    // ► w TRAKCIE cofki (jeszcze nie na końcu) ma tylko odwrócić kierunek i zostać
    // w tym samym miejscu filmu, a nie przeskoczyć do następnego kroku
    // (Henrich po testach v27). Sprawdzamy trzy rzeczy naraz: ten sam krok,
    // kierunek w przód i zbliżony czas w skali kroku.
    await zad.locator('.step-dot').nth(3).click({ force: true });
    await doSpoczynku();
    await zad.locator('.step-prev').click({ force: true });
    let wCofce = await czekajAz((s) => s.wstecz && !s.laduje && !s.pauza && s.czas > 0.2);
    if (!wCofce.wstecz || wCofce.pauza) {
        zle.push('nie udało się złapać trwającej cofki — zachowanie ► w cofce niesprawdzone');
    } else {
        const pozycjaPrzed = wCofce.dlugosc - wCofce.czas; // czas liczony od początku kroku
        await zad.locator('.step-next').click({ force: true });
        const s = await czekajAz((st) => !st.laduje && !st.wstecz && st.czas > 0);
        if (s.plik !== 'step3.mp4' || s.wstecz) {
            zle.push(`► w trakcie cofki: oczekiwano TEGO SAMEGO kroku w przód (step3.mp4), jest ${s.plik}`);
        } else if (s.pauza) {
            zle.push('► w trakcie cofki: film stanął zamiast grać dalej w przód');
        } else if (Math.abs(s.czas - pozycjaPrzed) > 1.2) {
            zle.push(`► w trakcie cofki: skok w czasie — było ${pozycjaPrzed.toFixed(2)} s, jest ${s.czas.toFixed(2)} s`);
        }
    }

    // Szybkie klikanie w jedną kropkę nie może zostawić odtwarzacza w „ładuję".
    // Porzucone elementy <video> zajmowały miejsce w puli mediów przeglądarki
    // i głodziły ten, na który czekamy (zmierzone: 5,6 s zawieszenia).
    const kropka = zad.locator('.step-dot').first();
    for (let i = 0; i < 6; i++) { await kropka.click({ force: true }); await spij(80); }
    const t0 = Date.now();
    await doSpoczynku();
    const czekanie = Date.now() - t0;
    if (czekanie > 4000) zle.push(`po serii kliknięć w kropkę odtwarzacz wracał do spoczynku ${czekanie} ms (limit 4000)`);

    await page.close();
    return zle;
}

(async () => {
    const browser = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
    let padlo = 0;

    // Zachowania sprawdzamy na zad. 1 — ma najwięcej kroków i komplet rewersów.
    const zleZachowania = await zachowania(browser, 0);
    padlo += zleZachowania.length;
    console.log(`zachowania (koniec rewersu, klikanie w kropkę): ${zleZachowania.length ? 'ŹLE' : 'ok'}`);
    zleZachowania.forEach((w) => console.log('    ' + w));

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
