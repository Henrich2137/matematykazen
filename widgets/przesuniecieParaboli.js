// SPDX-FileCopyrightText: 2026 Henrich2137
// SPDX-License-Identifier: LicenseRef-MatematykaZen-Proprietary
// Wszelkie prawa zastrzeżone / All rights reserved. Licencja: widgets/LICENSE.md
// NIE jest objęty PolyForm Noncommercial / NOT covered by PolyForm Noncommercial.

// --- Zad 14 (2026-maj): przesunięcie wykresu, g(x) = f(x + 1) --------------
// Parabola f o wierzchołku W = (3, -2) oraz g dana wzorem g(x) = f(x + 1).
// Dwie zakładki, bo zadanie ma dwa kroki:
//   1. liczba w nawiasie (suwak albo przeciąganie paraboli) przy ustalonym
//      a = 1/2. Sedno zadania: PLUS w nawiasie przesuwa wykres w LEWO,
//      czyli odwrotnie, niż podpowiada intuicja.
//   2. przy zablokowanej jedynce suwak zmienia rozwarcie a; uczeń doprowadza
//      wykres g do przejścia przez punkt (0, 0) i trafia w a = 1/2.
// Świadomie bez litery na przesunięcie: "c" kolidowałoby z wyrazem wolnym
// postaci ogólnej, "p" z pierwszą współrzędną wierzchołka. Uczeń widzi samą
// liczbę w zapisie f(x + 1) / f(x - 2), dokładnie jak w treści zadania.
// Kolory: fiolet = f (nieruchoma), błękit = g (uczeń nią rusza),
// pomarańcz = punkt (0, 0), w który g ma trafić.

const PARABOLE_ZAKRES = { X0: -3.4, X1: 9.2, Y0: -4.4, Y1: 4.4, szer: 520 };
const PAR_WX = 3;      // pierwsza współrzędna wierzchołka W z zadania
const PAR_WY = -2;     // druga współrzędna wierzchołka W z zadania
const PAR_A = 0.5;     // współczynnik a wyliczony w zadaniu
// Widełki suwaka rozwarcia (Henrich prosił o pełne <-2; 2>). Wartości tuż
// przy zerze są wycięte: przy a = 0 nie ma już paraboli, tylko pozioma prosta.
const PAR_A_MIN = -2, PAR_A_MAX = 2, PAR_A_MARTWA = 0.1;

function paraboleUklad(canvas) {
    return wgUklad(Object.assign({}, PARABOLE_ZAKRES, { wys: canvas.height }));
}

// Parabola y = a(x - p)^2 + PAR_WY przez całą szerokość układu. Ramiona
// wybiegają wysoko poza kadr, więc rysujemy w przycięciu do prostokąta
// układu - dzięki temu krzywa dochodzi do krawędzi i nie urywa się w środku.
function paraboleRysuj(ctx, u, a, p, kolor) {
    ctx.save();
    ctx.beginPath();
    ctx.rect(u.px(u.X0), u.py(u.Y1), u.px(u.X1) - u.px(u.X0), u.py(u.Y0) - u.py(u.Y1));
    ctx.clip();
    ctx.strokeStyle = kolor;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const N = 300;
    for (let i = 0; i <= N; i++) {
        const x = u.X0 + (u.X1 - u.X0) * i / N;
        const y = a * (x - p) * (x - p) + PAR_WY;
        if (i === 0) ctx.moveTo(u.px(x), u.py(y));
        else ctx.lineTo(u.px(x), u.py(y));
    }
    ctx.stroke();
    ctx.restore();
}

// Nazwa krzywej przy jej ramieniu. Etykiety siedzą na RÓŻNYCH wysokościach
// (f wyżej, g niżej), więc nie skleją się nawet wtedy, gdy obie parabole
// prawie się pokrywają.
function paraboleEtykieta(ctx, u, a, p, kolor, tekst, poziom, wLewo) {
    const dx = Math.sqrt((poziom - PAR_WY) / a);
    let x = wLewo ? p - dx : p + dx;
    // Lewe ramię g potrafi biec tuż przy osi y (miejsce zerowe g leży blisko
    // zera), a wtedy nazwa ląduje na osi. W takim razie przenosimy ją na
    // drugie ramię; to samo, gdy punkt wypadałby poza kadrem.
    if (Math.abs(x) < 0.8 || x < u.X0 + 0.5 || x > u.X1 - 0.5) {
        x = wLewo ? p + dx : p - dx;
        wLewo = !wLewo;
    }
    if (x < u.X0 + 0.5 || x > u.X1 - 0.5) return;
    ctx.fillStyle = kolor;
    ctx.font = "italic bold 15px Georgia";
    ctx.textAlign = wLewo ? "right" : "left";
    ctx.textBaseline = "middle";
    ctx.fillText(tekst, u.px(x) + (wLewo ? -10 : 10), u.py(poziom));
}

