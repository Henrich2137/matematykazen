// --- Zad 20 (2026-maj): dwie równoległe przecięte dwiema prostymi ----------
// Proste k i l są równoległe; m przecina je w A i C, n w D i B, a odcinki AC
// i BD (czyli same proste m i n) tną się w punkcie O. Dane |OA| = 12,
// |OB| = 6, |OC| = 8, szukane |OD| = 9.
// Sedno: trójkąty AOD i COB są podobne, więc |OA| : |OC| = |OD| : |OB|.
// Uczeń przesuwa k i l NIEZALEŻNIE od siebie (m i n stoją w miejscu, punkty
// przecięcia jadą po nich). Wszystkie cztery odcinki zmieniają wtedy długość,
// ale oba stosunki zostają sobie równe. Dopiero to tłumaczy, skąd wolno
// ułożyć proporcję.
// Kolory: kolorowe są WYŁĄCZNIE cztery odcinki z wypisaną długością, reszta
// rysunku (proste k, l oraz kawałki m i n poza pasem między równoległymi) jest
// neutralna. Odcinki przy prostej k dostają dwa odcienie błękitu, odcinki przy
// l dwa odcienie żółci: widać i który odcinek jest który, i która prosta go
// wyznacza.

// Kąty m i n dobrane tak, żeby przy pionowych k oraz l wyszły dokładnie
// długości z zadania (rysunek w arkuszu nie jest w skali).
const PROP_M = 60;          // stopnie, prosta m
const PROP_N = -48.19;      // stopnie, prosta n
const PROP_SKALA = 14;      // pikseli na jednostkę długości
const PROP_XK = -84;        // położenie k z zadania (|OA| = 12)
const PROP_XL = 56;         // położenie l z zadania (|OC| = 8)
// Widełki przesuwania. Górne granice biorą się z życzenia Henricha, żeby dało
// się dojechać do |OA| = 16 oraz |OC| = 12; dolne trzymają proste z dala od O,
// bo tam figura by się zdegenerowała.
const PROP_XK_MIN = -112, PROP_XK_MAX = -28;
const PROP_XL_MIN = 28, PROP_XL_MAX = 84;

function propKierunek(deg) {
    return { x: Math.cos(deg * Math.PI / 180), y: -Math.sin(deg * Math.PI / 180) };
}

// Punkt przecięcia prostej o kierunku u (przez O) z pionową prostą x = xp.
function propPrzeciecie(O, u, xp) {
    const t = xp / u.x;
    return { x: O.x + xp, y: O.y + t * u.y, dl: Math.abs(t) };
}

function propOdcinek(ctx, P, Q, kolor, grubosc) {
    ctx.strokeStyle = kolor;
    ctx.lineWidth = grubosc;
    ctx.beginPath();
    ctx.moveTo(P.x, P.y);
    ctx.lineTo(Q.x, Q.y);
    ctx.stroke();
}

function propPodpis(ctx, x, y, tekst, kolor, font) {
    ctx.font = font || "italic bold 14px Georgia";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    const w = ctx.measureText(tekst).width;
    ctx.fillStyle = WG_KOLORY.plotno;
    ctx.fillRect(x - w / 2 - 3, y - 9, w + 6, 18);
    ctx.fillStyle = kolor;
    ctx.fillText(tekst, x, y);
}

