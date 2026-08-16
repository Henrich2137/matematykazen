// --- Zad 19 (2026-maj): kąt wpisany i środkowy w okręgu --------------------
// Punkty A, B, C, D na okręgu o środku O; B na krótszym łuku AC, D na dłuższym.
// Kąt wpisany ADC ma 50°, kąt środkowy COB ma 30°, szukamy kąta AOB.
// Sedno zadania: kąt środkowy AOC jest dwa razy większy od wpisanego ADC,
// czyli ma 100°, a punkt B dzieli go na dwie części. Stąd 100° - 30° = 70°.
// Uczeń rusza dwoma punktami:
//   D po dłuższym łuku - kąt przy nim ANI DRGNIE (to widać najlepiej w ruchu),
//   B po krótszym łuku - kąt środkowy dzieli się inaczej, ale suma zostaje 100°.
// Punkty A i C są nieruchome, bo to one wyznaczają łuk z zadania.
// Kolory: fiolet = okrąg (jak na rysunku CKE), błękit = D i jego kąt,
// żółty = B i kąt COB, pomarańcz = szukany kąt AOB.

const OKR_A = 210;      // położenie A na okręgu (stopnie, jak w matematyce)
const OKR_C = 310;      // położenie C; kąt środkowy AOC ma więc 100°
const OKR_B0 = 280;     // B z zadania: kąt COB = 30°
const OKR_D0 = 85;      // D mniej więcej tam, gdzie na rysunku w arkuszu
const OKR_LUZ = 20;     // o tyle stopni D trzyma się z dala od A i C: bliżej
                        // jego podpis zlewa się z podpisem C, a cięciwa DC
                        // robi się krótsza niż łuczek kąta przy D

// Punkt na okręgu. Na płótnie oś y rośnie w dół, stąd minus przy sinusie.
function okragPunkt(cx, cy, R, deg) {
    return {
        x: cx + R * Math.cos(deg * Math.PI / 180),
        y: cy - R * Math.sin(deg * Math.PI / 180)
    };
}

// Łuk od kąta mniejszego do większego (miary matematyczne). Na płótnie kąty
// lecą w drugą stronę, więc przedział trzeba odbić i odwrócić kolejność.
function okragLuk(ctx, cx, cy, r, degOd, degDo) {
    ctx.arc(cx, cy, r, -degDo * Math.PI / 180, -degOd * Math.PI / 180, false);
}

function okragKatOpisany(ctx, cx, cy, r, degOd, degDo, kolor, wypelnij) {
    if (Math.abs(degDo - degOd) < 0.5) return;
    if (wypelnij) {
        ctx.fillStyle = WG_KOLORY.obszarWykres;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        okragLuk(ctx, cx, cy, r, degOd, degDo);
        ctx.closePath();
        ctx.fill();
    }
    ctx.strokeStyle = kolor;
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    okragLuk(ctx, cx, cy, r, degOd, degDo);
    ctx.stroke();
}

// Miara kąta wypisana na tle w kolorze płótna. Tło jest konieczne: ramiona
// kątów i cięciwy DA, DC przechodzą w różnych miejscach zależnie od tego,
// gdzie uczeń przeciągnie punkty, więc bez niego liczba bywa przekreślona.
function okragTekstZTlem(ctx, x, y, tekst, kolor) {
    ctx.font = "bold 13px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    const w = ctx.measureText(tekst).width;
    ctx.fillStyle = WG_KOLORY.plotno;
    ctx.fillRect(x - w / 2 - 3, y - 9, w + 6, 18);
    ctx.fillStyle = kolor;
    ctx.fillText(tekst, x, y);
}

// Podpis miary kąta w połowie jego rozwarcia, kawałek od wierzchołka.
function okragPodpisKata(ctx, cx, cy, r, degOd, degDo, kolor, tekst) {
    if (Math.abs(degDo - degOd) < 7) return;
    const P = okragPunkt(cx, cy, r, (degOd + degDo) / 2);
    okragTekstZTlem(ctx, P.x, P.y, tekst, kolor);
}

