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
