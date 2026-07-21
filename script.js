// script.js — logika strony arkusza: render zadań, tryb egzaminu, podpowiedzi,
// rozwiązania krok-po-kroku, panele PDF. Wydzielone z matematykazen.html.
// Ładowane PO solutionsInteractive.js (używa rejestru WIDZETY).

let totalScore = 0;

// Dane zadań — wypełniane z exercises.json w startSheet() (na dole skryptu),
// zanim zawoła loadExercises(). Wcześniej pusta tablica, żeby przypadkowe
// odwołanie nie wywróciło skryptu.
let exercises = [];

// Identyfikacja arkusza: wybierana parametrem URL ?arkusz=<id>, gdzie <id> to
// nazwa folderu pod matura/ (np. "2024-grudzien"). Ten sam id: klucz do fetch
// exercises.json, sufiks kluczy localStorage i (patrz startSheet()) zawartość
// bar-menu/tytułu. BEZ domyślnego fallbacku — brak/pusty/nieznany ?arkusz=
// kończy się komunikatem "błędny link" (startSheet()), nie cichym arkuszem.
const SHEET_ID = new URLSearchParams(location.search).get("arkusz");
// wybrane_wzory_matematyczne.pdf leży w rootcie obok template.html (jedynego
// pliku renderującego arkusze), więc ścieżka jest zawsze ta sama.
const TABLICE_PDF = "wybrane_wzory_matematyczne.pdf";

// Media zadań (obrazki, filmy) leżą w matura/<id>/media/… i są zapisane w
// exercises.json ścieżką WZGLĘDNĄ do folderu arkusza (np. "media/zad1/…").
// template.html renderuje arkusz z rootu, więc każdą taką ścieżkę trzeba
// poprzedzić folderem arkusza. Ścieżki bezwzględne / data:/http zostawiamy.
function mediaPath(src) {
    if (!src || /^(https?:|data:|\/)/.test(src)) return src;
    return `matura/${SHEET_ID}/${src}`;
}

// Klucz zapisu postępu w localStorage — używany przez loadExercises()
// (zapis/odczyt), przycisk "resetuj punktację" (menu ⋯) i start egzaminu.
const KLUCZ_POSTEPU = "matematykazen-postep-" + SHEET_ID;

// KaTeX: renderuje zapisy \( ... \) (inline) i \[ ... \] (blokowe) wewnątrz
// podanego elementu. Guard na window.renderMathInElement — gdyby vendor/katex/
// nie wczytał się (np. uszkodzony plik), strona ma dalej działać, tylko z
// surowym zapisem zamiast ładnych wzorów.
function renderMath(element) {
    if (window.renderMathInElement && element) {
        renderMathInElement(element, {
            delimiters: [
                { left: "\\(", right: "\\)", display: false },
                { left: "\\[", right: "\\]", display: true }
            ],
            throwOnError: false
        });
    }
}

// Okienko "więcej opcji" (⋯): pokaż/schowaj po kliknięciu przycisku,
// zamknij po kliknięciu gdziekolwiek poza okienkiem.
const menuButton = document.getElementById("menu-button");
const barMenu = document.getElementById("bar-menu");
menuButton.addEventListener("click", (e) => {
    e.stopPropagation();
    barMenu.style.display = barMenu.style.display === "block" ? "none" : "block";
});
document.addEventListener("click", (e) => {
    if (barMenu.style.display === "block" && !barMenu.contains(e.target)) {
        barMenu.style.display = "none";
    }
});

/* ===== MOTYW JASNY / CIEMNY =====
   Trzy stany: "auto" (za systemem, prefers-color-scheme), "jasny", "ciemny".
   Wybór ≠ auto zapisujemy w localStorage pod GLOBALNYM kluczem (bez SHEET_ID),
   żeby motyw był wspólny dla wszystkich arkuszy. Klasę theme-light/theme-dark
   na <html> ustawia już inline-skrypt w <head> (bez mignięcia) — tu tylko
   przełączamy stany i etykietę przycisku. */
const KLUCZ_MOTYWU = "matematykazen-motyw";
const MOTYWY = ["auto", "jasny", "ciemny"];
const themeToggle = document.getElementById("theme-toggle");

function readTheme() {
    try {
        const m = localStorage.getItem(KLUCZ_MOTYWU);
        if (m === "jasny" || m === "ciemny") return m;
    } catch (e) {}
    return "auto";
}
function applyTheme(motyw) {
    const html = document.documentElement;
    html.classList.toggle("theme-light", motyw === "jasny");
    html.classList.toggle("theme-dark", motyw === "ciemny");
    try {
        if (motyw === "auto") localStorage.removeItem(KLUCZ_MOTYWU);
        else localStorage.setItem(KLUCZ_MOTYWU, motyw);
    } catch (e) {}
    if (themeToggle) themeToggle.textContent = "motyw: " + motyw;
}
applyTheme(readTheme()); // zsynchronizuj etykietę ze stanem z <head>
if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        const next = MOTYWY[(MOTYWY.indexOf(readTheme()) + 1) % MOTYWY.length];
        applyTheme(next);
    });
}

// "Resetuj punktację": kasuje zapisany postęp i przeładowuje stronę — punkty,
// kolory odpowiedzi i wpisy wracają do zera jedną, wspólną drogą (świeży render).
document.getElementById("reset-scores").addEventListener("click", () => {
    if (!confirm("Wyczyścić zapisane odpowiedzi i punkty? Tej operacji nie można cofnąć.")) return;
    try {
        localStorage.removeItem(KLUCZ_POSTEPU);
        localStorage.removeItem(KLUCZ_OCENIANIA); // reset kasuje też fazę „oceń się"
    } catch (e) {}
    location.reload();
});

/* ===== TRYB EGZAMINACYJNY (próbny egzamin na czas) =====
   Zasada działania: ocenianie i zapis postępu biegną NORMALNIE, tą samą drogą
   co zawsze (jedna logika punktowania) — tryb egzaminu tylko dokłada klasę
   body.tryb-egzaminu, a style.css pod nią chowa wszystko, co zdradza wynik:
   kolory poprawności (zamienione na neutralne "zaznaczenie"), badge punktów,
   sumę w pasku, podpowiedzi, rozwiązania, samoocenę i PDF z zasadami oceniania.
   Tablice wzorów CKE zostają dostępne — na prawdziwej maturze też są.
   Stan egzaminu ({ start: timestamp }) siedzi w OSOBNYM kluczu localStorage,
   więc odświeżenie strony nie przerywa egzaminu, a zwykły zapis postępu
   (KLUCZ_POSTEPU) działa bez zmian. */
const KLUCZ_EGZAMINU = "matematykazen-egzamin-" + SHEET_ID;
const CZAS_EGZAMINU_MS = 170 * 60 * 1000; // 170 minut, jak na maturze podstawowej

const egzaminTimerSpan = document.getElementById("egzamin-timer");
const egzaminPodsumowanie = document.getElementById("egzamin-podsumowanie");
let egzaminInterval = null;

function readExamState() {
    try {
        const stan = JSON.parse(localStorage.getItem(KLUCZ_EGZAMINU));
        if (stan && typeof stan.start === "number") return stan;
    } catch (e) {}
    return null;
}

function formatTime(ms) {
    const s = Math.max(0, Math.round(ms / 1000));
    const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sek = s % 60;
    return `${h}:${String(m).padStart(2, "0")}:${String(sek).padStart(2, "0")}`;
}

