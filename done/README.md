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

ODNOŚNIKI DO COMMITÓW (zasada od 2026-08-16):
- DOMYŚLNIE NIE WPISUJ HASZA. Wpis prawie zawsze jedzie w tym samym commicie co praca,
  którą opisuje (zasada „jedna paczka = jeden commit"), więc hasz jest do odzyskania
  bez zapisywania go, jednym poleceniem:
  `git log -S'<kawałek nagłówka wpisu>' -- done/ | tail -3`
  Ostatni commit z wyniku to ten, który wpis wprowadził. Sprawdzone na wpisie
  „DO ZROBIENIA HOŚCIE" z 2026-08-14: wychodzi 14b0715.
- Hasz (7 znaków, w nawiasie tuż za datą) dopisuj TYLKO tam, gdzie niesie informację,
  której z samego wpisu odtworzyć się nie da:
  - praca weszła kilkoma commitami, wtedy zakres, np. `469b81f..87849b8`,
  - kod wszedł wcześniej niż wpis (inna sesja, inna maszyna, poprawka z hosta),
  - wpis powołuje się na CUDZĄ zmianę, np. „psuło się od 87f065e".
- Nie rób osobnego commita „uzupełnienie hasza". Kosztuje commit, a nie daje nic ponad
  przepis wyżej.

CO TU NIE POWINNO TRAFIAĆ (zasada od 2026-08-16):
- Ten katalog to opis TEGO, CO ZROBIONO. Ostrzeżenie na przyszłość („uwaga, ten test
  potrafi skłamać", „ta funkcja ma pułapkę") zapisane wyłącznie tutaj jest martwe,
  bo modele nie czytają done/ na starcie. Takie rzeczy idą do issues/ albo do nagłówka
  pliku, którego dotyczą (np. tools/zrzuty.js ma sekcję PUŁAPKI, a CLAUDE.md kieruje
  do niej wprost). W done/ zostaje wtedy sam opis wpadki, nie ostrzeżenie.

NIE wczytuj tych plików domyślnie — tylko gdy potrzebne jest szersze spojrzenie na projekt,
rozwiązanie trudniejszego problemu albo sprawdzenie, czy/jak coś już kiedyś rozwiązano.
Do szukania używaj najpierw tego indeksu (tagi niżej), potem grepa po konkretnym pliku.


== 04-biezace.md — partia OTWARTA (2026-07-27 → ?) ==
- 2026-08-22 (Opus 5, medium) — repo przygotowane pod hosting Cloudflare: wrangler.jsonc, .assetsignore,
  _headers, 404.html i test tools/sprawdz-cloudflare.py; pierwsze wdrożenie padło na wysyłanym katalogu .git
  [cloudflare, hosting, wrangler, wdrozenie]
- 2026-08-23 (Opus 5, medium) — porządki w dokumentacji: issues/krok-po-kroku-produkcja.md rozdzielony
  między manimations/README.md (produkcja filmu) i nowy issues/rozwiazanie-krok-po-kroku-odtwarzacz.md
  (odtwarzacz na stronie); issues/lekcje-z-sesji.md → sekcja „Przypuszczenie to nie ustalenie" w CLAUDE.md;
  issues/fable-brief-2026-maj.md rozebrany na playwright-podglad.md i dwie poprawki w ARCHITECTURE.md.
  Trzy pliki skasowane, odnośniki przepięte
  [dokumentacja, issues, porzadki, krok-po-kroku, playwright, manim]
- 2026-08-23 (Opus 5, medium) — zasady opisu kroków (wzór plus wyjaśnienie, bez przepisywania rachunku)
  i układu dwukolumnowego rozwiązania zwykłego spisane na zad. 2 z 2024-grudnia; nowa zasada ruchu:
  nie przewozi się znaku między miejscami, które nic ze sobą nie mają
  [zasady, opisy-krokow, solutionText, rozw-2kol, zad2, 2024-grudzien]
- 2026-08-13 (Henrich — testy) — odbiór v22/v23/v26/v28 odtwarzacza: sterowanie ◄ ► potwierdzone
  w komplecie, sekcje testowe skasowane z TODO.md; niedziałające pulsowanie i prefetch plus trzy nowe
  zamówienia (waity w filmach, większe ◄ ►, crash przy spamowaniu next-step) wróciły do DO ZROBIENIA
  [krok-po-kroku, wideo, ui, testy, odbior]
- 2026-08-12 (Henrich — testy) — odbiór v21 odtwarzacza krok po kroku: cała sekcja TESTOWANIE HENRICH
  przeklikana i potwierdzona (►/◄, start-pauza w cofce, kropki, ROW 2, prędkości, brak 404); pięć uwag
  z testów to nie błędy, tylko nowe zamówienie — wróciły do TODO.md jako „PO TESTACH v21"
  [krok-po-kroku, wideo, ui, testy, odbior]
- 2026-08-10 (Sonnet 5, high) — v15, paczka drobiazgów UI z docs/superpowers/specs/2026-08-09-paczka-ui-drobiazgi-design.md
  + 2 dodatkowe punkty z tej samej sekcji TODO.md: (1) usunięty hoverowy podgląd „wartość → następna"
  w panelu ustawień, wartość widoczna cały czas (kod archiwalny w issues/archiwum-hover-podglad.md);
  (2) kontrolki odpowiedzi (fillIn/P-F/ostateczna odpowiedź) na telefonie: pivot z poziomego na pionowy
  przez flex-wrap + flex-basis:100% na etykiecie (bez zmiany flex-direction, żeby dwa przyciski P/F
  zostały obok siebie), kontrolka pod spodem z małym marginesem z lewej zamiast wyśrodkowania —
  naprawia zad. 10/11 (issues/dark-mode-obrazki-wideo.md zamknięte przy okazji punktu 3); (3) dark mode:
  `--filtr-grafik-zadan: invert(92%)` (wyliczone z jasności --bg #141414 ≈ 7,8%, sprawdzone pixel-perfect
  w Playwright — biel PNG po odwróceniu ląduje dokładnie na rgb(20,20,20)) na `.question img` i na
  img/video w `.solution-step-by-step-container`; (4) „Sprawdź wszystkie odpowiedzi" przeniesiony jako
  podpunkt (`.sidebar-sub`, klasa uogólniona z `.sidebar-ustawienie.sidebar-sub`) pod „Poprawność”,
  wzorem Zegara/Wskaźników pod egzaminem; (5) pigułki kategorii w formularzu zgłoszenia błędu na
  telefonie: `flex: 1 1 calc(50% - 4px)` zamiast pełnej szerokości — dwie w rzędzie, opis błędu bliżej
  góry ekranu. Zweryfikowane w Playwright (tools/zrzuty.js + ręczne zrzuty per-zadanie) na desktopie,
  telefonie (390px) i szerokości pośredniej (700px), w obu motywach — zero błędów JS
  [css, ui, dark-mode, mobile, sidebar, formularz]
- 2026-08-09 (Opus 5) — devcontainer nie wstawał (`Permission denied` na `/vscode/vscode-server/bin`):
  wolumen `vscode` tworzony przez rozszerzenie miał uid sprzed `--userns=keep-id`, po `podman prune`
  podpiął się pod niego świeży kontener; naprawa = `podman rm` kontenera + `podman volume rm vscode`
  + rebuild; wykluczone obraz i SELinux; spis wolumenów, których nie wolno prune'ować
  [devcontainer, podman, keep-id, wolumeny, srodowisko]
- 2026-08-07 (Opus 5 Medium) — narzędzia, bez zmian w kodzie strony: auto-fetch + auto-pull przy starcie
  VS Code natywnymi mechanizmami (`.vscode/tasks.json` runOn folderOpen + `git.autofetch`), świadomie
  zamiast gitdoc.pullOnOpen; plugin superpowers 6.2.0 faktycznie zainstalowany w scope project
  (deklaracja w .claude/settings.json była poprawna, brakowało instalacji)
  [narzedzia, git, vscode, claude-code, pluginy, skille]
- 2026-08-02 (Opus 5 Medium) — licencja PolyForm Noncommercial 1.0.0 + CLA: zweryfikowany LICENSE.md,
  nowe CONTRIBUTING.md / README.md / .github/PULL_REQUEST_TEMPLATE.md, właściciel jako pseudonim
  `Henrich2137`, URL Required Notice na GitHub Pages zamiast nieistniejącej domeny; odkłamana faza
  projektu w OVERVIEW.md  [licencja, cla, dokumentacja, github]
- 2026-07-28 (Sonnet High) — `formulasPage` zweryfikowane dla całego arkusza 2024-grudzień (35 zadań)
  na podstawie transkryptu tablica-wzorow-transkrypt/: uzupełnione 6 brakujących (zad. 7, 8, 10,
  11, 12, 17 — z czego 7/8/10/12 świadomie zostają bez strony, bo nie wymagają tablic) oraz
  poprawionych 8 błędnych/zdezaktualizowanych (zad. 9→8; zad. 12.1-12.3→8 zamiast 7 —
  wierzchołek/postać kanoniczna są na str. 8, nie na str. 7 z wyróżnikiem; zad. 16→9; zad. 19→17 —
  podobieństwo trójkątów, nie Pitagoras; zad. 24→11 — to zadanie liczy wysokość z tangensa, nie
  objętość ostrosłupa; zad. 30→8; zad. 5 zostaje 10, potwierdzone). Metoda ustalona po korektach
  Henricha: strona formulasPage musi odpowiadać wzorowi FAKTYCZNIE użytemu w solutionText/hint, nie
  samemu tematowi zadania — patrz notatka w tablica-wzorow-transkrypt/README.md. Przy okazji,
  na prośbę Henricha odczytany fragment prawdziwego PDF-a (s. 7-11): dopisany do transkryptu
  brakujący wzór [8.10] „Procent składany" `Kₙ=K₀·(1+p/100)ⁿ` (s. 10, dół), którego wcześniej w
  ogóle nie było w 08-ciagi.md — stąd wcześniejsze niezgodności przy zad. 5/16 (Wybrane granice
  przenumerowane [8.10]→[8.11])  [tresc, formulasPage, weryfikacja, transkrypt]
- 2026-07-27 (Sonnet High) — „sprawdź wszystkie odpowiedzi": fillIn i finalAnswer dopisane do rejestru
  oczekujaceSprawdzenia (ocena wydzielona do ocenFillIn(), bez duplikacji logiki), bonus — finalAnswer
  auto-sprawdzany po zakończeniu egzaminu, komunikat „sprawdzono ✓"/„brak zaznaczonych odpowiedzi" obok
  obu kopii przycisku (aria-live, tokeny --correct/--text-faint, mobile fallback) — v0.08. Poprawka tego
  samego dnia po live-teście Henricha: mobilny fallback komunikatu w stopce wciągał go do flow i dokładał
  fantomowe ~6px pod przyciskiem nawet gdy pusty — naprawione, zostaje position: absolute
  [silnik, ui, egzamin, a11y, css]
- 2026-07-27 (Opus High) — trzy drobnice po przeglądzie sesji 1 przez Henricha (v0.07): cień zdjęty
  z #sidebara (panele PDF i toast zostają), ciemniejszy tekst „sprawdź wszystkie" w stopce,
  .sheet-title-heading zwężony do 32% z zawijaniem (pełna szerokość na telefonie)
  [css, ui, sidebar, stopka, tytul]

== 03-2026-07-27.md — partia ZAMKNIĘTA (2026-07-13 → 2026-07-27, niezmergowana do mastera) ==
- 2026-07-27 (Opus High) — SPÓJNOŚĆ UI, sesja 1: warstwa tokenów kształtu w base.css (--radius-kontrolka,
  --border-kontrolka, --shadow-panel, --segment-bg) + 6 punktów Henricha (jedna rodzina przycisków stopki,
  lżejszy aktywny segment przełącznika, panele PDF w stylu sidebara, #sidebar-linia zamiast border-right,
  docisk strzałki panelu, landing na tokenach); wsad dla sesji 2 w issues/ui-spojnosc-etap2.md
  [css, ui, tokeny, sidebar, pdf-panele, landing, motyw]
- 2026-07-27 (Opus High) — SESJA 2, redesign chrome: #top-bar zlikwidowany (pływające logo + pigułki
  w narożnikach), przełącznik trybu ćwiczenia/egzamin pod tytułem arkusza, panel boczny #sidebar zamiast
  okienka „⋯” (13 pozycji bez zmiany ID, akcje vs ustawienia, cykl na data-stan + kropki stanu, ikony SVG,
  próg 1300px); naprawiony poziomy scroll 360px (winna była .data-table w zad. 33, nie pasek)
  [css, ui, pasek, sidebar, egzamin, a11y, ikony, responsywnosc, refaktor]
