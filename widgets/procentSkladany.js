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
