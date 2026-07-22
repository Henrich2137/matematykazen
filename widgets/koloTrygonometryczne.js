// --- Zad 18: koło trygonometryczne -----------------------------------------
// Przeciągany kąt na półokręgu; widać sin (pion) i cos (poziom) oraz to,
// że dla kąta rozwartego cosinus jest ujemny.

function widgetKoloTrygonometryczne(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Przeciągaj punkt po okręgu jednostkowym. Szukamy kąta <b>rozwartego</b> z ${wgMath("\\sin\\alpha = \\tfrac{\\sqrt{3}}{4} \\approx 0{,}433")}:`));

    const canvas = wgCanvas(wrap, 520, 300);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const cx = 260, cy = 175, R = 115;
    const SIN_CEL = Math.sqrt(3) / 4;      // ≈ 0,4330
    const COS_CEL = -Math.sqrt(13) / 4;    // ≈ −0,9014

    const state = { deg: 30 };

    function draw() {
        const rad = state.deg * Math.PI / 180;
        const sin = Math.sin(rad), cos = Math.cos(rad);
        const P = { x: cx + R * cos, y: cy - R * sin };
        const sinOk = Math.abs(sin - SIN_CEL) < 0.012;

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // II ćwiartka (kąty rozwarte) — delikatne tło.
        ctx.fillStyle = "rgba(74, 144, 217, 0.07)";
        ctx.fillRect(cx - R - 15, cy - R - 15, R + 15, R + 15);
        ctx.fillStyle = "#9bb8d4";
        ctx.font = "11px Arial";
        ctx.textAlign = "left";
        ctx.textBaseline = "top";
        ctx.fillText("kąty rozwarte (90°–180°)", cx - R - 10, cy - R - 10);

        // Osie i okrąg.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, cx - R - 25, cy, cx + R + 25, cy);
        wgStrzalka(ctx, cx, cy + R + 20, cx, cy - R - 20);
        ctx.strokeStyle = "#999";
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, Math.PI * 2);
        ctx.stroke();

        // Linia sin = √3/4.
        const yCel = cy - R * SIN_CEL;
        ctx.strokeStyle = WG_KOLORY.info;
        ctx.setLineDash([5, 4]);
        ctx.beginPath();
        ctx.moveTo(cx - R - 20, yCel);
        ctx.lineTo(cx + R + 20, yCel);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = WG_KOLORY.info;
        ctx.font = "11px Arial";
        ctx.textAlign = "left";
        ctx.textBaseline = "bottom";
        ctx.fillText("sin α = √3/4", cx + R - 40, yCel - 3);

        // Ramię kąta + łuk.
        ctx.strokeStyle = "#555";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(P.x, P.y);
        ctx.stroke();
        ctx.strokeStyle = "#aaa";
        ctx.beginPath();
        ctx.arc(cx, cy, 24, 0, -rad, true);
        ctx.stroke();

        // cos (poziomy, czerwony) i sin (pionowy, zielony).
        ctx.strokeStyle = WG_KOLORY.zle;
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(P.x, cy);
        ctx.stroke();
        ctx.strokeStyle = WG_KOLORY.ok;
        ctx.beginPath();
        ctx.moveTo(P.x, cy);
        ctx.lineTo(P.x, P.y);
        ctx.stroke();

        // Punkt na okręgu.
        ctx.fillStyle = sinOk ? (cos < 0 ? WG_KOLORY.ok : WG_KOLORY.punkt) : "#333";
        ctx.beginPath();
        ctx.arc(P.x, P.y, 7, 0, Math.PI * 2);
        ctx.fill();

        const fmtTex = v => wgTexLiczba(v, 3, 3);
        let dodatek = "";
        if (sinOk && cos < 0) {
            dodatek = `<span class="wg-ok">✓ kąt rozwarty: ${wgMath(`\\cos\\alpha = -\\tfrac{\\sqrt{13}}{4} \\approx ${fmtTex(COS_CEL)}`)}</span>`;
        } else if (sinOk) {
            dodatek = `<span class="wg-neutral">sin się zgadza, ale ten kąt jest ostry — przejdź na lewą stronę!</span>`;
        }
        // Kolory sin/cos we wzorze = kolory odcinków na rysunku (KaTeXowy \textcolor).
        wgUstawHTML(readout,
            wgMath(`\\alpha \\approx ${Math.round(state.deg)}^{\\circ},\\quad ` +
                `\\textcolor{${WG_KOLORY.ok}}{\\sin\\alpha \\approx ${fmtTex(sin)}},\\quad ` +
                `\\textcolor{${WG_KOLORY.zle}}{\\cos\\alpha \\approx ${fmtTex(cos)}}`) +
            (dodatek ? `<br>${dodatek}` : ""));
    }

    // Kąt, przy którym sin α = √3/4 po stronie rozwartej (~154,3°) — i jego
    // ostre lustro; przyciąganie ułatwia trafienie dokładnie w tę sytuację.
    const KAT_CEL = 180 - Math.asin(SIN_CEL) * 180 / Math.PI;
    wgDraggable(canvas, null, pos => {
        let deg = Math.atan2(cy - pos.y, pos.x - cx) * 180 / Math.PI;
        deg = Math.max(0, Math.min(180, deg));
        const snap = wgPrzyciagnij(deg, [KAT_CEL, 180 - KAT_CEL], 2.5);
        state.deg = snap !== deg ? snap : Math.round(deg * 2) / 2;
        draw();
    });
    draw();
}
