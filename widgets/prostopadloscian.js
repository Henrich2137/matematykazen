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
