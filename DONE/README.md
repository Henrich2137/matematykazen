INDEKS ARCHIWUM ZROBIONYCH PUNKTÓW TODO.

Ukończone punkty NIE zostają w TODO.md — przenoszone są tutaj, do pliku bieżącej partii,
oznaczone [DONE]/[ZROBIONE] z datą i krótką notką jak zostały rozwiązane.

ZASADA PODZIAŁU (nie kalendarz!):
- Zawsze jest dokładnie JEDEN plik "bieżący" (`NN-biezace.md`) — do niego dopisujesz każdą
  ukończoną rzecz, na górze pliku (najnowsze pierwsze).
- Plik zamyka się w momencie MERGE gałęzi do mastera / domknięcia partii poprawek.
  Wtedy: zmiana nazwy `NN-biezace.md` → `NN-RRRR-MM-DD.md` (data domknięcia), założenie
  kolejnego `NN+1-biezace.md` i dopisanie linii w tym indeksie.
- Jeden plik ≈ jedna partia zmian, mniej więcej to co weszło do mastera jednym wejściem.
  Partia może trwać 3 dni albo 3 tygodnie — długość nie ma znaczenia.

NIE wczytuj tych plików domyślnie — tylko gdy potrzebne jest szersze spojrzenie na projekt,
rozwiązanie trudniejszego problemu albo sprawdzenie, czy/jak coś już kiedyś rozwiązano.
Do szukania używaj najpierw tego indeksu (tagi niżej), potem grepa po konkretnym pliku.


== 03-biezace.md — partia OTWARTA (2026-07-13 → 2026-07-24, niezmergowana do mastera) ==
- 2026-07-24 — „zgłoś błąd w zadaniu": link pod zadaniem + modal → Formspree (AJAX), toggle w
  menu, honeypot + throttling, toast; endpoint Formspree jako placeholder do uzupełnienia
  [ui, formularz, localStorage, antyspam, formspree]
- 2026-07-24 — toggle „widoczność zegara" w menu egzaminu (globalny, localStorage)
  [ui, egzamin, localStorage] — sprawdzone przez Henricha
- 2026-07-24 — „rozpocznij próbny egzamin" w menu ⋯ ukryty przed wczytaniem arkusza
  (nie pokazuje się już na stronie błędnego linku)  [ui, egzamin, css] — sprawdzone przez
  Henricha; dopisał do TODO.md drobny punkt (przycisk powinien być zablokowany, nie
  niewidoczny, na stronie błędu arkusza)
- 2026-07-24 — tablica wzorów zamyka się automatycznie po zakończeniu egzaminu
  [ui, egzamin] — sprawdzone przez Henricha
- 2026-07-24 — #toggle-tablica/#toggle-zasady przeniesione na stałe do menu ⋯ (zamiast
  paska), rozwiązuje też ogólny punkt "przyciski niemieszczące się na pasku do menu"
  [ui, css, pasek]
- 2026-07-24 — styl #natychmiastowa-toggle/#sprawdz-wszystkie w menu ⋯ dopasowany do
  reszty przycisków; przycisk „sprawdź" wyrównany (top: 8px) z górną krawędzią
  przycisków odpowiedzi  [ui, css]
