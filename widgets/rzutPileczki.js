// SPDX-FileCopyrightText: 2026 Henrich2137
// SPDX-License-Identifier: LicenseRef-MatematykaZen-Proprietary
// Wszelkie prawa zastrzeżone / All rights reserved. Licencja: widgets/LICENSE.md
// NIE jest objęty PolyForm Noncommercial / NOT covered by PolyForm Noncommercial.

// --- Zad 33.1 i 33.2 (2026-maj): piłeczka wyrzucona pionowo do góry --------
// h(t) = -4,9t^2 + bt, gdzie b z zadania wynosi 14,7. Pytania: kiedy piłeczka
// uderzy w ziemię (33.1) i kiedy będzie najwyżej (33.2).
// Sedno: to zwykła parabola przez punkt (0, 0), a oba pytania to jej dwa
// charakterystyczne miejsca. Upadek to drugie miejsce zerowe (t = b/4,9),
// szczyt to wierzchołek (t = b/9,8), więc szczyt wypada DOKŁADNIE w połowie
// lotu. Suwak zmienia b, a oba momenty jadą razem, cały czas w stosunku 1 do 2.
// Jeden widżet obsługuje obie części zadania (rozwiązanie 33.1 odsyła tutaj).
// Wykres nie jest zwykłym układem współrzędnych: na osiach są różne wielkości
// (sekundy i metry), więc siatka jest rysowana ręcznie, jedna kratka to 1 s
// w poziomie i 10 m w pionie. Kwadratowa kratka nie miałaby tu sensu.
// Kolory: błękit = tor piłeczki (uczeń rusza suwakiem), pomarańcz = szczyt
// (odpowiedź 33.2), żółty = moment upadku (odpowiedź 33.1).

const PIL_G = 4.9;              // współczynnik przy t^2 (ze znakiem minus)
const PIL_B0 = 14.7;            // wartość z zadania
const PIL_ZAKRES = { X0: -0.45, X1: 6.4, Y0: -4, Y1: 47, szer: 520 };

function pilUklad(canvas) {
    return wgUklad(Object.assign({}, PIL_ZAKRES, { wys: canvas.height }));
}

// Osie z podziałką co 1 s i co 10 m. Nie używamy wgRysujUklad, bo tamten
// rysuje siatkę co jedną jednostkę, a tu dałoby to pięćdziesiąt linii.
function pilRysujOsie(ctx, u) {
    ctx.strokeStyle = WG_KOLORY.siatka;
    ctx.lineWidth = 1;
    for (let t = 0; t <= 6; t++) {
        ctx.beginPath();
        ctx.moveTo(u.px(t), u.py(u.Y0));
        ctx.lineTo(u.px(t), u.py(u.Y1));
        ctx.stroke();
    }
    for (let h = 0; h <= 40; h += 10) {
        ctx.beginPath();
        ctx.moveTo(u.px(u.X0), u.py(h));
        ctx.lineTo(u.px(u.X1), u.py(h));
        ctx.stroke();
    }
    ctx.strokeStyle = ctx.fillStyle = WG_KOLORY.osie;
    wgStrzalka(ctx, u.px(u.X0), u.py(0), u.px(u.X1), u.py(0));
    wgStrzalka(ctx, u.px(0), u.py(u.Y0), u.px(0), u.py(u.Y1));
    ctx.font = "11px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "top";
    for (let t = 1; t <= 6; t++) ctx.fillText(t, u.px(t), u.py(0) + 11);
    ctx.textAlign = "right";
    ctx.textBaseline = "middle";
    for (let h = 10; h <= 40; h += 10) ctx.fillText(h, u.px(0) - 7, u.py(h));
    // Opisy osi: bez nich nie wiadomo, że poziomo są sekundy, a pionowo metry.
    ctx.font = "italic 12px Georgia";
    ctx.textAlign = "right";
    ctx.textBaseline = "bottom";
    ctx.fillText("t [s]", u.px(u.X1) - 4, u.py(0) - 6);
    ctx.textAlign = "left";
    ctx.fillText("h [m]", u.px(0) + 8, u.py(u.Y1) + 14);
}

