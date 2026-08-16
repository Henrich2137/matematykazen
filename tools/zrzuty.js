/* Zrzuty ekranu strony — narzędzie do pracy nad CSS-em wewnątrz devcontainera.
 *
 * PO CO TO JEST. Strona jest wizualna, a model pracujący w kontenerze nie ma jej
 * jak zobaczyć inaczej niż zrzutem. Bez porównania „przed/po" każda zmiana w CSS
 * to zgadywanie. Skrypt robi komplet ujęć jedną komendą, zawsze tych samych, żeby
 * dwa przebiegi dało się zestawić klatka w klatkę.
 *
 * WYMAGA URUCHOMIONEGO SERWERA (dane idą fetchem, file:// nie działa):
 *
 *   python3 -m http.server 8000 --bind 127.0.0.1
 *
 * Bind na 127.0.0.1, nie 0.0.0.0 — brama hosta jest w firewallu kontenera
 * przepuszczona, więc serwer na 0.0.0.0 byłby widoczny poza kontenerem.
 *
 * UŻYCIE:
 *
 *   NODE_PATH=/usr/local/share/npm-global/lib/node_modules node tools/zrzuty.js --przed
 *   … zmiany w CSS …
 *   NODE_PATH=/usr/local/share/npm-global/lib/node_modules node tools/zrzuty.js --po
 *
 * NODE_PATH jest OBOWIĄZKOWE. Playwright jest zainstalowany globalnie
 * (NPM_CONFIG_PREFIX=/usr/local/share/npm-global), a node nie szuka bibliotek
 * w globalnym prefiksie — bez tej zmiennej dostaniesz „Cannot find module".
 * Nigdy nie uruchamiaj `npx playwright install`: przeglądarka przychodzi bindem
 * z hosta, a CDN Playwrighta jest zablokowany firewallem (issues/playwright-podglad.md).
 *
 * Zrzuty lądują w /tmp/zrzuty/<etykieta>/ — poza repo, żeby nie zaśmiecać gita.
 *
 * PRZEŁĄCZNIKI:
 *   --przed | --po | --etykieta=<nazwa>   katalog wyjściowy (domyślnie „biezace")
 *   --tylko=<fragment>                    tylko ujęcia, których nazwa zawiera fragment
 *   --arkusz=<id>                         inny arkusz (domyślnie 2024-grudzien)
 *   --port=<n>                            inny port serwera (domyślnie 8000)
 *   --pelna                               cała strona, nie samo okno
 *
 * PUŁAPKI, na których łatwo się przejechać:
 *
 * 1. Pierwszy `.exercise-container` w DOM to pusty szablon. Wybierając zadanie
 *    w kodzie testowym bierz `.nth(1)`.
 * 2. Rysunki w treści zadań dostają `loading="lazy"` (app/render.js), więc
 *    dopóki test do nich nie przewinie, mają `complete === false`
 *    i `naturalWidth === 0`. Sprawdzanie ich zaraz po `goto` zgłasza awarię
 *    obrazków, których naprawdę nie ma. Najpierw `scrollIntoViewIfNeeded()`
 *    na każdym `.question img`, dopiero potem pomiar (wpadka z 2026-08-16).
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const flaga = (nazwa, dom) => {
    const t = args.find(a => a.startsWith(`--${nazwa}=`));
    return t ? t.slice(nazwa.length + 3) : dom;
};
const jest = nazwa => args.includes(`--${nazwa}`);

const ETYKIETA = jest('przed') ? 'przed' : jest('po') ? 'po' : flaga('etykieta', 'biezace');
const ARKUSZ = flaga('arkusz', '2024-grudzien');
const PORT = flaga('port', '8000');
const TYLKO = flaga('tylko', '');
const PELNA = jest('pelna');

const BAZA = `http://127.0.0.1:${PORT}`;
const KAT = path.join('/tmp/zrzuty', ETYKIETA);

/* Dwa okna wystarczają: szeroki desktop i typowy telefon (390px to iPhone 12/13/14
   i większość Androidów w tej klasie). Pośrednie szerokości dokładaj ad hoc
   przełącznikiem --tylko, gdy diagnozujesz konkretny breakpoint. */
const OKNA = {
    desktop: { viewport: { width: 1280, height: 900 } },
    telefon: { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 },
};

/* Motyw ustawiamy KLASĄ na <html>, nie samym colorScheme przeglądarki: strona ma
   własny przełącznik (jasny/ciemny/auto) zapisywany do localStorage, a klasa
   theme-dark jest tym, co realnie steruje paletą (app/theme.js). Ustawiamy oba,
   żeby zgadzało się też to, co widzą media queries. */
const MOTYWY = ['jasny', 'ciemny'];