function widgetKatyWOkregu(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Możesz przeciągać punkty ${wgMath("B")} i ${wgMath("D")}.`));

    const canvas = wgCanvas(wrap, 520, 400);
    const ctx = canvas.getContext("2d");
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const cx = 260, cy = 192, R = 156;
    const state = { d: OKR_D0, b: OKR_B0 };
    let ciagniety = null;   // "D" albo "B", ustawiane w chwili chwytu

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
    const zol = tex => `\\textcolor{${wgHex(WG_KOLORY.zolty)}}{${tex}}`;
    const pom = tex => `\\textcolor{${wgHex(WG_KOLORY.punkt)}}{${tex}}`;

    const pkt = deg => okragPunkt(cx, cy, R, deg);

    function draw() {
        const A = pkt(OKR_A), C = pkt(OKR_C), B = pkt(state.b), D = pkt(state.d);
        const O = { x: cx, y: cy };
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Okrąg.
        ctx.strokeStyle = WG_KOLORY.wykres;
        ctx.lineWidth = 1.8;
        ctx.beginPath();
        ctx.arc(cx, cy, R, 0, Math.PI * 2);
        ctx.stroke();

        // Kąt środkowy AOB (szukany) i BOC (dany) przy środku okręgu.
        okragKatOpisany(ctx, cx, cy, 46, OKR_A, state.b, WG_KOLORY.punkt, true);
        okragKatOpisany(ctx, cx, cy, 62, state.b, OKR_C, WG_KOLORY.zolty, false);

        // Ramiona kątów: środkowe z O, wpisane z D.
        ctx.lineWidth = 1.8;
        ctx.strokeStyle = WG_KOLORY.liniaMocna;
        [A, B, C].forEach(P => {
            ctx.beginPath();
            ctx.moveTo(O.x, O.y);
            ctx.lineTo(P.x, P.y);
            ctx.stroke();
        });
        ctx.strokeStyle = WG_KOLORY.niewiadoma;
        [A, C].forEach(P => {
            ctx.beginPath();
            ctx.moveTo(D.x, D.y);
            ctx.lineTo(P.x, P.y);
            ctx.stroke();
        });

        // Kąt wpisany przy D: łuk między ramionami DA i DC.
        const a1 = Math.atan2(A.y - D.y, A.x - D.x);
        const a2 = Math.atan2(C.y - D.y, C.x - D.x);
        let od = a1, doK = a2;
        if (((doK - od + Math.PI * 2) % (Math.PI * 2)) > Math.PI) [od, doK] = [doK, od];
        ctx.strokeStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(D.x, D.y, 34, od, doK, false);
        ctx.stroke();
        // Miara liczona z wektorów, żeby było widać, że naprawdę się nie zmienia.
        const katD = (() => {
            const v1 = { x: A.x - D.x, y: A.y - D.y };
            const v2 = { x: C.x - D.x, y: C.y - D.y };
            const dot = v1.x * v2.x + v1.y * v2.y;
            return Math.acos(dot / (Math.hypot(v1.x, v1.y) * Math.hypot(v2.x, v2.y))) * 180 / Math.PI;
        })();
        const sr = (od + doK) / 2;
        okragTekstZTlem(ctx, D.x + 50 * Math.cos(sr), D.y + 50 * Math.sin(sr),
            `${Math.round(katD)}°`, WG_KOLORY.niewiadoma);

        // Miary kątów środkowych przy O.
        // Obie miary siedzą tuż ZA swoim łukiem (46 + 16 oraz 62 + 16), więc
        // czyta się je tak samo, a nie jedną w środku i jedną na zewnątrz.
        const katAOB = state.b - OKR_A, katBOC = OKR_C - state.b;
        okragPodpisKata(ctx, cx, cy, 62, OKR_A, state.b, WG_KOLORY.punkt, `${Math.round(katAOB)}°`);
        okragPodpisKata(ctx, cx, cy, 78, state.b, OKR_C, WG_KOLORY.zolty, `${Math.round(katBOC)}°`);

        // Punkty. A, C i O są nieruchome (małe kropki), D i B przeciągane
        // (większe, w swoich kolorach).
        ctx.font = "italic bold 15px Georgia";
        const podpis = (P, nazwa, odsun) => {
            const kier = Math.hypot(P.x - cx, P.y - cy) || 1;
            ctx.fillText(nazwa, P.x + (P.x - cx) / kier * odsun, P.y + (P.y - cy) / kier * odsun);
        };
        ctx.fillStyle = WG_KOLORY.tekst;
        [[A, "A"], [C, "C"]].forEach(([P, nazwa]) => {
            ctx.beginPath();
            ctx.arc(P.x, P.y, 4, 0, Math.PI * 2);
            ctx.fill();
            podpis(P, nazwa, 16);
        });
        ctx.beginPath();
        ctx.arc(O.x, O.y, 4, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText("O", O.x, O.y - 15);

        ctx.fillStyle = WG_KOLORY.zolty;
        ctx.beginPath();
        ctx.arc(B.x, B.y, 7, 0, Math.PI * 2);
        ctx.fill();
        podpis(B, "B", 30);
        ctx.fillStyle = WG_KOLORY.niewiadoma;
        ctx.beginPath();
        ctx.arc(D.x, D.y, 7, 0, Math.PI * 2);
        ctx.fill();
        podpis(D, "D", 20);

        // Cały rachunek w jednej linijce (życzenie Henricha): wpisany razy dwa
        // daje środkowy, a ten rozpada się na dwie części. Każda liczba jest
        // brana z rysunku, więc idzie za punktami przy przeciąganiu.
        const trafiony = Math.round(katBOC) === 30;
        const st = v => `${Math.round(v)}^{\\circ}`;
        wgUstawHTML(readout,
            wgMath(`${nieb(st(katD))} \\cdot 2 = ${st(2 * katD)} = ${pom(st(katAOB))} + ${zol(st(katBOC))}`) +
            (trafiony ? ` <span class="wg-ok">✓</span>` : ""));
    }

    // Kąt wskaźnika widziany ze środka okręgu, w mierze matematycznej.
    function katWskaznika(pos) {
        let deg = Math.atan2(cy - pos.y, pos.x - cx) * 180 / Math.PI;
        return deg < 0 ? deg + 360 : deg;
    }

    wgDraggable(canvas,
        pos => {
            const dD = Math.hypot(pos.x - pkt(state.d).x, pos.y - pkt(state.d).y);
            const dB = Math.hypot(pos.x - pkt(state.b).x, pos.y - pkt(state.b).y);
            if (Math.min(dD, dB) > 30) return false;
            ciagniety = dD <= dB ? "D" : "B";
            return true;
        },
        pos => {
            const deg = katWskaznika(pos);
            if (ciagniety === "B") {
                // B zostaje na krótszym łuku AC. Końce są dozwolone: B wolno
                // dojechać do A albo do C i dać się stamtąd wyciągnąć.
                let b = Math.min(Math.max(deg, OKR_A), OKR_C);
                b = wgPrzyciagnij(Math.round(b), [OKR_B0], 2);
                state.b = b;
            } else {
                // D zostaje na dłuższym łuku, czyli poza przedziałem A..C.
                // Przy wejściu w zakazany kawałek zatrzymuje się przy bliższym
                // z jego końców, kilka stopni od samego A albo C.
                let d = Math.round(deg);
                if (d > OKR_A - OKR_LUZ && d < OKR_C + OKR_LUZ) {
                    const doA = Math.abs(d - (OKR_A - OKR_LUZ));
                    const doC = Math.abs(d - (OKR_C + OKR_LUZ));
                    d = doA <= doC ? OKR_A - OKR_LUZ : OKR_C + OKR_LUZ;
                }
                state.d = d;
            }
            draw();
        });
    // Przemalowanie po zmianie motywu (paleta z CSS, widgets/_helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    draw();
}
