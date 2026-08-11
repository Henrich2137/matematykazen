// app/steps.js — podsystem rozwiązań krok-po-kroku (film/obraz/tekst).
// Wydzielony z loadExercises (app/render.js). Funkcje są top-level, a stan
// wspólny dla wszystkich elementów sterowania przekazujemy JAWNIE w obiekcie
// `ctx` — dzięki temu pozostaje jedną, współdzieloną instancją (nie kopią).
//
// MODEL (2026-08-11, przebudowa interfejsu):
//   kropka = STAN działania, film = PRZEJŚCIE między stanami.
// Stąd kropek jest o jedną więcej niż filmów: N filmów → N+1 kropek, a odcinek
// między kropką k a k+1 to krok k (0-indeksowany). Głowica („O" w szkicu
// Henricha w TODO.md) stoi na kropce, na której faktycznie jesteśmy: dopóki film
// nie dobiegnie końca — na lewej kropce odcinka, po dobiegnięciu — na prawej.
// Pasek postępu wypełnia odcinek bieżącego kroku, a nie belkę pod filmem.
//
// Odtwarzanie wstecz to OSOBNY PLIK (stepNreverse.mp4) — przeglądarki nie
// odtwarzają wideo do tyłu, ujemne playbackRate nie działa. Rewers ma tę samą
// treść puszczoną od tyłu plus przytrzymanie doklejone na końcu, więc czas t
// w wersji w przód odpowiada czasowi (dlugoscPrzod - t) w rewersie.
//
// Kształt ctx budowanego per-zadanie w render.js:
//   { krok, uKonca, maxKropka, wstecz, swapToken, dlugoscPrzod, steps,
//     stepsContent, prevBtn, playBtn, nextBtn, kropkiBox, kropkiOkno,
//     przewinLewo, przewinPrawo, wyjasnienie, wyjasnienieTresc }

// Ile bezruchu tools/rewersy.sh dokleja na końcu rewersu (tpad). Potrzebne, gdy
// wchodzimy w krok od razu od tyłu i długości wersji w przód nie znamy jeszcze
// z żadnego wczytanego pliku.
const PRZYTRZYMANIE_REWERSU = 0.25;

// Nazwa pliku rewersu powstaje z nazwy kroku — katalog krok-po-kroku/ trzyma
// stepN.mp4 obok stepNreverse.mp4. Podmieniamy przed rozszerzeniem, nie sam
// ".mp4", żeby to samo działało dla dowolnego kontenera.
function sciezkaRewersu(src) {
    return src.replace(/(\.[^./]+)$/, "reverse$1");
}

function renderStep(step) {
    if (!step) return "";
    if (step.type === "video") {
        // Sterowanie (klik = pauza/play, ikonka stanu, prędkość) podpinamy do
        // realnego elementu w podepnijSterowanieWideo() — właściwości JS nie
        // przetrwałyby serializacji do stringa HTML.
        return `
            <div class="step-video">
                <video playsinline preload="auto">
                    <source src="${mediaPath(step.src)}" type="video/mp4">
                </video>
                <div class="video-overlay-icon"></div>
            </div>
        `;
    } else if (step.type === "image") {
        return `<img src="${mediaPath(step.src)}">`;
    }
    return "";
}

// Przewija film na zadany czas — od razu, gdy zna już długość, a w przeciwnym
// razie po jej poznaniu. `czas === "koniec"` to ostatnia klatka: skok dokładnie
// na duration bywa raportowany jako „ended", więc celujemy odrobinę przed.
function ustawCzasWideo(video, czas, gotowe) {
    if (!czas) { if (gotowe) gotowe(); return; }
    const skocz = () => {
        const cel = czas === "koniec" ? Math.max(0, video.duration - 0.02) : czas;
        if (!isFinite(cel) || Math.abs(video.currentTime - cel) < 0.005) {
            if (gotowe) gotowe();
            return;
        }
        if (gotowe) video.addEventListener("seeked", gotowe, { once: true });
        video.currentTime = cel;
    };
    if (video.readyState >= 1) skocz();                                    // HAVE_METADATA
    else video.addEventListener("loadedmetadata", skocz, { once: true });
}

