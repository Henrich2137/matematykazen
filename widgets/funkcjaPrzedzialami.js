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