// Tyka co sekundę: odświeża zegar w pasku; ostatnie 10 minut na czerwono.
// Koniec czasu kończy egzamin automatycznie — ale dopiero gdy zadania są
// wczytane (exercises.length), żeby podsumowanie miało skąd wziąć punkty
// (czas mógł minąć, gdy karta była zamknięta — wtedy kończymy zaraz po
// wczytaniu danych, pierwszym tyknięciem).
function tickExam() {
    const stan = readExamState();
    if (!stan) return;
    const pozostalo = stan.start + CZAS_EGZAMINU_MS - Date.now();
    egzaminTimerSpan.textContent = "⏱ " + formatTime(pozostalo);
    egzaminTimerSpan.classList.toggle("malo-czasu", pozostalo < 10 * 60 * 1000);
    if (pozostalo <= 0 && exercises.length) {
        finishExam(true);
    }
}

// Podtytuł trybu w pasku: stały element UI pokazujący, czy trwa zwykłe
// ćwiczenie czy próbny egzamin. Źródłem prawdy jest klasa body.tryb-egzaminu,
// więc wołamy to zawsze po jej dodaniu/zdjęciu.
function updateModeSubtitle() {
    const el = document.getElementById("exercises-mode-subtitle");
    if (el) el.textContent = document.body.classList.contains("tryb-egzaminu")
        ? "tryb egzaminu"
        : "tryb ćwiczenia";
}

// Opcje w menu "..." niedozwolone podczas próbnego egzaminu: zostają widoczne,
// ale disabled (CSS wyszarza je i blokuje klik) — inaczej po ukryciu menu
// zostawałoby pustą ramką. Odblokowujemy je z powrotem po zakończeniu egzaminu.
const OPCJE_MENU_EGZAMIN = ["show-all-solutions", "score-switch-button", "reset-scores", "egzamin-start"];
function setExamMenuDisabled(disabled) {
    OPCJE_MENU_EGZAMIN.forEach(id => {
        const btn = document.getElementById(id);
        if (!btn) return;
        btn.disabled = disabled;
        btn.title = disabled ? "Niedostępne podczas próbnego egzaminu" : "";
    });
}

function enableExamMode() {
    document.body.classList.add("tryb-egzaminu");
    updateModeSubtitle();
    setExamMenuDisabled(true);
    tickExam();
    if (!egzaminInterval) egzaminInterval = setInterval(tickExam, 1000);
}

// Start i koniec egzaminu mają po dwa przyciski w różnych miejscach UI
// (start: menu "⋯" + stopka arkusza; koniec: pasek górny + stopka arkusza).
// Każda para wisi na jednej wspólnej funkcji, żeby zachowanie nie mogło się
// kiedyś rozjechać między kopiami.
function startExamPrompt() {
    const zgoda = confirm(
        "Rozpocząć próbny egzamin?\n\n" +
        "• zapisane odpowiedzi i punkty zostaną wyczyszczone (egzamin startuje na czystym arkuszu),\n" +
        "• podpowiedzi, rozwiązania i punktacja będą ukryte do końca egzaminu,\n" +
        "• tablice wzorów CKE zostają dostępne — jak na prawdziwej maturze,\n" +
        "• czas: 170 minut."
    );
    if (!zgoda) return;
    try {
        localStorage.removeItem(KLUCZ_POSTEPU);
        localStorage.removeItem(KLUCZ_OCENIANIA); // nowy egzamin kasuje starą fazę „oceń się"
        localStorage.setItem(KLUCZ_EGZAMINU, JSON.stringify({ start: Date.now() }));
    } catch (e) {
        alert("Nie udało się zapisać stanu egzaminu (zablokowane localStorage) — egzamin nie wystartował.");
        return;
    }
    location.reload(); // świeży render: czysty arkusz + tryb egzaminu od pierwszej klatki
}
function finishExamPrompt() {
    if (confirm("Zakończyć egzamin i zobaczyć wynik?")) finishExam(false);
}

["egzamin-start", "egzamin-start-stopka"].forEach(id => {
    const btn = document.getElementById(id);
    if (btn) btn.addEventListener("click", startExamPrompt);
});
["egzamin-koniec", "egzamin-koniec-bar"].forEach(id => {
    const btn = document.getElementById(id);
    if (btn) btn.addEventListener("click", finishExamPrompt);
});

function finishExam(czasMinal) {
    const stan = readExamState();
    if (!stan) return;
    try { localStorage.removeItem(KLUCZ_EGZAMINU); } catch (e) {}
    if (egzaminInterval) { clearInterval(egzaminInterval); egzaminInterval = null; }
    document.body.classList.remove("tryb-egzaminu");
    updateModeSubtitle();
    setExamMenuDisabled(false);

    // Wynik z zadań zamkniętych (ocenianych automatycznie). Zadania otwarte
    // (selfScore) w egzaminie nie mają jak dostać punktów — samoocena była
    // schowana — więc rozliczamy je osobno, po egzaminie.
    const uzyty = Math.min(Date.now() - stan.start, CZAS_EGZAMINU_MS);
    const maxZamkniete = exercises.reduce((s, e) => s + (e.selfScore ? 0 : (e.maxScore || 0)), 0);
    const maxOtwarte = exercises.reduce((s, e) => s + (e.selfScore ? (e.maxScore || 0) : 0), 0);
    const punkty = exercises.reduce((s, e) => s + (e.earnedScore || 0), 0);
    const procent = maxZamkniete ? Math.round(punkty / maxZamkniete * 100) : 0;

    const okno = egzaminPodsumowanie.querySelector(".egzamin-okno");
    okno.innerHTML =
        `<h3>${czasMinal ? "Czas minął — egzamin zakończony" : "Egzamin zakończony"}</h3>` +
        `<p><b>Zadania zamknięte: ${punkty} / ${maxZamkniete} pkt (${procent}%).</b></p>` +
        `<p>Wykorzystany czas: ${formatTime(uzyty)} ze ${formatTime(CZAS_EGZAMINU_MS)}.</p>` +
        `<p><b>Zadania otwarte (${maxOtwarte} pkt) nie są jeszcze policzone.</b> Rozwiązania są już ` +
        `odblokowane — porównaj z nimi swoje notatki i oceń się pod każdym zadaniem otwartym ` +
        `("Rozwiąż na kartce…"); punkty doliczą się do sumy w pasku.</p>` +
        `<button id="egzamin-zamknij" class="light-button">wróć do arkusza</button>`;
    egzaminPodsumowanie.style.display = "flex";
    okno.querySelector("#egzamin-zamknij").addEventListener("click", () => {
        egzaminPodsumowanie.style.display = "none";
    });

    // Faza „oceń się": pokaż pływające wskaźniki przy zadaniach otwartych, które
    // uczeń wypełnił, ale których jeszcze nie ocenił.
    ustawFazeOceniania(true);
    pokazWskaznikiOtwarte();
}

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

function czyFazaOceniania() {
    try { return localStorage.getItem(KLUCZ_OCENIANIA) === "1"; } catch (e) { return false; }
}
function ustawFazeOceniania(wlacz) {
    try {
        if (wlacz) localStorage.setItem(KLUCZ_OCENIANIA, "1");
        else localStorage.removeItem(KLUCZ_OCENIANIA);
    } catch (e) {}
}

// Zadanie otwarte wypełnione (jest tok rozwiązania), ale bez samooceny.
function czyNieoceniony(zadanie) {
    return typeof zadanie.stan.open === "string" && zadanie.stan.open.trim() !== ""
        && !Number.isInteger(zadanie.stan.self);
}

function pokazWskaznikiOtwarte() {
    schowajWskaznikiZDOM(); // idempotentnie — zaczynamy od czysta
    const oczekujace = zadaniaOtwarte.filter(czyNieoceniony);
    if (!oczekujace.length) { ustawFazeOceniania(false); return; }

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
        wskaznikiUkryjBtn.textContent = "× ukryj";
        wskaznikiUkryjBtn.title = "Ukryj wszystkie wskaźniki nieocenionych zadań";
        wskaznikiUkryjBtn.addEventListener("click", ukryjWszystkieWskazniki);
        document.body.appendChild(wskaznikiUkryjBtn);
    }
    wskaznikiUkryjBtn.style.display = "block";

    window.addEventListener("scroll", zaplanujRepozycje, { passive: true });
    window.addEventListener("resize", zaplanujRepozycje);
    repozycjonujWskazniki();
}

