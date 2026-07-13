Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do DONE.md — patrz CLAUDE.md.)
(Zasada: Drogi LLM, Sonnecie, Opusie, Jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole)
Zadania realizuj od góry do dołu.

<br>

NASTAŁA ERA NOWEGO MASTERA BUHAHAHAHAHA

<h3>DO REALIZACJI</h3>
Jeżeli nie masz co robić to rób stąd.

WYSOKI PRIORYTET:
- nic

NISKI PRIORYTET:
- Przyciski "oceń się" (.self-score-container button, style.css ~493-516) są wyraźnie
  mniejsze od przycisków odpowiedzi (.button-container button: min-width 22%,
  padding 10px 12px, font-size 18px vs obecne min-width 56px, padding 6px 10px,
  font-size 15px). Powiększyć je UMIARKOWANIE (nie 1:1 z przyciskami odpowiedzi) —
  np. padding ~8px 11px, font-size ~16-17px — zachowując zwarty, poziomy rząd
  przycisków punktowych 0/1/2/... (to nie mają być pełnowymiarowe przyciski
  odpowiedzi, tylko przestać wyglądać "miniaturowo" obok nich).
- Panele PDF (#tablica-wzorow-panel, #zasady-oceniania-panel; drag/resize logika w
  script.js, funkcja makePanelDraggable ~linia 237) — jedyne ograniczenie do dodania:
  uchwyt przeciągania (.panel-uchwyt, górny pasek panelu) nie może zjechać POD
  top-bar — czyli panel.style.top nie powinien pozwolić, by cały pasek uchwytu
  schował się za top-barem (inaczej użytkownik traci możliwość złapania panelu i
  przesunięcia go z powrotem). To jedyny twardy limit. WSZYSTKIE pozostałe
  krawędzie (lewo, prawo, dół) mają zostać całkowicie swobodne — łącznie z
  obecnym Math.max(0, ...) na `left`, który należy USUNĄĆ (panel może wyjechać
  poza lewy/prawy/dolny brzeg ekranu bez ograniczeń). Dotyczy to przeciągania;
  zmiana rozmiaru (.panel-rozmiar, narożnik) zostaje bez zmian.
- Błędny LUB pusty/brakujący ?arkusz= (nieznane id — fetch matura/<id>/exercises.json
  zwraca błąd/404 — ORAZ całkowity brak parametru, ORAZ `?arkusz=` pusty string) ma
  skutkować komunikatem "błędny link, wróć do strony głównej" z hiperłączem do
  index.html — NIE cichym fallbackiem. To wymaga usunięcia obecnego domyślnego
  fallbacku `|| "2024-grudzien"` w script.js:16 (SHEET_ID). Sprawdzone: linki z
  index.html zawsze przekazują poprawny ?arkusz=, więc usunięcie fallbacku nic tam
  nie psuje.
