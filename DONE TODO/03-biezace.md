BIEZACA PARTIA ZROBIONYCH PUNKTOW TODO (otwarta). Tu trafiaja wpisy [DONE]/[ZROBIONE]
przenoszone z TODO.md. Nie wczytuj tego pliku domyslnie - tylko gdy potrzebne jest szersze
spojrzenie na projekt, rozwiazanie trudniejszego problemu albo sprawdzenie, czy/jak cos juz
kiedys rozwiazano. Zasada podzialu i indeks: DONE/README.md.
Zakres: 2026-07-13 (WYSOKI PRIORYTET) - 2026-07-21. Partia jeszcze niezmergowana do mastera.

ZROBIONE PRZEZ OPUSA (2026-07-21) — poprawki żółtych bombli (zgłoszone przez Henricha) z TODO.md:
- [ZROBIONE] Złe liczby na kropkach (np. „24" dotyczyła zad 19). Przyczyna: numer
  brany z index+1, a indeksy w tablicy rozjeżdżają się z numeracją CKE przez zadania
  nadrzędne (maxScore:0) i wieloczęściowe (kilka wpisów „Zadanie 12/17"). Teraz numer
  parsowany z treści zadania (.question textContent, regex „Zadanie N"), z fallbackiem
  do index+1. Zweryfikowane: wypełnione zad otwarte idx 2/23/34 dają kropki 3/19/30
  (a nie 3/24/35); kropka „19" wskazuje #exercise-23, którego treść to „Zadanie 19".
- [ZROBIONE] Przycisk „ukryj": tekst zmieniony z „× ukryj" na „✕ Ukryj wskaźniki
  nieocenionych zadań", przeniesiony do lewego dolnego rogu (kropki są po prawej, więc
  się nie zasłaniają) i dostał żółtą ramkę (2px var(--wskaznik-border)) wiążącą go
  wizualnie z kropkami. Kolumnie kropek zdjęto rezerwę na przycisk u dołu prawej (mogą
  schodzić prawie do dołu). Zweryfikowane wizualnie w jasnym i ciemnym.
- PRZY OKAZJI naprawiony zastany bug: restore postępu ustawiał tylko openTextarea.value,
  a nie stan.open — po reloadzie kolejny zapis kasował zapisany tok rozwiązania zadania
  otwartego. Teraz restore ustawia też stan.open (zrobione już w commicie z wskaźnikami).

ZROBIONE PRZEZ OPUSA (2026-07-21) — pływające żółte wskaźniki nieocenionych zadań otwartych z TODO.md:
- [ZROBIONE] Po zakończeniu próbnego egzaminu (faza „oceń się") każde zadanie
  otwarte (selfScore) WYPEŁNIONE (jest wpisany tok rozwiązania w textarea), ale bez
  przyznanej samooceny, dostaje pływającą żółtą kropkę z numerem zadania po prawej
  krawędzi (klasa .wskaznik-otwarte, style w style.css; kolory przez nowe zmienne
  motywu --wskaznik-* — działają w jasnym i ciemnym). Klik kropki przewija do
  zadania (scrollIntoView center). W trakcie egzaminu kropek nie ma.
- [ZROBIONE] Pozycjonowanie zależne od scrolla (repozycjonujWskazniki w script.js):
  środek kropki = środek jej zadania w viewport, zaklamowany do pasa pod paskiem
  górnym … nad przyciskiem „ukryj"; kropki są rozsuwane (declutter przód/tył), więc
  gdy zadanie jest poza ekranem, kropka przykleja się do góry lub dołu w zwartej
  kolumnie. Nasłuch scroll/resize przez requestAnimationFrame.
- [ZROBIONE] Wspólny przycisk „× ukryj" (#wskazniki-ukryj, prawy dolny róg) chowa
  wszystkie kropki naraz i kończy fazę. Kropka pojedynczego zadania znika po jego
  ocenieniu (klik samooceny woła odswiezWskaznikiOtwarte()); gdy zniknie ostatnia,
  faza się kończy.
- Faza „oceń się" trzymana w localStorage (KLUCZ_OCENIANIA = matematykazen-ocenianie-
  <sheet>), więc kropki przetrwają odświeżenie strony aż do ocenienia wszystkich albo
  „ukryj". Nowy egzamin i „resetuj punktację" kasują tę fazę. Rejestr zadań otwartych
  (zadaniaOtwarte) zbierany przy renderowaniu; wskaźniki odtwarzane w startSheet po
  loadExercises (tylko gdy NIE trwa egzamin).
- PRZY OKAZJI naprawiony zastany bug: przy przywracaniu postępu ustawiane było tylko
  openTextarea.value, ale NIE stan.open (input nie odpala się przy .value). Przez to
  po reloadzie stan.open był pusty i kolejny zapis (np. klik samooceny) kasował
  zapisany tok rozwiązania zadania otwartego. Teraz restore ustawia też stan.open.
- Zweryfikowane Playwrightem: brak kropek w trakcie egzaminu; po zakończeniu kropki
  dla wypełnionych nieocenionych zadań (3, 8) i przycisk „ukryj"; pozycja kropki
  zmienia się przy scrollu (711px→87px, przyklejenie do góry); ocenienie zad 3 usuwa
  jego kropkę; trwałość po reload; „ukryj" chowa wszystkie i kasuje fazę (po reload 0).
  Wizualnie sprawdzone w jasnym i ciemnym. Bez błędów w konsoli.

ZROBIONE PRZEZ OPUSA (2026-07-21) — zmienne CSS + dark mode (Etap 1 infrastruktura) z TODO.md:
- [ZROBIONE] Wprowadzone CSS custom properties na wszystkie kolory (tło, tekst,
  ramki, akcenty, stany poprawne/błędne, badge punktacji, komunikat błędu) w :root
  (style.css). Wartości w :root = dokładnie dotychczasowe kolory jasnego motywu,
  więc jasny wygląda 1:1 jak wcześniej (zweryfikowane computed: body bg
  rgb(255,255,255), tekst rgb(17,17,17), #total-score rgb(133,133,133)). Cały
  style.css (~136 użyć) przepięty na var(--...). Canvas ma własne --canvas-bg,
  które NIE ciemnieje (widżety rysują ciemnym po jasnym — inaczej wykresy
  zniknęłyby). Landing-cta odwraca kolory przez var(--text)/var(--bg), więc hover
  działa w obu motywach.
- [ZROBIONE] Ciemna paleta w dwóch bliźniaczych blokach: @media
  (prefers-color-scheme: dark) :root:not(.theme-light) (motyw systemowy/auto) oraz
  html.theme-dark (ręczne wymuszenie — pierwszeństwo nad systemem). Ręczny jasny =
  html.theme-light (wyłącza regułę systemową przez :not, zostają wartości :root).
- [ZROBIONE] Przełącznik #theme-toggle w menu „⋯" (template.html) cyklujący
  auto → jasny → ciemny → auto; wybór ≠ auto zapisywany w localStorage pod
  GLOBALNYM kluczem matematykazen-motyw (wspólny dla wszystkich arkuszy). Klasę na
  <html> ustawia mały inline-skrypt w <head> template.html (bez mignięcia motywu /
  FOUC), logika i etykieta w script.js. Ten sam snippet dodany do index.html, żeby
  landing honorował zapamiętany motyw (landing nie ma własnego przełącznika — bez
  zapisu idzie za systemem). Zweryfikowane Playwrightem: cykl stanów, klasy na
  <html> (theme-light/theme-dark), zapis/kasowanie w localStorage, trwałość po
  reload bez FOUC, brak błędów w konsoli; wizualnie sprawdzone dark: pasek, treść
  zadania + KaTeX, błędna odpowiedź (przygaszona czerwona ramka), blok rozwiązania,
  nakładka podsumowania egzaminu, landing.

ZROBIONE PRZEZ OPUSA (2026-07-21) — nudge #bar-center z TODO.md:
- [ZROBIONE] Tytuł arkusza (#exercises-sheet-title) i podtytuł trybu
  (#exercises-mode-subtitle) delikatnie niżej w pasku: na #bar-center dodane
  position: relative; top: 5px; (style.css). Wysokość #top-bar bez zmian
  (zmierzone Playwrightem: 64px, position=relative/top=5px, tytuł opuszczony
  o 5px). 5px wizualnie w porządku.

ZROBIONE PRZEZ OPUSA (2026-07-21) — "tryb egzaminu — pasek i stopka" z TODO.md:
- [ZROBIONE] Dodatkowy przycisk "zakończ egzamin" w pasku górnym (#egzamin-koniec-bar
  w template.html, w #bar-right zaraz po #egzamin-timer, przed #total-score). Styl jak
  #toggle-tablica (border 2px #e7e7e7, radius 3px, padding 8px 12px, bg #fff, cursor
  pointer) ale BEZ min-width. Widoczny tylko pod body.tryb-egzaminu (domyślnie display:
  none, odkrywany regułą body.tryb-egzaminu #egzamin-koniec-bar). W @media <=720px dostaje
  font-size:13px i padding:8px jak #total-score. Istniejący #egzamin-koniec pod ostatnim
  zadaniem został na miejscu.
- [ZROBIONE] #egzamin-koniec (stopka) dostał odstęp od góry: margin 0 auto 80px → 40px
  auto 80px (style.css).
- [ZROBIONE] Dodatkowy przycisk "rozpocznij próbny egzamin" w stopce arkusza
  (#egzamin-start-stopka w template.html, tuż obok #egzamin-koniec pod #exercises-wrapper),
  widoczny odwrotnie — tylko w trybie ćwiczeniowym (znika pod body.tryb-egzaminu). Styl
  identyczny jak #egzamin-koniec w stopce (ta sama ramka, 40px góra / 80px dół). Wersja
  w menu "⋯" (#egzamin-start) została bez zmian.
- Zachowanie: obie pary przycisków wiszą na wspólnych funkcjach w script.js
  (startExamPrompt / finishExamPrompt), podpiętych pętlą do obu id, żeby kopie nie mogły
  się kiedyś rozjechać. Zweryfikowane Playwrightem w obu trybach: w ćwiczeniowym widać tylko
  stopkowy start (total-score widoczny), w egzaminie widać oba "zakończ" + timer (total-score
  i stopkowy start ukryte); klik "zakończ egzamin" w pasku czyści stan egzaminu i pokazuje
  podsumowanie (identycznie jak przycisk w stopce). Wizualnie sprawdzony układ paska (1280px
  i 700px) oraz przyciski w stopce.

ZROBIONE PRZEZ OPUSA (2026-07-17) — NISKI PRIORYTET z TODO.md:
- [ZROBIONE] Przeciąganie paneli PDF ograniczone do widocznego viewportu
  (makePanelDraggable w script.js). Wcześniej dół/boki były swobodne i pasek
  tytułowy (.panel-uchwyt) mógł zjechać pod dolną krawędź ekranu (za pasek zadań
  Windows). Teraz w funkcji move() klampujemy: top ∈ [minTop, innerHeight −
  uchwytH] (uchwyt zawsze w pełni widoczny, nie chowa się pod top-barem ani pod
  dolną krawędzią), left ∈ [minWidoczne − szer, innerWidth − minWidoczne]
  (min. 60px panelu zostaje na ekranie w bok). ŚWIADOMA ZMIANA wcześniejszej
  decyzji z 2026-07-13 (wtedy celowo BEZ klampu dołu/boków) — użytkownik
  poprosił o ograniczenie do viewportu. Zweryfikowane Playwrightem: drag daleko
  w dół+prawo → uchwyt zostaje przy dolnej krawędzi i 60px w prawym rogu; drag
  daleko w lewo → panel left=-298px, czyli 60px widoczne po lewej.
- [ZROBIONE] Wcięcie treści zadania (.question padding-left: 16px w style.css) —
  tekst nie klei się już do lewej krawędzi karty i nie wygląda na przeciągnięty
  w lewo względem wyśrodkowanych odpowiedzi. Zweryfikowane (computed
  padding-left=16px, wizualnie treść przesunięta w prawo).
- [ZROBIONE] Wyrównanie badge'a punktacji zadania w pionie (.exercise-score
  margin-top: 16px w style.css) — wcześniej siedział optycznie ~16px za wysoko
  względem numeru zadania. Zmierzone Playwrightem: środek badge'a przesunięty
  z y≈172 na y≈188, zrównany ze środkiem pierwszej linii treści (≈188). W media
  query <=1024px (badge w rogu karty) margin-top wyzerowany, żeby trzymał się
  górnej krawędzi.
- [ZROBIONE] Procent zdobytych punktów obok sumy w pasku (tryb ćwiczeniowy).
  updateTotalScore() (script.js) dokłada do #total-score <span.total-percent>
  z bieżącym procentem (round(pkt/max*100)); od progu zdawalności 30% dostaje
  klasę .zdane (zielony #0AB32F, bold) i title="zdałeś", poniżej szary +
  title="nie zdałeś (jeszcze)" (CSS w style.css, cursor: help). Ponieważ procent
  jest WEWNĄTRZ #total-score, automatycznie znika w trybie egzaminu i w widoku
  punktów "nic". Zweryfikowane Playwrightem: 24% → szary/"nie zdałeś (jeszcze)";
  38% → zielony bold/"zdałeś".
- [ZROBIONE] Normalizacja odpowiedzi fillIn (normalizeAnswer w script.js) —
  dołożony .replace(/[xye∈]/gi, "") wycina znaki zmiennej/przynależności
  (x, y, E/∈), więc "x∈(-4,4]", "y ∈ [-1,3]", "X E (1,3)" pasują do samego
  przedziału z klucza. Sprawdzone, że żadna accepted w obu exercises.json nie
  zawiera x/y/e/∈, więc usunięcie z obu stron porównania jest bezpieczne.
  Zweryfikowane Playwrightem: normalizeAnswer(warianty) → czysty przedział;
  realne pole fillIn (zad 17, exercise-9) z wpisami "x∈(-4, 4]" itd. → wszystkie
  4 pola .correct.
- [ZROBIONE] TRYB PRÓBNY EGZAMIN — trzy poprawki (style.css + script.js):
  * (6a) Cały wiersz light-buttonów chowany w trybie egzaminu przez
    `body.tryb-egzaminu .light-button-container { display:none }` (wcześniej
    ukrywane były tylko .hint-button/.solution-button, a "Pokaż potrzebne wzory"
    zostawał sam z pustym odstępem). TABLICA wzorów CKE i #toggle-tablica nadal
    widoczne; #toggle-zasady (klucz odpowiedzi) nadal ukryty.
  * (6b) Opcje w menu "..." (pokaż rozwiązania / widok punktów / reset / start
    egzaminu) NIE znikają już w egzaminie — zostają widoczne, ale disabled
    (wyszarzone, nieklikalne), więc menu nie jest pustą ramką. setExamMenuDisabled()
    w script.js ustawia atrybut disabled na tych 4 przyciskach w enableExamMode()
    i zdejmuje go w finishExam(); CSS `#bar-menu button:disabled` daje opacity 0.4
    + cursor not-allowed. Usunięte te 4 id z listy display:none w bloku egzaminu.
  * (6c) Zadania otwarte (selfScore) dostają textarea "Twoja odpowiedź / tok
    rozwiązania" w OSOBNYM kontenerze .open-answer-container (poza
    .self-score-container, którą egzamin chowa) — dzięki temu textarea jest
    widoczna i podczas egzaminu (samoocena schowana), i po nim (samoocena wraca).
    Zapis do localStorage tą samą drogą co reszta (stan.open w zapiszPostep,
    przywracane w bloku "Przywrócenie postępu" gdy typeof zap.open === "string").
    Zweryfikowane Playwrightem: NORMAL → textarea+samoocena+light-buttony widoczne;
    EXAM → light-buttony ukryte, textarea widoczna, samoocena ukryta,
    #toggle-tablica widoczny, #toggle-zasady ukryty, 4 opcje menu disabled=true;
    wpis w textarea przetrwał reload; po "zakończ egzamin" — samoocena wraca,
    treść textarea zachowana, opcje menu disabled=false.

ZROBIONE PRZEZ OPUSA (2026-07-13) — cały WYSOKI PRIORYTET z TODO.md:
- [ZROBIONE] Powiększone UMIARKOWANIE przyciski "oceń się" (.self-score-container button
  w style.css): padding 6px 10px → 8px 11px, font-size 15px → 17px, min-width 56px → 62px.
  Zwarty poziomy rząd przycisków punktowych zostaje — nie robią się pełnowymiarowymi
  przyciskami odpowiedzi. Zweryfikowane Playwrightem (computed font-size=17px, padding=8px 11px).
- [ZROBIONE] Panele PDF (makePanelDraggable w script.js): jedyne ograniczenie przeciągania
  to top — uchwyt (.panel-uchwyt) nie zjedzie pod top-bar (minTop = dolna krawędź #top-bar,
  liczona z getBoundingClientRect przy każdym pointerdown, więc panel zawsze da się złapać).
  Usunięty Math.max(0,...) na left — lewo/prawo/dół całkowicie swobodne (panel może wyjechać
  poza brzeg ekranu). Zmiana rozmiaru (.panel-rozmiar) bez zmian. Zweryfikowane Playwrightem:
  drag w górę klampuje top do dolnej krawędzi paska, drag w lewo daje left=-821px (bez klampu).
  UWAGA/decyzja: prompt mówił "by CAŁY pasek uchwytu się nie schował"; wybrałem ostrzejszy,
  pewniejszy wariant — cały uchwyt zostaje pod paskiem (zawsze w pełni chwytalny), zamiast
  dopuszczać częściowe wsunięcie z pozostawionym skrawkiem. Efekt (uchwyt zawsze chwytalny)
  jest ten sam, a zachowanie czytelniejsze.
- [ZROBIONE] Błędny/pusty/brakujący ?arkusz= → komunikat "Błędny link" z hiperłączem do
  index.html zamiast cichego fallbacku. Usunięty `|| "2024-grudzien"` w script.js (SHEET_ID).
  startSheet() rozróżnia: brak/pusty param → od razu błędny link (bez fetchu); fetch 404 →
  błędny link; brak odpowiedzi (file:// / sieć) → dawny komunikat o serwerze; zły JSON →
  komunikat o uszkodzonym pliku. Zweryfikowane Playwrightem (brak param / ?arkusz= / nieznane
  id → "Błędny link" + link do index.html + zero wyrenderowanych zadań; poprawne id → render OK).
- [ZROBIONE] Stały, szarawy podtytuł trybu pod nazwą arkusza w pasku
  (#exercises-mode-subtitle w #bar-center, template.html; CSS 12px #999). Domyślnie
  "tryb ćwiczenia", przełącza się na "tryb egzaminu" pod body.tryb-egzaminu przez
  updateModeSubtitle() wołane w enableExamMode() i finishExam(). Chowany <900px razem
  z tytułem. Zweryfikowane Playwrightem (ćwiczenie → "tryb ćwiczenia", start egzaminu →
  "tryb egzaminu").
- [ZROBIONE] Krótkie confirm() przed "resetuj punktację" (#reset-scores, script.js):
  "Wyczyścić zapisane odpowiedzi i punkty? Tej operacji nie można cofnąć." Anulowanie
  przerywa akcję. Zweryfikowane Playwrightem (klik pokazuje dialog z tym tekstem).

