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
// PODMIANA KROKU TRWA W CZASIE (2026-08-12). Nowy plik ładuje się z sieci, więc
// między kliknięciem a pojawieniem się obrazu mija cała runda do serwera. Przez
// ten czas ctx opisuje już krok DOCELOWY, a w kadrze siedzi jeszcze POPRZEDNI
// film — dlatego żaden element sterowania nie może czytać `querySelector("video")`
// wprost. Od tego jest biezaceWideo(), które w trakcie podmiany zwraca null,
// i pozycjaWKroku(), które wtedy podaje pozycję ZAMÓWIONĄ, nie tę z obcego filmu.
// Bez tego przy wolnym łączu kropki i licznik uciekały o kilka kroków przed
// obrazem, pasek postępu nowego odcinka rysował się z czasu starego filmu,
// „play" pauzował film, który za chwilę znikał, a ◄ podejmował decyzje na
// podstawie pozycji w zupełnie innym kroku (zmierzone Playwrightem na łączu
// dławionym do 60 kB/s).
//
// Kształt ctx budowanego per-zadanie w render.js:
//   { krok, uKonca, maxKropka, wstecz, swapToken, tokenNaEkranie,
//     pozycjaZamowiona, grajPoPodmianie, dlugoscPrzod, steps,
//     stepsContent, prevBtn, playBtn, nextBtn, kropkiBox, kropkiOkno,
//     przewinLewo, przewinPrawo, wyjasnienie, wyjasnienieTresc }

// Ile bezruchu tools/rewersy.sh dokleja na końcu rewersu (tpad). Potrzebne, gdy
// wchodzimy w krok od razu od tyłu i długości wersji w przód nie znamy jeszcze
// z żadnego wczytanego pliku.
const PRZYTRZYMANIE_REWERSU = 0.25;

// Nazwa pliku rewersu powstaje z nazwy kroku — katalog solution-step-by-step/
// trzyma stepN.mp4 obok stepNreverse.mp4. Podmieniamy przed rozszerzeniem, nie
// sam ".mp4", żeby to samo działało dla dowolnego kontenera.
function sciezkaRewersu(src) {
    return src.replace(/(\.[^./]+)$/, "reverse$1");
}

// Czy zamówiona podmiana kroku jeszcze nie weszła na ekran.
function wPodmianie(ctx) {
    return ctx.swapToken !== ctx.tokenNaEkranie;
}

// Film, którym WOLNO sterować: ten w kadrze, ale tylko gdy należy do bieżącego
// stanu. W trakcie podmiany w kadrze wisi poprzedni krok — dla sterowania jest
// go tyle co nic.
function biezaceWideo(ctx) {
    return wPodmianie(ctx) ? null : ctx.stepsContent.querySelector("video");
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
    let straznik = 0;
    const zglos = (blad) => {
        if (wywolane) return;
        wywolane = true;
        clearTimeout(straznik);
        gotowe(box, video, blad);
    };

    // Brak pliku (np. nieprzerobiony rewers) — błąd ląduje na <source>, a przy
    // niektórych ścieżkach także na <video>; słuchamy obu i zgłaszamy od razu,
    // zamiast czekać na strażnika.
    video.addEventListener("error", () => zglos(true), { once: true });
    video.querySelector("source").addEventListener("error", () => zglos(true), { once: true });

    if (czas) ustawCzasWideo(video, czas, () => zglos(false));
    else video.addEventListener("loadeddata", () => zglos(false), { once: true });
    // Strażnik na wypadek łącza, które ani nie odpowiada, ani nie zrywa. Był
    // 1,5 s i przy wolnym łączu wpuszczał do kadru element bez jednej klatki —
    // kadr na moment gasł, a potem obraz wskakiwał drugi raz. Teraz limit jest
    // na tyle długi, że dochodzi do głosu dopiero przy realnym zawieszeniu, a do
    // tego czasu użytkownik widzi przygaszony poprzedni kadr (klasa „podmiana").
    straznik = setTimeout(() => zglos(video.readyState < 1), 8000);
    video.load();
}

