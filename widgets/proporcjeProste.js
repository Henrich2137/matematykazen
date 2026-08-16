// --- Zad 20 (2026-maj): dwie równoległe przecięte dwiema prostymi ----------
// Proste k i l są równoległe; m przecina je w A i C, n w D i B, a odcinki AC
// i BD (czyli same proste m i n) tną się w punkcie O. Dane |OA| = 12,
// |OB| = 6, |OC| = 8, szukane |OD| = 9.
// Sedno: trójkąty AOD i COB są podobne, więc |OA| : |OC| = |OD| : |OB|.
// Uczeń przesuwa k i l NIEZALEŻNIE od siebie (m i n stoją w miejscu, punkty
// przecięcia jadą po nich). Wszystkie cztery odcinki zmieniają wtedy długość,
// ale oba stosunki zostają sobie równe. Dopiero to tłumaczy, skąd wolno
// ułożyć proporcję.
// Kolory: fiolet = proste m i n (nieruchome), błękit = k z odcinkami OA i OD,
// żółty = l z odcinkami OC i OB.

// Kąty m i n dobrane tak, żeby przy pionowych k oraz l wyszły dokładnie
// długości z zadania (rysunek w arkuszu nie jest w skali).
const PROP_M = 60;          // stopnie, prosta m
const PROP_N = -48.19;      // stopnie, prosta n
const PROP_SKALA = 11;      // pikseli na jednostkę długości
const PROP_XK = -66;        // położenie k z zadania (piksele od O)
const PROP_XL = 44;         // położenie l z zadania

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

    const canvas = wgCanvas(wrap, 520, 380);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const O = { x: 250, y: 186 };
    const uM = propKierunek(PROP_M), uN = propKierunek(PROP_N);
    const state = { xk: PROP_XK, xl: PROP_XL };
    let ciagnieta = null;   // "k" albo "l"

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
    const zol = tex => `\\textcolor{${wgHex(WG_KOLORY.zolty)}}{${tex}}`;

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const A = propPrzeciecie(O, uM, state.xk), C = propPrzeciecie(O, uM, state.xl);
        const D = propPrzeciecie(O, uN, state.xk), B = propPrzeciecie(O, uN, state.xl);

        // Proste m i n przez cały kadr (to na nich leżą odcinki AC i BD).
        [[uM, "m"], [uN, "n"]].forEach(([u, nazwa]) => {
            const t = 400;
            propOdcinek(ctx, { x: O.x - t * u.x, y: O.y - t * u.y },
                { x: O.x + t * u.x, y: O.y + t * u.y }, WG_KOLORY.wykres, 1.6);
        });

        // Proste k i l, pionowe, przez cały kadr.
        [[state.xk, WG_KOLORY.niewiadoma, "k"], [state.xl, WG_KOLORY.zolty, "l"]].forEach(([xp, kolor, nazwa]) => {
            propOdcinek(ctx, { x: O.x + xp, y: 6 }, { x: O.x + xp, y: canvas.height - 6 }, kolor, 2.5);
            propPodpis(ctx, O.x + xp, 14, nazwa, kolor);
        });

        // Odcinki od O do czterech punktów, pogrubione: to o nich mówi zadanie.
        propOdcinek(ctx, O, A, WG_KOLORY.niewiadoma, 4);
        propOdcinek(ctx, O, D, WG_KOLORY.niewiadoma, 4);
        propOdcinek(ctx, O, C, WG_KOLORY.zolty, 4);
        propOdcinek(ctx, O, B, WG_KOLORY.zolty, 4);

        // Punkty i ich nazwy, odsunięte na zewnątrz od O.
        const nazwij = (P, nazwa, kolor) => {
            ctx.fillStyle = kolor;
            ctx.beginPath();
            ctx.arc(P.x, P.y, 5, 0, Math.PI * 2);
            ctx.fill();
            const d = Math.hypot(P.x - O.x, P.y - O.y) || 1;
            propPodpis(ctx, P.x + (P.x - O.x) / d * 17, P.y + (P.y - O.y) / d * 17, nazwa, kolor);
        };
        nazwij(A, "A", WG_KOLORY.niewiadoma);
        nazwij(D, "D", WG_KOLORY.niewiadoma);
        nazwij(C, "C", WG_KOLORY.zolty);
        nazwij(B, "B", WG_KOLORY.zolty);
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
            const dx = -105;
            propPodpis(ctx, O.x + dx, O.y + dx * u.y / u.x, nazwa, WG_KOLORY.wykres);
        });

        // Długości odcinków w jednostkach zadania.
        const dl = P => P.dl / PROP_SKALA;
        const OA = dl(A), OC = dl(C), OD = dl(D), OB = dl(B);
        // Podpisy długości w połowie każdego odcinka.
        [[A, OA, WG_KOLORY.niewiadoma], [C, OC, WG_KOLORY.zolty],
         [D, OD, WG_KOLORY.niewiadoma], [B, OB, WG_KOLORY.zolty]].forEach(([P, v, kolor]) => {
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
            wgMath(`\\frac{${nieb(wgTexLiczba(OA, 2))}}{${zol(wgTexLiczba(OC, 2))}} = ` +
                   `${wgTexLiczba(stosunek, 2)} = ` +
                   `\\frac{${nieb(wgTexLiczba(OD, 2))}}{${zol(wgTexLiczba(OB, 2))}}`) +
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
                state.xk = Math.round(wgPrzyciagnij(Math.max(-84, Math.min(-22, x)), [PROP_XK], 3));
            } else {
                state.xl = Math.round(wgPrzyciagnij(Math.max(22, Math.min(84, x)), [PROP_XL], 3));
            }
            draw();
        });
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
