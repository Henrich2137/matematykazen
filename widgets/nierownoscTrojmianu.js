// SPDX-FileCopyrightText: 2026 Henrich2137
// SPDX-License-Identifier: LicenseRef-MatematykaZen-Proprietary
// Wszelkie prawa zastrzeżone / All rights reserved. Licencja: widgets/LICENSE.md
// NIE jest objęty PolyForm Noncommercial / NOT covered by PolyForm Noncommercial.

// --- Zad 10 (2026-maj): nierówność 3x² + 4x ≥ 6x + 8 -----------------------
// Po uproszczeniu: 3x² − 2x − 8 ≥ 0. Parabola z zaznaczonymi przedziałami
// rozwiązań (na zewnątrz miejsc zerowych); punkt do przeciągania po osi x
// pokazuje, czy nierówność jest spełniona. Wzorowany na widżecie zad. 9
// z 2024-grudnia (nierownoscKwadratowa.js).

function widgetNierownoscTrojmianu(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Kliknij na dowolne miejsce na osi lub przeciągnij punkty, aby podstawić liczbę pod ${wgMath("x")}.`));

    const canvas = wgCanvas(wrap, 520, 260);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const X0 = -4, X1 = 6, Y0 = -14, Y1 = 34;
    const PIERW1 = -4 / 3, PIERW2 = 2;
    const px = x => 20 + (x - X0) / (X1 - X0) * 480;
    const py = y => 240 - (y - Y0) / (Y1 - Y0) * 230;
    const vx = p => X0 + (p - 20) / 480 * (X1 - X0);
    const f = x => 3 * x * x - 2 * x - 8;

    const state = { x: 1 };

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Obszary rozwiązań (parabola nad osią, na zewnątrz miejsc zerowych).
        ctx.fillStyle = WG_KOLORY.obszarOk;
        [[X0, PIERW1], [PIERW2, X1]].forEach(([a, b]) => {
            ctx.beginPath();
            ctx.moveTo(px(a), py(0));
            for (let x = a; x <= b; x += 0.05) ctx.lineTo(px(x), py(f(x)));
            ctx.lineTo(px(b), py(0));
            ctx.closePath();
            ctx.fill();
        });

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
            // +11 = promień punktu x (7) + odstęp, żeby kropka nie zasłaniała liczb.
            ctx.fillText(i, px(i), py(0) + 11);
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

        // Przedziały rozwiązań na osi: dwa promienie na zewnątrz pierwiastków.
        ctx.strokeStyle = WG_KOLORY.ok;
        ctx.lineWidth = 5;
        [[px(X0), px(PIERW1)], [px(PIERW2), px(X1)]].forEach(([a, b]) => {
            ctx.beginPath();
            ctx.moveTo(a, py(0));
            ctx.lineTo(b, py(0));
            ctx.stroke();
        });
        ctx.fillStyle = WG_KOLORY.ok;
        [[PIERW1, "−4/3"], [PIERW2, "2"]].forEach(([x, label]) => {
            ctx.beginPath();
            ctx.arc(px(x), py(0), 5, 0, Math.PI * 2);
            ctx.fill();
            ctx.font = "bold 12px Arial";
            ctx.textBaseline = "bottom";
            ctx.fillText(label, px(x), py(0) - 8);
        });

        // Punkt testowy na osi + wartość na paraboli.
        const val = f(state.x);
        const spelnia = val >= -1e-9;
        ctx.strokeStyle = WG_KOLORY.liniaSlaba;
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(px(state.x), py(0));
        ctx.lineTo(px(state.x), py(f(state.x)));
        ctx.stroke();
        ctx.setLineDash([]);

        // Punkt ma kolor PODSTAWIANIA (--wg-niewiadoma) niezależnie od tego,
        // czy nierówność wychodzi; o wyniku mówi ✓/✗ w odczycie pod spodem.
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(px(state.x), py(0), 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(px(state.x), py(f(state.x)), 4, 0, Math.PI * 2);
        ctx.fill();

        // Odczyt: postać ogólna, a pod nią to samo z podstawioną liczbą.
        // Pierwiastek -4/3 dostaje zapis ułamkiem, żeby podstawienie było
        // dokładne, a nie zaokrąglone do -1,33.
        const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
        const ulamek = state.x === PIERW1;
        const liczba = ulamek ? `-\\tfrac{4}{3}` : wgTexLiczba(state.x);
        // Ujemna liczba w nawiasie, bo stoi po znaku mnożenia albo przed ^2.
        const wNawiasie = state.x < 0 ? `\\left(${liczba}\\right)` : liczba;
        wgUstawHTML(readout,
            wgMath(`3${nieb("x")}^{2} - 2${nieb("x")} - 8 \\ge 0`) + `<br>` +
            wgMath(`3 \\cdot ${nieb(wNawiasie)}^{2} - 2 \\cdot ${nieb(wNawiasie)} - 8 \\ge 0`) +
            (spelnia ? ` <span class="wg-ok">✓</span>`
                     : ` <span class="wg-zle">✗</span>`));
    }

    wgDraggable(canvas, null, pos => {
        const raw = Math.min(X1, Math.max(X0, vx(pos.x)));
        // Przyciąganie do pierwiastków; poza nimi płynnie (krok 0,05).
        const snap = wgPrzyciagnij(raw, [PIERW1, PIERW2], 0.3);
        state.x = snap !== raw ? snap : Math.round(raw * 20) / 20;
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS, app/widget-helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