function schowajWskaznikiZDOM() {
    wskaznikiEls.forEach(({ el }) => el.remove());
    wskaznikiEls = [];
    if (wskaznikiUkryjBtn) wskaznikiUkryjBtn.style.display = "none";
    window.removeEventListener("scroll", zaplanujRepozycje);
    window.removeEventListener("resize", zaplanujRepozycje);
}

// Po ocenieniu zadania (klik samooceny) usuwamy jego kropkę; gdy nie zostanie
// żadna — kończymy fazę oceniania.
function odswiezWskaznikiOtwarte() {
    if (!wskaznikiEls.length) return;
    wskaznikiEls = wskaznikiEls.filter(({ el, zadanie }) => {
        if (czyNieoceniony(zadanie)) return true;
        el.remove();
        return false;
    });
    if (!wskaznikiEls.length) {
        schowajWskaznikiZDOM();
        ustawFazeOceniania(false);
    } else {
        repozycjonujWskazniki();
    }
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
    const dol = window.innerHeight - 44 - polowa; // miejsce na przycisk „ukryj" u dołu
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

// Egzamin w toku (np. po odświeżeniu strony)? Tryb włączamy od razu, zanim
// cokolwiek się wyrenderuje — żadnego mignięcia punktów ani kolorów.
if (readExamState()) {
    enableExamMode();
}

// Tablica wzorów: panel (kontener) + <object> z PDF-em w środku. Pokazywanie/
// chowanie działa na panelu, a etykieta przycisku w pasku jest z tym zsynchronizowana.
const tablicaPanel = document.getElementById("tablica-wzorow-panel");
const toggleTablicaButton = document.getElementById("toggle-tablica");

function showFormulasPanel() {
    tablicaPanel.style.display = "block";
    toggleTablicaButton.textContent = "▲ Schowaj tablice wzorów";
}
function hideFormulasPanel() {
    tablicaPanel.style.display = "none";
    toggleTablicaButton.textContent = "▼ Pokaż tablice wzorów";
}

toggleTablicaButton.addEventListener("click", function() {
    const ukryta = tablicaPanel.style.display === "none" || tablicaPanel.style.display === "";
    if (ukryta) {
        showFormulasPanel();
    } else {
        hideFormulasPanel();
    }
});

// Krzyżyk w rogu tablicy wzorów po prostu ją chowa.
document.getElementById("tablica-close").addEventListener("click", hideFormulasPanel);

// Zasady oceniania: działa identycznie jak tablica wzorów, tylko po lewej
// stronie i bez podmieniania strony PDF-a (jeden dokument CKE z odpowiedziami).
const zasadyPanel = document.getElementById("zasady-oceniania-panel");
const toggleZasadyButton = document.getElementById("toggle-zasady");

function showGradingRules() {
    zasadyPanel.style.display = "block";
    toggleZasadyButton.textContent = "▲ Schowaj zasady oceniania";
}
function hideGradingRules() {
    zasadyPanel.style.display = "none";
    toggleZasadyButton.textContent = "▼ Pokaż zasady oceniania";
}

toggleZasadyButton.addEventListener("click", function() {
    const ukryte = zasadyPanel.style.display === "none" || zasadyPanel.style.display === "";
    if (ukryte) {
        showGradingRules();
    } else {
        hideGradingRules();
    }
});
document.getElementById("zasady-close").addEventListener("click", hideGradingRules);

// "Odblokowane" panele PDF: przeciąganie za górny pasek i zmiana rozmiaru za
// narożnik. Używamy pointer capture na uchwytach, bo <object> z PDF-em połyka
// zdarzenia myszy — bez capture przeciąganie urywałoby się nad dokumentem.
function makePanelDraggable(panel) {
    const uchwyt = panel.querySelector(".panel-uchwyt");
    const rozmiar = panel.querySelector(".panel-rozmiar");

    const topBar = document.getElementById("top-bar");

    uchwyt.addEventListener("pointerdown", (e) => {
        const r = panel.getBoundingClientRect();
        const dx = e.clientX - r.left;
        const dy = e.clientY - r.top;
        // Pasek uchwytu (a więc "chwyt" panelu) musi zostać w widocznym
        // viewportcie, żeby nie dało się go zgubić: u góry nie chowa się pod
        // top-barem, u dołu nie zjeżdża pod dolną krawędź ekranu (za pasek
        // zadań Windows), a w bok zostaje zawsze min. kawałek do złapania.
        const minTop = topBar ? topBar.getBoundingClientRect().bottom : 0;
        const uchwytH = uchwyt.offsetHeight || 46;
        const minWidoczne = 60; // ile px panelu musi zostać na ekranie w poziomie
        uchwyt.setPointerCapture(e.pointerId);
        const move = (ev) => {
            const szer = panel.getBoundingClientRect().width;
            let noweLeft = ev.clientX - dx;
            let noweTop = ev.clientY - dy;
            noweLeft = Math.min(Math.max(noweLeft, minWidoczne - szer), window.innerWidth - minWidoczne);
            noweTop = Math.min(Math.max(noweTop, minTop), window.innerHeight - uchwytH);
            panel.style.left = noweLeft + "px";
            panel.style.top = noweTop + "px";
            panel.style.right = "auto"; // od tej pory pozycjonujemy od lewej/góry
        };
        const up = () => {
            uchwyt.removeEventListener("pointermove", move);
            uchwyt.removeEventListener("pointerup", up);
            uchwyt.removeEventListener("pointercancel", up);
        };
        uchwyt.addEventListener("pointermove", move);
        uchwyt.addEventListener("pointerup", up);
        uchwyt.addEventListener("pointercancel", up);
    });

    rozmiar.addEventListener("pointerdown", (e) => {
        const r = panel.getBoundingClientRect();
        rozmiar.setPointerCapture(e.pointerId);
        const move = (ev) => {
            panel.style.width = Math.max(260, ev.clientX - r.left) + "px";
            panel.style.height = Math.max(200, ev.clientY - r.top) + "px";
        };
        const up = () => {
            rozmiar.removeEventListener("pointermove", move);
            rozmiar.removeEventListener("pointerup", up);
            rozmiar.removeEventListener("pointercancel", up);
        };
        rozmiar.addEventListener("pointermove", move);
        rozmiar.addEventListener("pointerup", up);
        rozmiar.addEventListener("pointercancel", up);
    });
}
makePanelDraggable(tablicaPanel);
makePanelDraggable(zasadyPanel);

function openFormulasAtPage(numerStrony) {
    const tablica = document.getElementById("tablica-wzorow");

    // Tworzymy nowy <object> zamiast tylko zmieniać `data` (przeglądarkowy
    // podgląd PDF nie zawsze przeładowuje się po samej zmianie atrybutu).
    const nowyObject = document.createElement("object");
    nowyObject.id = "tablica-wzorow";
    nowyObject.type = "application/pdf";
    nowyObject.data = `${TABLICE_PDF}#page=${numerStrony}&toolbar=0`;

    // Zamieniamy stary <object> na nowy w panelu (styl bierze się z CSS #tablica-wzorow).
    tablica.parentNode.replaceChild(nowyObject, tablica);

    showFormulasPanel();
}

const scoreSwitchButton = document.getElementById("score-switch-button");


scoreSwitchButton.addEventListener("click", () => {

    //potem można to podmienić na switch(scoreSwitchButton.innerHTML){}
    if(scoreSwitchButton.innerHTML == "widok punktów: wszystko"){

        scoreSwitchButton.innerHTML="widok punktów: tylko suma"

        const elements = document.getElementsByClassName('exercise-score');
        for (let el of elements) {
            el.style.display = "none";
        }
    }else if(scoreSwitchButton.innerHTML == "widok punktów: tylko suma"){

        scoreSwitchButton.innerHTML="widok punktów: nic"

        document.getElementById('total-score').style.display = "none";

    }else{
        scoreSwitchButton.innerHTML="widok punktów: wszystko"

        document.getElementById('total-score').style.display = "block";
        const elements = document.getElementsByClassName('exercise-score');
        for (let el of elements) {
            el.style.display = "block";
        }


    }

})

// Normalizacja odpowiedzi wpisywanych ręcznie (typ fillIn): bez spacji i bez
// różnic zapisu — nawiasy przedziałów ⟨ ⟩ oraz klawiaturowe < > sprowadzamy
// do [ ], minus typograficzny do zwykłego, średnik do przecinka. Dodatkowo
// wycinamy znaki zmiennej/przynależności (x, y, E/∈), żeby "x∈(-4,4]" czy
// "y ∈ [-1,3]" pasowało do samego przedziału z klucza — żadna poprawna
// odpowiedź w danych ich nie zawiera, więc usunięcie z obu stron jest bezpieczne.
// Obie strony porównania (wpis ucznia i wzorzec z danych) przechodzą przez tę samą funkcję.
function normalizeAnswer(s) {
    let wynik = (s || "")
        .replace(/\s+/g, "")
        .replace(/[−–]/g, "-")
        .replace(/[⟨<]/g, "[")
        .replace(/[⟩>]/g, "]")
        .replace(/;/g, ",")
        .replace(/[xye∈]/gi, "")
        .toLowerCase();
    // Zbędne zera na końcu części dziesiętnej: "6,50" ≡ "6,5", "7,0" ≡ "7".
    // Tylko gdy CAŁY wpis jest pojedynczą liczbą dziesiętną — w przedziale
    // typu "(-4,40]" przecinek rozdziela końce i nie wolno go ruszać.
    if (/^-?\d+[,.]\d*$/.test(wynik)) {
        wynik = wynik.replace(/0+$/, "").replace(/[,.]$/, "");
    }
    return wynik;
}

function markCorrectAnswer(exercise) {
    const button = exercise.querySelector(".answers-container button.hiddenCorrect");
    if (button) {
        button.classList.add("correct");
    }
}

// Zebrane przy renderowaniu odnośniki do przycisków/paneli "Rozwiązanie"
// wszystkich zadań — używa ich przycisk "pokaż wszystkie rozwiązania" w pasku.
const wszystkieRozwiazania = [];

// Rejestr zadań otwartych (selfScore) zbierany przy renderowaniu — używają go
// pływające wskaźniki nieocenionych zadań po egzaminie. Każdy wpis:
// { el: element zadania w DOM, stan: obiekt postępu (stan.open / stan.self), numer }.
const zadaniaOtwarte = [];

// Function to load exercises
function loadExercises() {
    const exercisesWrapper = document.getElementById("exercises-wrapper");
    const template = document.getElementById("exercise-template");

    const totalScoreSpan = document.getElementById("total-score");

    // Maksymalna liczba punktów liczona wprost z danych — nie trzeba już ręcznie
    // synchronizować stałej w exercises.js z sumą pól maxScore.
    const maxTotalScore = exercises.reduce((sum, e) => sum + (e.maxScore || 0), 0);

    // Suma punktów = suma zdobytych punktów ze wszystkich zadań. Liczymy ją od nowa
    // przy każdej zmianie, więc kolejność klików nie ma znaczenia i nie da się
    // podwójnie naliczyć ani zapomnieć odjąć punktu.
    function updateTotalScore() {
        totalScore = exercises.reduce((sum, e) => sum + (e.earnedScore || 0), 0);
        // Procent na bieżąco (tryb ćwiczeniowy — w trybie egzaminu #total-score
        // i tak jest ukryty). Próg zdawalności matury podstawowej to 30%: od
        // niego procent robi się zielony, a tooltip mówi "zdałeś" zamiast
        // "nie zdałeś (jeszcze)".
        const procent = maxTotalScore ? Math.round(totalScore / maxTotalScore * 100) : 0;
        const zdane = procent >= 30;
        totalScoreSpan.innerHTML =
            `${totalScore} / ${maxTotalScore} pkt ` +
            `<span class="total-percent${zdane ? " zdane" : ""}" ` +
            `title="${zdane ? "zdałeś" : "nie zdałeś (jeszcze)"}">${procent}%</span>`;
    }
    updateTotalScore();

    // ZAPIS POSTĘPU (localStorage). Zapamiętujemy "co użytkownik kliknął/wpisał",
    // a przy wczytaniu strony odtwarzamy to symulując te same kliknięcia — dzięki
    // temu ocena, kolory i punkty liczą się dokładnie tą samą drogą co na żywo.
    // Zapis z inną liczbą zadań (zmiana arkusza/schematu) jest ignorowany.
    // (KLUCZ_POSTEPU jest zadeklarowany globalnie na górze skryptu.)
    let zapis = null;
    try { zapis = JSON.parse(localStorage.getItem(KLUCZ_POSTEPU)); } catch (e) { zapis = null; }
    if (!zapis || zapis.n !== exercises.length || !Array.isArray(zapis.stany)) zapis = null;
    const stanOdpowiedzi = exercises.map(() => ({}));
    function zapiszPostep() {
        try {
            localStorage.setItem(KLUCZ_POSTEPU, JSON.stringify({ n: exercises.length, stany: stanOdpowiedzi }));
        } catch (e) { /* np. zablokowane localStorage — działamy dalej bez zapisu */ }
    }

    exercises.forEach((exercise, index) => {
        exercise.earnedScore = 0;
        const stan = stanOdpowiedzi[index];

        // Odnośniki do elementów odpowiedzi, przez które odtwarzamy zapisany
        // postęp na końcu budowania zadania (patrz blok "Przywrócenie postępu").
        const abcdButtons = [];
        const pfButtons = [];      // tablica tablic [przyciskP, przyciskF]
        const multiButtons = [];
        const selfButtons = [];
        const fillRows = [];
        let fillCheck = null;
        let openTextarea = null;   // textarea zadania otwartego (tok rozwiązania)

        //in the future we can make something like studentAttempt object that is passed by php after login and maybe chossing certan attempt in acc menu or smth

        const exerciseClone = template.cloneNode(true);
        exerciseClone.style.display = "block";
        exerciseClone.id = `exercise-${index}`;

        const scoreSpan = exerciseClone.querySelector(".exercise-score");

        // Jeden wspólny sposób ustawiania punktów zadania: aktualizuje earnedScore,
        // badge przy zadaniu (kolor zależny od 0 / część / komplet) i sumę w pasku.
        function setScore(points) {
            exercise.earnedScore = points;
            scoreSpan.textContent = `${points} / ${exercise.maxScore} pkt`;
            scoreSpan.classList.remove("low-exercise-score", "mid-exercise-score", "high-exercise-score");
            scoreSpan.classList.add(
                points === exercise.maxScore ? "high-exercise-score"
                : points > 0 ? "mid-exercise-score"
                : "low-exercise-score"
            );
            updateTotalScore();
        }

        // Set question
        exerciseClone.querySelector(".question").innerHTML = exercise.question;
        // Grafiki zadań spoza pierwszego ekranu dociągają się dopiero przy scrollu.
        exerciseClone.querySelectorAll(".question img").forEach(img => { img.loading = "lazy"; });

        // Set answers
        const answersContainer = exerciseClone.querySelector(".answers-container");

        // Typ zadania: jawny (exercise.type) albo wywnioskowany — odpowiedzi w answers
        // oznaczają zwykły test jednokrotnego wyboru, brak odpowiedzi = zadanie otwarte.
        const type = exercise.type || (exercise.answers && exercise.answers.length ? "ABCD" : "open");

        if (type === "ABCD") {
            // Poprawną odpowiedź wskazuje indeks z danych (0 = A, 1 = B, ...).
            // -1 lub brak pola = zadanie jeszcze niewypełnione -> tryb "?".
            const correctIndex = Number.isInteger(exercise.correctAnswerIndex) ? exercise.correctAnswerIndex : -1;
            if (correctIndex >= exercise.answers.length) {
                console.warn(`Zadanie ${index + 1}: correctAnswerIndex (${correctIndex}) wykracza poza liczbę odpowiedzi`);
            }

            exercise.answers.forEach((answer, i) => {
                const answerButton = document.createElement("button");
                answerButton.innerHTML = answer;
                if (i === correctIndex) {
                    answerButton.classList.add("hiddenCorrect");
                }
                answerButton.addEventListener("click", () => {
                    // Tryb "?" — brak zdefiniowanej poprawnej odpowiedzi (niewypełnione).
                    // Klik dokłada lub zdejmuje znak "?" (tylko jeden na zadanie).
                    if (correctIndex === -1) {
                        const hadFeedback = !!answerButton.querySelector(".feedback");
                        answersContainer.querySelectorAll(".feedback").forEach(f => f.remove());
                        if (!hadFeedback) {
                            answerButton.innerHTML += `<span class="feedback">?</span>`;
                        }
                        return;
                    }

                    // Wyczyść stan wszystkich przycisków, potem ustaw stan klikniętego.
                    answersContainer.querySelectorAll("button").forEach(btn => {
                        btn.classList.remove("correct", "incorrect");
                    });

                    if (i === correctIndex) {
                        answerButton.classList.add("correct");
                        setScore(exercise.maxScore);
                    } else {
                        // Zła odpowiedź: zawsze 0 / X pkt.
                        answerButton.classList.add("incorrect");
                        setScore(0);
                    }
                    stan.abcd = i;
                    zapiszPostep();
                });
                abcdButtons.push(answerButton);
                answersContainer.appendChild(answerButton);
            });
        } else if (type === "PF") {
            // Prawda/Fałsz: każde stwierdzenie dostaje własny wiersz z przyciskami P i F.
            // Punkty (0 albo maxScore) wpadają dopiero, gdy WSZYSTKIE odpowiedzi są
            // zaznaczone i poprawne — jak w arkuszu CKE.
            answersContainer.classList.add("pf-container");
            const chosen = new Array(exercise.statements.length).fill(null);

            exercise.statements.forEach((statement, si) => {
                const row = document.createElement("div");
                row.className = "pf-row";

                const label = document.createElement("span");
                label.className = "pf-text";
                label.innerHTML = `${si + 1}. ${statement.text}`;
                row.appendChild(label);

                const buttons = [];
                [["P", true], ["F", false]].forEach(([caption, value]) => {
                    const btn = document.createElement("button");
                    btn.textContent = caption;
                    btn.addEventListener("click", () => {
                        chosen[si] = value;
                        buttons.forEach(b => b.classList.remove("correct", "incorrect"));
                        btn.classList.add(value === statement.answer ? "correct" : "incorrect");

                        const answeredAll = chosen.every(c => c !== null);
                        const allCorrect = chosen.every((c, ci) => c === exercise.statements[ci].answer);
                        setScore(answeredAll && allCorrect ? exercise.maxScore : 0);
                        stan.pf = [...chosen];
                        zapiszPostep();
                    });
                    buttons.push(btn);
                    row.appendChild(btn);
                });
                pfButtons.push(buttons);

                answersContainer.appendChild(row);
            });
        } else if (type === "multiSelect") {
            // Wybór kilku odpowiedzi: klik zaznacza (jasnoniebieska ramka), ponowny klik
            // odznacza. Gdy komplet już zaznaczony, klik kolejnej odpowiedzi podmienia
            // najdawniej wybraną (okno przesuwne) — nie trzeba nic ręcznie odklikiwać.
            // Ocena następuje dopiero po zaznaczeniu wymaganej liczby odpowiedzi;
            // punkty częściowe: po 1 pkt za każde trafienie (maxScore/wymagane).
            answersContainer.classList.add("multi-select-container");
            const required = exercise.correctAnswerIndices.length;
            const selected = new Set();
            const buttons = [];

            const note = document.createElement("div");
            note.className = "multi-select-note";
            note.textContent = `Wybierz ${required === 2 ? "dwie odpowiedzi" : required + " odpowiedzi"}.`;
            answersContainer.appendChild(note);

            function refresh() {
                buttons.forEach((btn, i) => {
                    btn.classList.remove("correct", "incorrect", "selected");
                    if (!selected.has(i)) return;
                    if (selected.size === required) {
                        btn.classList.add(exercise.correctAnswerIndices.includes(i) ? "correct" : "incorrect");
                    } else {
                        btn.classList.add("selected");
                    }
                });
                if (selected.size === required) {
                    const hits = [...selected].filter(i => exercise.correctAnswerIndices.includes(i)).length;
                    setScore(Math.round(exercise.maxScore * hits / required));
                } else {
                    setScore(0);
                }
            }

            exercise.answers.forEach((answer, i) => {
                const btn = document.createElement("button");
                btn.innerHTML = answer;
                btn.addEventListener("click", () => {
                    if (selected.has(i)) {
                        selected.delete(i);
                    } else {
                        // Komplet już zaznaczony? Klik nowej odpowiedzi podmienia
                        // najdawniej wybraną (okno przesuwne), więc nie trzeba nic
                        // ręcznie odklikiwać, żeby zmienić zdanie. Set zachowuje
                        // kolejność wstawiania → najstarszy wybór to pierwszy element.
                        if (selected.size >= required) {
                            selected.delete(selected.values().next().value);
                        }
                        selected.add(i);
                    }
                    refresh();
                    stan.multi = [...selected];
                    zapiszPostep();
                });
                buttons.push(btn);
                multiButtons.push(btn);
                answersContainer.appendChild(btn);
            });
        } else if (type === "open" && exercise.selfScore && exercise.maxScore) {
            // Textarea na własną odpowiedź / tok rozwiązania. OSOBNY kontener
            // (nie w .self-score-container, bo ta jest chowana w trybie egzaminu):
            // podczas egzaminu samoocena znika, ale uczeń ma tu gdzie zapisać
            // rozwiązanie, a po egzaminie — gdy rozwiązania i samoocena wracają —
            // porównuje wpisany tok z kluczem i przyznaje sobie punkty. Zapis
            // idzie do localStorage tą samą drogą co reszta odpowiedzi (stan.open).
            const openBox = document.createElement("div");
            openBox.className = "open-answer-container";

            const openLabel = document.createElement("div");
            openLabel.className = "open-answer-label";
            openLabel.textContent = "Twoja odpowiedź / tok rozwiązania:";
            openBox.appendChild(openLabel);

            openTextarea = document.createElement("textarea");
            openTextarea.className = "open-answer";
            openTextarea.rows = 4;
            openTextarea.placeholder = "Zapisz tu swoją odpowiedź lub tok rozwiązania — po odsłonięciu rozwiązania porównasz je z kluczem i ocenisz się.";
            openTextarea.addEventListener("input", () => {
                stan.open = openTextarea.value;
                zapiszPostep();
            });
            openBox.appendChild(openTextarea);
            answersContainer.appendChild(openBox);

            // Zadanie otwarte z samooceną: uczeń rozwiązuje na kartce, porównuje
            // z rozwiązaniem i sam przyznaje sobie punkty (0..maxScore).
            const box = document.createElement("div");
            box.className = "self-score-container";

            const label = document.createElement("div");
            label.className = "self-score-label";
            label.textContent = "Rozwiąż na kartce, porównaj z rozwiązaniem i oceń się:";
            box.appendChild(label);

            const buttons = [];
            for (let n = 0; n <= exercise.maxScore; n++) {
                const btn = document.createElement("button");
                btn.textContent = `${n} pkt`;
                btn.addEventListener("click", () => {
                    buttons.forEach(b => b.classList.remove("selected"));
                    btn.classList.add("selected");
                    setScore(n);
                    stan.self = n;
                    zapiszPostep();
                    // Zadanie właśnie ocenione — jego wskaźnik (jeśli był) znika.
                    odswiezWskaznikiOtwarte();
                });
                buttons.push(btn);
                selfButtons.push(btn);
                box.appendChild(btn);
            }
            answersContainer.appendChild(box);

            // Do rejestru dla pływających wskaźników „oceń się" po egzaminie.
            zadaniaOtwarte.push({ el: exerciseClone, stan, numer: index + 1 });
        } else if (type === "fillIn") {
            // Zadanie z polami do uzupełnienia ("...") — uczeń wpisuje odpowiedzi
            // ręcznie, a przycisk "Sprawdź" koloruje ramki pól na zielono/czerwono
            // i przyznaje punkty proporcjonalnie do trafień (po równo za pole).
            // Wpis porównujemy z listą akceptowanych wariantów po normalizacji
            // (patrz normalizeAnswer), więc "(−4, 4⟩" i "(-4,4>" są równoważne.
            answersContainer.classList.add("fill-in-container");

            exercise.blanks.forEach(blank => {
                const row = document.createElement("div");
                row.className = "fill-in-row";

                const label = document.createElement("span");
                label.className = "fill-in-label";
                label.innerHTML = blank.label;
                row.appendChild(label);

                const input = document.createElement("input");
                input.type = "text";
                input.className = "fill-in-input";
                // Edycja pola kasuje jego poprzednią ocenę, żeby kolor nie kłamał.
                input.addEventListener("input", () => {
                    input.classList.remove("correct", "incorrect");
                });
                row.appendChild(input);

                answersContainer.appendChild(row);
                fillRows.push({ blank, input });
            });

            fillCheck = document.createElement("button");
            fillCheck.className = "fill-in-check";
            fillCheck.textContent = "Sprawdź";
            fillCheck.addEventListener("click", () => {
                let trafienia = 0;
                fillRows.forEach(({ blank, input }) => {
                    const wpis = normalizeAnswer(input.value);
                    const ok = wpis !== "" && blank.accepted.some(acc => normalizeAnswer(acc) === wpis);
                    input.classList.remove("correct", "incorrect");
                    input.classList.add(ok ? "correct" : "incorrect");
                    if (ok) trafienia++;
                });
                setScore(Math.round(exercise.maxScore * trafienia / fillRows.length));
                stan.fill = fillRows.map(r => r.input.value);
                zapiszPostep();
            });
            answersContainer.appendChild(fillCheck);
        }

        // Set score. Zadanie nadrzędne (maxScore: 0, np. wspólny wstęp Zadania 12/17)
        // nie ma badge'a punktów wcale — usuwamy go z DOM (samo display:none nie
        // wystarczy, bo przełącznik widoku punktów ustawia display na wszystkich
        // .exercise-score i by go przywrócił).
        if (exercise.maxScore) {
            scoreSpan.textContent = `0 / ${exercise.maxScore} pkt`;
        } else {
            scoreSpan.remove();
        }

        // Set hint — przycisk "Podpowiedź" znika, gdy zadanie nie ma podpowiedzi.
        const hintContainer = exerciseClone.querySelector(".hint-container");
        const hasHint = !!(exercise.hint && exercise.hint.trim() !== "");
        hintContainer.innerHTML = exercise.hint || "";
        if (!hasHint) {
            exerciseClone.querySelector(".hint-button").style.display = "none";
        }

        // Set solution
        const solutionContainer = exerciseClone.querySelector(".solution-container");
        const solutionTextContainer = solutionContainer.querySelector(".solution-text-container");

        const solutionStepByStepContainer = exerciseClone.querySelector(".solution-step-by-step-container");

        const solutionInteractiveContainer = exerciseClone.querySelector(".solution-interactive-container");

        const solutionTextMoreContainer = solutionContainer.querySelector(".solution-text-more-container");
        const solutionTextMoreSpan = solutionTextMoreContainer.querySelector(".solution-text-more");
        const showMoreButton = solutionTextMoreContainer.querySelector("button");

        // Set solutionTextMore content
        solutionTextMoreSpan.innerHTML = exercise.solutionTextMore || "";

        // Initially hide the solutionTextMore content
        solutionTextMoreSpan.style.display = "none";

        // Add click event listener to show/hide button
        showMoreButton.addEventListener("click", () => {
            if (solutionTextMoreSpan.style.display === "none") {
                solutionTextMoreSpan.style.display = "block";
                showMoreButton.textContent = "Schowaj więcej";
            } else {
                solutionTextMoreSpan.style.display = "none";
                showMoreButton.textContent = "Pokaż więcej";
            }
        });

        // Hide the entire container if there's no solutionTextMore content
        if (!exercise.solutionTextMore || exercise.solutionTextMore.trim() === "") {
            solutionTextMoreContainer.style.display = "none";
        }

        solutionTextContainer.innerHTML = exercise.solutionText || "";

        // Widżet interaktywny: w danych (JSON) jest tylko NAZWA widżetu (string),
        // funkcję bierzemy z rejestru WIDZETY zdefiniowanego przy widżetach niżej.
        if (exercise.solutionInteractive) {
            const widget = WIDZETY[exercise.solutionInteractive];
            if (widget) {
                widget(solutionInteractiveContainer);
            } else {
                console.warn(`Zadanie ${index + 1}: nieznany widżet "${exercise.solutionInteractive}"`);
            }
        }

        // Add event listeners for hint and solution buttons
        const formulasButton = exerciseClone.querySelector(".formulas-button")

        if(exercise.formulasPage != null){
            formulasButton.addEventListener("click", () => {
                openFormulasAtPage(exercise.formulasPage)
            });
        }else{
            formulasButton.style.display = "none";

        }

        exerciseClone.querySelector(".hint-button").addEventListener("click", () => {
            hintContainer.style.display = hintContainer.style.display === "block" ? "none" : "block";
            solutionContainer.style.display = "none";
        });

        // SOLUTION STEP BY STEP
        // Kroki i showStep wynosimy poza blok if, żeby widział je jeden wspólny
        // handler przycisku "Rozwiązanie" (poniżej).
        const stepsContent = solutionStepByStepContainer.querySelector(".steps-content");
        const stepsNav = solutionStepByStepContainer.querySelector(".steps-nav");
        const prevBtn = stepsNav.querySelector(".step-prev");
        const nextBtn = stepsNav.querySelector(".step-next");
        const stepCounter = stepsNav.querySelector(".step-counter");

        function renderStep(step) {

            if (!step) return "";
            // Podpis kroku zawsze w .step-comment — rezerwuje stałe miejsce (~2 linijki),
            // dzięki czemu wysokość diva nie skacze między krokami o różnej długości tekstu.
            if (step.type === "video") {
                // Prędkość ustawiamy na realnym elemencie <video> w showStep(),
                // bo właściwość JS (defaultPlaybackRate) nie przetrwałaby
                // serializacji do stringa HTML. Tam też podpinamy klik (pauza/play)
                // i ikonkę ▶ (widoczną gdy zatrzymany).
                return `
                    <div class="step-video">
                        <video autoplay playsinline>
                            <source src="${mediaPath(step.src)}" type="video/mp4">
                        </video>
                        <div class="video-overlay-icon"></div>
                    </div>
                    <div class="step-comment">${step.text}</div>
                `;
            } else if (step.type === "image") {
                return `<img src="${mediaPath(step.src)}"><div class="step-comment">${step.text}</div>`;
            } else if (step.type === "text") {
                return `<div class="step-comment">${step.text}</div>`;
            }
            return "";
        }

        const hasSteps = Array.isArray(exercise.solutionStepByStep);
        const steps = hasSteps ? exercise.solutionStepByStep : [];
        let currentStep = 0;

        // Separator (dolna kreska) rozdziela kolejne bloki rozwiązania. Pod ostatnim
        // widocznym blokiem jest zbędny (np. gdy rozwiązanie to sam tekst) — zdejmujemy
        // go z ostatniego widocznego bloku.
        const hasText = !!(exercise.solutionText && exercise.solutionText.trim() !== "");
        const hasInteractive = !!(exercise.solutionInteractive && WIDZETY[exercise.solutionInteractive]);
        const hasMore = !!(exercise.solutionTextMore && exercise.solutionTextMore.trim() !== "");
        const solutionBlocks = [
            hasText ? solutionTextContainer : null,
            hasSteps ? solutionStepByStepContainer : null,
            hasInteractive ? solutionInteractiveContainer : null,
            hasMore ? solutionTextMoreContainer : null,
        ].filter(Boolean);
        if (solutionBlocks.length) {
            solutionBlocks[solutionBlocks.length - 1].style.borderBottom = "none";
        }

        // Przycisk "Rozwiązanie" ma sens tylko, gdy istnieje jakiekolwiek rozwiązanie
        // (tekst / kroki / interaktywne / "pokaż więcej"). W przeciwnym razie go chowamy.
        const hasAnySolution = solutionBlocks.length > 0;
        const solutionButton = exerciseClone.querySelector(".solution-button");
        if (!hasAnySolution) {
            solutionButton.style.display = "none";
        }
        // Rejestr dla przycisku "pokaż wszystkie rozwiązania" w pasku.
        wszystkieRozwiazania.push({ przycisk: solutionButton, panel: solutionContainer, ma: hasAnySolution });

        // Podwójny bufor kroków: przy przejściu na krok z filmem STARY krok
        // zostaje widoczny (na ostatniej klatce), a nowy podmieniamy dopiero,
        // gdy jego film ma zdekodowaną pierwszą klatkę (loadeddata) — dzięki
        // temu nie ma błysku pustego miejsca. Token chroni przed wyścigiem
        // przy szybkim klikaniu ◄/► (spóźniona podmiana starego kroku jest
        // ignorowana). Fallback setTimeout podmienia krok nawet, gdyby film
        // ładował się wyjątkowo długo (wtedy mignięcie może wrócić — trudno).
        let stepSwapToken = 0;

        function showStep(idx) {
            currentStep = idx;
            const swapToken = ++stepSwapToken;

            // Nawigacja aktualizuje się od razu (nie czeka na załadowanie filmu).
            stepCounter.textContent = `${currentStep + 1} / ${steps.length}`;
            prevBtn.disabled = currentStep === 0;
            nextBtn.disabled = currentStep === steps.length - 1;
            if (currentStep == steps.length - 1) {
                markCorrectAnswer(exerciseClone);
            }

            // Nowy krok budujemy w odłączonym elemencie i dopiero gotowy
            // wstawiamy w miejsce starego (replaceChildren).
            const nowyKrok = document.createElement("div");
            nowyKrok.innerHTML = renderStep(steps[currentStep]);
            renderMath(nowyKrok);

            const video = nowyKrok.querySelector("video");
            let krokWstawiony = false; // loadeddata i fallback setTimeout mogą przyjść oba
            const wstawKrok = () => {
                if (swapToken !== stepSwapToken) return; // w międzyczasie wybrano inny krok
                if (krokWstawiony) return;
                krokWstawiony = true;
                stepsContent.replaceChildren(...nowyKrok.childNodes);
                if (video) {
                    // play() zamiast atrybutu autoplay: film ma wystartować
                    // dopiero po wstawieniu do DOM, nie w buforze.
                    video.play().catch(() => {});
                }
                podepnijSterowanieWideo(video);
            };

            if (video && stepsContent.childElementCount) {
                video.removeAttribute("autoplay");
                video.preload = "auto";
                video.load(); // element odłączony też się ładuje
                if (video.readyState >= 2) { // HAVE_CURRENT_DATA — np. film z cache
                    wstawKrok();
                } else {
                    video.addEventListener("loadeddata", wstawKrok, { once: true });
                    setTimeout(wstawKrok, 1500);
                }
            } else {
                // Pierwszy render kroku albo krok bez filmu — podmiana od razu.
                wstawKrok();
            }

            // Podgrzewamy film następnego kroku, żeby przełączenie mniej migało —
            // przeglądarka ściąga go do cache, zanim użytkownik kliknie ►.
            const nextStep = steps[currentStep + 1];
            if (nextStep && nextStep.type === "video") {
                const preload = document.createElement("video");
                preload.preload = "auto";
                preload.src = mediaPath(nextStep.src);
            }
        }

        // Sterowanie filmem kroku (klik = pauza/play, ikonka stanu) —
        // podpinane do realnego, już wstawionego <video>.
        // (Pasek postępu z pętlą requestAnimationFrame usunięty: klatkował
        // stronę w Firefoksie podczas przewijania, a bajer nie był tego wart.)
        function podepnijSterowanieWideo(video) {
            if (video) {
                video.defaultPlaybackRate = 1;
                video.playbackRate = 1;

                const stepVideo = video.closest(".step-video");

                // Klik w film przełącza pauzę/odtwarzanie.
                video.addEventListener("click", () => {
                    if (video.paused) {
                        video.play();
                    } else {
                        video.pause();
                    }
                });

                // Klasy stanu na kontenerze sterują ikonką:
                //  .paused (bez .ended) → dwie kreski (pauza),
                //  .ended               → zakręcona strzałka (odtwórz od nowa).
                const syncState = () => {
                    if (stepVideo) {
                        stepVideo.classList.toggle("paused", video.paused);
                        stepVideo.classList.toggle("ended", video.ended);
                    }
                };
                video.addEventListener("play", syncState);
                video.addEventListener("pause", syncState);
                video.addEventListener("ended", syncState);

                syncState();
            }
        }

        if (hasSteps) {
            prevBtn.addEventListener("click", () => {
                if (currentStep > 0) showStep(currentStep - 1);
            });
            nextBtn.addEventListener("click", () => {
                if (currentStep < steps.length - 1) showStep(currentStep + 1);
            });
        }

        // Jeden handler przycisku "Rozwiązanie": chowa podpowiedź, przełącza panel
        // rozwiązania, a gdy zadanie ma kroki — pokazuje je i renderuje bieżący krok
        // (kroki pojawiają się dopiero po tym kliknięciu, ostatni woła markCorrectAnswer).
        solutionButton.addEventListener("click", () => {
            hintContainer.style.display = "none";
            solutionContainer.style.display = solutionContainer.style.display === "block" ? "none" : "block";

            if (hasSteps) {
                solutionStepByStepContainer.style.display = "block";
                showStep(currentStep);
            } else {
                solutionStepByStepContainer.style.display = "none";
            }
        });


        // Przywrócenie postępu: symulujemy dokładnie te kliknięcia/wpisy, które
        // użytkownik wykonał wcześniej — ocena i punkty liczą się tą samą drogą,
        // więc nie ma drugiej, równoległej logiki oceniania do utrzymywania.
        const zap = zapis ? zapis.stany[index] : null;
        if (zap) {
            if (Number.isInteger(zap.abcd) && abcdButtons[zap.abcd]) {
                abcdButtons[zap.abcd].click();
            }
            if (Array.isArray(zap.pf)) {
                zap.pf.forEach((wybor, si) => {
                    if (wybor !== null && pfButtons[si]) pfButtons[si][wybor ? 0 : 1].click();
                });
            }
            if (Array.isArray(zap.multi)) {
                zap.multi.forEach(i => { if (multiButtons[i]) multiButtons[i].click(); });
            }
            if (Number.isInteger(zap.self) && selfButtons[zap.self]) {
                selfButtons[zap.self].click();
            }
            if (typeof zap.open === "string" && openTextarea) {
                openTextarea.value = zap.open;
                // Odtwórz też stan w pamięci (input nie odpala się przy ustawianiu
                // .value): inaczej stan.open byłby pusty po reloadzie — kolejny
                // zapis (np. klik samooceny) skasowałby zapisany tok rozwiązania,
                // a wskaźniki „oceń się" nie wiedziałyby, że zadanie jest wypełnione.
                stan.open = zap.open;
            }
            if (Array.isArray(zap.fill) && fillRows.length) {
                zap.fill.forEach((tekst, i) => { if (fillRows[i]) fillRows[i].input.value = tekst || ""; });
                if (zap.fill.some(t => t) && fillCheck) fillCheck.click();
            }
        }

        // Obrazki osadzone w HTML zadania (treść, podpowiedź, rozwiązanie) mają
        // w danych ścieżki względne do folderu arkusza (np. "media/zad11/…") —
        // przepisujemy je przez mediaPath, bo strona renderuje się z rootu.
        // (Filmy/obrazki kroków step-by-step idą osobno przez renderStep.)
        exerciseClone.querySelectorAll("img[src]").forEach((img) => {
            img.setAttribute("src", mediaPath(img.getAttribute("src")));
        });

        // KaTeX: renderujemy wzory w całym zbudowanym zadaniu (treść, odpowiedzi,
        // podpowiedź, rozwiązania). Kroki step-by-step renderują się osobno w
        // showStep(), bo ich HTML powstaje dopiero przy przełączaniu kroków.
        renderMath(exerciseClone);

        // Append the exercise to the wrapper
        exercisesWrapper.appendChild(exerciseClone);
    });
}

// Wypełnia chrome strony (tytuł karty, meta description, tytuł w pasku, PDF
// zasad oceniania, domyślna strona tablicy wzorów) danymi z pola "meta"
// exercises.json — jedyne miejsce, gdzie template.html dowiaduje się, JAKI
// to arkusz (poza samymi zadaniami).
function applySheetMeta(meta) {
    if (!meta) return;
    if (meta.pageTitle) document.title = meta.pageTitle;
    if (meta.metaDescription) {
        const opis = document.querySelector('meta[name="description"]');
        if (opis) opis.setAttribute("content", meta.metaDescription);
    }
    const tytulEl = document.getElementById("exercises-sheet-title");
    if (tytulEl && meta.sheetTitle) tytulEl.textContent = meta.sheetTitle;
    if (meta.zasadyPdf) {
        // zasadyPdf jest ścieżką względną do folderu arkusza (jak media),
        // więc idzie przez mediaPath. encodeURI na wypadek spacji w nazwie.
        document.getElementById("zasady-oceniania").data = `${encodeURI(mediaPath(meta.zasadyPdf))}#toolbar=0`;
    }
    if (meta.tablicaPdfDefaultPage) {
        document.getElementById("tablica-wzorow").data =
            `${TABLICE_PDF}#page=${meta.tablicaPdfDefaultPage}&toolbar=0`;
    }
}

// Wspólny sposób pokazania komunikatu zamiast arkusza (pusta strona myli).
function pokazKomunikat(html) {
    const info = document.createElement("div");
    info.className = "blad-wczytywania";
    info.innerHTML = html;
    document.getElementById("exercises-wrapper").appendChild(info);
}

// Nieznany / brakujący / pusty ?arkusz= — to nie jest awaria serwera, tylko
// błędny link (np. wpisany ręcznie). Kierujemy użytkownika na stronę główną.
function pokazBladLinku() {
    pokazKomunikat(
        "<b>Błędny link.</b><br>" +
        "Nie znaleziono takiego arkusza. " +
        '<a href="index.html">Wróć do strony głównej</a> i wybierz arkusz z listy.'
    );
}

// Start strony: dane zadań przychodzą fetchem z matura/<SHEET_ID>/exercises.json
// (obiekt { meta, exercises } — patrz ARCHITECTURE.md). UWAGA: fetch nie
// działa z file:// — wtedy (i przy każdym innym niepowodzeniu) pokazujemy
// czytelny komunikat zamiast pustej strony.
async function startSheet() {
    // Brak parametru albo pusty ?arkusz= — bez fetchu, od razu błędny link.
    if (!SHEET_ID) {
        pokazBladLinku();
        return;
    }

    let odpowiedz;
    try {
        odpowiedz = await fetch(`matura/${SHEET_ID}/exercises.json`);
    } catch (blad) {
        // Brak odpowiedzi z serwera: najczęściej file:// (fetch zablokowany),
        // rzadziej padnięta sieć — to nie to samo co nieznany arkusz.
        pokazKomunikat(location.protocol === "file:"
            ? "<b>Nie udało się wczytać zadań (exercises.json).</b><br>" +
              "Strona jest otwarta bezpośrednio z pliku (<code>file://</code>), a przeglądarka " +
              "blokuje wtedy wczytywanie danych. Uruchom ją przez lokalny serwer, np. " +
              "<code>npx serve</code> albo <code>python -m http.server</code> w folderze strony."
            : "<b>Nie udało się wczytać zadań (exercises.json).</b><br>" +
              "Odśwież stronę; jeśli błąd wraca, sprawdź, czy plik exercises.json jest na serwerze. " +
              `<small>(${blad.message})</small>`);
        return;
    }

    // Serwer odpowiedział błędem (404 itp.) — nie ma folderu arkusza o tym id,
    // czyli ?arkusz= wskazuje na nieistniejący arkusz: błędny link.
    if (!odpowiedz.ok) {
        pokazBladLinku();
        return;
    }

    try {
        const dane = await odpowiedz.json();
        exercises = dane.exercises;
        applySheetMeta(dane.meta);
    } catch (blad) {
        pokazKomunikat(
            "<b>Nie udało się wczytać zadań (exercises.json).</b><br>" +
            "Odśwież stronę; jeśli błąd wraca, plik może być uszkodzony. " +
            `<small>(${blad.message})</small>`);
        return;
    }
    loadExercises();
    // Jeśli czas egzaminu minął, gdy karta była zamknięta — zakończ od razu
    // (tickExam ma warunek na wczytane zadania, teraz już spełniony).
    if (readExamState()) tickExam();
    // Faza „oceń się" po egzaminie (nie w trakcie egzaminu): odtwórz pływające
    // wskaźniki nieocenionych zadań otwartych, żeby przetrwały odświeżenie strony.
    else if (czyFazaOceniania()) pokazWskaznikiOtwarte();
}
startSheet();

// "Pokaż/schowaj wszystkie rozwiązania": przełącznik w pasku. Otwiera lub
// zamyka panel rozwiązania każdego zadania klikając jego własny przycisk
// (ta sama ścieżka co ręczne klikanie — kroki, filmy itd. działają normalnie).
// Pomijamy zadania będące już w docelowym stanie, więc ręcznie otwarte
// rozwiązania nie "mrugają" i nie zamykają się przy "pokaż wszystkie".
const showAllButton = document.getElementById("show-all-solutions");
let wszystkieOtwarte = false;
showAllButton.addEventListener("click", () => {
    wszystkieOtwarte = !wszystkieOtwarte;
    wszystkieRozwiazania.forEach(({ przycisk, panel, ma }) => {
        if (!ma) return;
        const otwarty = panel.style.display === "block";
        if (otwarty !== wszystkieOtwarte) przycisk.click();
    });
    showAllButton.textContent = wszystkieOtwarte
        ? "schowaj wszystkie rozwiązania"
        : "pokaż wszystkie rozwiązania";
});

    
