// widgets/_helpers.js — wspólne pomocniki widżetów interaktywnych rozwiązań
// (solutionWidget). Ładowany PRZED plikami poszczególnych widżetów w widgets/
// i przed script.js w template.html.

/* ===================================================================
   WIDŻETY INTERAKTYWNE (solutionWidget)

   Każdy widżet dostaje kontener (.solution-interactive-container) i buduje
   w nim własny DOM — bez sztywnych id, wszystko szukane wewnątrz kontenera,
   więc widżety mogą występować w wielu zadaniach naraz.
   =================================================================== */

// --- Wspólne pomocniki ---------------------------------------------------

function wgElement(tag, className, html) {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (html !== undefined) el.innerHTML = html;
    return el;
}

function wgCanvas(container, width, height) {
    const canvas = document.createElement("canvas");
    canvas.width = width;
    canvas.height = height;
    canvas.className = "widget-canvas";
    container.appendChild(canvas);
    return canvas;
}

// Pozycja wskaźnika we współrzędnych canvasa (uwzględnia ewentualne skalowanie CSS).
function wgPointerPos(canvas, event) {
    const r = canvas.getBoundingClientRect();
    return {
        x: (event.clientX - r.left) * (canvas.width / r.width),
        y: (event.clientY - r.top) * (canvas.height / r.height)
    };
}

// Przeciąganie na canvasie: onDrag dostaje pozycję wskaźnika przy wciśniętym
// przycisku; hitTest (opcjonalny) decyduje, czy start przeciągania jest "na" uchwycie.
function wgDraggable(canvas, hitTest, onDrag) {
    let dragging = false;
    canvas.addEventListener("pointerdown", (e) => {
        const pos = wgPointerPos(canvas, e);
        if (!hitTest || hitTest(pos)) {
            dragging = true;
            canvas.setPointerCapture(e.pointerId);
            onDrag(pos);
        }
    });
    canvas.addEventListener("pointermove", (e) => {
        if (dragging) onDrag(wgPointerPos(canvas, e));
    });
    canvas.addEventListener("pointerup", () => { dragging = false; });
    canvas.addEventListener("pointercancel", () => { dragging = false; });
}

// KaTeX w widżetach. Żywe readouty aktualizują się dziesiątki razy na sekundę
// przy przeciąganiu, więc NIE używamy tu auto-rendera (renderMathInElement).
// Zamiast tego: katex.renderToString z memoizacją — wartości w widżetach są
// skwantowane (kroki 0,25 / 0,5° / kroki suwaków), więc różnych wzorów jest
// skończenie mało i każdy renderuje się najwyżej raz. Fallback na surowy
// zapis, gdyby vendor/katex się nie wczytał (ta sama filozofia co
// renderMath na górze skryptu).
const wgMathCache = new Map();
function wgMath(tex) {
    let html = wgMathCache.get(tex);
    if (html === undefined) {
        html = (window.katex && katex.renderToString)
            ? katex.renderToString(tex, { throwOnError: false })
            : tex;
        wgMathCache.set(tex, html);
    }
    return html;
}

// Liczba w zapisie TeX po polsku: przecinek dziesiętny jako {,}, odstępy
// tysięcy jako \, , minus typograficzny sprowadzony do zwykłego.
function wgTexLiczba(v, maxFrac = 2, minFrac = 0) {
    return v.toLocaleString("pl-PL", { maximumFractionDigits: maxFrac, minimumFractionDigits: minFrac })
        .replace(/\s/g, "\\,")
        .replace(/[−–]/g, "-")
        .replace(/,/g, "{,}");
}

// Podmiana treści readoutu TYLKO gdy tekst faktycznie się zmienił — cache
// ostatniego stringa na elemencie; przy przeciąganiu bez zmiany wartości
// DOM zostaje w spokoju.
function wgUstawHTML(el, html) {
    if (el.__wgOstatniHTML !== html) {
        el.__wgOstatniHTML = html;
        el.innerHTML = html;
    }
}

// Delikatne "przyklejanie" przeciąganej wartości do najbliższego celu z listy
// (gdy jest bliżej niż prog) — łatwiej trafić dokładnie w sytuację z zadania.
// Zwraca cel albo wartość bez zmian; wołający decyduje, czy resztę zaokrąglić.
function wgPrzyciagnij(value, targets, prog) {
    for (const t of targets) {
        if (Math.abs(value - t) <= prog) return t;
    }
    return value;
}

function wgStrzalka(ctx, x1, y1, x2, y2) {
    const angle = Math.atan2(y2 - y1, x2 - x1);
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - 8 * Math.cos(angle - 0.4), y2 - 8 * Math.sin(angle - 0.4));
    ctx.lineTo(x2 - 8 * Math.cos(angle + 0.4), y2 - 8 * Math.sin(angle + 0.4));
    ctx.closePath();
    ctx.fill();
}

