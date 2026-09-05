/* Test strzałek przy suwakach widżetów (Playwright).
 *
 * PO CO. Strzałki po bokach suwaka wstawia jedna wspólna funkcja
 * (wgDodajStrzalkiSuwakow w app/widget-helpers.js) do CZTERNASTU suwaków w
 * dziesięciu widżetach naraz. Ręczne przeklikanie wszystkich po każdej zmianie
 * nie wchodzi w grę, a dwie rzeczy popsują się cicho:
 *   - krok liczony przez dodawanie (0,05 + 0,05 + …) rozjeżdża się
 *     zmiennoprzecinkowo i po kilkunastu naciśnięciach suwak przestaje trafiać
 *     w okrągłe wartości; okiem tego nie widać,
 *   - ustawienie .value z kodu NIE wywołuje zdarzenia "input", więc widżet
 *     przestałby się przerysowywać, choć suwak wygląda na przesunięty.
 * Test pilnuje obu, plus zakresów i blokowania strzałek na końcach.
 *
 * WYMAGA URUCHOMIONEGO SERWERA (dane idą fetchem, file:// nie działa):
 *   node tools/serwer.js 8000
 *
 * UŻYCIE (NODE_PATH obowiązkowe, patrz nagłówek tools/zrzuty.js):
 *   NODE_PATH=/usr/local/share/npm-global/lib/node_modules node tools/test-suwakow.js
 *
 * PRZEŁĄCZNIKI:
 *   --arkusz=<id>   domyślnie oba: 2024-grudzien i 2026-maj
 *   --port=<n>      domyślnie 8000
 */

const { chromium } = require('playwright');

const args = process.argv.slice(2);
const flaga = (n, d) => {
    const t = args.find(a => a.startsWith(`--${n}=`));
    return t ? t.slice(n.length + 3) : d;
};
const PORT = flaga('port', '8000');
const ARKUSZE = flaga('arkusz', '') ? [flaga('arkusz', '')] : ['2024-grudzien', '2026-maj'];

let bledy = 0;
function sprawdz(warunek, opis) {
    if (warunek) {
        console.log(`  ok   ${opis}`);
    } else {
        console.log(`  BLAD ${opis}`);
        bledy++;
    }
}

