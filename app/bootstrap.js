// app/bootstrap.js — punkt wejścia strony (startSheet + komunikaty błędów +
// applySheetMeta) oraz chrome panelu bocznego (otwieranie/zamykanie, reset,
// punktacja, pokaż wszystkie rozwiązania). Ładowany OSTATNI z bloku app/*, bo
// startSheet() woła loadExercises() i wiele funkcji z pozostałych plików.

/* ===== PANEL BOCZNY (#sidebar) =====
   Otwiera i zamyka JEDNA strzałka przy logo (#sidebar-toggle), dodatkowo Esc.
   Stan NIE jest zapamiętywany między odświeżeniami — świadomie: panel jest do
   sporadycznych akcji, nie do stałego trzymania otwartym.

   PRÓG 1300px („panel zasłania treść") steruje trzema rzeczami naraz, żeby nie
   mnożyć niezależnych warunków — na wąskim laptopie panel zasłania zadanie
   dokładnie tak samo jak na telefonie, więc warunek jest spięty z progiem,
   a nie z czyTelefon():
     • przyciemnienie treści     — CSS (style/responsive.css),
     • zamykanie klikiem w arkusz — CSS (pointer-events na przyciemnieniu),
     • zamykanie po kliknięciu AKCJI — tutaj, w JS.
   Kliknięcie USTAWIENIA nie zamyka panelu na żadnej szerokości: cykl klika się
   po kilka razy pod rząd (wszystko → tylko suma → wył.), więc zamykanie po
   każdym stopniu zmuszałoby do otwierania panelu od nowa. */
const PROG_SIDEBAR_NAKLADA = 1300;
const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebar-toggle");
const sidebarPrzyciemnienie = document.getElementById("sidebar-przyciemnienie");

function sidebarNaklada() {
    try {
        return window.matchMedia(`(max-width: ${PROG_SIDEBAR_NAKLADA - 1}px)`).matches;
    } catch (e) { return true; }
}
function czySidebarOtwarty() {
    return document.body.classList.contains("sidebar-otwarty");
}
function otworzSidebar() {
    document.body.classList.add("sidebar-otwarty");
    if (sidebarToggle) {
        sidebarToggle.setAttribute("aria-expanded", "true");
        sidebarToggle.setAttribute("aria-label", "Zamknij menu");
    }
    // Fokus na pierwszą WIDOCZNĄ pozycję (część jest chowana zależnie od trybu).
    // Świadomie BEZ focus trapu: panel nie jest modalem, ma się dać wyjść Tabem
    // do treści arkusza.
    // requestAnimationFrame jest KONIECZNE: zamknięty panel ma visibility: hidden,
    // a elementu z visibility: hidden nie da się zafokusować. Klasa dopiero co
    // wylądowała na <body>, więc bez odczekania jednej klatki (przeliczenie stylu)
    // focus() cicho nic nie robi i fokus zostaje na strzałce.
    requestAnimationFrame(() => {
        if (!czySidebarOtwarty() || !sidebar) return; // zamknięty w międzyczasie
        const pierwsza = Array.from(sidebar.querySelectorAll("button"))
            .find(b => !b.disabled && b.offsetParent !== null);
        if (pierwsza) pierwsza.focus();
    });
}
// wrocFokus: Esc oddaje fokus strzałce — inaczej fokus zostaje w zamkniętym
// (visibility: hidden) panelu i Tab startuje z nieoczywistego miejsca.
function zamknijSidebar(wrocFokus) {
    document.body.classList.remove("sidebar-otwarty");
    if (sidebarToggle) {
        sidebarToggle.setAttribute("aria-expanded", "false");
        sidebarToggle.setAttribute("aria-label", "Otwórz menu");
        if (wrocFokus) sidebarToggle.focus();
    }
}
if (sidebarToggle) {
    sidebarToggle.addEventListener("click", () => {
        if (czySidebarOtwarty()) zamknijSidebar(false);
        else otworzSidebar();
    });
}
if (sidebarPrzyciemnienie) {
    // Klikalne tylko poniżej progu (pointer-events z CSS), więc bez warunku w JS.
    sidebarPrzyciemnienie.addEventListener("click", () => zamknijSidebar(false));
}
document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && czySidebarOtwarty()) zamknijSidebar(true);
});
if (sidebar) {
    // Delegacja na kontenerze: własny handler przycisku odpala się PIERWSZY
    // (bąbelkowanie), więc akcja zawsze wykonuje się przed zamknięciem panelu.
    sidebar.addEventListener("click", (e) => {
        if (e.target.closest(".sidebar-akcja") && sidebarNaklada()) zamknijSidebar(false);
    });
}