- 2026-07-23 — toggle „natychmiastowa poprawność" + przyciski „sprawdź" / „sprawdź wszystkie"
  (zadania zamknięte, tryb „sprawdź później")  [ui, silnik, localStorage]
- 2026-07-23 — pozycja/warstwy wskaźników „oceń się": kolumna dalej od krawędzi, przycisk
  „Ukryj wskaźniki" w prawym dolnym rogu, z-index pod tablicą wzorów  [ui, css, egzamin]
- 2026-07-21 — poprawki żółtych bombli: numer zadania z treści, przycisk „ukryj"  [egzamin, ui, bugfix]
- 2026-07-21 — pływające żółte wskaźniki nieocenionych zadań otwartych  [egzamin, ui, localStorage]
- 2026-07-21 — zmienne CSS + dark mode (Etap 1: infrastruktura)  [css, motyw]
- 2026-07-21 — nudge #bar-center o 5px  [css, pasek]
- 2026-07-21 — tryb egzaminu: przyciski start/koniec w pasku i stopce  [egzamin, ui]
- 2026-07-17 — NISKI PRIORYTET: klamp paneli PDF do viewportu, wcięcie treści, wyrównanie
  badge'a, procent punktów w pasku, normalizacja fillIn (x/y/∈), 3 poprawki trybu egzaminu
  (light-buttony, menu disabled, textarea zadań otwartych)  [pdf-panele, css, fillIn, egzamin]
- 2026-07-13 — cały WYSOKI PRIORYTET: przyciski „oceń się", klamp paneli PDF, komunikat
  „Błędny link" przy złym ?arkusz=, podtytuł trybu w pasku, confirm przy resecie punktacji
  [css, pdf-panele, routing, egzamin]

== STARY_PRZENIESIONY_DONE.md — archiwum (2026-07-04 → 2026-07-13) ==
Stara, nieposegregowana zawartość dawnego DONE.md z rootu; granice partii/mergów w tej
historii są dziś nieodtwarzalne, więc zostaje jednym plikiem. Główne wątki:
- 2026-07-13 — usunięty duplikat „wyczyść zapisany postęp", „zakończ egzamin" przeniesiony
  na dół arkusza  [egzamin, ui]
- 2026-07-10 — MIGRACJA na wspólny template.html + ?arkusz=<id> + meta w exercises.json +
  mediaPath(); usunięte per-arkuszowe index.html  [migracja, routing, architektura]
- 2026-07-10 (Fable) — naprawa odnośników po reorganizacji na matura/<arkusz>/, prefiks
  media/ w ścieżkach  [migracja, media]
- 2026-07-06 (Fable) — arkusz 2026-maj: szkielet strony, weryfikacja odpowiedzi z kluczem
  CKE, formulasPage, normalizacja „6,50"  [2026-maj, tresc, fillIn]
- 2026-07-06 (Opus) — split inline <script> na script.js + solutionsInteractive.js,
  nazwy funkcji PL→EN  [refaktor, architektura]
- 2026-07-06 — migracja exercises.js → exercises.json, KaTeX w widżetach, TRYB EGZAMINU
  (170 min) — trzy duże zadania  [migracja, katex, widzety, egzamin]
- 2026-07-06 — KaTeX zvendorowany offline, menu ⋯, reset punktacji, anty-migotanie wideo
  [katex, ui, wideo]
- 2026-07-06 — sesja porządkowa: usunięte nieużywane PNG, opisy kroków zad 1, alt-y  [porzadki, a11y]
- 2026-07-05 — localStorage postępu, fillIn (zad 10/29), panel zasad oceniania, przeciąganie
  i resize paneli PDF, snap w widżetach, „pokaż wszystkie rozwiązania"  [localStorage, fillIn,
  pdf-panele, widzety]
- 2026-07-05 — zadania 21-30 podmienione na oryginały CKE, strona główna index.html  [tresc, landing]
- 2026-07-05 — weryfikacja całego arkusza 2024-grudzień z kluczem CKE (wszystkie 30 zgodne)
  [tresc, weryfikacja]
- 2026-07-05 — odchudzenie CLAUDE.md, powstanie ARCHITECTURE.md, zasada archiwum zrobionych
  [dokumentacja]
- 2026-07-04 — responsywność (breakpointy 1024/900/720/560), sugestie WYGLĄD/DESIGN,
  poprawki punktacji, correctAnswerIndex, 9 widżetów interaktywnych, nowe typy zadań
  (PF, multiSelect, selfScore)  [css, responsywnosc, widzety, silnik]