(async () => {
    const browser = await chromium.launch();

    for (const arkusz of ARKUSZE) {
        console.log(`\n=== ${arkusz} ===`);
        const page = await browser.newPage({ viewport: { width: 900, height: 1000 } });
        await page.goto(`http://127.0.0.1:${PORT}/template.html?arkusz=${arkusz}`,
            { waitUntil: 'networkidle' });
        await page.waitForFunction(() => document.querySelectorAll('.exercise-container').length > 2);

        // Rozwijamy WSZYSTKIE rozwiązania naraz - widżety budują się dopiero przy
        // renderze zadania, ale są już w DOM od startu, więc wystarczy pokazać
        // kontenery. Klikanie po kolei byłoby wolniejsze i niczego nie dodaje.
        await page.evaluate(() => {
            document.querySelectorAll('.solution-container')
                .forEach(el => { el.style.display = 'block'; });
        });

        const suwaki = page.locator('.solution-interactive-container input[type=range]');
        const ile = await suwaki.count();
        console.log(`suwaków: ${ile}`);
        sprawdz(ile > 0, 'arkusz ma w ogóle jakiś suwak');

        for (let i = 0; i < ile; i++) {
            const suwak = suwaki.nth(i);
            const opis = await suwak.evaluate((s) => {
                const karta = s.closest('.exercise-container');
                const q = karta ? (karta.querySelector('.question')?.textContent || '') : '';
                return (q.match(/Zadanie [\d.]+/) || ['?'])[0];
            });
            const etykieta = `${opis} suwak ${i + 1}/${ile}`;

            // 1. Strzałki są po obu stronach, suwak stoi między nimi.
            const uklad = await suwak.evaluate((s) => {
                const g = s.parentElement;
                return {
                    grupa: g && g.classList.contains('wg-suwak-grupa'),
                    dzieci: g ? Array.from(g.children).map(el =>
                        el.tagName.toLowerCase() + '.' + (el.className.baseVal || el.className)) : []
                };
            });
            sprawdz(uklad.grupa, `${etykieta}: suwak siedzi w .wg-suwak-grupa`);
            sprawdz(uklad.dzieci.length === 3
                && uklad.dzieci[0].startsWith('button')
                && uklad.dzieci[1].startsWith('input')
                && uklad.dzieci[2].startsWith('button'),
                `${etykieta}: układ strzałka-suwak-strzałka (${uklad.dzieci.join(' ')})`);
            if (!uklad.grupa) continue;
            // Część suwaków startuje schowana pod drugą zakładką widżetu
            // (np. zad. 12.2 maja). Same strzałki są już sprawdzone wyżej,
            // a klikanie w niewidoczny przycisk tylko zawiesiłoby test.
            if (!(await suwak.isVisible())) {
                console.log(`  --   ${etykieta}: schowany pod zakładką, dalsze próby pominięte`);
                continue;
            }

            const lewo = suwak.locator('xpath=preceding-sibling::button[1]');
            const prawo = suwak.locator('xpath=following-sibling::button[1]');
            const dane = await suwak.evaluate(s => ({
                min: parseFloat(s.min), max: parseFloat(s.max),
                krok: parseFloat(s.step) || 1, start: parseFloat(s.value)
            }));

            // 2. Jedno kliknięcie = dokładnie jeden krok, w obie strony.
            const przed = await suwak.inputValue();
            await prawo.click();
            const poPrawo = parseFloat(await suwak.inputValue());
            sprawdz(Math.abs(poPrawo - (parseFloat(przed) + dane.krok)) < dane.krok * 1e-6,
                `${etykieta}: strzałka w prawo o jeden krok (${przed} → ${poPrawo})`);
            await lewo.click();
            sprawdz(await suwak.inputValue() === przed,
                `${etykieta}: strzałka w lewo wraca do ${przed}`);

            // 3. Widżet dostaje "input" - inaczej rysunek zostałby w miejscu,
            //    mimo że suwak wygląda na przesunięty.
            await suwak.evaluate((s) => {
                s.__test = 0;
                s.addEventListener('input', () => { s.__test++; });
            });
            await prawo.click();
            await lewo.click();
            sprawdz(await suwak.evaluate(s => s.__test) === 2,
                `${etykieta}: każde kliknięcie wystawia zdarzenie "input"`);

            // 4. Tam i z powrotem 20 razy wraca DOKŁADNIE do wartości startowej
            //    (pułapka zmiennoprzecinkowa przy krokach typu 0,0833333).
            await suwak.evaluate((s, v) => { s.value = String(v); }, dane.start);
            const kroki = Math.min(20, Math.floor((dane.max - dane.start) / dane.krok));
            for (let k = 0; k < kroki; k++) await prawo.click();
            for (let k = 0; k < kroki; k++) await lewo.click();
            sprawdz(parseFloat(await suwak.inputValue()) === dane.start,
                `${etykieta}: ${kroki} kroków w prawo i w lewo wraca na ${dane.start}`);

            // 5. Strzałka blokuje się na końcu zakresu i nie wypycha wartości poza.
            await suwak.evaluate((s) => { s.value = s.max; s.dispatchEvent(new Event('input', { bubbles: true })); });
            sprawdz(await prawo.isDisabled(), `${etykieta}: przy max prawa strzałka wyłączona`);
            sprawdz(!(await lewo.isDisabled()), `${etykieta}: przy max lewa strzałka działa`);
            await suwak.evaluate((s) => { s.value = s.min; s.dispatchEvent(new Event('input', { bubbles: true })); });
            sprawdz(await lewo.isDisabled(), `${etykieta}: przy min lewa strzałka wyłączona`);
            sprawdz(parseFloat(await suwak.inputValue()) === dane.min,
                `${etykieta}: wartość nie zeszła poniżej min`);

            // 6. Przytrzymanie przewija dalej niż jedno stuknięcie.
            await suwak.evaluate((s, v) => { s.value = String(v); }, dane.start);
            const pudlo = await prawo.boundingBox();
            await page.mouse.move(pudlo.x + pudlo.width / 2, pudlo.y + pudlo.height / 2);
            await page.mouse.down();
            await page.waitForTimeout(1200);
            await page.mouse.up();
            const poTrzymaniu = parseFloat(await suwak.inputValue());
            const przeszlo = Math.round((poTrzymaniu - dane.start) / dane.krok);
            const doKonca = Math.round((dane.max - dane.start) / dane.krok);
            sprawdz(przeszlo >= Math.min(5, doKonca),
                `${etykieta}: przytrzymanie 1,2 s przesunęło o ${przeszlo} kroków`);

            await suwak.evaluate((s, v) => {
                s.value = String(v);
                s.dispatchEvent(new Event('input', { bubbles: true }));
            }, dane.start);
        }
        await page.close();
    }

    await browser.close();
    console.log(bledy === 0 ? '\nWSZYSTKO OK' : `\nBŁĘDÓW: ${bledy}`);
    process.exit(bledy === 0 ? 0 : 1);
})();