- 2026-07-26 (Opus) — limity długości opisu zgłoszenia: MIN 3 / MAX 2000 znaków liczone po trim(),
  egzekwowane dwukrotnie (maxlength w HTML + bladOpisu() w JS, bo maxlength omija się programowo),
  licznik „n / 2000" czerwieniejący powyżej 90%; komunikat błędu aktualizuje się na bieżąco przy pisaniu.
  Uwaga: gitdoc wypchnął na produkcję wersję przerwaną w połowie („zgLicznik is not defined")
  [formularz, walidacja, antyspam, ux, produkcja]
- 2026-07-26 (Opus) — BUGFIX: odpowiedzUcznia/odpowiedzPoprawna wysyłały zlepek „A. 545^{4}54", bo KaTeX
  renderuje wzór w dwóch warstwach, a .textContent skleja obie. Nowa funkcja tekstOdpowiedzi() czyta
  surowy LaTeX z <annotation>, pracując na klonie węzła. Wykryte na prawdziwym zgłoszeniu z produkcji
  [formularz, katex, bugfix, produkcja]
- 2026-07-26 (Opus High) — przebudowa formularza „zgłoś błąd": opis OBOWIĄZKOWY (disabled + komunikat
  role="alert" + focus), modal → BLOK INLINE w karcie zadania nad [Podpowiedź][Rozwiązanie] (jeden węzeł
  przenoszony przez insertBefore, więc zero refaktoru ID), 8 pigułek kategorii z wyborem wielokrotnym
  (idą też do _subject), nowe dane auto z DOM karty (odpowiedź ucznia/poprawna, krok rozwiązania, ekran);
  świadomie BEZ SDK @formspree/ajax z CDN (offline-first). 40/40 testów Playwright
  [formularz, formspree, ui, walidacja, mobile, a11y]