- Dodać mały, szarawy podtytuł pod nazwą arkusza w top-barze (#exercises-sheet-title,
  #bar-center w template.html) pokazujący aktualny tryb: "tryb ćwiczenia" domyślnie,
  przełącza się dynamicznie na "tryb egzaminu" gdy aktywne jest body.tryb-egzaminu
  (czyli po enableExamMode() i z powrotem po finishExam()) — ma być stałym, zawsze
  widocznym elementem UI (nie tylko ostrzeżeniem pokazywanym wyłącznie w trybie
  egzaminu).
- Dodać KRÓTKIE okno potwierdzenia (confirm()) przed akcją "resetuj punktację"
  (#reset-scores w menu ⋯, script.js) — jedno zdanie ostrzeżenia w stylu: "Wyczyścić
  zapisane odpowiedzi i punkty? Tej operacji nie można cofnąć." (BEZ szczegółowego
  wypunktowania jak w oknie startu egzaminu — to ma być krótkie, jednozdaniowe
  ostrzeżenie).

<br>


NAJNIŻSZY PRIORYTET, NA POTEM:

- na bieżąco obliczany procent obok sumy punktów, który świeci się na zielono gdy jest conajmniej 30%, po najechaniu myszką pokazuje się, zdałeś/nie zdałeś (jeszcze)

- utworzenie zmiennych css i zrobienie przełącznika na darkmode

- dodanie rozwiązań do matury 2026

- wyciągnięcie tekstu z PDF-ów:
  * matematyka-2025-maj-matura-podstawowa.pdf
  * matematyka-2025-maj-matura-podstawowa-odpowiedzi.pdf

- DOTYCZĄCE TRYBU PRÓBNY EGZAMIN
   * Przycisk pokaż potrzebne wzory nie powinien się pokazywać, zrób też tak, aby nie było tam przerwy zadużej można wyłączyć div który jest gdzieś wyżej w hierarchi czy coś
   * przycisk opcji "..." po kliknięciu pokazuje pustą ramkę, dobrze aby albo nie było go w ogóle albo był szary lub po rozwinięciu pokazywał zaszarzone te przyciski które nie powinny działać podczas egzaminu.
   * Zadania otwarte np. 30 powinny mieć pole do zanotowania odpowiedzi do samodzielnego sprawdzenia potem.

- do sekcji "oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu jak to skomponować aby miało sens.





<br>

DLA UŻYTKOWNIKA:
- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

- Punkt o widżecie zad 1 urwał się w połowie zdania: "opcjonalnie: sprawić aby przesuwanie" — dokończ myśl, to zostanie zrobione (reszta punktu o zad 1 jest już zrealizowana).

<br>

INNE NOTATKI:

- Obczaić analitykę czyli śledzenie ilości i zaangażowania użytkowników (moze da sięjakoś przez githuba)

- Stworzyć przycisk "zgłoś błąd w zadaniu" i odpowiedni formularz

- Tryb egzaminu nie powinien być tak "schowany" w opcjach. Przed rozpoczęciem arkusza powinno pytać użytkownika czy chce wejść w tryb ćwiczeniowy czy egzaminu z checkboxem o zapamiętanie wyboru.

- Etap sprawdzania odpowiedzi po trybie egzaminacyjnym. Idealnie powinien istnieć pomiędzy skończeniem egzaminu, a jego wyników pokazaniem wyników egzaminu.

- analogicznie do boxów z punktacją powinny być do włączenia boxy z opisem typu zadania

- na telefonie pdfy się nie ładują (tablica i zasady oceniania). Podczas naprawy warto sprawić aby odpalały się one nie w okienku ale wypełniały całą stronę z krzyżykiem w rogu. Jeżeli nie uda się tego naprawić to należy usunąć tę funkcjonalność z wersji mobilnej.

<br><br><br>


<h3>DO WERYFIKACJI PRZEZ HENRICHA</h3>
- Tryb egzaminacyjny (zrealizowany 2026-07-06): sprawdzić cały przebieg — start →
  parę odpowiedzi (ramki powinny być neutralne/niebieskie) → F5 (czy egzamin dalej
  trwa) → "zakończ egzamin" → podsumowanie → samoocena zadania otwartego.
  (Automatyczny smoke-test Playwright 2026-07-06 przeszedł cały ten przebieg bez
  błędów — patrz DONE.md; to tylko na wyczucie/UX zostaje do Ciebie.)


DO REALZACJI Dopisane przez SONNETA LUB OPUSA:

SONNET DOPISAŁ:
- Dokończenie arkusza 2026 (otwórz przez template.html?arkusz=2026-maj; dane w
  matura/2026-maj/exercises.json — teraz obiekt { meta, exercises }; odpowiedzi i
  punktacja zweryfikowane 2026-07-06 z kluczem CKE Wersja A + rachunkiem — NIE
  zmieniaj correctAnswerIndex/blanks/statements/maxScore):
  * hint + solutionText dla 41 wpisów — przepisz/zredaguj z gotowych rozwiązań w
    matura/2026-maj/matematyka-2026-maj-matura-podstawowa-odpowiedzi.txt (klucz
    zawiera pełne rozwiązania zadań otwartych; wzory w KaTeX, konwencje jak w 2024)
  * obrazki zad 12 (wykres łamanej), 13 (prosta z kątem α), 19 (okrąg A,B,C,D),
    20 (proste równoległe), 31 (diagramy IVA/IVB — dane TYLKO na obrazku) — wyciąć
    z matura/2026-maj/matematyka-2026-maj-matura-podstawowa.pdf wzorem zad30
    (pdftoppm -x/-y/-W/-H). Docelowe ścieżki (już w exercises.json, konwencja media/):
    matura/2026-maj/media/zadN/zadNrys.png. UWAGA: sesja zdalna nie ma
    pdftoppm/mutool/gs — tylko lokalnie.



