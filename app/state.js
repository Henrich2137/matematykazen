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
// tytułów (nagłówek arkusza + nagłówek panelu). BEZ domyślnego fallbacku —
// brak/pusty/nieznany ?arkusz=
// kończy się komunikatem "błędny link" (startSheet()), nie cichym arkuszem.
const SHEET_ID = new URLSearchParams(location.search).get("arkusz");
// tablica-wzorow.pdf leży w rootcie obok template.html (jedynego
// pliku renderującego arkusze), więc ścieżka jest zawsze ta sama.
const TABLICE_PDF = "tablica-wzorow.pdf";

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

// Czy jesteśmy na wąskim ekranie (telefon)? Próg 720px pokrywa się z głównym
// breakpointem „telefonu" w style/responsive.css (karta na całą szerokość,
// panele PDF 94%). Czytane na bieżąco (nie raz przy starcie), żeby obrót
// ekranu / zmiana rozmiaru okna były uwzględniane. Używane m.in. do:
//  • domyślnego ukrycia badge'y punktów na telefonie (app/bootstrap.js),
//  • otwierania PDF-ów tablicy/zasad w nowej karcie zamiast w panelu <object>,
//    którego Android i tak nie renderuje (app/panels.js).
function czyTelefon() {
    try { return window.matchMedia("(max-width: 720px)").matches; } catch (e) { return false; }
}

/* ===== POZYCJE PANELU BOCZNEGO (#sidebar) — pisanie etykiet i wartości =====
   Każdy wiersz panelu ma w środku ikonę SVG, <span class="etykieta">, a wiersze
   typu „ustawienie" dodatkowo <span class="wartosc"> i kropki stanu. Dlatego
   ŻADEN plik app/*.js nie może już pisać do `textContent` całego przycisku —
   pierwszy taki zapis skasowałby ikonę razem z resztą. Zamiast tego:
     • ustawEtykiete(btn, tekst)   — dla AKCJI, które zmieniają czasownik
                                     („Otwórz…" ↔ „Schowaj…"),
     • ustawWartosc(btn, wartosc)  — dla USTAWIEŃ: przestawia data-stan (jedyne
                                     źródło prawdy o pozycji w cyklu), tekst
                                     wartości, kropki i podgląd next-state.

   Cykl stanów jest opisany DEKLARATYWNIE w atrybutach przycisku w template.html:
     data-stany   — pełna lista etykiet, od lewej do prawej. Konwencja: skrajnie
                    LEWO = wyłączone, skrajnie PRAWO = „wszystko" (kropki czytają
                    się jak skala: ●○○ = wył., ○○● = pełnia).
     data-kierunek — "lewo" (domyślnie: klik UJMUJE o stopień, bo domyślny stan
                    siedzi na prawym końcu) albo "prawo" dla Motywu, który nie
                    jest skalą „więcej/mniej" i zostaje przy kolejności z kodu.
   Dzięki temu kropki, podgląd po najechaniu i sam cykl nie mogą się rozjechać —
   wszystkie trzy czytają tę samą listę. */
function ustawEtykiete(btn, tekst) {
    if (!btn) return;
    const el = btn.querySelector(".etykieta");
    if (el) el.textContent = tekst;
    else btn.textContent = tekst; // panel jeszcze bez ikon (albo inny kontener)
}

function stanyPrzycisku(btn) {
    return (btn.dataset.stany || "").split(",").filter(s => s !== "");
}

// Stan, na który przeskoczy NAJBLIŻSZY klik — używany i przez sam cykl,
// i przez podgląd „auto → jasny" po najechaniu myszą.
function nastepnyStan(btn) {
    if (!btn) return null;
    const stany = stanyPrzycisku(btn);
    if (!stany.length) return null;
    const i = stany.indexOf(btn.dataset.stan || "");
    if (i < 0) return stany[stany.length - 1]; // nieznany stan → wracamy na pełnię
    const krok = btn.dataset.kierunek === "prawo" ? 1 : -1;
    return stany[(i + krok + stany.length) % stany.length];
}

