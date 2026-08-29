/* Zrzut jednego rozwiązania (zwykłego, widżetu albo obu) z arkusza.
 *
 * PO CO. tools/zrzuty.js robi komplet ujęć CAŁEJ strony; przy pracy nad tekstem
 * jednego zadania trzeba widzieć samą kartę rozwiązania, w powiększeniu i bez
 * przewijania oczami po pełnej stronie.
 *
 * WYMAGA URUCHOMIONEGO SERWERA (dane idą fetchem, file:// nie działa):
 *   node tools/serwer.js 8000
 *
 * UŻYCIE (NODE_PATH obowiązkowe, patrz nagłówek tools/zrzuty.js):
 *   NODE_PATH=/usr/local/share/npm-global/lib/node_modules \
 *     node tools/zrzut-rozwiazania.js 7 8 9 --etykieta=po
 *
 * PRZEŁĄCZNIKI:
 *   --arkusz=<id>      domyślnie 2024-grudzien
 *   --port=<n>         domyślnie 8000
 *   --etykieta=<n>     katalog /tmp/zrzuty-rozw/<etykieta>/ (domyślnie „biezace")
 *   --szer=<px>        szerokość okna (domyślnie 900; 390 = telefon)
 *   --ciemny           motyw ciemny
 */

const { chromium } = require('playwright');
const fs = require('fs');

const args = process.argv.slice(2);
const flaga = (n, d) => {
    const t = args.find(a => a.startsWith(`--${n}=`));
    return t ? t.slice(n.length + 3) : d;
};
const jest = n => args.includes(`--${n}`);

const NUMERY = args.filter(a => !a.startsWith('--'));
const ARKUSZ = flaga('arkusz', '2024-grudzien');
const PORT = flaga('port', '8000');
const ETYKIETA = flaga('etykieta', 'biezace');
const SZER = parseInt(flaga('szer', '900'), 10);
const KAT = `/tmp/zrzuty-rozw/${ETYKIETA}`;

(async () => {
    if (NUMERY.length === 0) {
        console.error('podaj numery zadań, np.: node tools/zrzut-rozwiazania.js 7 9');
        process.exit(1);
    }
    fs.mkdirSync(KAT, { recursive: true });
    const browser = await chromium.launch();
    const page = await browser.newPage({ viewport: { width: SZER, height: 1000 }, deviceScaleFactor: 2 });

    if (jest('ciemny')) {
        await page.addInitScript(() => localStorage.setItem('motyw', 'ciemny'));
    }
    await page.goto(`http://127.0.0.1:${PORT}/template.html?arkusz=${ARKUSZ}`, { waitUntil: 'networkidle' });
    await page.waitForFunction(() => document.querySelectorAll('.exercise-container').length > 2);

    for (const nr of NUMERY) {
        // Pierwszy .exercise-container w DOM to pusty szablon, stąd filtr po treści.
        const karta = page.locator('.exercise-container').filter({
            has: page.locator(`.question:has-text("Zadanie ${nr}.")`),
        }).first();
        await karta.scrollIntoViewIfNeeded();
        const przycisk = karta.locator('.solution-button');
        if (await przycisk.count() === 0) { console.log(`zad ${nr}: brak rozwiązania`); continue; }
        await przycisk.click();
        await page.waitForTimeout(600);
        const plik = `${KAT}/zad${nr}.png`;
        await karta.locator('.solution-container').first().screenshot({ path: plik });
        console.log(plik);
    }
    await browser.close();
})();
