// SPDX-FileCopyrightText: 2026 Henrich2137
// SPDX-License-Identifier: LicenseRef-MatematykaZen-Proprietary
// Wszelkie prawa zastrzeżone / All rights reserved. Licencja: widgets/LICENSE.md
// NIE jest objęty PolyForm Noncommercial / NOT covered by PolyForm Noncommercial.

// --- Zad 12.1: monotoniczność paraboli -------------------------------------
// f(x) = −(x−3)²: punkt do przeciągania po wykresie, a gałąź, na której ten
// punkt właśnie stoi, zapala się na zielono.
//
// KOLORY ZMIENIONE 2026-08-30 (Henrich: „użyj innych kolorów, bo obecne
// wprowadzają w błąd co do tego, którą odpowiedź wybrać"). Wcześniej gałąź
// rosnąca była na stałe ZIELONA, a malejąca CZERWONA, czyli dokładnie odwrotnie,
// niż wypada odpowiedź: szukamy przedziału, w którym funkcja MALEJE, więc uczeń
// widział poprawną odpowiedź pomalowaną na czerwono. To łamie też COLORS.md,
// gdzie zieleń i czerwień znaczą wyłącznie „dobrze/źle".
//
// Teraz: cała parabola jest fioletowa (rola „wykres funkcji jak w arkuszach
// CKE"), przeciągany punkt niebieski (rola „podstawianie pod x"), wierzchołek
// pomarańczowy (rola „punkt / uchwyt"), a zieleń jest RUCHOMA i znaczy „tu
// jesteś, tutaj patrz" (rola „oznaczenie miejsca"). Żaden kolor nie mówi już
// „ta odpowiedź jest dobra".

function widgetParabola(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `${wgMath("f(x) = -(x - 3)^{2}")}. Przeciągaj punkt po paraboli, a zapali się gałąź, na której stoisz. Monotoniczność zmienia się dokładnie w wierzchołku:`));

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
        ctx.strokeStyle = WG_KOLORY.liniaSlaba;
        ctx.setLineDash([5, 4]);
        ctx.beginPath();
        ctx.moveTo(px(3), 245);
        ctx.lineTo(px(3), 20);
        ctx.stroke();
        ctx.setLineDash([]);

        // Obie gałęzie fioletowe; zapala się tylko ta, na której stoi punkt.
        // Zieleń znaczy „tu patrz", a nie „ta odpowiedź jest dobra".
        const naLewej = state.x < 3;
        const naPrawej = state.x > 3;
        rysujGalaz(X0, 3, naLewej ? WG_KOLORY.zielony : WG_KOLORY.wykres);
        rysujGalaz(3, X1, naPrawej ? WG_KOLORY.zielony : WG_KOLORY.wykres);

        // Wierzchołek: stały punkt odniesienia, więc pomarańczowy, a nie
        // w kolorze krzywej (na fiolecie by zniknął).
        ctx.fillStyle = WG_KOLORY.punkt;
        ctx.beginPath();
        ctx.arc(px(3), py(0), 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.font = "12px Arial";
        ctx.textBaseline = "bottom";
        ctx.fillText("W = (3, 0)", px(3) + 38, py(0) - 4);

        // Punkt użytkownika: to on podstawia liczbę pod x, więc błękit.
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(px(state.x), py(f(state.x)), 7, 0, Math.PI * 2);
        ctx.fill();

        const xTex = wgMath(`x = ${wgTexLiczba(state.x, 1)}`);
        wgUstawHTML(readout, state.x === 3
            ? `${xTex}<br><b>wierzchołek</b>: tu funkcja przechodzi z rośnięcia w malenie`
            : naLewej
                ? `${xTex}<br><span class="wg-neutral">↗ funkcja rośnie (${wgMath("x < 3")})</span>`
                : `${xTex}<br><span class="wg-neutral">↘ funkcja maleje (${wgMath("x > 3")}), czyli w przedziale ${wgMath("\\langle 3, +\\infty)")}</span>`);
    }

    wgDraggable(canvas, null, pos => {
        const raw = Math.min(X1, Math.max(X0, vx(pos.x)));
        // Przyciąganie do wierzchołka; poza nim krok co 0,5.
        const snap = wgPrzyciagnij(raw, [3], 0.3);
        state.x = snap !== raw ? snap : Math.round(raw * 2) / 2;
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS — app/widget-helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
