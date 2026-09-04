/* Test paska kropek w rozwiązaniu krok po kroku — dostępność kroków przy każdej
 * szerokości okna i ogranicznik przewijania.
 *
 * PO CO TO JEST. Pasek kropek ma dwa tryby: „wszystko widać" i „wąsko, więc
 * strzałki i przewijanie". Granica między nimi liczona jest z pomiarów układu,
 * a przy złym pomiarze powstaje MARTWA STREFA: kropki już nie mieszczą się
 * w oknie, a strzałki jeszcze się nie pokazały, więc do dalszych kroków nie ma
 * jak dojść. Zakres to raptem kilkanaście pikseli szerokości okna (Henrich
 * trafił na 310-325 px), więc ręcznym rozciąganiem okna łatwo go przegapić.
 * Drugi pilnowany niezmiennik: pasek nie może odjechać poza swoją treść, bo po
 * kilku kliknięciach strzałki w prawo kropki zostają za lewą krawędzią
 * (Henrich, Safari na iPhonie SE).
 *
 * WYMAGA URUCHOMIONEGO tools/serwer.js (obsługa Range; python -m http.server
 * NIE nadaje się, patrz CLAUDE.md):
 *
 *   node tools/serwer.js 8125 &
 *   NODE_PATH=/usr/local/share/npm-global/lib/node_modules node tools/test-paska-krokow.js --port=8125
 *
 * NODE_PATH jest OBOWIĄZKOWE — playwright siedzi w globalnym prefiksie
 * (patrz nagłówek tools/zrzuty.js i issues/playwright-podglad.md).
 *
 * PRZEŁĄCZNIKI:
 *   --port=<n>          serwer (domyślnie 8000)
 *   --arkusz=<id>       domyślnie 2024-grudzien
 *   --zadanie=<nr>      numer zadania z krokami (domyślnie 1)
 *   --szerokosci=a,b,c  szerokości okna do sprawdzenia (domyślnie 300..340 co 5
 *                       plus 360, 390, 485, 900)
 *   --klikniec=<n>      ile razy walić w strzałkę w prawo (domyślnie 12)
 *
 * SPRAWDZANE NIEZMIENNIKI:
 *   1. DOSTĘPNOŚĆ — jeżeli któraś kropka nie mieści się w oknie paska, muszą
 *      być widoczne strzałki przewijania. Inaczej martwa strefa.
 *   2. TRAFIALNOŚĆ — środek każdej widocznej kropki musi należeć do niej samej
 *      (nic jej nie zasłania), a pole dotyku kropki ma mieć co najmniej
 *      MIN_POLE px szerokości i wysokości — inaczej nie sposób trafić palcem.
 *   3. OGRANICZNIK — po wielokrotnym kliknięciu strzałki w prawo (i w lewo)
 *      scrollLeft musi zostać w przedziale [0, scrollWidth - clientWidth].
 *
 * Kod wyjścia 1, gdy któryś niezmiennik padł.
 *
 * PUŁAPKA: pierwszy `.exercise-container` w DOM to pusty szablon — zadanie
 * wybieramy filtrem po treści nagłówka, nie indeksem.
 */

const { chromium } = require('playwright');

const args = process.argv.slice(2);
const flaga = (n, d) => {
    const t = args.find(a => a.startsWith(`--${n}=`));
    return t ? t.slice(n.length + 3) : d;
};

const PORT = flaga('port', '8000');
const ARKUSZ = flaga('arkusz', '2024-grudzien');
const ZADANIE = flaga('zadanie', '1');
const SZEROKOSCI = flaga('szerokosci', '300,305,310,315,320,325,330,335,340,360,390,485,900')
    .split(',').map(Number);
const KLIKNIEC = Number(flaga('klikniec', 12));

