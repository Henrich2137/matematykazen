// --- Zad 12.1 i 12.2 (2026-maj): funkcja określona przedziałami ------------
// Wykres łamanej f: x+2 na [-4, 2] oraz -x+5 na (2, 5), jak na rysunku
// z arkusza (media/zad12/zad12rys.png). Dwa widżety (po jednym na podzadanie),
// każdy z dwiema zakładkami: jedna na każde zdanie do uzupełnienia.
// Wspólne klocki (zakładki, układ współrzędnych): widgets/_helpers.js.

// Dziedzina [-4, 5); w x = 2 funkcja skacze z 4 (pełne kółko) na 3 (puste).
function lamanaF(x) {
    return x <= 2 ? x + 2 : -x + 5;
}

function lamanaUklad(canvas) {
    return wgUklad({ X0: -5.4, X1: 6.2, Y0: -3.6, Y1: 5.6, szer: canvas.width, wys: canvas.height });
}

// Kółko na końcu odcinka: pełne = koniec należy do wykresu, puste = nie.
function lamanaKolko(ctx, u, x, y, pelne) {
    ctx.beginPath();
    ctx.arc(u.px(x), u.py(y), 4.5, 0, Math.PI * 2);
    if (pelne) {
        ctx.fillStyle = WG_KOLORY.wykres;
        ctx.fill();
    } else {
        ctx.fillStyle = WG_KOLORY.plotno;
        ctx.fill();
        ctx.strokeStyle = WG_KOLORY.wykres;
        ctx.lineWidth = 2;
        ctx.stroke();
    }
}

function lamanaWykres(ctx, u) {
    ctx.strokeStyle = WG_KOLORY.wykres;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(u.px(-4), u.py(-2));
    ctx.lineTo(u.px(2), u.py(4));
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(u.px(2), u.py(3));
    ctx.lineTo(u.px(5), u.py(0));
    ctx.stroke();
    lamanaKolko(ctx, u, -4, -2, true);
    lamanaKolko(ctx, u, 2, 4, true);
    lamanaKolko(ctx, u, 2, 3, false);
    lamanaKolko(ctx, u, 5, 0, false);
}

// --- Zad 12.1: równanie f(x) = c oraz największa wartość na przedziale -----

