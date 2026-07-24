// app/indicators.js — pływające wskaźniki nieocenionych zadań otwartych (po
// egzaminie) + ich repozycjonowanie przy scrollu/resize.

/* ===== WSKAŹNIKI NIEOCENIONYCH ZADAŃ OTWARTYCH (po egzaminie) =====
   Po zakończeniu próbnego egzaminu (faza „oceń się") każde zadanie otwarte,
   które zostało WYPEŁNIONE (jest wpisany tok rozwiązania), ale nie ma jeszcze
   przyznanej samooceny, dostaje pływającą żółtą kropkę po prawej stronie.
   Klik przewija do zadania; kropka znika, gdy zadanie zostanie ocenione
   (klik samooceny woła odswiezWskaznikiOtwarte()). W trakcie egzaminu ich nie
   ma. Fazę trzymamy w localStorage (KLUCZ_OCENIANIA), żeby przetrwała
   odświeżenie strony aż do ocenienia wszystkich albo ręcznego „ukryj".
   Rejestr zadań otwartych (zadaniaOtwarte) zbieramy przy renderowaniu. */
const KLUCZ_OCENIANIA = "matematykazen-ocenianie-" + SHEET_ID;
let wskaznikiEls = [];          // [{ el: <button> w DOM, zadanie: rekord z zadaniaOtwarte }]
let wskaznikiUkryjBtn = null;
let wskaznikiRafPending = false;
let wskaznikiScrollTimer = null;

function czyFazaOceniania() {
    try { return localStorage.getItem(KLUCZ_OCENIANIA) === "1"; } catch (e) { return false; }
}
function ustawFazeOceniania(wlacz) {
    try {
        if (wlacz) localStorage.setItem(KLUCZ_OCENIANIA, "1");
        else localStorage.removeItem(KLUCZ_OCENIANIA);
    } catch (e) {
        pokazZglosToast("nie udało się zapisać ustawienia", true);
    }
}

// Tryb pojawiania się wskaźników (ustawienie globalne, wspólne dla wszystkich
// arkuszy — jak motyw). Okienko na tok rozwiązania jest OPCJONALNE (uczeń może
// liczyć na kartce), więc domyślnie kropka ma pojawić się przy KAŻDYM zadaniu
// otwartym bez samooceny — tryb "wypelnione" (dawne zachowanie: kropka tylko,
// gdy uczeń coś wpisał w okienko) jest do wyboru w menu "⋯" dla tych, którzy
// wolą kropki tylko przy realnie wypełnionych zadaniach.
const KLUCZ_TRYBU_WSKAZNIKOW = "matematykazen-tryb-wskaznikow";
const TRYBY_WSKAZNIKOW = ["wszystkie", "wypelnione"];
const wskaznikiTrybToggle = document.getElementById("wskazniki-tryb-toggle");

function czytajTrybWskaznikow() {
    try {
        const t = localStorage.getItem(KLUCZ_TRYBU_WSKAZNIKOW);
        if (t === "wypelnione") return t;
    } catch (e) {}
    return "wszystkie";
}
function applyTrybWskaznikow(tryb) {
    try { localStorage.setItem(KLUCZ_TRYBU_WSKAZNIKOW, tryb); } catch (e) {}
    if (wskaznikiTrybToggle) {
        wskaznikiTrybToggle.textContent = tryb === "wypelnione"
            ? "wskaźniki „oceń się”: tylko wypełnione"
            : "wskaźniki „oceń się”: wszystkie zadania";
    }
    // Zmiana trybu w trakcie fazy "oceń się" ma być widoczna od razu.
    if (czyFazaOceniania()) pokazWskaznikiOtwarte();
}
applyTrybWskaznikow(czytajTrybWskaznikow());
if (wskaznikiTrybToggle) {
    wskaznikiTrybToggle.addEventListener("click", () => {
        const next = TRYBY_WSKAZNIKOW[(TRYBY_WSKAZNIKOW.indexOf(czytajTrybWskaznikow()) + 1) % TRYBY_WSKAZNIKOW.length];
        applyTrybWskaznikow(next);
    });
}

// Zadanie otwarte bez samooceny — w trybie "wszystkie" to wystarczy; w trybie
// "wypelnione" dodatkowo wymagamy niepustego toku rozwiązania w okienku.
function czyNieoceniony(zadanie) {
    if (Number.isInteger(zadanie.stan.self)) return false;
    if (czytajTrybWskaznikow() === "wypelnione") {
        return typeof zadanie.stan.open === "string" && zadanie.stan.open.trim() !== "";
    }
    return true;
}