// Minimalne pole dotyku kropki. 44 px to wytyczna dla kciuka; w poziomie
// tyle się nie zmieści bez zjedzenia liczby kropek, więc pilnujemy 30 px
// w poziomie i 44 px w pionie.
const MIN_POLE_X = 30;
const MIN_POLE_Y = 44;
// Tolerancja pomiarów układu w pikselach (zaokrąglenia subpikselowe).
const LUZ = 2;

let bledy = 0;
const zle = (t) => { bledy++; console.log(`  ✗ ${t}`); };
const dobrze = (t) => console.log(`  ✓ ${t}`);

// Zbiera z żywej strony wszystko, czego potrzebują niezmienniki.
// Pole dotyku mierzymy TRAFIENIAMI, nie prostokątem przycisku: powiększa się je
// pseudoelementem, którego getBoundingClientRect() przycisku nie widzi. Idziemy
// od środka kropki w bok i liczymy, dokąd klik wciąż w nią trafia.
const pomiar = (karta) => karta.evaluate((el) => {
    const okno = el.querySelector('.steps-dots-okno');
    const box = el.querySelector('.steps-dots');
    const lewo = el.querySelector('.steps-scroll-lewo');
    const prawo = el.querySelector('.steps-scroll-prawo');
    const ro = okno.getBoundingClientRect();
    const widoczna = (s) => s.offsetWidth > 0 && s.offsetHeight > 0;
    const kropki = [...box.querySelectorAll('.step-dot')].map((k, i) => {
        const r = k.getBoundingClientRect();
        const sx = Math.round(r.left + r.width / 2);
        const sy = Math.round(r.top + r.height / 2);
        const trafiony = document.elementFromPoint(sx, sy);
        const moja = (x, y) => {
            const e = document.elementFromPoint(x, y);
            return !!e && (e === k || k.contains(e));
        };
        const zasieg = (dx, dy) => {
            let n = 0;
            while (n < 40 && moja(sx + dx * (n + 1), sy + dy * (n + 1))) n++;
            return n;
        };
        return {
            i,
            szer: moja(sx, sy) ? zasieg(-1, 0) + zasieg(1, 0) + 1 : 0,
            wys: moja(sx, sy) ? zasieg(0, -1) + zasieg(0, 1) + 1 : 0,
            // Mieści się w oknie paska w całości?
            wOknie: r.left >= ro.left - 0.5 && r.right <= ro.right + 0.5,
            // Czy klik w środek kropki trafia w tę właśnie kropkę?
            swoj: !!trafiony && (trafiony === k || k.contains(trafiony)),
        };
    });
    return {
        strzalki: widoczna(lewo) && widoczna(prawo),
        wierszWidth: okno.parentElement.clientWidth,
        scrollLeft: okno.scrollLeft,
        scrollWidth: okno.scrollWidth,
        clientWidth: okno.clientWidth,
        trescSzer: box.scrollWidth,
        kropki,
    };
});

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage({ viewport: { width: 900, height: 1000 } });
    page.on('pageerror', (e) => zle(`błąd strony: ${e.message}`));

    await page.goto(`http://127.0.0.1:${PORT}/template.html?arkusz=${ARKUSZ}`,
        { waitUntil: 'networkidle' });
    await page.waitForFunction(() => document.querySelectorAll('.exercise-container').length > 2);

    const karta = page.locator('.exercise-container').filter({
        has: page.locator(`.question:has-text("Zadanie ${ZADANIE}.")`),
    }).first();
    await karta.locator('.solution-button').click();
    await page.waitForTimeout(600);

    for (const szer of SZEROKOSCI) {
        await page.setViewportSize({ width: szer, height: 1000 });
        await page.waitForTimeout(350); // ResizeObserver + requestAnimationFrame
        // Pasek musi być w kadrze: elementFromPoint pracuje we współrzędnych okna,
        // więc rząd kropek poza ekranem dałby fałszywe „zasłonięte".
        await karta.locator('.steps-dots-row').scrollIntoViewIfNeeded();
        await page.waitForTimeout(150);
        const p = await pomiar(karta);
        const schowane = p.kropki.filter(k => !k.wOknie).length;
        console.log(`szerokość ${szer} px — kropek poza oknem: ${schowane}/${p.kropki.length}, `
            + `strzałki: ${p.strzalki ? 'widoczne' : 'schowane'}, `
            + `treść ${Math.round(p.trescSzer)} px w oknie ${p.clientWidth} px `
            + `(wiersz ${p.wierszWidth} px)`);

        // 1. DOSTĘPNOŚĆ
        if (schowane > 0 && !p.strzalki) {
            zle(`MARTWA STREFA: ${schowane} kropek poza oknem, a strzałek nie ma`);
        } else {
            dobrze('każdy krok osiągalny (kropki widoczne albo strzałki na miejscu)');
        }

        // 2. TRAFIALNOŚĆ
        const zaslonione = p.kropki.filter(k => k.wOknie && !k.swoj);
        if (zaslonione.length) {
            zle(`kropki zasłonięte, klik w środek nie trafia: ${zaslonione.map(k => k.i).join(',')}`);
        }
        // Mierzymy tylko kropki mieszczące się w oknie w całości: kropka ucięta
        // krawędzią paska ma pole dotyku przycięte z definicji.
        const wOknie = p.kropki.filter(k => k.wOknie);
        // LUZ, bo pasek bywa przewinięty o ułamek piksela i sonda gubi wtedy
        // skrajny piksel pola dotyku.
        const male = wOknie.filter(k => k.szer < MIN_POLE_X - LUZ || k.wys < MIN_POLE_Y - LUZ);
        if (male.length) {
            const k = male[0];
            zle(`pole dotyku kropki ${k.i} za małe: ${Math.round(k.szer)}x${Math.round(k.wys)} px, `
                + `wymagane ${MIN_POLE_X}x${MIN_POLE_Y}`);
        } else if (wOknie.length) {
            dobrze(`pole dotyku kropki ${Math.round(wOknie[0].szer)}x${Math.round(wOknie[0].wys)} px `
                + `(sprawdzone ${wOknie.length} kropek w oknie)`);
        }

        // 3. OGRANICZNIK — tylko tam, gdzie w ogóle jest co przewijać.
        if (p.strzalki) {
            for (let i = 0; i < KLIKNIEC; i++) {
                await karta.locator('.steps-scroll-prawo').click();
                await page.waitForTimeout(60);
            }
            await page.waitForTimeout(600); // dojechanie płynnego przewijania
            await karta.locator('.steps-dots-row').scrollIntoViewIfNeeded();
            const po = await pomiar(karta);
            const max = po.scrollWidth - po.clientWidth;
            if (po.scrollLeft > max + LUZ) {
                zle(`przewinięte poza treść: scrollLeft ${Math.round(po.scrollLeft)} > `
                    + `${Math.round(max)} (scrollWidth ${po.scrollWidth} - clientWidth ${po.clientWidth})`);
            } else {
                dobrze(`ogranicznik w prawo trzyma: scrollLeft ${Math.round(po.scrollLeft)} <= ${Math.round(max)}`);
            }

            for (let i = 0; i < KLIKNIEC; i++) {
                await karta.locator('.steps-scroll-lewo').click();
                await page.waitForTimeout(60);
            }
            await page.waitForTimeout(600);
            await karta.locator('.steps-dots-row').scrollIntoViewIfNeeded();
            const wroc = await pomiar(karta);
            if (wroc.scrollLeft < -LUZ) {
                zle(`przewinięte przed początek: scrollLeft ${Math.round(wroc.scrollLeft)}`);
            } else {
                dobrze(`ogranicznik w lewo trzyma: scrollLeft ${Math.round(wroc.scrollLeft)} >= 0`);
            }
        }
    }

    await browser.close();
    console.log(bledy === 0 ? '\nWSZYSTKO PRZESZŁO' : `\nPADŁO: ${bledy} niezmiennik(ów)`);
    process.exit(bledy === 0 ? 0 : 1);
})();
