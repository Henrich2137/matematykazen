// SPDX-FileCopyrightText: 2026 Henrich2137
// SPDX-License-Identifier: LicenseRef-MatematykaZen-Proprietary
// Wszelkie prawa zastrzeżone / All rights reserved. Licencja: widgets/LICENSE.md
// NIE jest objęty PolyForm Noncommercial / NOT covered by PolyForm Noncommercial.

// --- Zad 13.1 i 13.2 (2026-maj): funkcja liniowa f(x) = ax + b -------------
// Rysunek z arkusza: prosta malejąca przez (-2, 0) i (0, -3), kąt alfa przy
// osi Ox. 13.1: dwa suwaki (a obraca, b unosi; b także punktem na osi y).
// 13.2: trójkąt na ramieniu kąta alfa jak w tablicach (s. 11, definicja
// funkcji trygonometrycznych dowolnego kąta): tg alfa = y/x, minus bierze
// się z ujemnego x, nie z y. Układ współrzędnych: wgUklad/wgRysujUklad.

const LINIOWA_ZAKRES = { X0: -5.4, X1: 5.8, Y0: -4.9, Y1: 5.3, szer: 520 };

function liniowaUklad(canvas) {
    return wgUklad(Object.assign({}, LINIOWA_ZAKRES, { wys: canvas.height }));
}

// Prosta y = ax + b przez całą szerokość układu.
function liniowaProsta(ctx, u, a, b) {
    ctx.strokeStyle = WG_KOLORY.wykres;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(u.px(u.X0), u.py(a * u.X0 + b));
    ctx.lineTo(u.px(u.X1), u.py(a * u.X1 + b));
    ctx.stroke();
}

// Łuk kąta alfa przy przecięciu prostej z osią Ox (jak na rysunku CKE):
// od dodatniej półosi x do ramienia prostej idącego w górę.
function liniowaKat(ctx, u, a, b) {
    if (a === 0) return;
    const x0 = -b / a;
    if (x0 < u.X0 + 0.3 || x0 > u.X1 - 0.3) return;
    const alfa = a > 0 ? Math.atan(a) : Math.PI + Math.atan(a);
    const cx = u.px(x0), cy = u.py(0), r = 26;
    ctx.fillStyle = WG_KOLORY.obszarWykres;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    // Na płótnie oś y rośnie w dół, stąd kąt ze znakiem minus.
    ctx.arc(cx, cy, r, 0, -alfa, true);
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle = WG_KOLORY.wykres;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, -alfa, true);
    ctx.stroke();
    ctx.fillStyle = WG_KOLORY.wykres;
    ctx.font = "italic bold 13px Georgia";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    const srodek = -alfa / 2;
    ctx.fillText("α", cx + (r + 11) * Math.cos(srodek), cy + (r + 11) * Math.sin(srodek));
}

// --- Zad 13.1: znaki współczynników a i b ----------------------------------

