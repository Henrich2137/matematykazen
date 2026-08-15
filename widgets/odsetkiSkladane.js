// --- Zad 2 (2026-maj): odsetki z procentu składanego -----------------------
// Suwak oprocentowania + słupki kapitału po 0/1/2 latach. Odsetki doliczone
// w danym roku: górny segment słupka plus strzałka między słupkami z kwotą,
// bo sednem zadania jest to, że drugi rok liczy się od powiększonego kapitału.

function widgetOdsetkiSkladane(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmień oprocentowanie ${wgMath("p")} przy pomocy suwaka.`));

    const canvas = wgCanvas(wrap, 520, 250);
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
        const baseY = 215, maxVal = 12600, scale = 175 / maxVal;

        const etykiety = ["wpłata", "po 1 roku", "po 2 latach"];
        // Kwota odsetek w podpisie: bez groszy, gdy wychodzi okrągło.
        const zlKrotko = v => v.toLocaleString("pl-PL", { maximumFractionDigits: 2 }) + " zł";
        kwoty.forEach((kwota, i) => {
            // 65 zamiast 90, żeby środkowy słupek stał na środku płótna.
            const x = 65 + i * 150;
            const h = kwota * scale;
            // Odsetki doliczone w tym roku: górny segment słupka w kolorze
            // niewiadomej (odwraca się z motywem); kwota siedzi na strzałce
            // między słupkami. Dolna część to kapitał z poprzedniego roku.
            const hPoprz = i > 0 ? kwoty[i - 1] * scale : h;
            ctx.fillStyle = WG_KOLORY.slupek;
            ctx.fillRect(x, baseY - hPoprz, 90, hPoprz);
            if (i > 0) {
                ctx.globalAlpha = 0.3;
                ctx.fillStyle = WG_KOLORY.niewiadoma;
                ctx.fillRect(x, baseY - h, 90, h - hPoprz);
                ctx.globalAlpha = 1;
            }

            ctx.strokeStyle = WG_KOLORY.wykres;
            ctx.strokeRect(x, baseY - h, 90, h);

            ctx.fillStyle = WG_KOLORY.tekst;
            ctx.textAlign = "center";
            ctx.textBaseline = "bottom";
            ctx.font = "13px Arial";
            ctx.fillText(zl(kwota), x + 45, baseY - h - 4);
            ctx.textBaseline = "top";
            ctx.fillText(etykiety[i], x + 45, baseY + 6);
        });

        // Linia bazowa na poziomie wpłaty: widać, o ile każdy słupek
        // odchyla się od 10 000 zł.
        const bazaY = baseY - START * scale;
        ctx.strokeStyle = WG_KOLORY.linia;
        ctx.setLineDash([5, 4]);
        ctx.beginPath();
        ctx.moveTo(45, bazaY);
        ctx.lineTo(475, bazaY);
        ctx.stroke();
        ctx.setLineDash([]);

        // Strzałki między kolejnymi słupkami z kwotą odsetek doliczonych
        // w danym roku (żeby "+ 636 zł" nie wyglądało na sumę odsetek).
        for (let i = 1; i < kwoty.length; i++) {
            const xPoprz = 65 + (i - 1) * 150 + 90;
            const xTen = 65 + i * 150;
            const yPoprz = baseY - kwoty[i - 1] * scale;
            const yTen = baseY - kwoty[i] * scale;
            ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.niewiadoma;
            ctx.lineWidth = 1;
            wgStrzalka(ctx, xPoprz + 3, yPoprz, xTen - 3, yTen);
            ctx.font = "13px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "bottom";
            ctx.fillText("+ " + zlKrotko(kwoty[i] - kwoty[i - 1]),
                (xPoprz + xTen) / 2, Math.min(yPoprz, yTen) - 5);
        }

        // Odczyt: ustawione p, podstawienie do wzoru, suma odsetek z obu lat.
        // "p = ..." i suwak w kolorze niewiadomej (to uczeń nim rusza, ten sam
        // kolor co strzałki "+kwota"); trafienie w 6% zielenieje sumę odsetek.
        slider.style.accentColor = wgHex(WG_KOLORY.niewiadoma);
        const pTex = `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{p = ${wgTexLiczba(p, 1, 1)}\\%}`;
        const odsetki1 = kwoty[1] - kwoty[0];
        const odsetki2 = kwoty[2] - kwoty[1];
        wgUstawHTML(readout,
            wgMath(pTex) + `<br>` +
            wgMath(`10\\,000 \\cdot (1 + ${wgTexLiczba(r, 3)})^{2} = `) +
            ` <b>${zl(kwoty[2])}</b><br>` +
            `odsetki: ${zl(odsetki1)} + ${zl(odsetki2)} = ` +
            `<b${trafiony ? ` class="wg-ok"` : ""}>${zl(odsetki1 + odsetki2)}</b>`);
    }

    slider.addEventListener("input", draw);
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
