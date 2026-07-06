// solutionsInteractive.js — widżety interaktywne rozwiązań (solutionInteractive).
// Wydzielone z matematykazen.html. Ładowane PRZED script.js, bo rejestr WIDZETY
// (na końcu tego pliku) jest odczytywany przez loadExercises() w script.js.

/* ===================================================================
   WIDŻETY INTERAKTYWNE (solutionInteractive)

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

const WG_KOLORY = {
    osie: "#666",
    siatka: "#eee",
    wykres: "#7a3fa8",   // fiolet jak na rysunkach CKE
    punkt: "#e8871e",    // pomarańcz
    ok: "#0AB32F",
    zle: "#d9534f",
    info: "#4a90d9"
};

// --- Zad 1: oś liczbowa |x + a| = b --------------------------------------
// Środek (−a) + dwa rozwiązania w odległości b. Zielony punkt testowy do
// przeciągania pokazuje, jak zmienia się |x + a|.

function widgetOsLiczbowa(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Rozwiązania ${wgMath("|x + a| = b")} to liczby odległe o ${wgMath("b")} od liczby ${wgMath("(-a)")}. Przeciągaj żółty punkt i zmieniaj a, b:`));

    const canvas = wgCanvas(wrap, 520, 130);
    const ctx = canvas.getContext("2d");

    // Kolory okienek = kolory na osi: a (zielone) to środek −a, b (niebieskie)
    // to strzałki odległości. Reset przywraca dane z zadania. Okienek <input>
    // nie da się włożyć do wzoru KaTeXa, więc wzór jest sklejony z kawałków
    // KaTeXa wokół pól.
    const controls = wgElement("div", "widget-controls",
        `<span class="wg-wzor-z-polami">${wgMath("|\\,x\\,+")} <input type="number" class="wg-a" value="4"> ${wgMath("\\,| =")} <input type="number" class="wg-b" value="7"></span>` +
        `<button class="light-button wg-reset" title="Przywróć a = 4, b = 7">↺ reset</button>`);
    wrap.appendChild(controls);

    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const aInput = controls.querySelector(".wg-a");
    const bInput = controls.querySelector(".wg-b");

    const MIN = -15, MAX = 5;
    const state = { x: 0 };
    const toPix = v => 20 + (v - MIN) / (MAX - MIN) * (canvas.width - 40);
    const toVal = px => MIN + (px - 20) / (canvas.width - 40) * (MAX - MIN);

    function draw() {
        const a = parseFloat(aInput.value) || 0;
        const b = parseFloat(bInput.value) || 0;
        const centerY = 85;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Oś ze strzałką i podziałką.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, 12, centerY, canvas.width - 4, centerY);
        ctx.font = "11px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        for (let i = MIN; i <= MAX; i++) {
            const px = toPix(i);
            ctx.beginPath();
            ctx.moveTo(px, centerY - 3);
            ctx.lineTo(px, centerY + 3);
            ctx.stroke();
            ctx.fillText(i, px, centerY + 7);
        }

        const center = -a;
        // Strzałki odległości b od środka do obu rozwiązań — każda na innej
        // wysokości i lekko skrócona z obu końców, żeby nie zlewały się
        // w jedną długą linię przechodzącą przez środek.
        if (b >= 0) {
            ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.info;
            ctx.lineWidth = 1.5;
            [[center + b, centerY - 26], [center - b, centerY - 42]].forEach(([sol, y]) => {
                if (Math.abs(sol - center) < 0.01) return;
                const odX = toPix(center), doX = toPix(sol);
                const kier = Math.sign(doX - odX);
                wgStrzalka(ctx, odX + kier * 7, y, doX - kier * 5, y);
                ctx.font = "12px Arial";
                ctx.textBaseline = "bottom";
                ctx.fillText(`${b}`, (odX + doX) / 2, y - 3);
            });

            // Rozwiązania (pomarańczowe punkty).
            ctx.fillStyle = WG_KOLORY.punkt;
            [center + b, center - b].forEach(sol => {
                if (sol >= MIN && sol <= MAX) {
                    ctx.beginPath();
                    ctx.arc(toPix(sol), centerY, 5, 0, Math.PI * 2);
                    ctx.fill();
                }
            });
        }

        // Środek (−a) — zielony, jak okienko z a (ta sama liczba, tylko z minusem).
        ctx.fillStyle = "#2e7d32";
        if (center >= MIN && center <= MAX) {
            ctx.beginPath();
            ctx.arc(toPix(center), centerY, 4, 0, Math.PI * 2);
            ctx.fill();
        }

        // Punkt testowy x (ciemnożółty) + jego odległość od środka;
        // po trafieniu w rozwiązanie dostaje zieloną obwódkę.
        const dist = Math.abs(state.x + a);
        const trafiony = b >= 0 && Math.abs(dist - b) < 0.01;
        ctx.fillStyle = "#c99700";
        ctx.beginPath();
        ctx.arc(toPix(state.x), centerY, 7, 0, Math.PI * 2);
        ctx.fill();
        if (trafiony) {
            ctx.strokeStyle = WG_KOLORY.ok;
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.arc(toPix(state.x), centerY, 10, 0, Math.PI * 2);
            ctx.stroke();
        }

        wgUstawHTML(readout,
            wgMath(`|\\,${wgTexLiczba(state.x)} + ${wgTexLiczba(a)}\\,| = \\mathbf{${wgTexLiczba(Math.round(dist * 100) / 100)}}`) + `<br>` +
            (trafiony ? `<span class="wg-ok">✓ to rozwiązanie!</span>`
                      : `<span class="wg-neutral">(szukamy odległości ${b})</span>`));
    }

    wgDraggable(canvas,
        pos => Math.abs(pos.x - toPix(state.x)) < 25,
        pos => {
            const a = parseFloat(aInput.value) || 0;
            const b = parseFloat(bInput.value) || 0;
            const raw = Math.min(MAX, Math.max(MIN, toVal(pos.x)));
            // Przyciąganie do rozwiązań i środka; poza nimi krok co 0,25.
            const snap = wgPrzyciagnij(raw, b >= 0 ? [-a + b, -a - b, -a] : [-a], 0.35);
            state.x = snap !== raw ? snap : Math.round(raw * 4) / 4;
            draw();
        });

    aInput.addEventListener("input", draw);
    bInput.addEventListener("input", draw);
    controls.querySelector(".wg-reset").addEventListener("click", () => {
        aInput.value = 4;
        bInput.value = 7;
        state.x = 0;
        draw();
    });
    draw();
}

// --- Zad 5: procent składany ----------------------------------------------
// Suwak oprocentowania + słupki kapitału po 0/1/2 latach i linia celu.

function widgetProcentSkladany(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmieniaj oprocentowanie ${wgMath("p")} i sprawdź, kiedy kapitał po 2 latach trafi w <b>67 925,76 zł</b>:`));

    const canvas = wgCanvas(wrap, 520, 230);
    const ctx = canvas.getContext("2d");

    const controls = wgElement("div", "widget-controls",
        `<input type="range" min="0" max="10" step="0.1" value="3">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const slider = controls.querySelector("input");
    const START = 60000, CEL = 67925.76;

    const zl = v => v.toLocaleString("pl-PL", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " zł";

    function draw() {
        const p = parseFloat(slider.value);
        const r = p / 100;
        const kwoty = [START, START * (1 + r), START * (1 + r) * (1 + r)];
        const trafiony = Math.abs(kwoty[2] - CEL) < 0.5;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const baseY = 195, maxVal = 78000, scale = 160 / maxVal;

        // Linia celu (przerywana czerwona).
        const celY = baseY - CEL * scale;
        ctx.strokeStyle = WG_KOLORY.zle;
        ctx.setLineDash([6, 4]);
        ctx.beginPath();
        ctx.moveTo(40, celY);
        ctx.lineTo(490, celY);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = WG_KOLORY.zle;
        ctx.font = "12px Arial";
        ctx.textAlign = "left";
        ctx.textBaseline = "bottom";
        ctx.fillText("cel: 67 925,76 zł", 42, celY - 3);

        // Słupki.
        const etykiety = ["wpłata", "po 1 roku", "po 2 latach"];
        kwoty.forEach((kwota, i) => {
            const x = 90 + i * 150;
            const h = kwota * scale;
            ctx.fillStyle = (i === 2 && trafiony) ? WG_KOLORY.ok : "#c9b3dd";
            ctx.fillRect(x, baseY - h, 90, h);
            ctx.strokeStyle = WG_KOLORY.wykres;
            ctx.strokeRect(x, baseY - h, 90, h);

            ctx.fillStyle = "#333";
            ctx.textAlign = "center";
            ctx.textBaseline = "bottom";
            ctx.font = "12px Arial";
            ctx.fillText(zl(kwota), x + 45, baseY - h - 4);
            ctx.textBaseline = "top";
            ctx.fillText(etykiety[i], x + 45, baseY + 6);
        });

        wgUstawHTML(readout,
            wgMath(`p = ${wgTexLiczba(p, 1, 1)}\\%\\ \\rightarrow\\ 60\\,000 \\cdot (1 + ${wgTexLiczba(r, 4)})^{2} = `) + `<b>${zl(kwoty[2])}</b>` +
            (trafiony ? `<br><span class="wg-ok">✓ ${wgMath("p = 6{,}4\\%")}!</span>` : ""));
    }

    slider.addEventListener("input", draw);
    draw();
}

// --- Zad 9: nierówność kwadratowa x(x−6) ≤ 7 ------------------------------
// Parabola x² − 6x − 7 z zaznaczonym przedziałem rozwiązań; punkt do przeciągania
// po osi x pokazuje, czy nierówność jest spełniona.

function widgetNierownoscKwadratowa(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Przeciągaj punkt po osi x — nierówność ${wgMath("x(x - 6) \\le 7")} spełniają te ${wgMath("x")}, dla których parabola ${wgMath("x^{2} - 6x - 7")} jest pod osią (lub na niej):`));

    const canvas = wgCanvas(wrap, 520, 260);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const X0 = -4, X1 = 10, Y0 = -20, Y1 = 28;
    const px = x => 20 + (x - X0) / (X1 - X0) * 480;
    const py = y => 240 - (y - Y0) / (Y1 - Y0) * 230;
    const vx = p => X0 + (p - 20) / 480 * (X1 - X0);
    const f = x => x * x - 6 * x - 7;

    const state = { x: 3 };

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Obszar rozwiązań (parabola pod osią) — delikatne zielone tło.
        ctx.fillStyle = "rgba(10, 179, 47, 0.08)";
        ctx.beginPath();
        ctx.moveTo(px(-1), py(0));
        for (let x = -1; x <= 7; x += 0.1) ctx.lineTo(px(x), py(f(x)));
        ctx.closePath();
        ctx.fill();

        // Osie.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, px(X0), py(0), px(X1), py(0));
        wgStrzalka(ctx, px(0), py(Y0), px(0), py(Y1));
        ctx.font = "11px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        for (let i = X0 + 1; i < X1; i++) {
            if (i === 0) continue;
            ctx.beginPath();
            ctx.moveTo(px(i), py(0) - 3);
            ctx.lineTo(px(i), py(0) + 3);
            ctx.stroke();
            if (i % 2 === 0 || i === -1 || i === 7) ctx.fillText(i, px(i), py(0) + 6);
        }

        // Parabola.
        ctx.strokeStyle = WG_KOLORY.wykres;
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let x = X0; x <= X1; x += 0.05) {
            const p = { x: px(x), y: py(f(x)) };
            x === X0 ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y);
        }
        ctx.stroke();

        // Przedział rozwiązań na osi.
        ctx.strokeStyle = WG_KOLORY.ok;
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(px(-1), py(0));
        ctx.lineTo(px(7), py(0));
        ctx.stroke();
        ctx.fillStyle = WG_KOLORY.ok;
        [[-1, "−1"], [7, "7"]].forEach(([x, label]) => {
            ctx.beginPath();
            ctx.arc(px(x), py(0), 5, 0, Math.PI * 2);
            ctx.fill();
            ctx.font = "bold 12px Arial";
            ctx.textBaseline = "bottom";
            ctx.fillText(label, px(x), py(0) - 8);
        });

        // Punkt testowy na osi + wartość na paraboli.
        const val = state.x * (state.x - 6);
        const spelnia = val <= 7.0001;
        ctx.strokeStyle = "#aaa";
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(px(state.x), py(0));
        ctx.lineTo(px(state.x), py(f(state.x)));
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = spelnia ? WG_KOLORY.ok : WG_KOLORY.zle;
        ctx.beginPath();
        ctx.arc(px(state.x), py(0), 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(px(state.x), py(f(state.x)), 4, 0, Math.PI * 2);
        ctx.fill();

        wgUstawHTML(readout,
            wgMath(`x = ${wgTexLiczba(state.x)}\\!:\\quad x(x - 6) = ${wgTexLiczba(val)}`) + `<br>` +
            (spelnia ? `<span class="wg-ok">${wgMath("\\le 7")} ✓ spełnia</span>`
                     : `<span class="wg-zle">${wgMath("> 7")} ✗ nie spełnia</span>`));
    }

    wgDraggable(canvas, null, pos => {
        const raw = Math.min(X1, Math.max(X0, vx(pos.x)));
        // Przyciąganie do końców przedziału rozwiązań; poza nimi krok co 0,25.
        const snap = wgPrzyciagnij(raw, [-1, 7], 0.3);
        state.x = snap !== raw ? snap : Math.round(raw * 4) / 4;
        draw();
    });
    draw();
}

// --- Zad 10: funkcja określona przedziałami --------------------------------
// Suwak przesuwa punkt po wykresie; podświetla się wzór aktualnie "aktywnego"
// przedziału, a odczyt pokazuje znak wartości.

function widgetFunkcjaPrzedzialami(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Przesuwaj ${wgMath("x")} wzdłuż dziedziny i obserwuj, który wzór działa i jaki znak ma ${wgMath("f(x)")}:`));

    const canvas = wgCanvas(wrap, 520, 300);
    const ctx = canvas.getContext("2d");

    const formulas = wgElement("div", "widget-formula-list",
        `<div class="wg-formula" data-i="0">${wgMath("3 \\quad \\text{dla } x \\in (-4,\\ -2\\rangle")}</div>` +
        `<div class="wg-formula" data-i="1">${wgMath("-x + 1 \\quad \\text{dla } x \\in (-2,\\ 2\\rangle")}</div>` +
        `<div class="wg-formula" data-i="2">${wgMath("x - 3 \\quad \\text{dla } x \\in (2,\\ 4\\rangle")}</div>`);
    wrap.appendChild(formulas);

    const controls = wgElement("div", "widget-controls",
        `<input type="range" min="-3.98" max="4" step="0.02" value="0">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const slider = controls.querySelector("input");
    const px = x => 260 + x * 44;
    const py = y => 150 - y * 44;
    const f = x => x <= -2 ? 3 : x <= 2 ? -x + 1 : x - 3;
    const aktywny = x => x <= -2 ? 0 : x <= 2 ? 1 : 2;

    function draw() {
        const x = parseFloat(slider.value);
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Siatka.
        ctx.strokeStyle = WG_KOLORY.siatka;
        ctx.lineWidth = 1;
        for (let i = -5; i <= 5; i++) {
            ctx.beginPath(); ctx.moveTo(px(i), py(-3)); ctx.lineTo(px(i), py(3.5)); ctx.stroke();
        }
        for (let j = -3; j <= 3; j++) {
            ctx.beginPath(); ctx.moveTo(px(-5), py(j)); ctx.lineTo(px(5), py(j)); ctx.stroke();
        }

        // Osie.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        wgStrzalka(ctx, px(-5.2), py(0), px(5.3), py(0));
        wgStrzalka(ctx, px(0), py(-3.2), px(0), py(3.6));
        ctx.font = "10px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        for (let i = -5; i <= 5; i++) if (i !== 0) ctx.fillText(i, px(i), py(0) + 5);
        ctx.textAlign = "right";
        ctx.textBaseline = "middle";
        for (let j = -3; j <= 3; j++) if (j !== 0) ctx.fillText(j, px(0) - 6, py(j));

        // Wykres (3 kawałki).
        ctx.strokeStyle = WG_KOLORY.wykres;
        ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(px(-4), py(3)); ctx.lineTo(px(-2), py(3)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(px(-2), py(3)); ctx.lineTo(px(2), py(-1)); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(px(2), py(-1)); ctx.lineTo(px(4), py(1)); ctx.stroke();

        // Kółko otwarte na początku dziedziny i pełne na końcu.
        ctx.lineWidth = 2;
        ctx.fillStyle = "#fff";
        ctx.beginPath(); ctx.arc(px(-4), py(3), 4, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
        ctx.fillStyle = WG_KOLORY.wykres;
        ctx.beginPath(); ctx.arc(px(4), py(1), 4, 0, Math.PI * 2); ctx.fill();

        // Ruchomy punkt.
        const y = f(x);
        ctx.fillStyle = y < 0 ? WG_KOLORY.zle : WG_KOLORY.ok;
        ctx.beginPath();
        ctx.arc(px(x), py(y), 6, 0, Math.PI * 2);
        ctx.fill();

        // Podświetlenie aktywnego wzoru.
        formulas.querySelectorAll(".wg-formula").forEach(el =>
            el.classList.toggle("active", parseInt(el.dataset.i) === aktywny(x)));

        wgUstawHTML(readout,
            wgMath(`x = ${wgTexLiczba(x)},\\quad f(x) = \\mathbf{${wgTexLiczba(y)}}`) +
            (y < 0 ? `<br><span class="wg-zle">wartość ujemna (pod osią)</span>`
             : y === 3 ? `<br><span class="wg-ok">największa wartość!</span>` : ""));
    }

    slider.addEventListener("input", draw);
    draw();
}

// --- Zad 12.1: monotoniczność paraboli -------------------------------------
// f(x) = −(x−3)²: lewa gałąź (rośnie) zielona, prawa (maleje) czerwona,
// punkt do przeciągania po wykresie.

function widgetParabola(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `${wgMath("f(x) = -(x - 3)^{2}")}. Przeciągaj punkt po paraboli — monotoniczność zmienia się dokładnie w wierzchołku:`));

    const canvas = wgCanvas(wrap, 520, 260);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const X0 = -2, X1 = 8;
    const px = x => 30 + (x - X0) / (X1 - X0) * 460;
    const py = y => 40 - y * 17;
    const vx = p => X0 + (p - 30) / 460 * (X1 - X0);
    const f = x => -(x - 3) * (x - 3);

    const state = { x: 5 };

    function rysujGalaz(od, doX, kolor) {
        ctx.strokeStyle = kolor;
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let x = od; x <= doX + 0.001; x += 0.05) {
            const p = { x: px(x), y: py(f(x)) };
            x === od ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y);
        }
        ctx.stroke();
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Osie.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, px(X0) - 10, py(0), px(X1) + 10, py(0));
        wgStrzalka(ctx, px(0), 250, px(0), 15);
        ctx.font = "11px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        for (let i = X0; i <= X1; i++) if (i !== 0) ctx.fillText(i, px(i), py(0) + 6);

        // Oś symetrii x = 3.
        ctx.strokeStyle = "#bbb";
        ctx.setLineDash([5, 4]);
        ctx.beginPath();
        ctx.moveTo(px(3), 245);
        ctx.lineTo(px(3), 20);
        ctx.stroke();
        ctx.setLineDash([]);

        // Gałęzie: rosnąca zielona, malejąca czerwona.
        rysujGalaz(X0, 3, WG_KOLORY.ok);
        rysujGalaz(3, X1, WG_KOLORY.zle);

        // Wierzchołek.
        ctx.fillStyle = WG_KOLORY.wykres;
        ctx.beginPath();
        ctx.arc(px(3), py(0), 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.font = "12px Arial";
        ctx.textBaseline = "bottom";
        ctx.fillText("W = (3, 0)", px(3) + 38, py(0) - 4);

        // Punkt użytkownika.
        ctx.fillStyle = "#333";
        ctx.beginPath();
        ctx.arc(px(state.x), py(f(state.x)), 7, 0, Math.PI * 2);
        ctx.fill();

        const xTex = wgMath(`x = ${wgTexLiczba(state.x, 1)}`);
        wgUstawHTML(readout, state.x === 3
            ? `${xTex}<br><b>wierzchołek</b>: tu funkcja przechodzi z rośnięcia w malenie`
            : state.x < 3
                ? `${xTex}<br><span class="wg-ok">↗ funkcja rośnie (${wgMath("x < 3")})</span>`
                : `${xTex}<br><span class="wg-zle">↘ funkcja maleje (${wgMath("x > 3")}) — przedział ${wgMath("\\langle 3, +\\infty)")}</span>`);
    }

    wgDraggable(canvas, null, pos => {
        const raw = Math.min(X1, Math.max(X0, vx(pos.x)));
        // Przyciąganie do wierzchołka; poza nim krok co 0,5.
        const snap = wgPrzyciagnij(raw, [3], 0.3);
        state.x = snap !== raw ? snap : Math.round(raw * 2) / 2;
        draw();
    });
    draw();
}

// --- Zad 15: ciąg arytmetyczny (5m, 4+2m, m) --------------------------------
// Suwak m; słupki trzech wyrazów i różnice między nimi — równe przy m = 4.

function widgetCiagArytmetyczny(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmieniaj ${wgMath("m")} i patrz na różnice między kolejnymi wyrazami — w ciągu arytmetycznym muszą być identyczne:`));

    const canvas = wgCanvas(wrap, 520, 240);
    const ctx = canvas.getContext("2d");
    const controls = wgElement("div", "widget-controls",
        `${wgMath("m =")} <input type="range" min="-6" max="6" step="0.25" value="1">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const slider = controls.querySelector("input");

    function draw() {
        const m = parseFloat(slider.value);
        const wyrazy = [5 * m, 4 + 2 * m, m];
        const r1 = wyrazy[1] - wyrazy[0];
        const r2 = wyrazy[2] - wyrazy[1];
        const arytmetyczny = Math.abs(r1 - r2) < 1e-9;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const zeroY = 120;
        const maxAbs = Math.max(8, ...wyrazy.map(Math.abs));
        const scale = 85 / maxAbs;

        // Linia zera.
        ctx.strokeStyle = "#ccc";
        ctx.beginPath();
        ctx.moveTo(30, zeroY);
        ctx.lineTo(490, zeroY);
        ctx.stroke();

        const nazwy = ["a₁ = 5m", "a₂ = 4 + 2m", "a₃ = m"];
        const fmt = v => v.toLocaleString("pl-PL", { maximumFractionDigits: 2 });

        wyrazy.forEach((w, i) => {
            const x = 70 + i * 150;
            const h = w * scale;
            ctx.fillStyle = arytmetyczny ? "rgba(10,179,47,0.35)" : "#c9b3dd";
            ctx.strokeStyle = arytmetyczny ? WG_KOLORY.ok : WG_KOLORY.wykres;
            ctx.fillRect(x, Math.min(zeroY, zeroY - h), 80, Math.abs(h));
            ctx.strokeRect(x, Math.min(zeroY, zeroY - h), 80, Math.abs(h));

            ctx.fillStyle = "#333";
            ctx.font = "13px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = h >= 0 ? "bottom" : "top";
            ctx.fillText(fmt(w), x + 40, h >= 0 ? zeroY - h - 5 : zeroY - h + 5);
            ctx.textBaseline = "top";
            ctx.fillText(nazwy[i], x + 40, 214);
        });

        // Różnice między słupkami.
        ctx.font = "13px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        [[145, r1], [295, r2]].forEach(([x, r]) => {
            ctx.fillStyle = arytmetyczny ? WG_KOLORY.ok : WG_KOLORY.zle;
            ctx.fillText(`r = ${fmt(r)}`, x + 40, 25);
            wgStrzalka(ctx, x + 12, 40, x + 68, 40);
        });

        wgUstawHTML(readout,
            wgMath(`m = ${wgTexLiczba(m)}\\!:\\quad (${wgTexLiczba(wyrazy[0])},\\ ${wgTexLiczba(wyrazy[1])},\\ ${wgTexLiczba(wyrazy[2])})`) + `<br>` +
            (arytmetyczny ? `<span class="wg-ok">✓ różnice równe — ciąg arytmetyczny (${wgMath("m = 4")})</span>`
                          : `<span class="wg-zle">różnice ${wgMath(`${wgTexLiczba(r1)} \\ne ${wgTexLiczba(r2)}`)}</span>`));
    }

    slider.addEventListener("input", draw);
    draw();
}

// --- Zad 18: koło trygonometryczne -----------------------------------------
// Przeciągany kąt na półokręgu; widać sin (pion) i cos (poziom) oraz to,
// że dla kąta rozwartego cosinus jest ujemny.

function widgetKoloTrygonometryczne(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Przeciągaj punkt po okręgu jednostkowym. Szukamy kąta <b>rozwartego</b> z ${wgMath("\\sin\\alpha = \\tfrac{\\sqrt{3}}{4} \\approx 0{,}433")}:`));

    const canvas = wgCanvas(wrap, 520, 300);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const cx = 260, cy = 175, R = 115;
    const SIN_CEL = Math.sqrt(3) / 4;      // ≈ 0,4330
    const COS_CEL = -Math.sqrt(13) / 4;    // ≈ −0,9014

    const state = { deg: 30 };

    function draw() {
        const rad = state.deg * Math.PI / 180;
        const sin = Math.sin(rad), cos = Math.cos(rad);
        const P = { x: cx + R * cos, y: cy - R * sin };
        const sinOk = Math.abs(sin - SIN_CEL) < 0.012;

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // II ćwiartka (kąty rozwarte) — delikatne tło.
        ctx.fillStyle = "rgba(74, 144, 217, 0.07)";
        ctx.fillRect(cx - R - 15, cy - R - 15, R + 15, R + 15);
        ctx.fillStyle = "#9bb8d4";
        ctx.font = "11px Arial";
        ctx.textAlign = "left";
        ctx.textBaseline = "top";
        ctx.fillText("kąty rozwarte (90°–180°)", cx - R - 10, cy - R - 10);

        // Osie i okrąg.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, cx - R - 25, cy, cx + R + 25, cy);
        wgStrzalka(ctx, cx, cy + R + 20, cx, cy - R - 20);
        ctx.strokeStyle = "#999";
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, Math.PI * 2);
        ctx.stroke();

        // Linia sin = √3/4.
        const yCel = cy - R * SIN_CEL;
        ctx.strokeStyle = WG_KOLORY.info;
        ctx.setLineDash([5, 4]);
        ctx.beginPath();
        ctx.moveTo(cx - R - 20, yCel);
        ctx.lineTo(cx + R + 20, yCel);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = WG_KOLORY.info;
        ctx.font = "11px Arial";
        ctx.textAlign = "left";
        ctx.textBaseline = "bottom";
        ctx.fillText("sin α = √3/4", cx + R - 40, yCel - 3);

        // Ramię kąta + łuk.
        ctx.strokeStyle = "#555";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(P.x, P.y);
        ctx.stroke();
        ctx.strokeStyle = "#aaa";
        ctx.beginPath();
        ctx.arc(cx, cy, 24, 0, -rad, true);
        ctx.stroke();

        // cos (poziomy, czerwony) i sin (pionowy, zielony).
        ctx.strokeStyle = WG_KOLORY.zle;
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(P.x, cy);
        ctx.stroke();
        ctx.strokeStyle = WG_KOLORY.ok;
        ctx.beginPath();
        ctx.moveTo(P.x, cy);
        ctx.lineTo(P.x, P.y);
        ctx.stroke();

        // Punkt na okręgu.
        ctx.fillStyle = sinOk ? (cos < 0 ? WG_KOLORY.ok : WG_KOLORY.punkt) : "#333";
        ctx.beginPath();
        ctx.arc(P.x, P.y, 7, 0, Math.PI * 2);
        ctx.fill();

        const fmtTex = v => wgTexLiczba(v, 3, 3);
        let dodatek = "";
        if (sinOk && cos < 0) {
            dodatek = `<span class="wg-ok">✓ kąt rozwarty: ${wgMath(`\\cos\\alpha = -\\tfrac{\\sqrt{13}}{4} \\approx ${fmtTex(COS_CEL)}`)}</span>`;
        } else if (sinOk) {
            dodatek = `<span class="wg-neutral">sin się zgadza, ale ten kąt jest ostry — przejdź na lewą stronę!</span>`;
        }
        // Kolory sin/cos we wzorze = kolory odcinków na rysunku (KaTeXowy \textcolor).
        wgUstawHTML(readout,
            wgMath(`\\alpha \\approx ${Math.round(state.deg)}^{\\circ},\\quad ` +
                `\\textcolor{${WG_KOLORY.ok}}{\\sin\\alpha \\approx ${fmtTex(sin)}},\\quad ` +
                `\\textcolor{${WG_KOLORY.zle}}{\\cos\\alpha \\approx ${fmtTex(cos)}}`) +
            (dodatek ? `<br>${dodatek}` : ""));
    }

    // Kąt, przy którym sin α = √3/4 po stronie rozwartej (~154,3°) — i jego
    // ostre lustro; przyciąganie ułatwia trafienie dokładnie w tę sytuację.
    const KAT_CEL = 180 - Math.asin(SIN_CEL) * 180 / Math.PI;
    wgDraggable(canvas, null, pos => {
        let deg = Math.atan2(cy - pos.y, pos.x - cx) * 180 / Math.PI;
        deg = Math.max(0, Math.min(180, deg));
        const snap = wgPrzyciagnij(deg, [KAT_CEL, 180 - KAT_CEL], 2.5);
        state.deg = snap !== deg ? snap : Math.round(deg * 2) / 2;
        draw();
    });
    draw();
}

// --- Zad 20: kąt wpisany i środkowy ----------------------------------------
// C przeciągany po dużym łuku — kąt wpisany ACB cały czas ma 60°, a środkowy 120°.

function widgetKatWpisany(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        "Przeciągaj punkt C po okręgu — kąt wpisany oparty na tym samym łuku się nie zmienia:"));

    const canvas = wgCanvas(wrap, 520, 310);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const cx = 260, cy = 155, R = 120;
    const A_DEG = 210, B_DEG = 330;          // kąt środkowy AB = 120° (łuk dołem)
    const pt = deg => ({
        x: cx + R * Math.cos(deg * Math.PI / 180),
        y: cy - R * Math.sin(deg * Math.PI / 180)
    });

    const state = { deg: 90 };

    function draw() {
        const A = pt(A_DEG), B = pt(B_DEG), C = pt(state.deg), S = { x: cx, y: cy };
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Okrąg.
        ctx.strokeStyle = WG_KOLORY.wykres;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, Math.PI * 2);
        ctx.stroke();

        // Łuk AB (dołem) — wyróżniony. W układzie canvasa (y w dół) punktowi o kącie
        // matematycznym θ odpowiada kąt −θ, więc łuk 210°→330° dołem to 30°→150°.
        ctx.strokeStyle = WG_KOLORY.punkt;
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.arc(cx, cy, R, 30 * Math.PI / 180, 150 * Math.PI / 180, false);
        ctx.stroke();
        ctx.fillStyle = WG_KOLORY.punkt;
        ctx.font = "13px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        ctx.fillText("łuk AB = ⅓ · 2π·6 = 4π", cx, cy + R + 12);

        // Ramiona kąta środkowego.
        ctx.strokeStyle = "#999";
        ctx.lineWidth = 1.5;
        [A, B].forEach(P => {
            ctx.beginPath();
            ctx.moveTo(S.x, S.y);
            ctx.lineTo(P.x, P.y);
            ctx.stroke();
        });
        // Łuczek kąta środkowego (między ramionami SA i SB, od strony łuku AB).
        ctx.strokeStyle = WG_KOLORY.zle;
        ctx.beginPath();
        ctx.arc(cx, cy, 26, 30 * Math.PI / 180, 150 * Math.PI / 180, false);
        ctx.stroke();
        ctx.fillStyle = WG_KOLORY.zle;
        ctx.font = "12px Arial";
        ctx.textBaseline = "top";
        ctx.fillText("120°", cx, cy + 32);

        // Ramiona kąta wpisanego.
        ctx.strokeStyle = "#444";
        [A, B].forEach(P => {
            ctx.beginPath();
            ctx.moveTo(C.x, C.y);
            ctx.lineTo(P.x, P.y);
            ctx.stroke();
        });

        // Miara kąta wpisanego (liczona z wektorów — zawsze wyjdzie 60°).
        const kat = (() => {
            const v1 = { x: A.x - C.x, y: A.y - C.y };
            const v2 = { x: B.x - C.x, y: B.y - C.y };
            const dot = v1.x * v2.x + v1.y * v2.y;
            const len = Math.hypot(v1.x, v1.y) * Math.hypot(v2.x, v2.y);
            return Math.acos(dot / len) * 180 / Math.PI;
        })();

        // Łuczek przy C.
        ctx.strokeStyle = WG_KOLORY.info;
        const a1 = Math.atan2(A.y - C.y, A.x - C.x);
        const a2 = Math.atan2(B.y - C.y, B.x - C.x);
        ctx.beginPath();
        // rysuj krótszy łuk między ramionami
        let od = a1, do_ = a2;
        if (((do_ - od + Math.PI * 2) % (Math.PI * 2)) > Math.PI) [od, do_] = [do_, od];
        ctx.arc(C.x, C.y, 22, od, do_, false);
        ctx.stroke();

        // Punkty.
        const punkty = [[A, "A"], [B, "B"], [S, "S"]];
        ctx.font = "bold 13px Arial";
        punkty.forEach(([P, name]) => {
            ctx.fillStyle = "#333";
            ctx.beginPath();
            ctx.arc(P.x, P.y, 3.5, 0, Math.PI * 2);
            ctx.fill();
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            const przesX = name === "S" ? 12 : (P.x - cx) * 0.14;
            const przesY = name === "S" ? -8 : (P.y - cy) * 0.14;
            ctx.fillText(name, P.x + przesX, P.y + przesY);
        });
        ctx.fillStyle = WG_KOLORY.info;
        ctx.beginPath();
        ctx.arc(C.x, C.y, 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText("C", C.x + (C.x - cx) * 0.16, C.y + (C.y - cy) * 0.16);

        wgUstawHTML(readout,
            `kąt wpisany ${wgMath(`\\angle ACB = \\mathbf{${Math.round(kat)}^{\\circ}}`)}, ` +
            `kąt środkowy ${wgMath("\\angle ASB = \\mathbf{120^{\\circ}}")}<br>` +
            `<span class="wg-neutral">środkowy jest zawsze 2× większy</span>`);
    }

    wgDraggable(canvas, null, pos => {
        let deg = Math.atan2(cy - pos.y, pos.x - cx) * 180 / Math.PI;
        if (deg < 0) deg += 360;
        // C zostaje na dużym łuku (nie wchodzi na łuk AB między 330° a 210° dołem).
        if (deg > 205 && deg < 270) deg = 205;
        if ((deg >= 270 && deg < 335)) deg = 335;
        state.deg = deg;
        draw();
    });
    draw();
}

// --- Zad 30: prostopadłościan o sumie krawędzi 48 ---------------------------
// AE = 3·AB, suma krawędzi 48 → AD = 12 − 4x. Suwak x rysuje bryłę i wykres
// P(x) = −26x² + 96x z maksimum w x = 24/13.

function widgetProstopadloscian(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Suma krawędzi stale 48 i ${wgMath("AE = 3 \\cdot AB")}. Zmieniaj ${wgMath("x = AB")} i szukaj największego pola całkowitego:`));

    const canvas = wgCanvas(wrap, 520, 260);
    const ctx = canvas.getContext("2d");
    const controls = wgElement("div", "widget-controls",
        `${wgMath("x =")} <input type="range" min="0.25" max="2.75" step="0.05" value="1">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const slider = controls.querySelector("input");
    const X_MAX_POLA = 24 / 13; // wierzchołek paraboli P(x)
    const P = x => -26 * x * x + 96 * x;

    // Wykres P(x) po prawej stronie.
    const gx = x => 300 + x / 3 * 195;
    const gy = p => 225 - p / 95 * 190;

    function draw() {
        const x = parseFloat(slider.value);
        const y = 12 - 4 * x;           // AD
        const h = 3 * x;                // AE
        const pole = P(x);
        const max = Math.abs(x - X_MAX_POLA) < 0.01;

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Prostopadłościan w rzucie ukośnym (ściana przednia x × 3x, głębokość AD).
        const s = 15;
        const dx = y * s * 0.55, dy = y * s * 0.3;
        const bx = 60, by = 225;        // lewy-dolny róg ściany przedniej
        const w = x * s, wys = h * s;

        ctx.strokeStyle = max ? WG_KOLORY.ok : WG_KOLORY.wykres;
        ctx.fillStyle = max ? "rgba(10,179,47,0.15)" : "rgba(122,63,168,0.08)";
        ctx.lineWidth = 1.5;
        // ściana przednia
        ctx.fillRect(bx, by - wys, w, wys);
        ctx.strokeRect(bx, by - wys, w, wys);
        // krawędzie w głąb + ściana górna i boczna
        ctx.beginPath();
        ctx.moveTo(bx, by - wys); ctx.lineTo(bx + dx, by - wys - dy);
        ctx.lineTo(bx + dx + w, by - wys - dy); ctx.lineTo(bx + w, by - wys);
        ctx.moveTo(bx + dx + w, by - wys - dy); ctx.lineTo(bx + w + dx, by - dy);
        ctx.lineTo(bx + w, by);
        ctx.stroke();

        // Podpisy krawędzi.
        ctx.fillStyle = "#333";
        ctx.font = "12px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        const fmt = v => v.toLocaleString("pl-PL", { maximumFractionDigits: 2 });
        ctx.fillText(`x = ${fmt(x)}`, bx + w / 2, by + 6);
        ctx.textAlign = "right";
        ctx.textBaseline = "middle";
        ctx.fillText(`3x = ${fmt(h)}`, bx - 8, by - wys / 2);
        ctx.textAlign = "left";
        ctx.fillText(`${fmt(y)}`, bx + w + dx / 2 + 6, by - dy / 2);

        // Wykres P(x).
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, gx(0), gy(0), gx(3) + 12, gy(0));
        wgStrzalka(ctx, gx(0), gy(0) + 5, gx(0), gy(95) - 6);
        ctx.font = "11px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        [1, 2, 3].forEach(v => ctx.fillText(v, gx(v), gy(0) + 4));

        ctx.strokeStyle = WG_KOLORY.wykres;
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let t = 0; t <= 3; t += 0.05) {
            const p = { x: gx(t), y: gy(P(t)) };
            t === 0 ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y);
        }
        ctx.stroke();

        // Maksimum (24/13, 1152/13).
        ctx.strokeStyle = "#bbb";
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(gx(X_MAX_POLA), gy(0));
        ctx.lineTo(gx(X_MAX_POLA), gy(P(X_MAX_POLA)));
        ctx.lineTo(gx(0), gy(P(X_MAX_POLA)));
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = WG_KOLORY.osie;
        ctx.textAlign = "center";
        ctx.textBaseline = "bottom";
        ctx.fillText("24/13", gx(X_MAX_POLA), gy(0) - 4);

        // Aktualny punkt na wykresie.
        ctx.fillStyle = max ? WG_KOLORY.ok : WG_KOLORY.punkt;
        ctx.beginPath();
        ctx.arc(gx(x), gy(pole), 6, 0, Math.PI * 2);
        ctx.fill();

        wgUstawHTML(readout,
            wgMath(`x = ${wgTexLiczba(x)},\\quad AD = 12 - 4x = ${wgTexLiczba(y)},\\quad P(x) = -26x^{2} + 96x = \\mathbf{${wgTexLiczba(pole)}}`) +
            (max ? `<br><span class="wg-ok">✓ największe pole przy ${wgMath("x = \\tfrac{24}{13}")}</span>` : ""));
    }

    slider.addEventListener("input", draw);
    draw();
}

// Rejestr widżetów: exercises.json nie może przechowywać funkcji, więc pole
// solutionInteractive to nazwa (string), a tu leży mapa nazwa → funkcja.
// Deklaracje funkcji są hoistowane, więc rejestr można zbudować przed nimi
// w kolejności pliku. Nowy widżet = nowa funkcja + wpis tutaj.
const WIDZETY = {
    widgetOsLiczbowa,
    widgetProcentSkladany,
    widgetNierownoscKwadratowa,
    widgetFunkcjaPrzedzialami,
    widgetParabola,
    widgetCiagArytmetyczny,
    widgetKoloTrygonometryczne,
    widgetKatWpisany,
    widgetProstopadloscian
};
