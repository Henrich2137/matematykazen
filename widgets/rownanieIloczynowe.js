// --- Zad 8 (2026-maj): równanie iloczynowe 3(x+3)(x-m)(2x+4) = 0 -----------
// Suwak (i przeciąganie punktu) rusza x po osi liczbowej. Gdy x trafi w
// rozwiązanie, jeden nawias się zeruje i cały iloczyn robi się 0 - to jest
// sedno zadania. Rozwiązania (-3, m, -2) są oznaczone na osi jednym kolorem,
// m wyróżnionym odcieniem; m = 5 wynika z warunku o sumie rozwiązań.

function widgetRownanieIloczynowe(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmień ${wgMath("x")} przy pomocy suwaka lub przeciągnij punkt po osi.`));

    const canvas = wgCanvas(wrap, 520, 120);
    const ctx = canvas.getContext("2d");

    const controls = wgElement("div", "widget-controls",
        `<input type="range" min="-5" max="7" step="0.25" value="1">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const slider = controls.querySelector("input");
    const X0 = -5, X1 = 7, M = 5;
    const ROZWIAZANIA = [-3, -2, M];
    const px = x => 20 + (x - X0) / (X1 - X0) * 480;
    const vx = p => X0 + (p - 20) / 480 * (X1 - X0);
    const osY = 78;

    const state = { x: 1 };

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Oś z podziałką.
        ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
        ctx.lineWidth = 1;
        wgStrzalka(ctx, 8, osY, 512, osY);
        ctx.font = "11px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        for (let i = X0; i <= X1 - 1; i++) {
            ctx.beginPath();
            ctx.moveTo(px(i), osY - 3);
            ctx.lineTo(px(i), osY + 3);
            ctx.stroke();
            ctx.fillText(i, px(i), osY + 7);
        }

        // Rozwiązania równania: jeden kolor (fiolet), m wyróżnionym odcieniem.
        ROZWIAZANIA.forEach(r => {
            const czyM = r === M;
            ctx.fillStyle = czyM ? WG_KOLORY.fioletMocny : WG_KOLORY.wykres;
            ctx.beginPath();
            ctx.arc(px(r), osY, czyM ? 6 : 5, 0, Math.PI * 2);
            ctx.fill();
            ctx.font = "bold 13px Arial";
            ctx.textBaseline = "bottom";
            ctx.fillText(czyM ? "m" : String(r).replace("-", "−"), px(r), osY - 10);
        });

        // Punkt x: kolor podstawiania, niezależny od tego, czy równanie wychodzi
        // (o tym mówi ✓/✗ w odczycie). Rysowany na końcu, więc widać go też
        // wtedy, gdy stanie dokładnie na rozwiązaniu.
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(px(state.x), osY, 7, 0, Math.PI * 2);
        ctx.fill();

        // Odczyt: równanie z zadania, pod nim to samo z podstawioną liczbą
        // (m już jako 5), na końcu skąd wzięło się m = 5.
        const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
        const fio = tex => `\\textcolor{${wgHex(WG_KOLORY.fioletMocny)}}{${tex}}`;
        const liczba = wgTexLiczba(state.x);
        const wNawiasie = state.x < 0 ? `(${liczba})` : liczba;
        const iloczyn = 3 * (state.x + 3) * (state.x - M) * (2 * state.x + 4);
        const spelnia = Math.abs(iloczyn) < 1e-9;
        wgUstawHTML(readout,
            wgMath(`3(${nieb("x")} + 3)(${nieb("x")} - ${fio("m")})(2${nieb("x")} + 4) = 0`) + `<br>` +
            wgMath(`3 \\cdot (${nieb(liczba)} + 3) \\cdot (${nieb(liczba)} - ${fio("5")}) \\cdot (2 \\cdot ${nieb(wNawiasie)} + 4) = 0`) +
            (spelnia ? ` <span class="wg-ok">✓</span>`
                     : ` <span class="wg-zle">✗</span>`) + `<br>` +
            wgMath(`-3 + ${fio("m")} - 2 = 0 \\;\\Rightarrow\\; ${fio("m")} = 5`));
    }

    function ustawX(raw) {
        const ograniczone = Math.min(X1, Math.max(X0, raw));
        // Przyciąganie do rozwiązań, żeby dało się w nie trafić palcem.
        const snap = wgPrzyciagnij(ograniczone, ROZWIAZANIA, 0.3);
        state.x = snap !== ograniczone ? snap : Math.round(ograniczone * 4) / 4;
        slider.value = state.x;
        draw();
    }

    slider.addEventListener("input", () => {
        state.x = parseFloat(slider.value);
        draw();
    });
    wgDraggable(canvas, null, pos => ustawX(vx(pos.x)));
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
