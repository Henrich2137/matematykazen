// app/state.js — globalne zmienne i najbardziej podstawowe helpery (mediaPath,
// renderMath) oraz współdzielone rejestry. Ładowany PIERWSZY z bloku app/*,
// bo pozostałe pliki (i tak w globalnym scope) korzystają z tych symboli.
// Ładowany PO plikach z widgets/ (render.js używa rejestru WIDZETY).

let totalScore = 0;

// Dane zadań — wypełniane z exercises.json w startSheet() (app/bootstrap.js),
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

// Zebrane przy renderowaniu odnośniki do przycisków/paneli "Rozwiązanie"
// wszystkich zadań — używa ich przycisk "pokaż wszystkie rozwiązania" w pasku.
const wszystkieRozwiazania = [];

// Rejestr zadań otwartych (selfScore) zbierany przy renderowaniu — używają go
// pływające wskaźniki nieocenionych zadań po egzaminie. Każdy wpis:
// { el: element zadania w DOM, stan: obiekt postępu (stan.open / stan.self), numer }.
const zadaniaOtwarte = [];