function paraboleKropka(ctx, u, x, y, kolor, r) {
    ctx.fillStyle = kolor;
    ctx.beginPath();
    ctx.arc(u.px(x), u.py(y), r, 0, Math.PI * 2);
    ctx.fill();
}

// Odległość wskaźnika od paraboli w pikselach - do "łapania" wykresu palcem.
function paraboleOdleglosc(u, pos, a, p) {
    let min = Infinity;
    const N = 200;
    for (let i = 0; i <= N; i++) {
        const x = u.X0 + (u.X1 - u.X0) * i / N;
        const y = a * (x - p) * (x - p) + PAR_WY;
        const dx = u.px(x) - pos.x, dy = u.py(y) - pos.y;
        const d = dx * dx + dy * dy;
        if (d < min) min = d;
    }
    return Math.sqrt(min);
}

function widgetPrzesuniecieParaboli(container) {
    const wrap = wgElement("div", "widget");
    const tytul = wgElement("div", "widget-title", "");
    const zakladki = wgZakladki(wrap, ["Przesunięcie", "Rozwarcie"], () => {
        ustawTytul();
        ustawSterowanie();
        draw();
    });
    wrap.appendChild(tytul);

    const canvas = wgCanvas(wrap, 520, wgWysokoscKwadratowa(PARABOLE_ZAKRES));
    const ctx = canvas.getContext("2d");
    const u = paraboleUklad(canvas);

    const sterowanie1 = wgElement("div", "widget-controls",
        `<span class="wg-suwak-etykieta"></span><input type="range" min="-3" max="3" step="0.05" value="1">`);
    const sterowanie2 = wgElement("div", "widget-controls",
        `<span class="wg-suwak-etykieta"></span><input type="range" min="-2" max="2" step="0.05" value="1.2">`);
    // Szersza kolumna etykiety: musi pomieścić cały zapis f(x + 1), a suwak
    // ma stać w miejscu także wtedy, gdy liczba zmienia długość.
    sterowanie1.style.setProperty("--wg-etykieta-szer", "112px");
    wrap.appendChild(sterowanie1);
    wrap.appendChild(sterowanie2);

    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const suwakT = sterowanie1.querySelector("input");
    const suwakA = sterowanie2.querySelector("input");
    const etykietaT = sterowanie1.querySelector(".wg-suwak-etykieta");
    const etykietaA = sterowanie2.querySelector(".wg-suwak-etykieta");

    // t = liczba dodawana do x we wzorze g(x) = f(x + t); a = rozwarcie obu
    // parabol. Każda zakładka rusza jedną z nich, druga jest wtedy ustalona.
    const state = { t: 1, a: 1.2 };
    // Ile jednostek dzieli chwycony punkt od wierzchołka g - żeby parabola
    // nie skakała pod palec, tylko jechała za nim od miejsca chwytu.
    let chwyt = 0;
    // Wierzchołek tej paraboli, którą uczeń faktycznie chwycił (zakładka 2
    // pozwala ciągnąć obie). Zapamiętany przy chwycie, bo w trakcie ruchu
    // wskaźnik potrafi znaleźć się bliżej tej drugiej.
    let chwytP = PAR_WX;

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;

    function wZakladce2() { return zakladki.aktywna === 1; }
    function biezaceA() { return wZakladce2() ? state.a : PAR_A; }
    function biezaceT() { return wZakladce2() ? 1 : state.t; }

    function ustawTytul() {
        wgUstawHTML(tytul, wZakladce2()
            ? `Zmień ${wgMath("a")} suwakiem tak, aby wykres ${wgMath("g")} przeszedł przez zaznaczony punkt.`
            // Oba tytuły mają zbliżoną długość celowo: gdy jeden zajmuje
            // więcej linii niż drugi, płótno skacze przy zmianie zakładki.
            : `Zmień suwakiem liczbę w nawiasie albo chwyć parabolę ${wgMath("g")} i przeciągnij ją w bok.`);
    }

    function ustawSterowanie() {
        sterowanie1.style.display = wZakladce2() ? "none" : "";
        sterowanie2.style.display = wZakladce2() ? "" : "none";
    }

    // Zapis nawiasu tak, jak pisze się go w zadaniu: f(x + 1), f(x - 2).
    function zapisNawiasu(t) {
        return t < 0 ? `x - ${wgTexLiczba(-t)}` : `x + ${wgTexLiczba(t)}`;
    }

    function drawPrzesuniecie(a, t) {
        const pg = PAR_WX - t;
        // Strzałka przesunięcia PONIŻEJ wierzchołków, w wolnym miejscu pod
        // wykresem (uwaga Henricha). Pod nią sama liczba: kierunek widać po
        // grocie, więc dopisek "w lewo" byłby zbędny.
        if (Math.abs(t) > 0.35) {
            const yp = u.py(PAR_WY) + 30;
            const kier = pg > PAR_WX ? 1 : -1;
            ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.niewiadoma;
            ctx.lineWidth = 2;
            wgStrzalka(ctx, u.px(PAR_WX) + 9 * kier, yp, u.px(pg) - 9 * kier, yp);
            ctx.font = "bold 12px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "top";
            ctx.fillText(wgTexLiczba(Math.abs(t)).replace("{,}", ","),
                (u.px(PAR_WX) + u.px(pg)) / 2, yp + 6);
        }

        const zera = [pg - Math.sqrt(-PAR_WY / a), pg + Math.sqrt(-PAR_WY / a)];
        const trafiony = t === 1;
        wgUstawHTML(readout,
            wgMath(`g(x) = f(${nieb(zapisNawiasu(t))})`) + `<br>` +
            wgMath(`\\text{wierzchołek } g = (${nieb(wgTexLiczba(pg))},\\ ${wgTexLiczba(PAR_WY)})`) + `<br>` +
            wgMath(`\\text{miejsca zerowe } g\\text{: } ${wgTexLiczba(zera[0])} \\text{ i } ${wgTexLiczba(zera[1])}`) +
            (trafiony ? ` <span class="wg-ok">✓</span>` : "") + `<br>` +
            (t === 0
                ? `nic nie dodajemy, więc wykres ${wgMath("g")} pokrywa się z wykresem ${wgMath("f")}`
                : (t > 0
                    ? `w nawiasie dodajemy, a wykres jedzie w lewo`
                    : `w nawiasie odejmujemy, a wykres jedzie w prawo`)));
    }

    function drawRozwarcie(a) {
        // Wartość g(0) jako kropka na osi y: im dalej od pomarańczowego
        // pierścienia, tym mocniej wykres chybia warunku z zadania. Bez
        // kreski do punktu (0, 0), bo leżałaby dokładnie na osi y.
        const g0 = a * (0 - 2) * (0 - 2) + PAR_WY;
        if (g0 >= u.Y0 + 0.15 && g0 <= u.Y1 - 0.15) {
            paraboleKropka(ctx, u, 0, g0, WG_KOLORY.niewiadoma, 5.5);
        } else {
            // Przy skrajnym rozwarciu wartość ucieka poza kadr - zamiast
            // kropki przyklejonej do krawędzi rysujemy grot pokazujący,
            // w którą stronę uciekła. Liczba i tak jest w odczycie.
            const gora = g0 > 0;
            const yk = u.py(gora ? u.Y1 - 0.12 : u.Y0 + 0.12);
            ctx.fillStyle = WG_KOLORY.niewiadoma;
            ctx.beginPath();
            ctx.moveTo(u.px(0), yk + (gora ? -9 : 9));
            ctx.lineTo(u.px(0) - 6, yk);
            ctx.lineTo(u.px(0) + 6, yk);
            ctx.closePath();
            ctx.fill();
        }

        const trafiony = a === 0.5;
        wgUstawHTML(readout,
            wgMath(`g(0) = a \\cdot (0 - 2)^2 - 2 = 4a - 2`) + `<br>` +
            // Ujemne a w nawias: "4 * -2" czyta się fatalnie.
            wgMath(`4 \\cdot ${nieb(a < 0 ? `(${wgTexLiczba(a)})` : wgTexLiczba(a))} - 2 = ${wgTexLiczba(g0)}`) +
            (trafiony ? ` <span class="wg-ok">✓</span>` : "") + `<br>` +
            (trafiony
                ? wgMath(`f(x) = \\tfrac{1}{2}x^2 - 3x + \\tfrac{5}{2}`)
                : `szukaj takiego ${wgMath("a")}, przy którym wyjdzie ${wgMath("0")}`));
    }

    function draw() {
        const a = biezaceA(), t = biezaceT();
        const pg = PAR_WX - t;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        wgRysujUklad(ctx, u);

        // Punkt (0, 0): miejsce zerowe funkcji g podane w zadaniu.
        ctx.strokeStyle = WG_KOLORY.punkt;
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(u.px(0), u.py(0), 8, 0, Math.PI * 2);
        ctx.stroke();

        paraboleRysuj(ctx, u, a, PAR_WX, WG_KOLORY.wykres);
        paraboleRysuj(ctx, u, a, pg, WG_KOLORY.niewiadoma);
        // Przy ujemnym a ramiona idą w dół, więc nazwy krzywych muszą zjechać
        // pod wierzchołek - inaczej szukalibyśmy punktu, którego nie ma.
        paraboleEtykieta(ctx, u, a, PAR_WX, WG_KOLORY.wykres, "f", a > 0 ? 3.0 : -3.6, false);
        paraboleEtykieta(ctx, u, a, pg, WG_KOLORY.niewiadoma, "g", a > 0 ? 2.0 : -3.0, true);

        // Wierzchołki: W należy do f, drugi jedzie razem z g.
        paraboleKropka(ctx, u, pg, PAR_WY, WG_KOLORY.niewiadoma, 6);
        paraboleKropka(ctx, u, PAR_WX, PAR_WY, WG_KOLORY.wykres, 6);
        ctx.fillStyle = WG_KOLORY.wykres;
        ctx.font = "italic bold 14px Georgia";
        ctx.textAlign = "left";
        ctx.textBaseline = "top";
        ctx.fillText("W", u.px(PAR_WX) + 9, u.py(PAR_WY) + 2);

        // Miejsca zerowe g na osi x: to one mają trafić w zaznaczony punkt.
        // Przy a < 0 ramiona idą w dół spod osi, więc miejsc zerowych nie ma
        // wcale i nie ma czego rysować.
        if (a > 0) {
            const d = Math.sqrt(-PAR_WY / a);
            [pg - d, pg + d].forEach(x => paraboleKropka(ctx, u, x, 0, WG_KOLORY.niewiadoma, 5));
        }

        suwakT.style.accentColor = suwakA.style.accentColor = wgHex(WG_KOLORY.niewiadoma);
        wgUstawHTML(etykietaT, wgMath(nieb(`f(${zapisNawiasu(state.t)})`)));
        wgUstawHTML(etykietaA, wgMath(nieb(`a = ${wgTexLiczba(state.a)}`)));

        if (wZakladce2()) drawRozwarcie(a);
        else drawPrzesuniecie(a, t);
    }

    suwakT.addEventListener("input", () => {
        state.t = wgPrzyciagnij(parseFloat(suwakT.value), [1, 0], 0.08);
        draw();
    });
    suwakA.addEventListener("input", () => {
        let a = parseFloat(suwakA.value);
        // Okolice zera odpadają: parabola robi się poziomą prostą.
        if (Math.abs(a) < PAR_A_MARTWA) a = a >= 0 ? PAR_A_MARTWA : -PAR_A_MARTWA;
        state.a = wgPrzyciagnij(a, [0.5], 0.04);
        // Suwak wraca na wartość faktycznie użytą (martwa strefa przy zerze).
        suwakA.value = state.a;
        draw();
    });

    // Łapanie wykresu: w zakładce 1 ciągniemy g w bok (to samo, co suwak,
    // tylko od razu na wykresie), w zakładce 2 ciągniemy dowolne ramię
    // w pionie i zmieniamy tym rozwarcie a.
    wgDraggable(canvas,
        pos => {
            const a = biezaceA(), pg = PAR_WX - biezaceT();
            const dG = paraboleOdleglosc(u, pos, a, pg);
            if (wZakladce2()) {
                const dF = paraboleOdleglosc(u, pos, a, PAR_WX);
                if (Math.min(dG, dF) > 26) return false;
                chwytP = dG <= dF ? pg : PAR_WX;
                return true;
            }
            if (dG > 26) return false;
            chwyt = u.vx(pos.x) - pg;
            return true;
        },
        pos => {
            if (wZakladce2()) {
                // a z położenia wskaźnika na ramieniu chwyconej paraboli.
                // Okolice wierzchołka odpadają, bo tam rozwarcie prawie nie
                // zmienia wysokości i wartość skakałaby na oślep.
                const x = u.vx(pos.x), y = u.vy(pos.y);
                const p = chwytP;
                if (Math.abs(x - p) < 0.7) return;
                const raw = (y - PAR_WY) / ((x - p) * (x - p));
                let clamped = Math.max(PAR_A_MIN, Math.min(PAR_A_MAX, raw));
                if (Math.abs(clamped) < PAR_A_MARTWA) {
                    clamped = clamped >= 0 ? PAR_A_MARTWA : -PAR_A_MARTWA;
                }
                const snap = wgPrzyciagnij(clamped, [0.5], 0.05);
                state.a = snap !== clamped ? snap : Math.round(clamped * 20) / 20;
                suwakA.value = state.a;
            } else {
                const raw = Math.max(-3, Math.min(3, PAR_WX - (u.vx(pos.x) - chwyt)));
                const snap = wgPrzyciagnij(raw, [1, 0], 0.12);
                state.t = snap !== raw ? snap : Math.round(raw * 20) / 20;
                suwakT.value = state.t;
            }
            draw();
        });

    // Przemalowanie po zmianie motywu (paleta z CSS, app/widget-helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    ustawTytul();
    ustawSterowanie();
    draw();
}
