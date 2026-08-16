// --- Zad 26 (2026-maj): prosta równoległa przez zadany punkt ---------------
// Prosta k ma równanie y = ax + b, prosta l jest do niej równoległa i przechodzi
// przez punkt (2, -2). Szukane: gdzie l przecina oś Oy.
// Sedno: równoległość przenosi na l TYLKO współczynnik kierunkowy a. Wyraz
// wolny prostej l wynika z punktu, przez który ona przechodzi, więc suwak b
// rusza samą prostą k i nie zmienia odpowiedzi ani na jotę. Uczeń rusza b
// i widzi, że wynik stoi; rusza a i wynik natychmiast się zmienia.
// Kolory: fiolet = prosta k (dana), błękit = prosta l i jej punkt na osi y,
// pomarańcz = punkt (2, -2), którym l jest przybita.

const ROWN_ZAKRES = { X0: -3.5, X1: 6.5, Y0: -5.5, Y1: 3.5, szer: 520 };
const ROWN_PX = 2, ROWN_PY = -2;    // punkt, przez który przechodzi l
const ROWN_KROK = 12;               // suwak a chodzi po wielokrotnościach 1/12,
                                    // dzięki czemu -1/3 z zadania jest osiągalne

function rownUklad(canvas) {
    return wgUklad(Object.assign({}, ROWN_ZAKRES, { wys: canvas.height }));
}

function rownProsta(ctx, u, a, b, kolor, grubosc) {
    ctx.strokeStyle = kolor;
    ctx.lineWidth = grubosc;
    ctx.save();
    ctx.beginPath();
    ctx.rect(u.px(u.X0), u.py(u.Y1), u.px(u.X1) - u.px(u.X0), u.py(u.Y0) - u.py(u.Y1));
    ctx.clip();
    ctx.beginPath();
    ctx.moveTo(u.px(u.X0), u.py(a * u.X0 + b));
    ctx.lineTo(u.px(u.X1), u.py(a * u.X1 + b));
    ctx.stroke();
    ctx.restore();
}

// Liczba n/ROWN_KROK w zapisie TeX: całkowite bez ułamka, reszta skrócona,
// żeby -1/3 i -4/3 z zadania pokazywały się dokładnie, a nie jako -0,33.
function rownUlamek(v) {
    const nwd = (x, y) => y ? nwd(y, x % y) : x;
    let licz = Math.round(v * ROWN_KROK), mian = ROWN_KROK;
    if (licz === 0) return "0";
    const znak = licz < 0 ? "-" : "";
    licz = Math.abs(licz);
    const d = nwd(licz, mian);
    licz /= d; mian /= d;
    return mian === 1 ? `${znak}${licz}` : `${znak}\\frac{${licz}}{${mian}}`;
}

function widgetProsteRownolegle(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Zmieniaj suwakami ${wgMath("a")} i ${wgMath("b")} prostej ${wgMath("k")}. Prosta ${wgMath("l")} zostaje równoległa i trzyma się punktu ${wgMath("(2,\\ -2)")}.`));

    const canvas = wgCanvas(wrap, 520, wgWysokoscKwadratowa(ROWN_ZAKRES));
    const ctx = canvas.getContext("2d");
    const u = rownUklad(canvas);

    const controls = wgElement("div", "widget-controls",
        `<span class="wg-suwak-etykieta"></span><input type="range" min="-1.25" max="1.25" step="0.0833333" value="-0.3333332"><br>` +
        `<span class="wg-suwak-etykieta"></span><input type="range" min="-4" max="4" step="0.5" value="2">`);
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const [suwakA, suwakB] = controls.querySelectorAll("input");
    const [etykietaA, etykietaB] = controls.querySelectorAll(".wg-suwak-etykieta");
    const state = { a: -1 / 3, b: 2 };

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
    const fio = tex => `\\textcolor{${wgHex(WG_KOLORY.wykres)}}{${tex}}`;

    function draw() {
        const { a, b } = state;
        // Prosta l: przechodzi przez (2, -2) i ma to samo nachylenie co k.
        const bl = ROWN_PY - a * ROWN_PX;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        wgRysujUklad(ctx, u);
        rownProsta(ctx, u, a, b, WG_KOLORY.wykres, 2.5);
        rownProsta(ctx, u, a, bl, WG_KOLORY.niewiadoma, 2.5);

        // Punkt (2, -2): gwóźdź, na którym wisi prosta l.
        ctx.fillStyle = WG_KOLORY.punkt;
        ctx.beginPath();
        ctx.arc(u.px(ROWN_PX), u.py(ROWN_PY), 7, 0, Math.PI * 2);
        ctx.fill();
        // Szukany punkt przecięcia l z osią Oy.
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(u.px(0), u.py(bl), 7, 0, Math.PI * 2);
        ctx.fill();

        // Nazwy prostych przy prawej krawędzi kadru.
        ctx.font = "italic bold 15px Georgia";
        ctx.textAlign = "right";
        ctx.textBaseline = "middle";
        [[b, WG_KOLORY.wykres, "k"], [bl, WG_KOLORY.niewiadoma, "l"]].forEach(([wyraz, kolor, nazwa]) => {
            const yk = a * (u.X1 - 0.35) + wyraz;
            if (yk < u.Y0 + 0.3 || yk > u.Y1 - 0.3) return;
            ctx.fillStyle = kolor;
            ctx.fillText(nazwa, u.px(u.X1 - 0.35), u.py(yk));
        });

        suwakA.style.accentColor = wgHex(WG_KOLORY.niewiadoma);
        suwakB.style.accentColor = wgHex(WG_KOLORY.wykres);
        wgUstawHTML(etykietaA, wgMath(nieb(`a = ${rownUlamek(a)}`)));
        wgUstawHTML(etykietaB, wgMath(fio(`b = ${wgTexLiczba(b, 1)}`)));

        const trafiony = Math.round(a * ROWN_KROK) === -4;
        wgUstawHTML(readout,
            // Znak wyrazu wolnego wchodzi do zapisu, żeby nie wyszło "x + -4/3".
            wgMath(`l\\text{: } y = ${nieb(rownUlamek(a))}x ${bl < 0 ? "-" : "+"} ${nieb(rownUlamek(Math.abs(bl)))}`) + `<br>` +
            wgMath(`l \\cap Oy = (0,\\ ${nieb(`\\boldsymbol{${rownUlamek(bl)}}`)})`) +
            (trafiony ? ` <span class="wg-ok">✓</span>` : "") + `<br>` +
            `suwak ${wgMath(fio("b"))} rusza samą prostą ${wgMath("k")}, a wynik stoi w miejscu`);
    }

    suwakA.addEventListener("input", () => {
        state.a = Math.round(parseFloat(suwakA.value) * ROWN_KROK) / ROWN_KROK;
        draw();
    });
    suwakB.addEventListener("input", () => {
        state.b = parseFloat(suwakB.value);
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