function widgetLiniowaWspolczynniki(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmień ${wgMath("a")} i ${wgMath("b")} suwakami; ${wgMath("b")} możesz też przeciągać punktem na osi ${wgMath("y")}.`));

    const canvas = wgCanvas(wrap, 520, wgWysokoscKwadratowa(LINIOWA_ZAKRES));
    const ctx = canvas.getContext("2d");
    const u = liniowaUklad(canvas);

    const controls = wgElement("div", "widget-controls",
        `<span class="wg-suwak-etykieta"></span><input type="range" min="-3" max="3" step="0.05" value="-1.5"><br>` +
        `<span class="wg-suwak-etykieta"></span><input type="range" min="-4" max="4" step="0.05" value="-3">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const [suwakA, suwakB] = controls.querySelectorAll("input");
    const [etykietaA, etykietaB] = controls.querySelectorAll(".wg-suwak-etykieta");
    const state = { a: -1.5, b: -3 };

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
    const zol = tex => `\\textcolor{${wgHex(WG_KOLORY.zolty)}}{${tex}}`;

    // Znak liczby zapisany do porównania w odczycie (wsparcie dla zdań P/F).
    const znak = v => v < 0 ? "< 0" : (v > 0 ? "> 0" : "= 0");

    function draw() {
        const { a, b } = state;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        wgRysujUklad(ctx, u);
        liniowaKat(ctx, u, a, b);
        liniowaProsta(ctx, u, a, b);

        // Punkt przecięcia z osią y w kolorze b (można go przeciągać).
        ctx.fillStyle = WG_KOLORY.zolty;
        ctx.beginPath();
        ctx.arc(u.px(0), u.py(b), 7, 0, Math.PI * 2);
        ctx.fill();

        suwakA.style.accentColor = wgHex(WG_KOLORY.niewiadoma);
        suwakB.style.accentColor = wgHex(WG_KOLORY.zolty);
        wgUstawHTML(etykietaA, wgMath(nieb(`a = ${wgTexLiczba(a)}`)));
        wgUstawHTML(etykietaB, wgMath(zol(`b = ${wgTexLiczba(b)}`)));

        // Odczyt: wzór z kolorami a i b oraz znaki obu współczynników
        // (dokładnie o to pytają zdania P/F).
        const bTex = b < 0 ? `- ${wgTexLiczba(-b)}` : `+ ${wgTexLiczba(b)}`;
        wgUstawHTML(readout,
            wgMath(`f(x) = ${nieb(wgTexLiczba(a))}x ${zol(bTex)}`) + `<br>` +
            wgMath(`${nieb(`a ${znak(a)}`)} \\qquad ${zol(`b ${znak(b)}`)}`));
    }

    suwakA.addEventListener("input", () => {
        state.a = wgPrzyciagnij(parseFloat(suwakA.value), [-1.5], 0.08);
        draw();
    });
    suwakB.addEventListener("input", () => {
        state.b = wgPrzyciagnij(parseFloat(suwakB.value), [-3], 0.08);
        draw();
    });
    // Przeciąganie po płótnie ustawia b (wysokość punktu na osi y).
    wgDraggable(canvas, null, pos => {
        const raw = Math.max(-4, Math.min(4, u.vy(pos.y)));
        const snap = wgPrzyciagnij(raw, [-3], 0.15);
        state.b = snap !== raw ? snap : Math.round(raw * 20) / 20;
        suwakB.value = state.b;
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS, app/widget-helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}

// --- Zad 13.2: tangens kąta alfa -------------------------------------------

function widgetLiniowaTangens(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmień ${wgMath("a")} przy pomocy suwaka i obserwuj trójkąt przy kącie ${wgMath("\\alpha")}.`));

    const canvas = wgCanvas(wrap, 520, wgWysokoscKwadratowa(LINIOWA_ZAKRES));
    const ctx = canvas.getContext("2d");
    const u = liniowaUklad(canvas);

    const controls = wgElement("div", "widget-controls",
        `<span class="wg-suwak-etykieta"></span><input type="range" min="-3" max="3" step="0.05" value="-1.5">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const suwak = controls.querySelector("input");
    const etykieta = controls.querySelector(".wg-suwak-etykieta");
    const B = -3;
    const state = { a: -1.5 };

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
    const zol = tex => `\\textcolor{${wgHex(WG_KOLORY.zolty)}}{${tex}}`;

    function draw() {
        const a = state.a;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        wgRysujUklad(ctx, u);
        liniowaKat(ctx, u, a, B);
        liniowaProsta(ctx, u, a, B);

        // Trójkąt na ramieniu kąta alfa (idziemy od wierzchołka W GÓRĘ po
        // prostej, jak w definicji z tablic): pionowa przyprostokątna
        // y = 3 (zawsze dodatnia), pozioma x = 3/a (ujemna, gdy idziemy
        // w lewo) - stąd znak tangensa siedzi w x.
        const x0 = -B / a;          // wierzchołek kąta (przecięcie z osią x)
        const dx = -B / a;          // x = 3/a, ze znakiem
        const xr = x0 + dx;         // róg trójkąta przy kącie prostym

        // Pozioma przyprostokątna (mianownik).
        ctx.strokeStyle = WG_KOLORY.niewiadoma;
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(u.px(x0), u.py(0));
        ctx.lineTo(u.px(xr), u.py(0));
        ctx.stroke();
        // Pionowa przyprostokątna (licznik).
        ctx.strokeStyle = WG_KOLORY.zolty;
        ctx.beginPath();
        ctx.moveTo(u.px(xr), u.py(0));
        ctx.lineTo(u.px(xr), u.py(3));
        ctx.stroke();
        // Znacznik kąta prostego.
        ctx.strokeStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        const k = dx > 0 ? -8 : 8;
        ctx.strokeRect(u.px(xr) + Math.min(k, 0), u.py(0) - 8, 8, 8);

        // Podpisy przyprostokątnych w notacji z tablicy wzorów (s. 11):
        // x i y to współrzędne liczone od wierzchołka kąta.
        ctx.font = "bold 13px Arial";
        // Nad osią (w trójkącie), żeby nie nachodził na liczby podziałki.
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.textAlign = "center";
        ctx.textBaseline = "bottom";
        ctx.fillText("x = " + wgTexLiczba(dx).replace("{,}", ","), (u.px(x0) + u.px(xr)) / 2, u.py(0) - 7);
        ctx.fillStyle = WG_KOLORY.zolty;
        ctx.textAlign = dx > 0 ? "left" : "right";
        ctx.textBaseline = "middle";
        ctx.fillText("y = 3", u.px(xr) + (dx > 0 ? 8 : -8), u.py(1.5));

        suwak.style.accentColor = wgHex(WG_KOLORY.niewiadoma);
        wgUstawHTML(etykieta, wgMath(nieb(`a = ${wgTexLiczba(a)}`)));

        // Odczyt: definicja tangensa z podstawionymi przyprostokątnymi.
        // Minus (dla prostej malejącej) bierze się z ujemnego x.
        const trafiony = a === -1.5;
        const komentarz = a < 0
            ? `idziemy w lewo, więc ${wgMath(nieb("x < 0"))} i tangens jest ujemny`
            : `idziemy w prawo, więc ${wgMath(nieb("x > 0"))} i tangens jest dodatni`;
        wgUstawHTML(readout,
            wgMath(`\\operatorname{tg}\\alpha = \\dfrac{y}{x} = \\dfrac{${zol("3")}}{${nieb(wgTexLiczba(dx))}}`) +
            (trafiony ? ` <span class="wg-ok">✓</span>` : "") + `<br>` +
            komentarz);
    }

    suwak.addEventListener("input", () => {
        let a = parseFloat(suwak.value);
        // Okolice zera odpadają: trójkąt uciekałby poza rysunek.
        if (Math.abs(a) < 0.5) a = (a >= 0 ? 0.5 : -0.5);
        state.a = wgPrzyciagnij(a, [-1.5], 0.08);
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS, app/widget-helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