- 2026-07-26 (Sonnet Medium) — sesja 1 „Dla Sonneta": ciemniejsze tło dark mode (--bg #141414); kropki
  „oceń się" ukryte pod 480px; „sprawdź wszystkie odpowiedzi" w egzaminie wyszarzone zamiast display:none;
  przycisk „Sprawdź" przy odpowiedzi ostatecznej ukryty w egzaminie; tytuł arkusza z paska do
  #sheet-title-heading nad pierwszym zadaniem  [css, motyw, mobile, egzamin, ui]
- 2026-07-26 (Sonnet) — wklejony prawdziwy endpoint Formspree (xvzedgjg) zamiast placeholdera
  [formspree, formularz]
- 2026-07-24 (Opus) — przepisanie sekcji „Exam mode" w ARCHITECTURE.md (8 zatytułowanych podsekcji, poziom
  jak dark mode; dopisane ?test-egzamin=1, final-answer w egzaminie, setExamMenuDisabled) + uzupełnienie
  listy „stabilnych ID" paska/menu w ARCHITECTURE_CSS.md  [dokumentacja, egzamin]
- 2026-07-24 (Opus) — formularz samooceny zadań otwartych (prototyp zad. 8/9): pole „ostateczna odpowiedź"
  (exercise.finalAnswer, auto-sprawdzane jak fillIn, widoczne w egzaminie), pomocnicza checklista kryteriów
  CKE (exercise.gradingCriteria, nie sumuje punktów), ogólne zastrzeżenie w stopce  [zadania-otwarte,
  samoocena, silnik, schemat]
- 2026-07-24 (Opus) — trzy usprawnienia „na telefonie": domyślnie ukryte badge'e punktów (czyTelefon,
  score-view „tylko suma"); PDF-y tablicy/zasad/„potrzebne wzory" w nowej karcie zamiast panelu <object>
  (window.open); ukryty tryb testowy egzaminu ?test-egzamin=1 → 1 min  [mobile, ui, egzamin, pdf-panele]
- 2026-07-24 (Opus) — arkusz nie wczytuje się na telefonie (Pixel 7a/GrapheneOS): nie do odtworzenia
  w emulacji, więc globalna belka diagnostyczna (window.onerror/rejection, template.html) + utwardzenie
  loadExercises (per-zadanie try/catch, placeholder .blad-zadania, guardy widżet/KaTeX) — siatka
  bezpieczeństwa zamiast pustej strony  [mobile, diagnostyka, render, odpornosc, bugfix]
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

== 00-stary-done.md — archiwum (2026-07-04 → 2026-07-13) ==
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