// Piłka nożna: białe koło z czarnym obrysem, pięciokąt w środku i trzy szwy
// biegnące do brzegu. Przy tym rozmiarze to wystarcza, żeby czytało się jako
// piłka, a nie kolejna kropka pomiarowa jak szczyt czy moment upadku.
function pilRysujPilke(ctx, x, y, r) {
    ctx.fillStyle = WG_KOLORY.pilkaTlo;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = WG_KOLORY.pilkaWzor;
    ctx.lineWidth = 1.4;
    ctx.stroke();

    const wierzcholek = i => {
        const kat = (-90 + i * 72) * Math.PI / 180;
        return { x: x + r * 0.42 * Math.cos(kat), y: y + r * 0.42 * Math.sin(kat) };
    };
    ctx.fillStyle = WG_KOLORY.pilkaWzor;
    ctx.beginPath();
    for (let i = 0; i < 5; i++) {
        const P = wierzcholek(i);
        if (i === 0) ctx.moveTo(P.x, P.y);
        else ctx.lineTo(P.x, P.y);
    }
    ctx.closePath();
    ctx.fill();

    ctx.lineWidth = 1.2;
    for (let i = 0; i < 5; i += 2) {
        const P = wierzcholek(i);
        const kat = Math.atan2(P.y - y, P.x - x);
        ctx.beginPath();
        ctx.moveTo(P.x, P.y);
        ctx.lineTo(x + r * Math.cos(kat), y + r * Math.sin(kat));
        ctx.stroke();
    }
}