// "Zresetuj arkusz": kasuje zapisany postęp i przeładowuje stronę — punkty,
// kolory odpowiedzi i wpisy wracają do zera jedną, wspólną drogą (świeży render).
document.getElementById("reset-scores").addEventListener("click", () => {
    if (!confirm(
        "Zresetować arkusz? Zapisane odpowiedzi i punkty zostaną wyczyszczone, " +
        "a tej operacji nie można cofnąć.\n\n" +
        "Jeśli w innej karcie trwa właśnie próbny egzamin na tym arkuszu, zostanie on też zakończony."
    )) return;
    try {
        localStorage.removeItem(KLUCZ_POSTEPU);
        localStorage.removeItem(KLUCZ_OCENIANIA); // reset kasuje też fazę „oceń się"
        localStorage.removeItem(KLUCZ_EGZAMINU); // ...i ewentualny trwający egzamin w innej karcie
    } catch (e) {}
    location.reload();
});

/* Ustawienie „Punktacja" w panelu bocznym: wszystko → tylko suma → wył. → ...
   Trzy stany, dwa niezależne elementy:
     wszystko   — badge przy każdym zadaniu + suma w narożniku,
     tylko suma — bez badge'y, suma zostaje,
     wył.       — jedno i drugie schowane.
   Kolejność i kierunek cyklu (w LEWO, czyli „ujmuje o stopień") biorą się
   z data-stany/data-kierunek w template.html — patrz nastepnyStan() w state.js.
   Dawniej ten cykl rozpoznawał stan przez porównanie innerHTML przycisku ze
   stringiem; z ikoną i kropkami w środku było to nie do utrzymania, więc
   jedynym źródłem prawdy jest teraz data-stan. */
const scoreSwitchButton = document.getElementById("score-switch-button");

function zastosujWidokPunktow(stan) {
    const pokazBadge = stan === "wszystko";
    const pokazSume = stan !== "wył.";
    document.querySelectorAll(".exercise-score").forEach(el => {
        el.style.display = pokazBadge ? "block" : "none";
    });
    const suma = document.getElementById("total-score");
    // Uwaga: w trybie egzaminu exam.css chowa #total-score przez !important,
    // więc ten inline display go nie odsłoni — i dobrze.
    if (suma) suma.style.display = pokazSume ? "block" : "none";
    ustawWartosc(scoreSwitchButton, stan);
}

if (scoreSwitchButton) {
    ustawWartosc(scoreSwitchButton, scoreSwitchButton.dataset.stan); // kropki + podgląd na starcie
    scoreSwitchButton.addEventListener("click", () => {
        zastosujWidokPunktow(nastepnyStan(scoreSwitchButton));
    });
}

// Na TELEFONIE domyślnie chowamy badge'e punktów przy zadaniach — na wąskim
// ekranie zaśmiecają kartę, a bieżąca suma i tak jest w narożniku. To tylko
// wartość DOMYŚLNA: użytkownik dalej może cyklicznie przełączać widok tym samym
// ustawieniem „Punktacja". Ustawiamy stan „tylko suma" po wyrenderowaniu zadań
// (badge'e muszą już istnieć). Na desktopie no-op.
function zastosujDomyslnyWidokPunktowMobile() {
    if (!czyTelefon()) return;
    zastosujWidokPunktow("tylko suma");
}