// Buduje ODŁĄCZONY element z filmem ustawionym na właściwym pliku i czasie
// i woła gotowe() dopiero, gdy pierwsza klatka jest zdekodowana ORAZ przewinięta
// na miejsce. Bez czekania na „seeked" podmiana mignęłaby klatką z czasu 0 —
// przy rewersie byłby to stan KOŃCOWY kroku, czyli dokładnie to, od czego
// uciekamy.
//
// Przewinięcie zamówione tu jest tylko PRÓBĄ: odłączony element bywa ładowany
// leniwie i nie zdąża przed awaryjnym setTimeoutem, więc pokazKrok() egzekwuje
// czas jeszcze raz po wstawieniu do DOM. Bez tego kliknięcie ostatniej kropki
// pokazywało pierwszą klatkę ostatniego kroku zamiast stanu końcowego
// (wykryte odczytem pikseli 2026-08-11).
function przygotujKrok(ctx, idx, wstecz, czas, gotowe) {
    const step = ctx.steps[idx];
    const box = document.createElement("div");
    box.innerHTML = renderStep(step);

    const video = box.querySelector("video");
    if (!video) {
        gotowe(box, null);
        return;
    }
    if (wstecz) {
        video.querySelector("source").src = mediaPath(sciezkaRewersu(step.src));
    }

    let wywolane = false;
    const zglos = () => {
        if (wywolane) return;
        wywolane = true;
        gotowe(box, video);
    };

    if (czas) ustawCzasWideo(video, czas, zglos);
    else video.addEventListener("loadeddata", zglos, { once: true });
    // Awaryjnie: gdyby plik ładował się wyjątkowo długo albo nie istniał
    // (np. brak rewersu), krok i tak ma się pokazać.
    setTimeout(zglos, 1500);
    video.load();
}

// Wstawia krok idx z podwójnym buforem: stary krok zostaje widoczny, dopóki nowy
// film nie ma gotowej klatki — dzięki temu nie ma błysku pustego miejsca.
// Token chroni przed wyścigiem przy szybkim klikaniu (spóźniona podmiana jest
// ignorowana).
function pokazKrok(ctx, idx, { wstecz = false, czas = 0, graj = true } = {}) {
    ctx.krok = idx;
    ctx.wstecz = wstecz;
    const swapToken = ++ctx.swapToken;

    odswiezNawigacje(ctx);

    przygotujKrok(ctx, idx, wstecz, czas, (box, video) => {
        if (swapToken !== ctx.swapToken) return; // w międzyczasie wybrano co innego
        ctx.stepsContent.replaceChildren(...box.childNodes);
        if (video && isFinite(video.duration)) {
            ctx.dlugoscPrzod = wstecz
                ? video.duration - PRZYTRZYMANIE_REWERSU
                : video.duration;
        }
        if (video) {
            podepnijSterowanieWideo(ctx, video);
            // Egzekwujemy czas jeszcze raz — na wstawionym elemencie przewinięcie
            // wykonuje się na pewno (patrz komentarz przy przygotujKrok).
            ustawCzasWideo(video, czas, () => {
                rysujPostep(ctx, video);
                if (graj) video.play().catch(() => {});
            });
            if (graj && !czas) video.play().catch(() => {});
        }
        odswiezNawigacje(ctx);
    });

    // Podgrzewamy film następnego kroku, żeby przełączenie mniej migało.
    const nastepny = ctx.steps[idx + 1];
    if (nastepny && nastepny.type === "video") {
        const preload = document.createElement("video");
        preload.preload = "auto";
        preload.src = mediaPath(nastepny.src);
    }
}

// Kropka, na której stoi głowica: dopóki film bieżącego kroku nie dobiegł końca,
// jesteśmy na lewej kropce odcinka; po dobiegnięciu — na prawej.
function biezacaKropka(ctx) {
    return ctx.uKonca ? ctx.krok + 1 : ctx.krok;
}

// Pozycja w SKALI KROKU: 0 = pierwsza klatka, dlugoscPrzod = ostatnia.
// Rewers liczy czas od końca kroku, więc trzeba go odwrócić.
function pozycjaWKroku(ctx, video) {
    // Rewers ma pierwszeństwo przed uKonca: w trakcie cofki głowica wciąż stoi na
    // kropce, z której wyruszyła, ale pasek ma pokazywać realny postęp filmu.
    if (ctx.wstecz && video) return Math.max(0, ctx.dlugoscPrzod - video.currentTime);
    if (ctx.uKonca) return ctx.dlugoscPrzod;
    return video ? video.currentTime : 0;
}

