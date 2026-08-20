// SPDX-FileCopyrightText: 2026 Henrich2137
// SPDX-License-Identifier: LicenseRef-MatematykaZen-Proprietary
// Wszelkie prawa zastrzeżone / All rights reserved. Licencja: widgets/LICENSE.md
// NIE jest objęty PolyForm Noncommercial / NOT covered by PolyForm Noncommercial.

// --- Zad 11 (2026-maj): bilety do teatru (n + u = 200, zostaje 4665 zł) ----
// Suwak rusza liczbą biletów normalnych n. Niski wykres pokazuje kwotę po
// kosztach w zależności od n (prosta 3750 + 7,5n) z zieloną linią celu
// 4665 zł. Rachunek pod suwakiem jest ułożony w kolumny jak w tabelce
// (n pod n, u pod u), żeby nic nie skakało przy przewijaniu suwaka.

function widgetBilety(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmień liczbę biletów normalnych ${wgMath("n")} przy pomocy suwaka.`));

    const canvas = wgCanvas(wrap, 520, 175);
    const ctx = canvas.getContext("2d");

    const controls = wgElement("div", "widget-controls",
        `<input type="range" min="0" max="200" step="1" value="50">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const slider = controls.querySelector("input");
    const RAZEM = 200, CENA_N = 35, CENA_U = 25, CEL = 4665;

    const px = n => 40 + n / RAZEM * 450;
    // Oś pieniędzy: 3600..5400 zł mieści całą prostą (3750 przy n=0, 5250 przy n=200).
    const py = v => 140 - (v - 3600) / 1800 * 120;

    function draw() {
        const n = parseInt(slider.value, 10);
        const u = RAZEM - n;
        const wplywy = n * CENA_N + u * CENA_U;
        const poKosztach = 0.75 * wplywy;
        const trafiony = Math.abs(poKosztach - CEL) < 0.001;

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Oś n z podziałką co 50 biletów.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, 30, 140, 505, 140);
        ctx.font = "11px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        for (let i = 0; i <= RAZEM; i += 50) {
            ctx.beginPath();
            ctx.moveTo(px(i), 137);
            ctx.lineTo(px(i), 143);
            ctx.stroke();
            ctx.fillText(i, px(i), 146);
        }
        ctx.textAlign = "left";
        ctx.fillText("n", 508, 146);

        // Linia celu: zostało 4665 zł (zielona przerywana, jak cel w zad. 5 grudnia).
        ctx.strokeStyle = WG_KOLORY.ok;
        ctx.setLineDash([6, 4]);
        ctx.beginPath();
        ctx.moveTo(40, py(CEL));
        ctx.lineTo(490, py(CEL));
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = WG_KOLORY.ok;
        ctx.font = "12px Arial";
        ctx.textAlign = "left";
        ctx.textBaseline = "bottom";
        ctx.fillText("zostało: 4 665 zł", 42, py(CEL) - 3);

        // Kwota po kosztach w zależności od n: prosta 3750 + 7,5n.
        ctx.strokeStyle = WG_KOLORY.wykres;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(px(0), py(3750));
        ctx.lineTo(px(RAZEM), py(3750 + 7.5 * RAZEM));
        ctx.stroke();

        // Punkt bieżącego n na prostej + zejście do osi.
        ctx.strokeStyle = WG_KOLORY.liniaSlaba;
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(px(n), py(poKosztach));
        ctx.lineTo(px(n), 140);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(px(n), py(poKosztach), 6, 0, Math.PI * 2);
        ctx.fill();

        // Suwak w kolorze niewiadomej (to nim rusza uczeń), jak w zad. 2.
        slider.style.accentColor = wgHex(WG_KOLORY.niewiadoma);

        // Rachunek w kolumnach (n pod n, u pod u, wyniki pod sobą).
        // \hphantom dopycha liczby do trzech cyfr, żeby kolumny nie skakały.
        const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
        const pad3 = v => `\\hphantom{${"0".repeat(3 - String(v).length)}}${v}`;
        const zl = v => `${wgTexLiczba(v)}\\ \\text{zł}`;
        wgUstawHTML(readout,
            wgMath(
                `\\begin{array}{rclcl}` +
                `${nieb("n")} & + & u & = & 200\\\\` +
                `${nieb(pad3(n))} & + & ${pad3(u)} & = & 200\\\\` +
                `${nieb(pad3(n))} \\cdot 35\\ \\text{zł} & + & ${pad3(u)} \\cdot 25\\ \\text{zł} & = & ${zl(wplywy)}` +
                `\\end{array}`) + `<br>` +
            wgMath(`${zl(wplywy)} - 25\\% = ${zl(poKosztach)}`) +
            (trafiony ? ` <span class="wg-ok">✓</span>`
                      : ` <span class="wg-zle">✗</span>`));
    }

    slider.addEventListener("input", draw);
    // Przemalowanie po zmianie motywu (paleta z CSS, app/widget-helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