function widgetProporcjeProste(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Przesuwaj proste ${wgMath("k")} i ${wgMath("l")} na boki. Proste ${wgMath("m")} i ${wgMath("n")} stoją w miejscu.`));

    const canvas = wgCanvas(wrap, 520, 430);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const O = { x: 250, y: 175 };
    const uM = propKierunek(PROP_M), uN = propKierunek(PROP_N);
    const state = { xk: PROP_XK, xl: PROP_XL };
    let ciagnieta = null;   // "k" albo "l"

    // Cztery odcienie: ciemniejszy dla odcinka bliższego prostej m, jaśniejszy
    // dla odcinka na prostej n. Te same barwy wracają w odczycie.
    const barwaOA = () => WG_KOLORY.niewiadoma, barwaOD = () => WG_KOLORY.niewiadomaJasna;
    const barwaOC = () => WG_KOLORY.zolty, barwaOB = () => WG_KOLORY.zoltyJasny;
    const kol = (kolor, tex) => `\\textcolor{${wgHex(kolor)}}{${tex}}`;

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const A = propPrzeciecie(O, uM, state.xk), C = propPrzeciecie(O, uM, state.xl);
        const D = propPrzeciecie(O, uN, state.xk), B = propPrzeciecie(O, uN, state.xl);

        // Proste m i n przez cały kadr, neutralnie. Kolorowe fragmenty rysujemy
        // na nich dopiero za chwilę, więc poza pasem między k i l zostaje szarość.
        [uM, uN].forEach(u => {
            const t = 460;
            propOdcinek(ctx, { x: O.x - t * u.x, y: O.y - t * u.y },
                { x: O.x + t * u.x, y: O.y + t * u.y }, WG_KOLORY.liniaMocna, 1.6);
        });

        // Proste k i l, pionowe, też neutralne: kolor niosą tylko odcinki.
        [[state.xk, "k"], [state.xl, "l"]].forEach(([xp, nazwa]) => {
            propOdcinek(ctx, { x: O.x + xp, y: 6 }, { x: O.x + xp, y: canvas.height - 6 },
                WG_KOLORY.liniaMocna, 2);
            propPodpis(ctx, O.x + xp, canvas.height - 13, nazwa, WG_KOLORY.tekst);
        });

        // Cztery odcinki z zadania, każdy własnym odcieniem.
        propOdcinek(ctx, O, A, barwaOA(), 4.5);
        propOdcinek(ctx, O, D, barwaOD(), 4.5);
        propOdcinek(ctx, O, C, barwaOC(), 4.5);
        propOdcinek(ctx, O, B, barwaOB(), 4.5);

        // Punkty i ich nazwy, odsunięte na zewnątrz od O.
        const nazwij = (P, nazwa, kolor) => {
            ctx.fillStyle = kolor;
            ctx.beginPath();
            ctx.arc(P.x, P.y, 5, 0, Math.PI * 2);
            ctx.fill();
            const d = Math.hypot(P.x - O.x, P.y - O.y) || 1;
            propPodpis(ctx, P.x + (P.x - O.x) / d * 17, P.y + (P.y - O.y) / d * 17, nazwa, kolor);
        };
        nazwij(A, "A", barwaOA());
        nazwij(D, "D", barwaOD());
        nazwij(C, "C", barwaOC());
        nazwij(B, "B", barwaOB());
        ctx.fillStyle = WG_KOLORY.tekst;
        ctx.beginPath();
        ctx.arc(O.x, O.y, 4.5, 0, Math.PI * 2);
        ctx.fill();
        propPodpis(ctx, O.x + 14, O.y + 13, "O", WG_KOLORY.tekst);

        // Nazwy prostych m i n na ich lewych ramionach. Odsunięcie liczone
        // wzdłuż osi x, bo pionowo prosta m ucieka szybko (nachylenie 60 st.).
        // Odsunięcie 105 px: dalej niż najdalsze położenie prostej k (84 px),
        // żeby nazwa nie wpadła pod przesuwaną prostą ani pod punkty A i D.
        [[uM, "m"], [uN, "n"]].forEach(([u, nazwa]) => {
            const dx = -135;
            propPodpis(ctx, O.x + dx, O.y + dx * u.y / u.x, nazwa, WG_KOLORY.tekst);
        });

        // Długości odcinków w jednostkach zadania.
        const dl = P => P.dl / PROP_SKALA;
        const OA = dl(A), OC = dl(C), OD = dl(D), OB = dl(B);
        // Podpisy długości w połowie każdego odcinka.
        [[A, OA, barwaOA()], [C, OC, barwaOC()],
         [D, OD, barwaOD()], [B, OB, barwaOB()]].forEach(([P, v, kolor]) => {
            // Dwa miejsca po przecinku, nie jedno: przy jednym iloraz liczony
            // z zaokrąglonych długości rozjeżdżał się z pokazanym stosunkiem
            // (np. 11,2/10,6 = 1,06 przy wypisanym 1,05).
            propPodpis(ctx, (O.x + P.x) / 2, (O.y + P.y) / 2,
                wgTexLiczba(v, 2).replace("{,}", ","), kolor, "bold 12px Arial");
        });

        const trafiony = Math.round(OA * 10) === 120 && Math.round(OC * 10) === 80;
        // Wspólny stosunek liczony z DOKŁADNYCH położeń prostych, nie
        // z zaokrąglonych długości: inaczej przy niepełnych liczbach obie
        // strony różniłyby się na drugim miejscu po przecinku i wyglądałoby
        // to na sprzeczność, choć są równe co do joty.
        const stosunek = Math.abs(state.xk) / state.xl;
        wgUstawHTML(readout,
            wgMath(`\\frac{|OA|}{|OC|} = \\frac{|OD|}{|OB|}`) + `<br>` +
            wgMath(`\\frac{${kol(barwaOA(), wgTexLiczba(OA, 2))}}{${kol(barwaOC(), wgTexLiczba(OC, 2))}} = ` +
                   `${wgTexLiczba(stosunek, 2)} = ` +
                   `\\frac{${kol(barwaOD(), wgTexLiczba(OD, 2))}}{${kol(barwaOB(), wgTexLiczba(OB, 2))}}`) +
            (trafiony ? ` <span class="wg-ok">✓</span>` : ""));
    }

    // Chwytamy tę prostą, która jest bliżej wskaźnika; obie zostają pionowe
    // i nie przechodzą przez punkt O, bo wtedy figura by się zdegenerowała.
    wgDraggable(canvas,
        pos => {
            const dk = Math.abs(pos.x - (O.x + state.xk));
            const dl = Math.abs(pos.x - (O.x + state.xl));
            if (Math.min(dk, dl) > 30) return false;
            ciagnieta = dk <= dl ? "k" : "l";
            return true;
        },
        pos => {
            const x = pos.x - O.x;
            if (ciagnieta === "k") {
                state.xk = Math.round(wgPrzyciagnij(Math.max(PROP_XK_MIN, Math.min(PROP_XK_MAX, x)), [PROP_XK], 3));
            } else {
                state.xl = Math.round(wgPrzyciagnij(Math.max(PROP_XL_MIN, Math.min(PROP_XL_MAX, x)), [PROP_XL], 3));
            }
            draw();
        });
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