function odswiezNawigacje(ctx) {
    const biezaca = biezacaKropka(ctx);
    if (biezaca > ctx.maxKropka) ctx.maxKropka = biezaca;

    ctx.kropkiBox.querySelectorAll(".step-dot").forEach((kropka, i) => {
        kropka.classList.toggle("biezaca", i === biezaca);
        kropka.classList.toggle("odwiedzona", i <= ctx.maxKropka && i !== biezaca);
        kropka.setAttribute("aria-current", i === biezaca ? "step" : "false");
    });
    // Pasek wypełnia odcinek TYLKO bieżącego kroku — pozostałe zostają samą
    // cienką kreską (szkic ROW 1 Henricha w TODO.md).
    ctx.kropkiBox.querySelectorAll(".step-link").forEach((link, i) => {
        link.classList.toggle("biezacy", i === ctx.krok);
        if (i !== ctx.krok) link.style.setProperty("--postep", "0%");
    });

    odswiezPrzyciski(ctx);

    // Licznik jest niewidoczny (zastąpiły go kropki), ale zostaje dla czytników
    // ekranu i dla zgłoszeń błędów — czyta go krokRozwiazania() w app/report.js.
    ctx.stepCounter.textContent = `${ctx.krok + 1} / ${ctx.steps.length}`;

    const step = ctx.steps[ctx.krok];
    ctx.wyjasnienieTresc.innerHTML = (step && step.text) || "";
    renderMath(ctx.wyjasnienieTresc);
    // Krok bez opisu nie ma czego pokazywać — przycisk znika, żeby nie otwierał
    // pustki.
    ctx.wyjasnienie.style.display = (step && step.text) ? "" : "none";

    przewinDoKropki(ctx, biezaca);
}

// ◄ gaśnie tylko na pierwszej klatce pierwszego kroku — tam nie ma już czego
// cofać. ► gaśnie na samym końcu ostatniego.
function odswiezPrzyciski(ctx) {
    const video = ctx.stepsContent.querySelector("video");
    ctx.prevBtn.disabled = ctx.krok === 0 && pozycjaWKroku(ctx, video) <= 0.001;
    ctx.nextBtn.disabled = ctx.krok === ctx.steps.length - 1 && ctx.uKonca;
}

// Pasek postępu w odcinku bieżącego kroku. Pętla requestAnimationFrame chodzi
// TYLKO w trakcie odtwarzania i sama się kończy, gdy film stanie albo zniknie
// z DOM — wcześniejsza wersja na `timeupdate` + `transition` sprawiała, że pasek
// jechał gumowato, a stale chodząca pętla klatkowała stronę przy przewijaniu.
function rysujPostep(ctx, video) {
    const link = ctx.kropkiBox.querySelectorAll(".step-link")[ctx.krok];
    if (!link) return;
    const dlugosc = ctx.dlugoscPrzod;
    if (!isFinite(dlugosc) || !dlugosc) return;
    const proc = Math.max(0, Math.min(100, (pozycjaWKroku(ctx, video) / dlugosc) * 100));
    link.style.setProperty("--postep", proc.toFixed(1) + "%");
}

function podepnijSterowanieWideo(ctx, video) {
    if (!video) return;

    const tempo = predkoscWideo();
    video.defaultPlaybackRate = tempo;
    video.playbackRate = tempo;

    const stepVideo = video.closest(".step-video");

    // Kadr dostaje proporcje z samego pliku — arkusz ma naraz filmy 16:9 (zad. 2,
    // nowy format) i 21:9 (zad. 1 i 3, jeszcze nieprzerobione). Bez tego te
    // drugie siedziały w pudełku 16:9 z martwym pasem nad i pod obrazem.
    const ustawProporcje = () => {
        if (!video.videoWidth || !video.videoHeight) return;
        ctx.stepsContent.style.setProperty("--proporcje-filmu",
            `${video.videoWidth} / ${video.videoHeight}`);
    };
    if (video.readyState >= 1) ustawProporcje();
    else video.addEventListener("loadedmetadata", ustawProporcje, { once: true });

    // Klik w film przełącza pauzę/odtwarzanie (Henrich: „zostawić
    // funkcjonalność zatrzymywania kliknięciem w film").
    video.addEventListener("click", () => przelaczOdtwarzanie(ctx));

    const syncState = () => {
        if (stepVideo) {
            stepVideo.classList.toggle("paused", video.paused);
            stepVideo.classList.toggle("ended", video.ended && !ctx.wstecz);
        }
        ctx.playBtn.classList.toggle("gra", !video.paused);
        ctx.playBtn.setAttribute("aria-label", video.paused ? "Odtwórz" : "Zatrzymaj");
    };

    let raf = 0;
    const petla = () => {
        if (!video.isConnected || video.paused || video.ended) { raf = 0; return; }
        rysujPostep(ctx, video);
        odswiezPrzyciski(ctx);
        raf = requestAnimationFrame(petla);
    };

    video.addEventListener("play", () => { syncState(); if (!raf) raf = requestAnimationFrame(petla); });
    video.addEventListener("pause", () => { syncState(); rysujPostep(ctx, video); odswiezPrzyciski(ctx); });
    video.addEventListener("ended", () => {
        // Dobiegnięcie do końca przesuwa głowicę na sąsiednią kropkę: w przód na
        // prawą (stan po kroku), w rewersie na lewą (początek kroku).
        ctx.uKonca = !ctx.wstecz;
        syncState();
        odswiezNawigacje(ctx);
        rysujPostep(ctx, video);
    });

    syncState();
    rysujPostep(ctx, video);
}