// Wstawia krok idx z podwójnym buforem: stary krok zostaje widoczny, dopóki nowy
// film nie ma gotowej klatki — dzięki temu nie ma błysku pustego miejsca.
// Token chroni przed wyścigiem przy szybkim klikaniu (spóźniona podmiana jest
// ignorowana).
function pokazKrok(ctx, idx, { wstecz = false, czas = 0, graj = true } = {}) {
    ctx.krok = idx;
    ctx.wstecz = wstecz;
    // Dokąd zmierzamy, w SKALI KROKU (0 = pierwsza klatka). Nieskończoność
    // oznacza „koniec kroku, długości jeszcze nie znamy" — tak jest przy cofaniu
    // całego poprzedniego kroku i przy skoku na stan końcowy.
    if (czas === "koniec") ctx.pozycjaZamowiona = Infinity;
    else if (wstecz) ctx.pozycjaZamowiona = ctx.dlugoscPrzod ? Math.max(0, ctx.dlugoscPrzod - czas) : Infinity;
    else ctx.pozycjaZamowiona = czas;
    // Zamiar grania trzymamy w ctx, a nie w domknięciu: „play" kliknięty w trakcie
    // ładowania ma go odwrócić, a nie sterować filmem, który zaraz zniknie.
    ctx.grajPoPodmianie = graj;
    const swapToken = ++ctx.swapToken;

    odswiezNawigacje(ctx);

    // Pusty kadr → puls tła. Kadr z poprzednim krokiem → delikatne przygaszenie
    // (puls byłby pod filmem niewidoczny). Jedno i drugie odpala się dopiero po
    // ~200 ms, opóźnieniem w CSS, żeby przy szybkim łączu nic nie mrugnęło.
    ctx.stepsContent.classList.add(ctx.stepsContent.childElementCount ? "podmiana" : "laduje");

    przygotujKrok(ctx, idx, wstecz, czas, (box, video, blad) => {
        if (swapToken !== ctx.swapToken) return; // w międzyczasie wybrano co innego
        // Rewersu nie ma (nieprzerobiony arkusz) — cofka nie ma czego odtworzyć.
        // Zamiast pustego kadru ląduje od razu tam, gdzie i tak by się skończyła:
        // na pierwszej klatce kroku. Powtórka nie zapętli się, bo idzie już
        // w przód.
        if (blad && wstecz) {
            pokazKrok(ctx, idx, { wstecz: false, czas: 0, graj: false });
            return;
        }
        ctx.stepsContent.classList.remove("laduje", "podmiana");
        ctx.stepsContent.replaceChildren(...box.childNodes);
        ctx.tokenNaEkranie = swapToken; // od tej chwili kadr znów opisuje stan
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
                if (ctx.grajPoPodmianie) video.play().catch(() => {});
            });
            if (ctx.grajPoPodmianie && !czas) video.play().catch(() => {});
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
// W trakcie COFANIA głowica siedzi od razu na lewej kropce (czyli na początku
// kroku, do którego zmierzamy) — Henrich po testach v20: „od razu po kliknięciu
// cofnij powinna podświetlić się kropka, która określa początek filmiku".
function biezacaKropka(ctx) {
    return ctx.uKonca ? ctx.krok + 1 : ctx.krok;
}

// Pozycja w SKALI KROKU: 0 = pierwsza klatka, dlugoscPrzod = ostatnia.
// Rewers liczy czas od końca kroku, więc trzeba go odwrócić.
function pozycjaWKroku(ctx, video) {
    // W trakcie podmiany kadr należy jeszcze do poprzedniego kroku — jego czas
    // nie mówi nic o tym, gdzie jesteśmy. Liczy się pozycja zamówiona.
    if (wPodmianie(ctx)) return ctx.pozycjaZamowiona;
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
    // Odcinki NA LEWO od głowicy są w całości wypełnione (Henrich po testach v20),
    // odcinek bieżącego kroku pokazuje realny postęp filmu (pisze go rysujPostep),
    // a te przed nami zostają pustą kreską.
    ctx.kropkiBox.querySelectorAll(".step-link").forEach((link, i) => {
        link.classList.toggle("biezacy", i === ctx.krok);
        if (i < biezaca) link.style.setProperty("--postep", "100%");
        else if (i !== ctx.krok) link.style.setProperty("--postep", "0%");
    });
    // Odcinek bieżącego kroku pisze rysujPostep — także tutaj, bo inaczej przy
    // zmianie kroku zostawałby z wypełnieniem poprzedniego.
    rysujPostep(ctx, biezaceWideo(ctx));

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
    const video = biezaceWideo(ctx);
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
    const poz = pozycjaWKroku(ctx, video);
    const dlugosc = ctx.dlugoscPrzod;
    let proc;
    // Długości kroku nie znamy dopóki nie wczyta się jego plik. Wtedy liczy się
    // tylko to, z którego końca odcinka startujemy: „koniec" (Infinity) rysujemy
    // pełnym paskiem, początek — pustym. Wcześniej odcinek zostawał wtedy
    // z wartością POPRZEDNIEGO kroku.
    if (poz === Infinity) proc = 100;
    else if (!isFinite(dlugosc) || !dlugosc) proc = 0;
    else proc = Math.max(0, Math.min(100, (poz / dlugosc) * 100));
    link.style.setProperty("--postep", proc.toFixed(1) + "%");
}

// Środkowy przycisk ma trzy stany: odtwórz / pauza / odtwórz ponownie.
// Wydzielone z podepnijSterowanieWideo, bo w trakcie ładowania kroku nie ma
// jeszcze filmu, którego stan można by odczytać — a przycisk i tak musi pokazać,
// czy krok zagra po wejściu.
function ustawIkoneGrania(ctx, gra, koniec) {
    ctx.playBtn.classList.toggle("gra", gra);
    ctx.playBtn.classList.toggle("koniec", koniec);
    ctx.playBtn.setAttribute("aria-label",
        koniec ? "Odtwórz ponownie" : (gra ? "Zatrzymaj" : "Odtwórz"));
}

function podepnijSterowanieWideo(ctx, video) {
    if (!video) return;

    // Ten element obsługuje DOKŁADNIE tę podmianę kroku, w której powstał.
    // Bez tej pieczątki pętla postępu STAREGO filmu dopisywała swoją pozycję do
    // odcinka NOWEGO kroku: po kliknięciu kropki w trakcie odtwarzania film
    // skakał poprawnie na t=0, ale pasek zostawał tam, gdzie był (zmierzone
    // 2026-08-11: odcinek nowego kroku pokazywał 55% przy pustym filmie).
    // `video.isConnected` tego nie łapie — stary element jest jeszcze w DOM,
    // dopóki replaceChildren go nie wymieni.
    const mojToken = ctx.swapToken;
    const aktualny = () => ctx.swapToken === mojToken;

    const tempo = predkoscWideo();
    video.defaultPlaybackRate = tempo;
    video.playbackRate = tempo;


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

    // „Odtwórz ponownie" tylko dla filmu w przód — rewers dobiega do początku
    // kroku i tam naturalnym następnym ruchem jest odtworzenie w przód, nie
    // powtórka.
    const syncState = () => ustawIkoneGrania(ctx, !video.paused, video.ended && !ctx.wstecz);

    let raf = 0;
    const petla = () => {
        if (!aktualny() || !video.isConnected || video.paused || video.ended) { raf = 0; return; }
        rysujPostep(ctx, video);
        odswiezPrzyciski(ctx);
        raf = requestAnimationFrame(petla);
    };

    video.addEventListener("play", () => {
        if (!aktualny()) return;
        syncState();
        if (!raf) raf = requestAnimationFrame(petla);
    });
    video.addEventListener("pause", () => {
        if (!aktualny()) return;
        syncState();
        rysujPostep(ctx, video);
        odswiezPrzyciski(ctx);
    });
    video.addEventListener("ended", () => {
        if (!aktualny()) return;
        // Dobiegnięcie do końca przesuwa głowicę na sąsiednią kropkę: w przód na
        // prawą (stan po kroku). W rewersie głowica już tam stoi (patrz
        // biezacaKropka), więc zostaje bez zmian.
        ctx.uKonca = !ctx.wstecz;
        syncState();
        odswiezNawigacje(ctx);
        rysujPostep(ctx, video);
    });

    syncState();
    rysujPostep(ctx, video);
}

// Start/pauza NIGDY nie odpala rewersu (Henrich po testach v20). Kliknięty
// w trakcie cofania najpierw je zatrzymuje w miejscu, a dopiero drugi klik rusza
// stamtąd DO PRZODU.
function przelaczOdtwarzanie(ctx) {
    // Krok się jeszcze ładuje: w kadrze wisi poprzedni film. Pauzowanie go nie
    // miałoby sensu (i tak za chwilę zniknie), a użytkownik pyta o to, co się
    // wczytuje — więc odwracamy ZAMIAR. Bez tego przy wolnym łączu „play"
    // kończył się filmem zatrzymanym na pierwszej klatce (zmierzone).
    if (wPodmianie(ctx)) {
        ctx.grajPoPodmianie = !ctx.grajPoPodmianie;
        ustawIkoneGrania(ctx, ctx.grajPoPodmianie, false);
        return;
    }

    const video = ctx.stepsContent.querySelector("video");
    if (!video) return;

    if (ctx.wstecz) {
        if (!video.paused) { video.pause(); return; }
        const poz = pozycjaWKroku(ctx, video);
        ctx.uKonca = false;
        pokazKrok(ctx, ctx.krok, { czas: poz, graj: true });
        return;
    }
    if (video.ended) {
        // Skończony film odtwarzamy od nowa — to ten sam przycisk, tyle że
        // z ikoną „odtwórz ponownie".
        ctx.uKonca = false;
        video.currentTime = 0;
        video.play().catch(() => {});
    } else if (video.paused) {
        video.play().catch(() => {});
    } else {
        video.pause();
    }
}

// ► — skok na POCZĄTEK następnego kroku, także w trakcie odtwarzania: przycisk
// ma pozwalać pominąć krok, a nie tylko dograć go do końca (Henrich po testach
// v20). Początek kroku k+1 to ta sama klatka co koniec kroku k, więc nic
// z rozwiązania nie ucieka — pomijana jest sama animacja.
function krokDalej(ctx) {
    if (ctx.krok >= ctx.steps.length - 1) {
        // Na ostatnim kroku „dalej" prowadzi już tylko do stanu końcowego.
        if (!ctx.uKonca) skoczDoKropki(ctx, ctx.steps.length);
        return;
    }
    ctx.uKonca = false;
    ctx.dlugoscPrzod = 0;
    pokazKrok(ctx, ctx.krok + 1, { czas: 0, graj: true });
}

// ◄ — odtwarzanie wstecz zawsze zatrzymuje się na POCZĄTKU obecnego kroku;
// kliknięte już na pierwszej klatce cofa cały poprzedni krok (odpowiedź
// Henricha w TODO.md).
function krokWstecz(ctx) {
    const video = biezaceWideo(ctx);
    const pozycja = pozycjaWKroku(ctx, video);

    // JUŻ COFAMY → doskakujemy na pierwszą klatkę bieżącego kroku i stajemy
    // (Henrich po testach v21). Wcześniej drugie ◄ w trakcie cofki startowało
    // rewers jeszcze raz od nowego miejsca i obraz się zacinał.
    // Pokazujemy plik W PRZÓD na czasie 0 — to ta sama klatka co koniec rewersu,
    // ale zostawia nas w stanie, z którego start/pauza rusza naturalnie naprzód.
    if (ctx.wstecz) {
        ctx.uKonca = false;
        pokazKrok(ctx, ctx.krok, { czas: 0, graj: false });
        return;
    }

    // uKonca gasimy OD RAZU, więc kropka początku kroku podświetla się w chwili
    // kliknięcia, a nie dopiero gdy cofka dobiegnie do końca (Henrich po
    // testach v20).
    if (pozycja > 0.001) {
        ctx.uKonca = false;
        // Rewers startuje z klatki odpowiadającej bieżącej pozycji.
        pokazKrok(ctx, ctx.krok, {
            wstecz: true,
            czas: Math.max(0, ctx.dlugoscPrzod - pozycja),
            graj: true,
        });
        return;
    }
    if (ctx.krok === 0) return; // kropka 0 — nie ma czego cofać
    // Cofamy cały poprzedni krok: głowica ląduje od razu na jego początku.
    ctx.uKonca = false;
    ctx.dlugoscPrzod = 0; // długość poprzedniego kroku pozna dopiero jego plik
    pokazKrok(ctx, ctx.krok - 1, { wstecz: true, czas: 0, graj: true });
}

// Kliknięcie kropki — „przenosi to do pierwszej klatki danego kroku" (Henrich).
// Ostatnia kropka nie ma własnego kroku: to stan PO ostatnim filmie, więc
// pokazujemy zatrzymaną ostatnią klatkę.
// Klik w kropkę, na której już stoimy, PUSZCZA krok, który się w niej zaczyna —
// stąd `graj: tenSam` (Henrich po testach v20).
function skoczDoKropki(ctx, i) {
    const video = biezaceWideo(ctx);
    const tenSam = i === biezacaKropka(ctx);

    if (i >= ctx.steps.length) {
        ctx.dlugoscPrzod = 0;
        ctx.uKonca = true;
        pokazKrok(ctx, ctx.steps.length - 1, { czas: "koniec", graj: false });
        return;
    }
    // Właściwy film już stoi na swojej pierwszej klatce — wystarczy go puścić,
    // bez przeładowania (uniknięcie mignięcia).
    if (tenSam && !ctx.wstecz && ctx.krok === i && video && video.paused
        && !video.ended && pozycjaWKroku(ctx, video) <= 0.001) {
        video.play().catch(() => {});
        return;
    }
    ctx.dlugoscPrzod = 0;
    ctx.uKonca = false;
    pokazKrok(ctx, i, { czas: 0, graj: tenSam });
}

// Strzałki przewijania pokazujemy wtedy i tylko wtedy, gdy kropki NAPRAWDĘ się
// nie mieszczą (w zad. 3 dziewięć kropek mieści się na komputerze bez reszty,
// a decydowała sama ich liczba — Henrich po testach v20).
//
// POMIAR NIE MOŻE NICZEGO PRZESTAWIAĆ. Pierwsza wersja chowała strzałki, żeby
// zmierzyć miejsce „bez nich" — a że strzałki są w tym samym wierszu co okno
// kropek, każdy pomiar zmieniał układ i budził ResizeObserver od nowa.
// Chrome ucinał to po kilku obrotach błędem „ResizeObserver loop completed with
// undelivered notifications", który Henrich zobaczył na Pixelu 7a (v21).
// Zamiast tego porównujemy szerokość, jakiej kropki CHCĄ, z szerokością całego
// wiersza — ta druga nie zależy od tego, czy strzałki akurat widać:
//   • strzałki widoczne, kropki się nie mieszczą → scrollWidth to realna
//     szerokość treści, więc porównanie jest wprost;
//   • kropki się mieszczą → scrollWidth schodzi do szerokości okna, która jest
//     nie większa niż wiersz, więc wynik wychodzi „nie trzeba" — i słusznie,
//     bo bez strzałek miejsca będzie tylko więcej.
function odswiezStrzalkiKropek(ctx) {
    const okno = ctx.kropkiOkno;
    const wiersz = okno && okno.parentElement;
    if (!wiersz) return;

    const trzeba = ctx.kropkiBox.scrollWidth > wiersz.clientWidth + 1;
    if (trzeba === ctx.strzalkiWidoczne) return; // bez zmiany nie ruszamy DOM

    ctx.strzalkiWidoczne = trzeba;
    ctx.przewinLewo.style.display = trzeba ? "" : "none";
    ctx.przewinPrawo.style.display = trzeba ? "" : "none";
}

// Przewijanie paska kropek: bieżąca kropka jest utrzymywana w polu widzenia.
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
    ctx.strzalkiWidoczne = undefined; // po przebudowie kropek liczymy od nowa
    odswiezStrzalkiKropek(ctx);
    // Szerokość wiersza zmienia się z oknem przeglądarki i przy obrocie telefonu,
    // więc potrzebę strzałek przeliczamy na bieżąco, a nie raz przy budowie.
    // Zapis odkładamy do najbliższej klatki: przestawienie czegokolwiek wprost
    // w uchwycie ResizeObserver jest właśnie tym, na co Chrome krzyczy
    // „loop completed with undelivered notifications".
    if (window.ResizeObserver && !ctx.obserwatorKropek) {
        ctx.obserwatorKropek = new ResizeObserver(() => {
            if (ctx.rafStrzalek) return;
            ctx.rafStrzalek = requestAnimationFrame(() => {
                ctx.rafStrzalek = 0;
                odswiezStrzalkiKropek(ctx);
            });
        });
        ctx.obserwatorKropek.observe(ctx.kropkiOkno.parentElement);
    }
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
