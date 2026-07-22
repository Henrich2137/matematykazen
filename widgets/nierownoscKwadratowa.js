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