const UJECIA = [
    { nazwa: 'arkusz', url: () => `${BAZA}/template.html?arkusz=${ARKUSZ}` },
    { nazwa: 'landing', url: () => `${BAZA}/index.html`, motywKlasa: false },
    {
        nazwa: 'sidebar',
        url: () => `${BAZA}/template.html?arkusz=${ARKUSZ}`,
        po: async page => {
            await page.click('#sidebar-toggle');
            await page.waitForTimeout(400); // animacja wysuwania
        },
    },
    {
        /* ?test-egzamin=1 skraca timer do minuty (app/exam.js) — parametr istnieje
           właśnie po to, żeby dało się obejrzeć tryb egzaminu bez czekania. */
        nazwa: 'egzamin',
        url: () => `${BAZA}/template.html?arkusz=${ARKUSZ}&test-egzamin=1`,
        po: async page => {
            /* Start egzaminu przechodzi przez confirm() — celowo, żeby nie dało się
               go odpalić przypadkiem (app/exam.js, startExamPrompt). Bez tej zgody
               klik nic nie robi i dostajesz zrzut zwykłych ćwiczeń. */
            page.on('dialog', d => d.accept().catch(() => {}));
            await page.click('#tryb-egzamin');
            await page.waitForSelector('body.tryb-egzaminu', { timeout: 3000 });
            await page.waitForTimeout(300);
        },
    },
];

(async () => {
    fs.mkdirSync(KAT, { recursive: true });
    const przegladarka = await chromium.launch();
    const problemy = [];
    let zrobione = 0;

    for (const ujecie of UJECIA) {
        for (const [nazwaOkna, opcjeOkna] of Object.entries(OKNA)) {
            for (const motyw of MOTYWY) {
                const nazwa = `${ujecie.nazwa}-${nazwaOkna}-${motyw}`;
                if (TYLKO && !nazwa.includes(TYLKO)) continue;

                const kontekst = await przegladarka.newContext({
                    ...opcjeOkna,
                    colorScheme: motyw === 'ciemny' ? 'dark' : 'light',
                });
                /* Wstrzykiwane PRZED skryptami strony — inaczej app/theme.js zdąży
                   odczytać pusty localStorage i ustawić motyw domyślny.
                   Klucz musi być dokładnie ten, co w app/theme.js (KLUCZ_MOTYWU);
                   przy literówce zrzuty „ciemne" wychodzą jasne i nic tego nie zgłasza. */
                await kontekst.addInitScript(m => {
                    try { localStorage.setItem('matematykazen-motyw', m); } catch (e) { /* prywatny tryb */ }
                }, motyw);

                const page = await kontekst.newPage();
                const bledy = [];
                page.on('pageerror', e => bledy.push(String(e)));

                try {
                    await page.goto(ujecie.url(), { waitUntil: 'networkidle', timeout: 20000 });
                } catch (e) {
                    /* networkidle nie nastąpi, dopóki analityka (gc.zgo.at) dobija się
                       przez firewall. Strona jest wtedy już wyrenderowana, więc lecimy
                       dalej — brak ciszy w sieci to nie jest błąd strony. */
                    await page.waitForLoadState('domcontentloaded').catch(() => {});
                }
                await page.evaluate(() => document.fonts.ready).catch(() => {});

                /* Zapadka na najgroźniejszy cichy błąd tego skryptu: gdyby klucz
                   localStorage rozjechał się z app/theme.js, wszystkie „ciemne"
                   zrzuty wyszłyby jasne i wyglądałyby zupełnie wiarygodnie.
                   Uwaga: wartość w localStorage jest po polsku („jasny"/„ciemny"),
                   a klasa na <html> po angielsku (theme-light/theme-dark) — stąd mapowanie.
                   Landing nie ładuje app/theme.js i jedzie wyłącznie na
                   prefers-color-scheme, więc jego nie sprawdzamy. */
                if (ujecie.motywKlasa !== false) {
                    const klasa = motyw === 'ciemny' ? 'theme-dark' : 'theme-light';
                    const klasaOk = await page.evaluate(
                        k => document.documentElement.classList.contains(k), klasa).catch(() => true);
                    if (!klasaOk) bledy.push(`motyw „${motyw}" NIE został nałożony (brak klasy ${klasa} na <html>)`);
                }

                if (ujecie.po) await ujecie.po(page).catch(e => bledy.push('krok „po": ' + e.message));
                await page.waitForTimeout(200);

                await page.screenshot({ path: path.join(KAT, nazwa + '.png'), fullPage: PELNA });
                zrobione++;
                if (bledy.length) problemy.push(`${nazwa}: ${bledy.join(' | ')}`);
                await kontekst.close();
            }
        }
    }

    await przegladarka.close();
    console.log(`Zrzuty (${zrobione}) w ${KAT}`);
    if (problemy.length) {
        console.log('\nBŁĘDY JS NA STRONIE — obejrzyj, zanim zaufasz zrzutom:');
        problemy.forEach(p => console.log('  ' + p));
    }
})().catch(e => { console.error('Nie udało się:', e.message); process.exit(1); });
