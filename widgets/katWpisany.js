// --- Zad 20: kąt wpisany i środkowy ----------------------------------------
// C przeciągany po dużym łuku — kąt wpisany ACB cały czas ma 60°, a środkowy 120°.

function widgetKatWpisany(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        "Przeciągaj punkt C po okręgu — kąt wpisany oparty na tym samym łuku się nie zmienia:"));

    const canvas = wgCanvas(wrap, 520, 310);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const cx = 260, cy = 155, R = 120;
    const A_DEG = 210, B_DEG = 330;          // kąt środkowy AB = 120° (łuk dołem)
    const pt = deg => ({
        x: cx + R * Math.cos(deg * Math.PI / 180),
        y: cy - R * Math.sin(deg * Math.PI / 180)
    });

    const state = { deg: 90 };

    function draw() {
        const A = pt(A_DEG), B = pt(B_DEG), C = pt(state.deg), S = { x: cx, y: cy };
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Okrąg.
        ctx.strokeStyle = WG_KOLORY.wykres;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, Math.PI * 2);
        ctx.stroke();

        // Łuk AB (dołem) — wyróżniony. W układzie canvasa (y w dół) punktowi o kącie
        // matematycznym θ odpowiada kąt −θ, więc łuk 210°→330° dołem to 30°→150°.
        ctx.strokeStyle = WG_KOLORY.punkt;
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.arc(cx, cy, R, 30 * Math.PI / 180, 150 * Math.PI / 180, false);
        ctx.stroke();
        ctx.fillStyle = WG_KOLORY.punkt;
        ctx.font = "13px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        ctx.fillText("łuk AB = ⅓ · 2π·6 = 4π", cx, cy + R + 12);

        // Ramiona kąta środkowego.
        ctx.strokeStyle = "#999";
        ctx.lineWidth = 1.5;
        [A, B].forEach(P => {
            ctx.beginPath();
            ctx.moveTo(S.x, S.y);
            ctx.lineTo(P.x, P.y);
            ctx.stroke();
        });
        // Łuczek kąta środkowego (między ramionami SA i SB, od strony łuku AB).
        ctx.strokeStyle = WG_KOLORY.zle;
        ctx.beginPath();
        ctx.arc(cx, cy, 26, 30 * Math.PI / 180, 150 * Math.PI / 180, false);
        ctx.stroke();
        ctx.fillStyle = WG_KOLORY.zle;
        ctx.font = "12px Arial";
        ctx.textBaseline = "top";
        ctx.fillText("120°", cx, cy + 32);

        // Ramiona kąta wpisanego.
        ctx.strokeStyle = "#444";
        [A, B].forEach(P => {
            ctx.beginPath();
            ctx.moveTo(C.x, C.y);
            ctx.lineTo(P.x, P.y);
            ctx.stroke();
        });

        // Miara kąta wpisanego (liczona z wektorów — zawsze wyjdzie 60°).
        const kat = (() => {
            const v1 = { x: A.x - C.x, y: A.y - C.y };
            const v2 = { x: B.x - C.x, y: B.y - C.y };
            const dot = v1.x * v2.x + v1.y * v2.y;
            const len = Math.hypot(v1.x, v1.y) * Math.hypot(v2.x, v2.y);
            return Math.acos(dot / len) * 180 / Math.PI;
        })();

        // Łuczek przy C.
        ctx.strokeStyle = WG_KOLORY.info;
        const a1 = Math.atan2(A.y - C.y, A.x - C.x);
        const a2 = Math.atan2(B.y - C.y, B.x - C.x);
        ctx.beginPath();
        // rysuj krótszy łuk między ramionami
        let od = a1, do_ = a2;
        if (((do_ - od + Math.PI * 2) % (Math.PI * 2)) > Math.PI) [od, do_] = [do_, od];
        ctx.arc(C.x, C.y, 22, od, do_, false);
        ctx.stroke();

        // Punkty.
        const punkty = [[A, "A"], [B, "B"], [S, "S"]];
        ctx.font = "bold 13px Arial";
        punkty.forEach(([P, name]) => {
            ctx.fillStyle = "#333";
            ctx.beginPath();
            ctx.arc(P.x, P.y, 3.5, 0, Math.PI * 2);
            ctx.fill();
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            const przesX = name === "S" ? 12 : (P.x - cx) * 0.14;
            const przesY = name === "S" ? -8 : (P.y - cy) * 0.14;
            ctx.fillText(name, P.x + przesX, P.y + przesY);
        });
        ctx.fillStyle = WG_KOLORY.info;
        ctx.beginPath();
        ctx.arc(C.x, C.y, 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText("C", C.x + (C.x - cx) * 0.16, C.y + (C.y - cy) * 0.16);

        wgUstawHTML(readout,
            `kąt wpisany ${wgMath(`\\angle ACB = \\mathbf{${Math.round(kat)}^{\\circ}}`)}, ` +
            `kąt środkowy ${wgMath("\\angle ASB = \\mathbf{120^{\\circ}}")}<br>` +
            `<span class="wg-neutral">środkowy jest zawsze 2× większy</span>`);
    }

    wgDraggable(canvas, null, pos => {
        let deg = Math.atan2(cy - pos.y, pos.x - cx) * 180 / Math.PI;
        if (deg < 0) deg += 360;
        // C zostaje na dużym łuku (nie wchodzi na łuk AB między 330° a 210° dołem).
        if (deg > 205 && deg < 270) deg = 205;
        if ((deg >= 270 && deg < 335)) deg = 335;
        state.deg = deg;
        draw();
    });
    draw();
}