function widgetRzutPileczki(container) {
    const wrap = wgElement("div", "widget");
    wrap.appendChild(wgElement("div", "widget-title",
        `Suwak zmienia liczbę przy ${wgMath("t")} we wzorze. Patrz na moment szczytu i moment upadku.`));

    // Wysokość podana wprost, NIE przez wgWysokoscKwadratowa: tamta zrównuje
    // piksele na jednostkę obu osi, a tu jedna oś liczy sekundy, druga metry
    // (wyszłoby płótno na 3600 px). Chcemy 1 s w poziomie = 10 m w pionie.
    const canvas = wgCanvas(wrap, 520, 396);
    const ctx = canvas.getContext("2d");
    const u = pilUklad(canvas);

    const controls = wgElement("div", "widget-controls",
        `<span class="wg-akcja-kolumna">` +
        `<button type="button" class="wg-akcja">Wystrzel<br>piłeczkę</button>` +
        `<div class="wg-akcja-zegar"></div></span>` +
        `<span class="wg-suwak-etykieta"></span><input type="range" min="0" max="29.4" step="2.45" value="14.7">`);
    controls.style.setProperty("--wg-etykieta-szer", "72px");
    wrap.appendChild(controls);
    const readout = wgElement("div", "widget-readout", "");
    wrap.appendChild(readout);
    container.appendChild(wrap);

    const suwak = controls.querySelector("input");
    const przycisk = controls.querySelector(".wg-akcja");
    const zegar = controls.querySelector(".wg-akcja-zegar");
    const etykieta = controls.querySelector(".wg-suwak-etykieta");
    // t = null znaczy "piłeczka czeka na ziemi"; liczba to chwila lotu.
    const state = { b: PIL_B0, t: null };
    let klatka = null, startLotu = 0;

    const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.niewiadoma)}}{${tex}}`;
    const pom = tex => `\\textcolor{${wgHex(WG_KOLORY.punkt)}}{${tex}}`;
    const zol = tex => `\\textcolor{${wgHex(WG_KOLORY.zolty)}}{${tex}}`;

    function draw() {
        const b = state.b;
        const tUpadek = b / PIL_G;          // drugie miejsce zerowe
        const tSzczyt = b / (2 * PIL_G);    // wierzchołek, czyli połowa lotu
        const hSzczyt = b * b / (4 * PIL_G);

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        pilRysujOsie(ctx, u);

        // Tor piłeczki tylko na dziedzinie z zadania: od wyrzutu do upadku.
        if (tUpadek > 0) {
            ctx.strokeStyle = WG_KOLORY.niewiadoma;
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            const N = 160;
            for (let i = 0; i <= N; i++) {
                const t = tUpadek * i / N;
                const h = -PIL_G * t * t + b * t;
                if (i === 0) ctx.moveTo(u.px(t), u.py(h));
                else ctx.lineTo(u.px(t), u.py(h));
            }
            ctx.stroke();

            // Szczyt: kreski pomocnicze do obu osi plus kropka.
            ctx.strokeStyle = WG_KOLORY.punkt;
            ctx.lineWidth = 1.5;
            ctx.setLineDash([5, 4]);
            ctx.beginPath();
            ctx.moveTo(u.px(tSzczyt), u.py(0));
            ctx.lineTo(u.px(tSzczyt), u.py(hSzczyt));
            ctx.lineTo(u.px(0), u.py(hSzczyt));
            ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = WG_KOLORY.punkt;
            ctx.beginPath();
            ctx.arc(u.px(tSzczyt), u.py(hSzczyt), 6.5, 0, Math.PI * 2);
            ctx.fill();
            // Moment upadku na osi czasu.
            ctx.fillStyle = WG_KOLORY.zolty;
            ctx.beginPath();
            ctx.arc(u.px(tUpadek), u.py(0), 6.5, 0, Math.PI * 2);
            ctx.fill();

            // Piłka: czeka w (0, 0) albo leci po torze w tempie rzeczywistym.
            // Licznik czasu siedzi pod przyciskiem, nie przy niej.
            const tp = state.t === null ? 0 : Math.min(state.t, tUpadek);
            pilRysujPilke(ctx, u.px(tp), u.py(-PIL_G * tp * tp + b * tp), 9);

            // Podpisy obu momentów pod osią czasu, na tle płótna.
            ctx.font = "bold 12px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "top";
            [[tSzczyt, WG_KOLORY.punkt], [tUpadek, WG_KOLORY.zolty]].forEach(([t, kolor]) => {
                const tekst = wgTexLiczba(t, 2).replace("{,}", ",");
                const w = ctx.measureText(tekst).width;
                ctx.fillStyle = WG_KOLORY.plotno;
                ctx.fillRect(u.px(t) - w / 2 - 3, u.py(0) + 9, w + 6, 16);
                ctx.fillStyle = kolor;
                ctx.fillText(tekst, u.px(t), u.py(0) + 10);
            });
        }

        suwak.style.accentColor = wgHex(WG_KOLORY.niewiadoma);
        wgUstawHTML(etykieta, wgMath(nieb(wgTexLiczba(b, 2))));
        const tZegar = state.t === null ? 0 : Math.min(state.t, tUpadek);
        wgUstawHTML(zegar, `t = ${wgTexLiczba(tZegar, 2).replace("{,}", ",")} s`);

        const trafiony = Math.abs(b - PIL_B0) < 1e-9;
        wgUstawHTML(readout,
            // Przy zerze nie dopisujemy "+ 0t", bo tego się nie pisze.
            wgMath(b === 0 ? `h(t) = -4{,}9t^2`
                : `h(t) = -4{,}9t^2 + ${nieb(wgTexLiczba(b, 2))}t`) + `<br>` +
            (b === 0
                ? `przy zerze piłeczka nie zostaje wyrzucona`
                : wgMath(`\\text{szczyt } ${pom(`t = ${wgTexLiczba(tSzczyt, 2)}`)} \\quad ` +
                         `\\text{upadek } ${zol(`t = ${wgTexLiczba(tUpadek, 2)}`)}`) +
                  (trafiony ? ` <span class="wg-ok">✓</span>` : "")) + `<br>` +
            `upadek wypada dwa razy później niż szczyt, bo parabola jest symetryczna`);
    }

    // Lot w tempie rzeczywistym: chwila na wykresie to naprawdę ta sama liczba
    // sekund, o którą pyta zadanie. Po dolocie piłeczka zostaje na ziemi.
    function lec() {
        const tUpadek = state.b / PIL_G;
        if (tUpadek <= 0) return;
        startLotu = performance.now();
        cancelAnimationFrame(klatka);
        // Zegar rusza PRZED sprawdzeniem stanu przycisku, inaczej ustawPrzycisk
        // widzi jeszcze piłeczkę na ziemi i nie blokuje ponownego strzału.
        state.t = 0;
        const krok = () => {
            state.t = (performance.now() - startLotu) / 1000;
            if (state.t >= tUpadek) {
                state.t = tUpadek;
                draw();
                ustawPrzycisk();
                return;
            }
            draw();
            klatka = requestAnimationFrame(krok);
        };
        ustawPrzycisk();
        krok();
    }

    function leci() {
        return state.t !== null && state.t < state.b / PIL_G;
    }

    function ustawPrzycisk() {
        wgUstawHTML(przycisk, leci() ? "Leci…" : "Wystrzel<br>piłeczkę");
        przycisk.disabled = leci() || state.b === 0;
    }

    przycisk.addEventListener("click", lec);
    suwak.addEventListener("input", () => {
        state.b = parseFloat(suwak.value);
        // Zmiana wzoru w locie nie ma sensu: piłeczka wraca na ziemię.
        cancelAnimationFrame(klatka);
        state.t = null;
        ustawPrzycisk();
        draw();
    });
    // Przemalowanie po zmianie motywu (paleta z CSS, app/widget-helpers.js).
    wgZarejestrujRysowanie(canvas, draw);
    ustawPrzycisk();
    draw();
}