// Ustawienie „Poprawność odpowiedzi" (panel boczny): GLOBALNE (localStorage,
// bez sufiksu arkusza — patrz app/state.js). „natychmiast" = klik odpowiedzi
// zamkniętej od razu koloruje ramkę; „po „sprawdź"" = dopiero po kliknięciu
// przycisku. body.reczne-sprawdzanie (w tym drugim trybie) odsłania przyciski
// „sprawdź wszystkie odpowiedzi".
const natychmiastowaToggle = document.getElementById("natychmiastowa-toggle");
const WARTOSC_NATYCHMIAST = "natychmiast";
function odswiezTrybPoprawnosci() {
    const on = czyNatychmiastowaPoprawnosc();
    document.body.classList.toggle("reczne-sprawdzanie", !on);
    ustawWartosc(natychmiastowaToggle, on ? WARTOSC_NATYCHMIAST : "po „sprawdź”");
}
odswiezTrybPoprawnosci();
if (natychmiastowaToggle) {
    natychmiastowaToggle.addEventListener("click", () => {
        const nast = nastepnyStan(natychmiastowaToggle);
        try {
            localStorage.setItem(KLUCZ_NATYCHM_POPRAWNOSC, nast === WARTOSC_NATYCHMIAST ? "1" : "0");
        } catch (e) {}
        odswiezTrybPoprawnosci();
    });
}

// „Sprawdź wszystkie odpowiedzi" (panel boczny + kopia w stopce arkusza):
// odsłania ocenę wszystkich zadań (ABCD/PF/multiSelect/fillIn/finalAnswer —
// patrz rejestracje w oczekujaceSprawdzenia w app/render.js), które mają
// zaznaczoną, a jeszcze nieodsłoniętą odpowiedź (to samo, co ręczne kliknięcie
// każdego widocznego „sprawdź"). Pomija zadania bez zaznaczenia i już sprawdzone.
function sprawdzWszystkieOdpowiedzi() {
    oczekujaceSprawdzenia.forEach(z => {
        if (z.maZaznaczenie() && !z.czySprawdzone()) z.ocen();
    });
    // Czy jest cokolwiek zaznaczone (czyli oceniona odpowiedź, czy to teraz, czy
    // wcześniej) — to decyduje o kolorze komunikatu niżej, NIE to, czy ten klik
    // akurat coś nowego ocenił: jeśli wszystko było już sprawdzone wcześniej,
    // "sprawdzono ✓" wciąż jest prawdziwe, a "brak zaznaczonych odpowiedzi"
    // byłoby kłamstwem.
    return oczekujaceSprawdzenia.some(z => z.maZaznaczenie());
}

// Potwierdzenie kliknięcia (issues/sprawdz-wszystkie-pola-i-komunikat.md, punkt
// 2): dziś klik nie dawał żadnej informacji zwrotnej — przy pustym arkuszu
// wyglądało jak zepsuty przycisk. Osobny timer na stopkę i panel, bo to dwa
// niezależne elementy DOM (klik w jeden nie gasi komunikatu przy drugim).
let sprawdzStatusStopkaTimer = null;
let sprawdzStatusSidebarTimer = null;

// Wspólna mechanika pokazania/zgaszenia jednego komunikatu: wypełnia treść,
// koloruje przez klasę (token --correct / --text-faint w CSS, nie inline
// kolor), i planuje zniknięcie po ~2,5s. Kolejny klik czyści poprzedni timer,
// więc licznik zniknięcia się resetuje zamiast się nakładać.
function pokazStatusSprawdzania(el, poprzedniTimer, sukces, tekst, ariaLabel) {
    if (!el) return poprzedniTimer;
    if (poprzedniTimer) clearTimeout(poprzedniTimer);
    el.textContent = tekst;
    if (ariaLabel !== undefined) el.setAttribute("aria-label", ariaLabel);
    el.classList.toggle("przygaszony", !sukces);
    el.classList.add("widoczny");
    return setTimeout(() => el.classList.remove("widoczny"), 2500);
}

