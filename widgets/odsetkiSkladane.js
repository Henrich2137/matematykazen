// --- Zad 2 (2026-maj): odsetki z procentu składanego -----------------------
// Suwak oprocentowania + słupki kapitału po 0/1/2 latach. Odsetki doliczone
// w danym roku są zaznaczone jako górny segment słupka, z podpisem "+kwota",
// bo sednem zadania jest to, że drugi rok liczy się od powiększonego kapitału.

function widgetOdsetkiSkladane(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmień oprocentowanie ${wgMath("p")} przy pomocy suwaka.`));

    const canvas = wgCanvas(wrap, 520, 230);
    const ctx = canvas.getContext("2d");

    const controls = wgElement("div", "widget-controls",
        `<input type="range" min="0" max="10" step="0.1" value="6">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const slider = controls.querySelector("input");
    const START = 10000, P_ZADANIA = 6;

    const zl = v => v.toLocaleString("pl-PL", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " zł";

    function draw() {
        const p = parseFloat(slider.value);
        const r = p / 100;
        const kwoty = [START, START * (1 + r), START * (1 + r) * (1 + r)];
        // Trafienie = ustawione oprocentowanie z zadania (6%).
        const trafiony = Math.abs(p - P_ZADANIA) < 0.05;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // maxVal z zapasem na kapitał przy p = 10% (12 100 zł) plus podpisy.
        const baseY = 195, maxVal = 12600, scale = 160 / maxVal;

        const etykiety = ["wpłata", "po 1 roku", "po 2 latach"];
        // Kwota odsetek w podpisie: bez groszy, gdy wychodzi okrągło.
        const zlKrotko = v => v.toLocaleString("pl-PL", { maximumFractionDigits: 2 }) + " zł";
        kwoty.forEach((kwota, i) => {
            // 65 zamiast 90, żeby środkowy słupek stał na środku płótna.
            const x = 65 + i * 150;
            const h = kwota * scale;
            // Odsetki doliczone w tym roku: górny segment słupka w kolorze
            // niewiadomej (odwraca się z motywem), plus podpis nad słupkiem.
            // Dolna część słupka to kapitał z poprzedniego roku.
            const hPoprz = i > 0 ? kwoty[i - 1] * scale : h;
            ctx.fillStyle = WG_KOLORY.slupek;
            ctx.fillRect(x, baseY - hPoprz, 90, hPoprz);
            if (i > 0) {
                ctx.globalAlpha = 0.3;
                ctx.fillStyle = WG_KOLORY.niewiadoma;
                ctx.fillRect(x, baseY - h, 90, h - hPoprz);
                ctx.globalAlpha = 1;
                ctx.fillStyle = WG_KOLORY.niewiadoma;
                ctx.font = "12px Arial";
                ctx.textAlign = "center";
                ctx.textBaseline = "bottom";
                ctx.fillText("( + " + zlKrotko(kwota - kwoty[i - 1]) + " )", x + 45, baseY - h - 24);
            }

            ctx.strokeStyle = WG_KOLORY.wykres;
            ctx.strokeRect(x, baseY - h, 90, h);

            ctx.fillStyle = WG_KOLORY.tekst;
            ctx.textAlign = "center";
            ctx.textBaseline = "bottom";
            ctx.font = "12px Arial";
            ctx.fillText(zl(kwota), x + 45, baseY - h - 4);
            ctx.textBaseline = "top";
            ctx.fillText(etykiety[i], x + 45, baseY + 6);
        });

        // Odczyt w dwóch linijkach: ustawione p, pod nim podstawienie do wzoru.
        // Przy oprocentowaniu z zadania (6%) zielenieje istniejące "p = 6,0%".
        const pTex = `p = ${wgTexLiczba(p, 1, 1)}\\%`;
        wgUstawHTML(readout,
            wgMath(trafiony ? `\\textcolor{${wgHex(WG_KOLORY.ok)}}{${pTex}}` : pTex) + `<br>` +
            wgMath(`10\\,000 \\cdot (1 + ${wgTexLiczba(r, 3)})^{2} = `) +
            ` <b>${zl(kwoty[2])}</b>`);
    }

    slider.addEventListener("input", draw);
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