function ustawWartosc(btn, wartosc) {
    if (!btn) return;
    btn.dataset.stan = wartosc;
    const w = btn.querySelector(".wartosc");
    if (w) w.textContent = wartosc;
    const podglad = btn.querySelector(".wartosc-podglad");
    if (podglad) {
        const nast = nastepnyStan(btn);
        podglad.textContent = nast ? `${wartosc} → ${nast}` : wartosc;
    }
    // Kropki stanu: generowane z data-stany, nigdy nie wpisywane ręcznie w HTML.
    // Na telefonie to ONE rozwiązują cykl — bez nich tapnięcie jest klikaniem
    // w ciemno (podgląd po najechaniu tam się nie stosuje).
    const kropki = btn.querySelector(".kropki");
    if (!kropki) return;
    const stany = stanyPrzycisku(btn);
    const aktywny = stany.indexOf(wartosc);
    kropki.textContent = "";
    stany.forEach((_, i) => {
        const k = document.createElement("span");
        k.className = i === aktywny ? "kropka kropka-aktywna" : "kropka";
        kropki.appendChild(k);
    });
}

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

// TRYB „natychmiastowa poprawność" (ustawienie GLOBALNE, wspólne dla wszystkich
// arkuszy — jak motyw czy tryb wskaźników, dlatego klucz BEZ sufiksu SHEET_ID).
// Dotyczy tylko zadań ZAMKNIĘTYCH z wyborem z przycisków (ABCD/PF/multiSelect):
//   ON  (domyślnie) — klik odpowiedzi od razu koloruje ramkę correct/incorrect.
//   OFF — klik tylko zaznacza (neutralnie); ocena odsłania się dopiero po
//         kliknięciu osobnego przycisku „sprawdź" przy zadaniu (albo „sprawdź
//         wszystkie odpowiedzi"). fillIn ma własny przycisk „Sprawdź" i tu go
//         nie ruszamy.
const KLUCZ_NATYCHM_POPRAWNOSC = "matematykazen-natychmiastowa-poprawnosc";
function czyNatychmiastowaPoprawnosc() {
    // Brak wpisu = domyślnie ON; tylko jawne "0" wyłącza tryb natychmiastowy.
    try { return localStorage.getItem(KLUCZ_NATYCHM_POPRAWNOSC) !== "0"; } catch (e) { return true; }
}
// Czy oceniać od razu przy kliknięciu odpowiedzi. W trybie egzaminu ZAWSZE od
// razu (ocena i tak liczy się „pod spodem", a kolory/punkty są schowane przez
// exam.css) — deferowanie „sprawdź" na egzaminie nie ma sensu i by przeszkadzało.
function natychmiastowaOcenaAktywna() {
    return czyNatychmiastowaPoprawnosc() || document.body.classList.contains("tryb-egzaminu");
}

// Widoczność zegara próbnego egzaminu (ustawienie GLOBALNE, jak wyżej — bez
// sufiksu SHEET_ID). Toggle steruje TYLKO widocznością #egzamin-timer — sam
// zegar dalej tyka i kończy egzamin po czasie w tle (patrz app/exam.js).
const KLUCZ_ZEGAR_WIDOCZNY = "matematykazen-zegar-widoczny";
function czyZegarWidoczny() {
    // Brak wpisu = domyślnie widoczny; tylko jawne "0" wyłącza.
    try { return localStorage.getItem(KLUCZ_ZEGAR_WIDOCZNY) !== "0"; } catch (e) { return true; }
}

// Rejestr zadań zamkniętych do zbiorczego „sprawdź wszystkie odpowiedzi". Każdy
// wpis: { ocen, maZaznaczenie, czySprawdzone } — patrz app/render.js (typy
// ABCD/PF/multiSelect). Przycisk w menu ⋯ i w stopce (app/bootstrap.js)
// odsłania ocenę wszystkich zadań, które mają zaznaczoną, a jeszcze nieodsłoniętą
// odpowiedź.
const oczekujaceSprawdzenia = [];