const sprawdzStatusStopka = document.getElementById("sprawdz-wszystkie-status-stopka");
const sprawdzStatusSidebar = document.getElementById("sprawdz-wszystkie-status-sidebar");

["sprawdz-wszystkie", "sprawdz-wszystkie-stopka"].forEach(id => {
    const btn = document.getElementById(id);
    if (!btn) return;
    btn.addEventListener("click", () => {
        const sukces = sprawdzWszystkieOdpowiedzi();
        if (id === "sprawdz-wszystkie-stopka") {
            sprawdzStatusStopkaTimer = pokazStatusSprawdzania(
                sprawdzStatusStopka, sprawdzStatusStopkaTimer, sukces,
                sukces ? "sprawdzono ✓" : "brak zaznaczonych odpowiedzi"
            );
        } else {
            // Panel boczny: 260px nie mieści zdania obok etykiety (patrz
            // style/sheet.css), więc widoczny jest tylko glif "✓" — prawdziwy
            // tekst dla czytnika ekranu idzie do aria-label.
            sprawdzStatusSidebarTimer = pokazStatusSprawdzania(
                sprawdzStatusSidebar, sprawdzStatusSidebarTimer, sukces, "✓",
                sukces ? "sprawdzono" : "brak zaznaczonych odpowiedzi"
            );
        }
    });
});

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
    const tytulEl = document.getElementById("sheet-title-heading");
    if (tytulEl && meta.sheetTitle) tytulEl.textContent = meta.sheetTitle;
    // Nagłówek panelu bocznego — ten sam tekst co <h1> nad pierwszym zadaniem.
    const sidebarTytul = document.getElementById("sidebar-tytul");
    if (sidebarTytul && meta.sheetTitle) sidebarTytul.textContent = meta.sheetTitle;
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
    try {
        loadExercises();
        zastosujDomyslnyWidokPunktowMobile();
    } catch (blad) {
        // loadExercises jest już odporne na błędy pojedynczych zadań, ale gdyby
        // padło wcześniej (np. brak #exercises-wrapper), nie zostawiamy pustej
        // strony — pokazujemy komunikat i sygnalizujemy błąd na belce diagnostycznej.
        console.error("Błąd renderowania arkusza", blad);
        pokazKomunikat(
            "<b>Nie udało się wyświetlić zadań.</b><br>" +
            "Odśwież stronę; jeśli błąd wraca, przekaż autorowi treść komunikatu z czerwonego paska na dole. " +
            `<small>(${blad && blad.message ? blad.message : blad})</small>`);
        if (window.__pokazBladStrony) window.__pokazBladStrony(blad, "loadExercises");
        return;
    }
    // Jeśli czas egzaminu minął, gdy karta była zamknięta — zakończ od razu
    // (tickExam ma warunek na wczytane zadania, teraz już spełniony).
    if (readExamState()) tickExam();
    // Faza „oceń się" po egzaminie (nie w trakcie egzaminu): odtwórz pływające
    // wskaźniki nieocenionych zadań otwartych, żeby przetrwały odświeżenie strony.
    else if (czyFazaOceniania()) pokazWskaznikiOtwarte();
}
startSheet();

// „Pokaż/schowaj wszystkie rozwiązania": AKCJA w panelu bocznym (nie ustawienie
// — nie ma wartości ani kropek, zmienia się sam czasownik). Otwiera lub zamyka
// panel rozwiązania każdego zadania klikając jego własny przycisk (ta sama
// ścieżka co ręczne klikanie — kroki, filmy itd. działają normalnie).
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
    // ustawEtykiete, nie textContent całego przycisku — inaczej zapis skasowałby
    // ikonę SVG (patrz komentarz przy ustawEtykiete w app/state.js).
    ustawEtykiete(showAllButton, wszystkieOtwarte
        ? "Schowaj wszystkie rozwiązania"
        : "Pokaż wszystkie rozwiązania");
});
