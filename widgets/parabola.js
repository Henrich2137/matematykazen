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
