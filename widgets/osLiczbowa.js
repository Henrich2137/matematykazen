// --- Zad 1: oś liczbowa |x + a| = b --------------------------------------
// Środek (−a) + dwa rozwiązania w odległości b. Zielony punkt testowy do
// przeciągania pokazuje, jak zmienia się |x + a|.

function widgetOsLiczbowa(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Rozwiązania ${wgMath("|x + a| = b")} to liczby odległe o ${wgMath("b")} od liczby ${wgMath("(-a)")}. Przeciągaj żółty punkt i zmieniaj a, b:`));

    const canvas = wgCanvas(wrap, 520, 130);
    const ctx = canvas.getContext("2d");

    // Kolory okienek = kolory na osi: a (zielone) to środek −a, b (niebieskie)
    // to strzałki odległości. Reset przywraca dane z zadania. Okienek <input>
    // nie da się włożyć do wzoru KaTeXa, więc wzór jest sklejony z kawałków
    // KaTeXa wokół pól.
    const controls = wgElement("div", "widget-controls",
        `<span class="wg-wzor-z-polami">${wgMath("|\\,x\\,+")} <input type="number" class="wg-a" value="4"> ${wgMath("\\,| =")} <input type="number" class="wg-b" value="7"></span>` +
        `<button class="light-button wg-reset" title="Przywróć a = 4, b = 7">↺ reset</button>`);
    wrap.appendChild(controls);

    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const aInput = controls.querySelector(".wg-a");
    const bInput = controls.querySelector(".wg-b");

    const MIN = -15, MAX = 5;
    const state = { x: 0 };
    const toPix = v => 20 + (v - MIN) / (MAX - MIN) * (canvas.width - 40);
    const toVal = px => MIN + (px - 20) / (canvas.width - 40) * (MAX - MIN);

    function draw() {
        const a = parseFloat(aInput.value) || 0;
        const b = parseFloat(bInput.value) || 0;
        const centerY = 85;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Oś ze strzałką i podziałką.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, 12, centerY, canvas.width - 4, centerY);
        ctx.font = "11px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        for (let i = MIN; i <= MAX; i++) {
            const px = toPix(i);
            ctx.beginPath();
            ctx.moveTo(px, centerY - 3);
            ctx.lineTo(px, centerY + 3);
            ctx.stroke();
            ctx.fillText(i, px, centerY + 7);
        }

        const center = -a;
        // Strzałki odległości b od środka do obu rozwiązań — każda na innej
        // wysokości i lekko skrócona z obu końców, żeby nie zlewały się
        // w jedną długą linię przechodzącą przez środek.
        if (b >= 0) {
            ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.info;
            ctx.lineWidth = 1.5;
            [[center + b, centerY - 26], [center - b, centerY - 42]].forEach(([sol, y]) => {
                if (Math.abs(sol - center) < 0.01) return;
                const odX = toPix(center), doX = toPix(sol);
                const kier = Math.sign(doX - odX);
                wgStrzalka(ctx, odX + kier * 7, y, doX - kier * 5, y);
                ctx.font = "12px Arial";
                ctx.textBaseline = "bottom";
                ctx.fillText(`${b}`, (odX + doX) / 2, y - 3);
            });

            // Rozwiązania (pomarańczowe punkty).
            ctx.fillStyle = WG_KOLORY.punkt;
            [center + b, center - b].forEach(sol => {
                if (sol >= MIN && sol <= MAX) {
                    ctx.beginPath();
                    ctx.arc(toPix(sol), centerY, 5, 0, Math.PI * 2);
                    ctx.fill();
                }
            });
        }

        // Środek (−a) — zielony, jak okienko z a (ta sama liczba, tylko z minusem).
        ctx.fillStyle = "#2e7d32";
        if (center >= MIN && center <= MAX) {
            ctx.beginPath();
            ctx.arc(toPix(center), centerY, 4, 0, Math.PI * 2);
            ctx.fill();
        }

        // Punkt testowy x (ciemnożółty) + jego odległość od środka;
        // po trafieniu w rozwiązanie dostaje zieloną obwódkę.
        const dist = Math.abs(state.x + a);
        const trafiony = b >= 0 && Math.abs(dist - b) < 0.01;
        ctx.fillStyle = "#c99700";
        ctx.beginPath();
        ctx.arc(toPix(state.x), centerY, 7, 0, Math.PI * 2);
        ctx.fill();
        if (trafiony) {
            ctx.strokeStyle = WG_KOLORY.ok;
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.arc(toPix(state.x), centerY, 10, 0, Math.PI * 2);
            ctx.stroke();
        }

        wgUstawHTML(readout,
            wgMath(`|\\,${wgTexLiczba(state.x)} + ${wgTexLiczba(a)}\\,| = \\mathbf{${wgTexLiczba(Math.round(dist * 100) / 100)}}`) + `<br>` +
            (trafiony ? `<span class="wg-ok">✓ to rozwiązanie!</span>`
                      : `<span class="wg-neutral">(szukamy odległości ${b})</span>`));
    }

    wgDraggable(canvas,
        pos => Math.abs(pos.x - toPix(state.x)) < 25,
        pos => {
            const a = parseFloat(aInput.value) || 0;
            const b = parseFloat(bInput.value) || 0;
            const raw = Math.min(MAX, Math.max(MIN, toVal(pos.x)));
            // Przyciąganie do rozwiązań i środka; poza nimi krok co 0,25.
            const snap = wgPrzyciagnij(raw, b >= 0 ? [-a + b, -a - b, -a] : [-a], 0.35);
            state.x = snap !== raw ? snap : Math.round(raw * 4) / 4;
            draw();
        });

    aInput.addEventListener("input", draw);
    bInput.addEventListener("input", draw);
    controls.querySelector(".wg-reset").addEventListener("click", () => {
        aInput.value = 4;
        bInput.value = 7;
        state.x = 0;
        draw();
    });
    draw();
}