function przelaczOdtwarzanie(ctx) {
    const video = ctx.stepsContent.querySelector("video");
    if (!video) return;
    if (video.ended) {
        // Skończony film odtwarzamy od nowa (tak jak ikonka ↺).
        video.currentTime = 0;
        ctx.uKonca = false;
        video.play().catch(() => {});
    } else if (video.paused) {
        video.play().catch(() => {});
    } else {
        video.pause();
    }
}

// ► — głowica przesuwa się o JEDNĄ kropkę w prawo: stojąc w środku kroku
// dogrywamy go do końca, stojąc już na kropce wchodzimy w kolejny krok.
function krokDalej(ctx) {
    const video = ctx.stepsContent.querySelector("video");
    if (ctx.wstecz) {
        // Byliśmy w cofce — wracamy do wersji w przód od tego samego miejsca.
        const poz = pozycjaWKroku(ctx, video);
        ctx.uKonca = false;
        pokazKrok(ctx, ctx.krok, { czas: poz, graj: true });
        return;
    }
    if (ctx.uKonca) {
        if (ctx.krok >= ctx.steps.length - 1) return;
        ctx.uKonca = false;
        pokazKrok(ctx, ctx.krok + 1, { czas: 0, graj: true });
        return;
    }
    if (video) video.play().catch(() => {});
}

// ◄ — odtwarzanie wstecz zawsze zatrzymuje się na POCZĄTKU obecnego kroku;
// kliknięte już na pierwszej klatce cofa cały poprzedni krok (odpowiedź
// Henricha w TODO.md).
function krokWstecz(ctx) {
    const video = ctx.stepsContent.querySelector("video");
    const pozycja = pozycjaWKroku(ctx, video);

    // uKonca zostaje nietknięte: w trakcie cofki głowica stoi na kropce, z której
    // wyruszyła, i przeskakuje na sąsiednią dopiero, gdy rewers dobiegnie końca
    // (obsługuje to zdarzenie „ended"). Tak samo jak przy odtwarzaniu w przód.
    if (pozycja > 0.001) {
        // Rewers startuje z klatki odpowiadającej bieżącej pozycji.
        pokazKrok(ctx, ctx.krok, {
            wstecz: true,
            czas: Math.max(0, ctx.dlugoscPrzod - pozycja),
            graj: true,
        });
        return;
    }
    if (ctx.krok === 0) return; // kropka 0 — nie ma czego cofać
    // Wchodzimy w poprzedni krok od jego KOŃCA, czyli stojąc na jego prawej
    // kropce — tej samej, na której właśnie byliśmy.
    ctx.uKonca = true;
    ctx.dlugoscPrzod = 0; // długość poprzedniego kroku pozna dopiero jego plik
    pokazKrok(ctx, ctx.krok - 1, { wstecz: true, czas: 0, graj: true });
}

