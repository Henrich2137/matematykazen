// --- Zad 8 (2026-maj): równanie iloczynowe 3(x+3)(x-m)(2x+4) = 0 -----------
// Kliknięcie w oś / przeciąganie punktu rusza x. Gdy x trafi w rozwiązanie,
// jeden nawias się zeruje i cały iloczyn robi się 0 - to jest sedno zadania.
// Rozwiązania (-3, m, -2) są oznaczone na osi jednym kolorem; m = 5 wynika
// z warunku o sumie rozwiązań (rachunek w rozwiązaniu opisowym).

function widgetRownanieIloczynowe(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Kliknij na dowolne miejsce na osi lub przeciągnij punkt, aby podstawić liczbę pod ${wgMath("x")}.`));

    const canvas = wgCanvas(wrap, 520, 125);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const X0 = -5, X1 = 7, M = 5;
    const ROZWIAZANIA = [-3, -2, M];
    const R_PUNKT = 7;      // promień punktu x (największego znacznika na osi)
    const px = x => 20 + (x - X0) / (X1 - X0) * 480;
    const vx = p => X0 + (p - 20) / 480 * (X1 - X0);
    const osY = 74;

    const state = { x: 1 };

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Oś z podziałką. Liczby schodzą pod największy znacznik, żeby
        // żadna kropka ich nie zasłaniała - odstęp liczony z promienia.
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
            ctx.fillText(i, px(i), osY + R_PUNKT + 4);
        }

        // Rozwiązania równania: jeden kolor, m bez wyróżnienia.
        ctx.fillStyle = WG_KOLORY.wykres;
        ROZWIAZANIA.forEach(r => {
            ctx.beginPath();
            ctx.arc(px(r), osY, 5, 0, Math.PI * 2);
            ctx.fill();
            ctx.font = "bold 13px Arial";
            ctx.textBaseline = "bottom";
            ctx.fillText(r === M ? "m" : String(r).replace("-", "−"), px(r), osY - 10);
        });

        // Punkt x: kolor podstawiania, niezależny od tego, czy równanie wychodzi
        // (o tym mówi ✓/✗ w odczycie). Rysowany na końcu, więc widać go też
        // wtedy, gdy stanie dokładnie na rozwiązaniu.
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(px(state.x), osY, R_PUNKT, 0, Math.PI * 2);
        ctx.fill();

        // Odczyt: równanie z zadania, podstawienie (m już jako 5), obliczone
        // nawiasy i na końcu porównanie z zerem ze znakiem poprawności.
        const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
        const liczba = wgTexLiczba(state.x);
        const wNawiasie = state.x < 0 ? `(${liczba})` : liczba;
        const czynnik = v => v < 0 ? `(${wgTexLiczba(v)})` : wgTexLiczba(v);
        const c1 = state.x + 3, c2 = state.x - M, c3 = 2 * state.x + 4;
        const iloczyn = 3 * c1 * c2 * c3;
        const spelnia = Math.abs(iloczyn) < 1e-9;
        wgUstawHTML(readout,
            wgMath(`3(${nieb("x")} + 3)(${nieb("x")} - m)(2${nieb("x")} + 4) = 0`) + `<br>` +
            wgMath(`3 \\cdot (${nieb(liczba)} + 3) \\cdot (${nieb(liczba)} - 5) \\cdot (2 \\cdot ${nieb(wNawiasie)} + 4) = 0`) + `<br>` +
            wgMath(`3 \\cdot ${czynnik(c1)} \\cdot ${czynnik(c2)} \\cdot ${czynnik(c3)} = 0`) + `<br>` +
            wgMath(`${wgTexLiczba(iloczyn)} = 0`) +
            (spelnia ? ` <span class="wg-ok">✓</span>`
                     : ` <span class="wg-zle">✗</span>`));
    }

    wgDraggable(canvas, null, pos => {
        const raw = Math.min(X1, Math.max(X0, vx(pos.x)));
        // Przyciąganie do rozwiązań, żeby dało się w nie trafić palcem.
        const snap = wgPrzyciagnij(raw, ROZWIAZANIA, 0.3);
        state.x = snap !== raw ? snap : Math.round(raw * 20) / 20;
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
