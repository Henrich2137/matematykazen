// app/exam.js — tryb egzaminacyjny (próbny egzamin na czas) + timer.

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
        // Zapis stanu egzaminu NAJPIERW: jeśli setItem rzuci (pełne localStorage,
        // tryb prywatny), zapisany postęp ma zostać nietknięty — inaczej alert
        // mówiłby "egzamin nie wystartował", a odpowiedzi i tak by już zniknęły.
        localStorage.setItem(KLUCZ_EGZAMINU, JSON.stringify({ start: Date.now() }));
        localStorage.removeItem(KLUCZ_POSTEPU);
        localStorage.removeItem(KLUCZ_OCENIANIA); // nowy egzamin kasuje starą fazę „oceń się"
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

    // Tablica wzorów CKE zostaje dostępna W TRAKCIE egzaminu (jak na prawdziwej
    // maturze), ale po jego zakończeniu nie ma już powodu trzymać ją otwartą —
    // chowamy ją razem z resztą ukrytych podczas egzaminu elementów.
    const tablicaPanel = document.getElementById("tablica-wzorow-panel");
    if (tablicaPanel && tablicaPanel.style.display === "block") hideFormulasPanel();

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

// Egzamin w toku (np. po odświeżeniu strony)? Tryb włączamy od razu, zanim
// cokolwiek się wyrenderuje — żadnego mignięcia punktów ani kolorów.
if (readExamState()) {
    enableExamMode();
}