/* ===== PALETA WIDŻETÓW (motyw jasny/ciemny) =============================
   Canvas nie dziedziczy kolorów z CSS, więc paleta jest czytana ze zmiennych
   motywu (style/base.css, sekcja „PALETA WIDŻETÓW") przez getComputedStyle
   i trzymana tutaj jako gotowe stringi. Wartości poniżej to tylko FALLBACK
   (jasny motyw), gdyby zmiennej zabrakło.
   Reguła: w plikach widżetów NIE ma literałów kolorów — wszystko przez
   WG_KOLORY, inaczej element nie przełączy się razem z motywem. */
const WG_KOLORY = {
    plotno: "#fff",           // --canvas-bg (tło płótna, np. „puste" kółko)
    osie: "#666",
    siatka: "#eee",
    tekst: "#333",            // liczby, nazwy punktów, podpisy
    linia: "#999",            // linie pomocnicze
    liniaSlaba: "#bbb",       // przerywane, linia zera
    liniaMocna: "#444",       // wyróżnione ramiona/odcinki
    wykres: "#7a3fa8",        // fiolet jak na rysunkach CKE (--accent-purple)
    punkt: "#e8871e",         // pomarańcz
    zolty: "#c99700",
    niewiadoma: "#0077b6",   // x i liczba na jego miejscu (podstawianie)
    zielony: "#2e7d32",       // --accent-green (środek osi w zad. 1)
    slupek: "#c9b3dd",
    etykietaInfo: "#9bb8d4",
    ok: "#0AB32F",
    zle: "#d9534f",
    info: "#4a90d9",
    obszarOk: "rgba(10, 179, 47, 0.08)",
    obszarInfo: "rgba(74, 144, 217, 0.07)",
    obszarWykres: "rgba(122, 63, 168, 0.08)",
    slupekOk: "rgba(10, 179, 47, 0.35)"
};

// Nazwa w WG_KOLORY → zmienna CSS.
const WG_ZMIENNE = {
    plotno: "--canvas-bg",
    osie: "--wg-osie",
    siatka: "--wg-siatka",
    tekst: "--wg-tekst",
    linia: "--wg-linia",
    liniaSlaba: "--wg-linia-slaba",
    liniaMocna: "--wg-linia-mocna",
    wykres: "--accent-purple",
    punkt: "--wg-punkt",
    zolty: "--wg-zolty",
    niewiadoma: "--wg-niewiadoma",
    zielony: "--accent-green",
    slupek: "--wg-slupek",
    etykietaInfo: "--wg-etykieta-info",
    ok: "--correct",
    zle: "--incorrect",
    info: "--accent-blue-strong",
    obszarOk: "--wg-obszar-ok",
    obszarInfo: "--wg-obszar-info",
    obszarWykres: "--wg-obszar-wykres",
    slupekOk: "--wg-slupek-ok"
};

// getComputedStyle oddaje kolory jako "rgb(r, g, b)"; canvasowi to nie
// przeszkadza, ale KaTeXowy \textcolor{...} (zad. 18) przyjmuje tylko hex,
// więc kolory bez alfy sprowadzamy do #rrggbb. rgba(...) zostaje jak jest.
function wgHex(kolor) {
    const m = kolor.match(/^rgb\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)\s*\)$/);
    if (!m) return kolor;
    return "#" + [1, 2, 3].map(i => Number(m[i]).toString(16).padStart(2, "0")).join("");
}

function wgOdswiezKolory() {
    const s = getComputedStyle(document.documentElement);
    for (const [nazwa, zmienna] of Object.entries(WG_ZMIENNE)) {
        const v = s.getPropertyValue(zmienna).trim();
        if (v) WG_KOLORY[nazwa] = wgHex(v);
    }
}

/* Przemalowanie widżetów po zmianie motywu — bez reloadu strony.
   Każdy widżet rejestruje swoją funkcję rysującą razem z canvasem; canvasy,
   których nie ma już w dokumencie, wypadają z listy przy pierwszej okazji.
   Wołane z applyTheme() (app/theme.js) oraz przy zmianie motywu systemowego
   w trybie „auto". */
const wgRysowania = [];
function wgZarejestrujRysowanie(canvas, rysuj) {
    wgRysowania.push({ canvas, rysuj });
}
function wgPrzemaluj() {
    wgOdswiezKolory();
    for (let i = wgRysowania.length - 1; i >= 0; i--) {
        if (!wgRysowania[i].canvas.isConnected) { wgRysowania.splice(i, 1); continue; }
        try { wgRysowania[i].rysuj(); } catch (e) { console.warn("Widżet: nie udało się przemalować.", e); }
    }
}
wgOdswiezKolory();
window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", wgPrzemaluj);