function widgetLamana121(container) {
    const wrap = wgElement("div", "widget");
    const tytul = wgElement("div", "widget-title", "");
    const zakladki = wgZakladki(wrap, ["Zdanie 1.", "Zdanie 2."], () => {
        ustawTytul();
        draw();
    });
    wrap.appendChild(tytul);
    const canvas = wgCanvas(wrap, 520, 300);
    const ctx = canvas.getContext("2d");
    const u = lamanaUklad(canvas);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const state = { c: 3, a: 2, b: 3 };

    function ustawTytul() {
        wgUstawHTML(tytul, zakladki.aktywna === 0
            ? "Przeciągnij poziomą prostą w górę lub w dół."
            : "Przeciągnij pionowe proste, aby zmienić przedział.");
    }

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;

    // Rozwiązania równania f(x) = c odczytane z obu kawałków łamanej.
    function rozwiazania(c) {
        const wynik = [];
        if (c - 2 >= -4 && c - 2 <= 2) wynik.push(c - 2);
        if (5 - c > 2 && 5 - c < 5) wynik.push(5 - c);
        return wynik;
    }

    function drawZdanie1() {
        const c = state.c;
        ctx.strokeStyle = WG_KOLORY.niewiadoma;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(u.px(u.X0), u.py(c));
        ctx.lineTo(u.px(u.X1), u.py(c));
        ctx.stroke();

        const sol = rozwiazania(c);
        sol.forEach(x => {
            ctx.strokeStyle = WG_KOLORY.liniaSlaba;
            ctx.setLineDash([4, 3]);
            ctx.beginPath();
            ctx.moveTo(u.px(x), u.py(c));
            ctx.lineTo(u.px(x), u.py(0));
            ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = WG_KOLORY.niewiadoma;
            ctx.beginPath();
            ctx.arc(u.px(x), u.py(c), 5.5, 0, Math.PI * 2);
            ctx.fill();
        });

        const trafiony = state.c === 3;
        const rownanie = `f(x) = ${nieb(wgTexLiczba(c))}`;
        const odpowiedz = sol.length === 0
            ? "prosta nie przecina wykresu"
            : wgMath(sol.map(x => `x = ${wgTexLiczba(x)}`).join("\\ \\text{ lub }\\ "));
        wgUstawHTML(readout,
            wgMath(rownanie) + `<br>` + odpowiedz +
            (trafiony ? ` <span class="wg-ok">✓</span>` : ""));
    }

    // Największa wartość f na [a, b]: łamana najpierw rośnie, potem maleje,
    // więc wystarczy porównać końce przedziału i punkt szczytu x = 2.
    function maksimum(a, b) {
        const kandydaci = [a, b];
        if (a <= 2 && 2 <= b) kandydaci.push(2);
        let xm = kandydaci[0];
        for (const x of kandydaci) if (lamanaF(x) > lamanaF(xm)) xm = x;
        return { xm, ym: lamanaF(xm) };
    }

    function drawZdanie2() {
        const { a, b } = state;
        // Pas przedziału [a, b] przez całą wysokość rysunku.
        ctx.fillStyle = WG_KOLORY.obszarInfo;
        ctx.fillRect(u.px(a), u.py(u.Y1), u.px(b) - u.px(a), u.py(u.Y0) - u.py(u.Y1));
        ctx.strokeStyle = WG_KOLORY.niewiadoma;
        ctx.lineWidth = 2;
        [a, b].forEach(x => {
            ctx.beginPath();
            ctx.moveTo(u.px(x), u.py(u.Y0));
            ctx.lineTo(u.px(x), u.py(u.Y1));
            ctx.stroke();
        });
        // Zapis przedziału pod prostymi, na dole płótna.
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.font = "bold 13px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "bottom";
        ctx.fillText(`[${wgTexLiczba(a).replace("{,}", ",")}, ${wgTexLiczba(b).replace("{,}", ",")}]`,
            (u.px(a) + u.px(b)) / 2, canvas.height - 4);

        // Punkt największej wartości + lekka pozioma kreska do osi y.
        const { xm, ym } = maksimum(a, b);
        ctx.strokeStyle = WG_KOLORY.liniaSlaba;
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(u.px(xm), u.py(ym));
        ctx.lineTo(u.px(0), u.py(ym));
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = WG_KOLORY.punkt;
        ctx.beginPath();
        ctx.arc(u.px(xm), u.py(ym), 5.5, 0, Math.PI * 2);
        ctx.fill();
        // Wartość maksimum wyróżniona przy osi y (nadpisuje szarą podziałkę).
        ctx.font = "bold 12px Arial";
        ctx.textAlign = "right";
        ctx.textBaseline = "middle";
        ctx.fillText(wgTexLiczba(ym).replace("{,}", ","), u.px(0) - 7, u.py(ym));

        const trafiony = a === 2 && b === 3;
        wgUstawHTML(readout,
            wgMath(`x \\in [${nieb(wgTexLiczba(a))},\\ ${nieb(wgTexLiczba(b))}]`) + `<br>` +
            `największa wartość: ` + wgMath(`\\boldsymbol{${wgTexLiczba(ym)}}`) +
            (trafiony ? ` <span class="wg-ok">✓</span>` : ""));
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        wgRysujUklad(ctx, u);
        if (zakladki.aktywna === 1) drawZdanie2();
        lamanaWykres(ctx, u);
        if (zakladki.aktywna === 0) drawZdanie1();
    }

    // Zdanie 1: przeciąganie ustawia wysokość prostej. Zdanie 2: łapiemy
    // bliższą z dwóch pionowych prostych; proste nie mogą się minąć.
    wgDraggable(canvas, null, pos => {
        if (zakladki.aktywna === 0) {
            const raw = Math.max(-3, Math.min(5, u.vy(pos.y)));
            const snap = wgPrzyciagnij(raw, [3], 0.2);
            state.c = snap !== raw ? snap : Math.round(raw * 4) / 4;
        } else {
            const raw = Math.max(-4, Math.min(4.75, u.vx(pos.x)));
            const x = Math.round(raw * 4) / 4;
            if (Math.abs(u.px(state.a) - pos.x) <= Math.abs(u.px(state.b) - pos.x)) {
                state.a = Math.min(x, state.b - 0.5);
            } else {
                state.b = Math.max(x, state.a + 0.5);
            }
        }
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    ustawTytul();
    draw();
}

// --- Zad 12.2: zbiór wartości oraz argumenty z f(x) > c --------------------

function widgetLamana122(container) {
    const wrap = wgElement("div", "widget");
    const tytul = wgElement("div", "widget-title", "");
    const zakladki = wgZakladki(wrap, ["Zdanie 1.", "Zdanie 2."], () => {
        ustawTytul();
        controls.style.display = zakladki.aktywna === 1 ? "" : "none";
        draw();
    });
    wrap.appendChild(tytul);
    const canvas = wgCanvas(wrap, 520, 300);
    const ctx = canvas.getContext("2d");
    const u = lamanaUklad(canvas);
    const controls = wgElement("div", "widget-controls",
        `<input type="range" min="-2" max="4" step="0.25" value="1">`);
    controls.style.display = "none";
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const slider = controls.querySelector("input");
    const state = { c: 1 };

    function ustawTytul() {
        wgUstawHTML(tytul, zakladki.aktywna === 0
            ? `Odczytaj z osi ${wgMath("y")}, jakie wartości przyjmuje funkcja.`
            : `Przeciągnij prostą po osi ${wgMath("y")} albo użyj suwaka.`);
    }

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;

    function drawZdanie1() {
        // Zbiór wartości [-2, 4]: pas między poziomymi prostymi (na stałe)
        // i pogrubiony odcinek na osi y.
        ctx.fillStyle = WG_KOLORY.obszarOk;
        ctx.fillRect(u.px(u.X0), u.py(4), u.px(u.X1) - u.px(u.X0), u.py(-2) - u.py(4));
        ctx.strokeStyle = WG_KOLORY.ok;
        ctx.setLineDash([6, 4]);
        ctx.lineWidth = 1.5;
        [-2, 4].forEach(y => {
            ctx.beginPath();
            ctx.moveTo(u.px(u.X0), u.py(y));
            ctx.lineTo(u.px(u.X1), u.py(y));
            ctx.stroke();
        });
        ctx.setLineDash([]);
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(u.px(0), u.py(-2));
        ctx.lineTo(u.px(0), u.py(4));
        ctx.stroke();
        ctx.fillStyle = WG_KOLORY.ok;
        [-2, 4].forEach(y => {
            ctx.beginPath();
            ctx.arc(u.px(0), u.py(y), 5, 0, Math.PI * 2);
            ctx.fill();
        });
        wgUstawHTML(readout,
            `zbiór wartości: ` + wgMath(`\\boldsymbol{[-2,\\ 4]}`));
    }

    // Przedział argumentów z f(x) > c. Prawy koniec domknięty, gdy jedynym
    // punktem nad prostą przy x = 2 jest szczyt (2, 4).
    function przedzial(c) {
        if (c >= 4) return null;
        if (c >= 3) return { od: c - 2, do: 2, doDomkniete: true };
        return { od: c - 2, do: Math.min(5 - c, 5), doDomkniete: false };
    }

    function drawZdanie2() {
        const c = state.c;
        slider.value = c;
        slider.style.accentColor = wgHex(WG_KOLORY.niewiadoma);
        ctx.strokeStyle = WG_KOLORY.niewiadoma;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(u.px(u.X0), u.py(c));
        ctx.lineTo(u.px(u.X1), u.py(c));
        ctx.stroke();

        const p = przedzial(c);
        if (p) {
            ctx.strokeStyle = WG_KOLORY.ok;
            ctx.lineWidth = 5;
            ctx.beginPath();
            ctx.moveTo(u.px(p.od), u.py(0));
            ctx.lineTo(u.px(p.do), u.py(0));
            ctx.stroke();
            // Końce przedziału: puste kółko = koniec wykluczony (nierówność
            // ostra albo koniec dziedziny), pełne = należy do rozwiązania.
            [[p.od, false], [p.do, p.doDomkniete]].forEach(([x, pelne]) => {
                ctx.beginPath();
                ctx.arc(u.px(x), u.py(0), 5, 0, Math.PI * 2);
                if (pelne) {
                    ctx.fillStyle = WG_KOLORY.ok;
                    ctx.fill();
                } else {
                    ctx.fillStyle = WG_KOLORY.plotno;
                    ctx.fill();
                    ctx.strokeStyle = WG_KOLORY.ok;
                    ctx.lineWidth = 2;
                    ctx.stroke();
                }
            });
        }

        // Uchwyt na osi y rysowany na końcu, żeby był nad wykresem.
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(u.px(0), u.py(c), 7, 0, Math.PI * 2);
        ctx.fill();

        const trafiony = c === 1;
        let odpowiedz;
        if (!p) {
            odpowiedz = "brak takich argumentów";
        } else {
            const domkniecie = p.doDomkniete ? "\\rangle" : ")";
            odpowiedz = wgMath(
                `x \\in (${wgTexLiczba(p.od)},\\ ${wgTexLiczba(p.do)}${domkniecie}`);
        }
        wgUstawHTML(readout,
            wgMath(`f(x) > ${nieb(wgTexLiczba(c))}`) + `<br>` + odpowiedz +
            (trafiony ? ` <span class="wg-ok">✓</span>` : ""));
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        wgRysujUklad(ctx, u);
        if (zakladki.aktywna === 0) drawZdanie1();
        lamanaWykres(ctx, u);
        if (zakladki.aktywna === 1) drawZdanie2();
    }

    slider.addEventListener("input", () => {
        state.c = parseFloat(slider.value);
        draw();
    });
    wgDraggable(canvas, null, pos => {
        if (zakladki.aktywna !== 1) return;
        const raw = Math.max(-2, Math.min(4, u.vy(pos.y)));
        const snap = wgPrzyciagnij(raw, [1], 0.15);
        state.c = snap !== raw ? snap : Math.round(raw * 4) / 4;
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    ustawTytul();
    draw();
}