// Kliknięcie kropki — „przenosi to do pierwszej klatki danego kroku" (Henrich).
// Ostatnia kropka nie ma własnego kroku: to stan PO ostatnim filmie, więc
// pokazujemy zatrzymaną ostatnią klatkę.
function skoczDoKropki(ctx, i) {
    ctx.dlugoscPrzod = 0;
    if (i >= ctx.steps.length) {
        ctx.uKonca = true;
        pokazKrok(ctx, ctx.steps.length - 1, { czas: "koniec", graj: false });
        return;
    }
    ctx.uKonca = false;
    pokazKrok(ctx, i, { czas: 0, graj: false });
}

// Przewijanie paska kropek: powyżej siedmiu kropek pojawiają się strzałki po
// bokach, a bieżąca kropka jest utrzymywana w polu widzenia.
function przewinDoKropki(ctx, i) {
    const okno = ctx.kropkiOkno;
    if (!okno || okno.scrollWidth <= okno.clientWidth) return;
    const kropka = ctx.kropkiBox.querySelectorAll(".step-dot")[i];
    if (!kropka) return;
    const lewo = kropka.offsetLeft - okno.clientWidth / 2 + kropka.offsetWidth / 2;
    okno.scrollTo({ left: Math.max(0, lewo), behavior: "smooth" });
}

// Buduje ROW 1: N+1 kropek przedzielonych odcinkami (odcinek k = krok k).
function zbudujKropki(ctx) {
    ctx.kropkiBox.textContent = "";
    for (let i = 0; i <= ctx.steps.length; i++) {
        if (i > 0) {
            const link = document.createElement("span");
            link.className = "step-link";
            link.innerHTML = `<span class="step-link-fill"></span>`;
            ctx.kropkiBox.appendChild(link);
        }
        const kropka = document.createElement("button");
        kropka.type = "button";
        kropka.className = "step-dot";
        kropka.setAttribute("aria-label", i === ctx.steps.length
            ? "Stan końcowy" : `Początek kroku ${i + 1}`);
        kropka.addEventListener("click", () => skoczDoKropki(ctx, i));
        ctx.kropkiBox.appendChild(kropka);
    }
    // Strzałki przewijania mają sens dopiero powyżej siedmiu kropek.
    const duzo = ctx.steps.length + 1 > 7;
    ctx.przewinLewo.style.display = duzo ? "" : "none";
    ctx.przewinPrawo.style.display = duzo ? "" : "none";
}

// Odtwarzacz, do którego odnoszą się strzałki ← → na klawiaturze. Arkusz ma
// wiele zadań, więc „ten, z którym użytkownik miał ostatnio do czynienia" jest
// jedyną jednoznaczną odpowiedzią; ustawia go render.js przy otwarciu
// rozwiązania i przy każdym kliknięciu w odtwarzacz.
let aktywnyOdtwarzaczKrokow = null;

document.addEventListener("keydown", (e) => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    const ctx = aktywnyOdtwarzaczKrokow;
    if (!ctx || !ctx.stepsContent.isConnected) return;
    // Strzałki w polu tekstowym przesuwają kursor, nie kroki.
    const cel = e.target;
    if (cel && (cel.tagName === "INPUT" || cel.tagName === "TEXTAREA" || cel.isContentEditable)) return;
    // Odtwarzacz musi być widoczny — inaczej strzałka sterowałaby czymś, czego
    // nie widać, zamiast przewijać stronę.
    const box = ctx.stepsContent.closest(".solution-step-by-step-container");
    if (!box || box.style.display === "none" || !box.getClientRects().length) return;

    e.preventDefault();
    if (e.key === "ArrowRight") krokDalej(ctx); else krokWstecz(ctx);
});

// Przesuwanie palcem po filmie: w lewo = następny krok, w prawo = poprzedni.
// Pionowe gesty zostawiamy przewijaniu strony.
function podepnijPrzesuwanie(ctx, obszar) {
    let x0 = 0, y0 = 0, sledzimy = false;
    obszar.addEventListener("touchstart", (e) => {
        if (e.touches.length !== 1) { sledzimy = false; return; }
        x0 = e.touches[0].clientX;
        y0 = e.touches[0].clientY;
        sledzimy = true;
    }, { passive: true });
    obszar.addEventListener("touchend", (e) => {
        if (!sledzimy) return;
        sledzimy = false;
        const dx = e.changedTouches[0].clientX - x0;
        const dy = e.changedTouches[0].clientY - y0;
        if (Math.abs(dx) < 40 || Math.abs(dx) < Math.abs(dy)) return;
        if (dx < 0) krokDalej(ctx); else krokWstecz(ctx);
    }, { passive: true });
}