function pokazWskaznikiOtwarte() {
    schowajWskaznikiZDOM(); // idempotentnie — zaczynamy od czysta
    const oczekujace = zadaniaOtwarte.filter(czyNieoceniony);
    if (!oczekujace.length) {
        // Wołane też przy starcie strony, ZANIM loadExercises wypełni
        // zadaniaOtwarte — wtedy lista jest pusta, ale to nie znaczy, że
        // naprawdę nic nie zostało do oceny. Gasimy fazę tylko, gdy arkusz
        // jest już wyrenderowany (klasa z app/render.js), inaczej startSheet()
        // odtworzy wskaźniki poprawnie po renderze.
        if (document.body.classList.contains("arkusz-wczytany")) ustawFazeOceniania(false);
        return;
    }

    oczekujace.forEach(zadanie => {
        const w = document.createElement("button");
        w.className = "wskaznik-otwarte";
        w.type = "button";
        w.textContent = zadanie.numer;
        w.title = `Zadanie ${zadanie.numer}: wpisana odpowiedź bez oceny — kliknij, aby przejść i ocenić się`;
        w.addEventListener("click", () => {
            zadanie.el.scrollIntoView({ behavior: "smooth", block: "center" });
        });
        document.body.appendChild(w);
        wskaznikiEls.push({ el: w, zadanie });
    });

    if (!wskaznikiUkryjBtn) {
        wskaznikiUkryjBtn = document.createElement("button");
        wskaznikiUkryjBtn.id = "wskazniki-ukryj";
        wskaznikiUkryjBtn.type = "button";
        wskaznikiUkryjBtn.textContent = "Ukryj wskaźniki";
        wskaznikiUkryjBtn.title = "Ukryj wszystkie wskaźniki nieocenionych zadań otwartych";
        wskaznikiUkryjBtn.addEventListener("click", ukryjWszystkieWskazniki);
        document.body.appendChild(wskaznikiUkryjBtn);
    }
    wskaznikiUkryjBtn.style.display = "block";

    window.addEventListener("scroll", zaplanujRepozycje, { passive: true });
    window.addEventListener("scroll", oznaczScrollAktywny, { passive: true });
    window.addEventListener("resize", zaplanujRepozycje);
    repozycjonujWskazniki();
}

function schowajWskaznikiZDOM() {
    wskaznikiEls.forEach(({ el }) => el.remove());
    wskaznikiEls = [];
    if (wskaznikiUkryjBtn) wskaznikiUkryjBtn.style.display = "none";
    window.removeEventListener("scroll", zaplanujRepozycje);
    window.removeEventListener("scroll", oznaczScrollAktywny);
    window.removeEventListener("resize", zaplanujRepozycje);
    clearTimeout(wskaznikiScrollTimer);
    document.body.classList.remove("wskazniki-scroll-aktywny");
}

// Podczas aktywnego scrolla wyłączamy `transition: top` na kropkach (inaczej
// tranzycja restartuje się co klatkę rAF-pętli repozycjonującej i kropki
// "gumkują" za zadaniami) — celowo debounce timerem, nie `scrollend`, dla
// szerszej zgodności przeglądarek.
function oznaczScrollAktywny() {
    document.body.classList.add("wskazniki-scroll-aktywny");
    clearTimeout(wskaznikiScrollTimer);
    wskaznikiScrollTimer = setTimeout(() => {
        document.body.classList.remove("wskazniki-scroll-aktywny");
    }, 150);
}

// Wywoływane po każdej zmianie mogącej ruszyć zestaw nieocenionych zadań
// (ocena zadania, wpis w okienku toku rozwiązania). Poza fazą "oceń się" nic
// nie robi. W trakcie fazy przeliczamy listę OD NOWA (nie tylko usuwamy) —
// pokazWskaznikiOtwarte() jest idempotentne, więc bezpiecznie odtwarza cały
// zestaw kropek; dzięki temu wpis w okienku dokłada kropkę, a nie tylko ją
// zdejmuje. Fazę kończymy dopiero, gdy naprawdę nic nieocenionego nie zostanie
// (to samo pokazWskaznikiOtwarte() robi przy braku wyniku filtra).
function odswiezWskaznikiOtwarte() {
    if (!czyFazaOceniania()) return;
    pokazWskaznikiOtwarte();
}

function ukryjWszystkieWskazniki() {
    schowajWskaznikiZDOM();
    ustawFazeOceniania(false);
}

function zaplanujRepozycje() {
    if (wskaznikiRafPending) return;
    wskaznikiRafPending = true;
    requestAnimationFrame(() => { wskaznikiRafPending = false; repozycjonujWskazniki(); });
}

// Każdą kropkę ustawiamy na wysokości środka jej zadania (współrzędne viewportu),
// zaklamowanej do widocznego pasa (pod paskiem górnym … nad przyciskiem „ukryj").
// Potem rozsuwamy je, żeby się nie nakładały (przód: min. odstęp; tył: docisk do
// dolnej krawędzi) — standardowy „declutter" etykiet, dzięki któremu przy scrollu
// kropki albo trzymają się zadań, albo kleją do góry/dołu w zwartej kolumnie.
function repozycjonujWskazniki() {
    if (!wskaznikiEls.length) return;
    const topBar = document.getElementById("top-bar");
    const polowa = 13; // połowa wysokości kropki (26px)
    const gora = (topBar ? topBar.getBoundingClientRect().bottom : 0) + 10 + polowa;
    // Przycisk „ukryj" stoi w prawym dolnym rogu OBOK kolumny kropek (odsunięty od
    // niej w lewo, right: 96px vs right: 70px), więc kropki nie chowają się za nim
    // i mogą schodzić prawie do samego dołu — zostawiamy tylko drobny margines.
    const dol = window.innerHeight - 12 - polowa;
    const krok = 32;   // min. odstęp między środkami kropek
    const items = wskaznikiEls.map(({ el, zadanie }) => {
        const r = zadanie.el.getBoundingClientRect();
        const srodek = r.top + r.height / 2;
        return { el, y: Math.min(Math.max(srodek, gora), Math.max(gora, dol)) };
    });
    for (let i = 1; i < items.length; i++)
        if (items[i].y < items[i - 1].y + krok) items[i].y = items[i - 1].y + krok;
    if (items[items.length - 1].y > dol) items[items.length - 1].y = dol;
    for (let i = items.length - 2; i >= 0; i--)
        if (items[i].y > items[i + 1].y - krok) items[i].y = items[i + 1].y - krok;
    items.forEach(({ el, y }) => { el.style.top = Math.max(gora, y) + "px"; });
}
