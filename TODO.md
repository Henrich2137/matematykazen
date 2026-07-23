Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod DONE/ — patrz DONE/README.md i CLAUDE.md.)
(Zasada: Drogi LLM, Sonnecie, Opusie, Jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole)
Zadania realizuj od góry do dołu.
Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

<br>

<h3>DO REALIZACJI</h3>
Jeżeli nie masz co robić to rób stąd.

- Przenieść przycisk skrócić nazwę przycisku na "Ukryj wskaźniki" i przenieść go do prawego dolnego rogu. Same wskaźniki dopracować tak, aby nie nachodziły na niego tylko zzatrzymywały się troche wyżej jeśli wskazują coś na dole.

- Naprawić włącznie trybu egzaminu który działa tylko raz a potem się blokuje.

- Plan podziału plików (.claude/plans/czy-my-lisz-e-mam-tingly-hamster.md): kroki 1, 1b, 2 i 3 zrobione i zautomatyzowanie zweryfikowane (patrz DONE/03-biezace.md) — zostaje tylko wizualny przegląd kroku 3 przez Henricha (jasny/ciemny motyw, okno ~500px, landing), patrz sekcja „DO SPRAWDZENIA PRZEZ HENRICHA" niżej. Krok 4 zrobiony wcześniej inaczej (katalog nazwano "DONE TODO"; od 2026-07-22 zmieniony na "DONE"). Krok 5 (script.js → js/) świadomie odłożony, poza zakresem.

<br>


NIE REALIZUJ
czyli nieskonkretyzowane

- Stworzyć przycisk "zgłoś błąd w zadaniu" i odpowiedni formularz. Formspree / Getform ale wewnątrz strony (submit przez fetch (AJAX) czy coś) można jeszcze to doprecyzować albo zmienić troche koncepcje.

- dodanie rozwiązań do matury 2026

- zadania otwarte powinny też mieć okienko normalizujące i sprawdzające wpisaną odpowiedź. Do tego można rozpisać i dorobić donich pytania w stylu "Czy masz opisana długość boku BC?" które wynikają z zasad oceniania i ułatiwają ustalenie ilości punktów. przy nich można dać gwiazdkę, że trzeba każdy przypadek sprawdzić indywidualnie i autor strony nie jest egzaminatorem. 

- do sekcji "oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu jak to skomponować aby miało sens.

- wyciągnięcie tekstu z PDF-ów:
  * matematyka-2025-maj-matura-podstawowa.pdf
  * matematyka-2025-maj-matura-podstawowa-odpowiedzi.pdf


- dodać w opcjach toggle "pokaż poprawność odpowiedzi natychmiast po zaznaczeniu" oraz gdy jest wyłączony to musi być widać
  * przycisk sprawdź po wybraniu odpowiedzi po prawej stronie, tak aby nie zmieniało wysokości diva/strony. Przycisk po kliknięciu powinien: włączyć kolory ramek w zależności od odpowiedzi takie jakie są obecnie, zniknąć.  
  * przycisk "sprawdź wszystkie odpowiedzi" na dole arkusza oraz w ustawieniach powinien widnieć.


<br>


DLA HENRICHA:

- Obczaić analitykę czyli śledzenie ilości i zaangażowania użytkowników (moze da sięjakoś przez githuba)

- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.


<br>


INNE NOTATKI:

- Tryb egzaminu nie powinien być tak "schowany" w opcjach. Moze pod tytułem zrobić zamiast stałego napisu "tryb ćwiczeniowy" zrobić toggle między dwoma trybami.

- na telefonie pdfy się nie ładują (tablica i zasady oceniania). Podczas naprawy warto sprawić aby odpalały się one nie w okienku ale wypełniały całą stronę z krzyżykiem w rogu. Jeżeli nie uda się tego naprawić to należy usunąć tę funkcjonalność z wersji mobilnej.

- ZMIANA UI: Wywalić top-bar i przenieśc wszystko na rozwijany pasek boczny po lewej który można łatwo schować, aby widzieć tylko zadania i włączone elementy takie jak tablica, punktacja itd.

- Na telefonie defaltowo:
  * wyłączone punkty
  * przyciski Pokaż tablice wzorów itd schowane w trzech kropkach a okna z pdf odpalają się albo na full screen albo otwierają pdf w nowym oknie przeglądrki lub w ogóle w nowej "aplikacji" jeśli tak się da. mogą też odpalać pdf w przeglądarce pdf w tel jeśli to nie z byt skomplkowane
  * Przycisk pokaż wybrane wzory się nie wyświetla

- Zgłaszanie błędów - Formspree / Getform ale wewnątrz strony (submit przez fetch (AJAX) czy coś)
- Analityka - GoatCounter
- W index.html dodać sekcję o autorze i link do patronite

<br><br><br>


DO SPRAWDZENIA PRZEZ HENRICHA.
Claudzie, możesz tutaj dopisywać rzeczy które mam sprawdzić/przetestować.
- Krok 3 podziału plików: style.css → style/ (base/sheet/landing/exam/responsive.css).
  Wszystko co dało się zautomatyzować jest zweryfikowane (node/grep, Playwright: liczba
  zadań, wszystkie widżety, klik ABCD/PF/fillIn, kaskada — computed styles dla jasny/ciemny
  motyw, grid #bar-container na 500px i 1280px, tryb egzaminu, landing). Zostaje sam wygląd —
  otwórz template.html?arkusz=2024-grudzien i sprawdź: jasny i ciemny motyw (⋯ → motyw),
  okno zwężone do ~500px (pasek, karta zadania, przyciski), oraz index.html (landing). Nie
  spodziewam się różnic względem starego style.css — to czysty podział plików (diff to
  potwierdził), ale to jedyna rzecz, której sam nie zweryfikuję.

<br><br><br>


<h3>DO REALZACJI Dopisane przez CLAUDA</h3>

OPUS DOPISAŁ PODCZAS ROBIENIA CODE-REVIEW:
(code review gałęzi claude/do-sprawdzenia-yfi2mu, 2026-07-22 — dark mode + podwojone przyciski egzaminu + żółte wskaźniki. Punkty oznaczone [POTWIERDZONE] odtworzyłem realnie w przeglądarce, reszta z czytania kodu.)

[Punkty 1-7 z tej sekcji — znikanie wpisanego toku rozwiązania, żółte wskaźniki
(oba problemy) i cztery poprawki UI (przycisk startu egzaminu na stronie błędu,
menu ⋯ na telefonie, przełącznik motywu) — naprawione przez Sonneta 2026-07-22
na gałęzi claude/po-review, zweryfikowane Playwrightem. Szczegóły: DONE/03-biezace.md.]

TRYB EGZAMINU I PAMIĘĆ PRZEGLĄDARKI:

- Dwie karty tego samego arkusza blokują "zakończ egzamin". Karta A kończy egzamin i usuwa `KLUCZ_EGZAMINU`, po czym karta B zostaje na zawsze w `body.tryb-egzaminu` — `finishExam()` wychodzi od razu na `if (!stan) return;` (script.js), więc zegar stoi, rozwiązania/punkty są ukryte, a klik "zakończ egzamin" nic nie robi i nie daje żadnego komunikatu. Ratuje tylko ręczne odświeżenie. NIE naprawione (2026-07-22, Sonnet) — wymaga większej przebudowy niż drobna poprawka (np. nasłuch zdarzenia `storage`, żeby karta B zauważyła zmianę localStorage z karty A, albo inna architektura synchronizacji stanu między kartami). Dwie mniejsze, powiązane poprawki z tej samej sekcji (nieudany start egzaminu kasujący postęp; "resetuj punktację" niekasujący trwającego egzaminu) zostały już naprawione — patrz DONE/03-biezace.md.

DARK MODE — WYGLĄD:

- Obrazki CKE i filmy z Manima świecą na biało w ciemnym motywie. Migracja świadomie przypięła `--canvas-bg: #fff` dla płócien widgetów, ale `.question img` (style/sheet.css:293), obrazki kroków i `<video>` nie dostały żadnej reguły tła/filtra — wszystkie PNG w matura/**/ są nieprzezroczyste białe, więc renderują się jako jaskrawe prostokąty na karcie #1b1b1b.

- Dwie zmienne CSS użyte niezgodnie z przeznaczeniem na stronie głównej:
  * `.landing-footer` (style/landing.css:90) bierze kolor tekstu z `--border-close` — tokena ramki krzyżyka paneli. Jego ciemna wartość to #666 na tle #1b1b1b, czyli kontrast 3.0:1, poniżej progu WCAG AA 4.5:1 dla tekstu 13px. Powinien iść przez `--text-faint-*`.
  * `.landing-card` (style/landing.css:63) bierze ramkę z `--bg-hover` — tokena tła hoveru. Powinna iść przez któryś `--border*`.
  * Skutek uboczny obu: przestrojenie krzyżyka paneli PDF po cichu zmienia wygląd strony głównej, a testowany będzie panel, nie landing.

- Kropki "gumkują" przy scrollowaniu. `.wskaznik-otwarte` ma `transition: top 0.12s ease` (style/exam.css:164), a `repozycjonujWskazniki()` przepisuje `top` w każdej klatce rAF — tranzycja restartuje się co klatkę i nigdy nie kończy, więc kropki wloką się za zadaniami i drgają jeszcze ~120ms po zatrzymaniu scrolla. Animacja ma sens tylko dla skokowej repozycji po ocenieniu zadania.

DOKUMENTACJA:

- ARCHITECTURE.md opisuje tylko połowę tej gałęzi. Dark mode udokumentowany wzorowo, ale sekcja "Exam mode" (ARCHITECTURE.md ~80) nadal opisuje kończenie egzaminu wyłącznie przez `#egzamin-koniec` i wymienia dwa klucze localStorage — brak `#egzamin-koniec-bar`, `#egzamin-start-stopka`, trzeciego klucza `KLUCZ_OCENIANIA` i całej fazy "oceń się" ze wskaźnikami. Lista ID "referenced by the inline JS, so keep the IDs stable" (ARCHITECTURE.md ~97) nie zawiera `#egzamin-koniec-bar` ani `#theme-toggle`, więc ktoś restylujący pasek może je skasować jako niepodpięte.

DROBIAZGI (niski priorytet, dziś nieszkodliwe):

- Numer zadania wyciągany regexem `/Zadanie\s*(\d+)/i` (script.js:891) gubi część po kropce — gdyby kiedyś zadanie 12.1 i 12.2 były otwarte (selfScore), dostałyby dwie identyczne kropki "12" z identycznym tooltipem. Dziś nieosiągalne: w obu arkuszach żadne zadanie otwarte nie ma podnumeru. Docelowo lepsze byłoby pole `numer` w exercises.json (przydałoby się też w console.warn w script.js:695 i :1004, które nadal drukują mylące `index + 1`).
- Motyw rozjeżdża się między kartami: `readTheme()` czyta localStorage zamiast stanu, który ta karta faktycznie renderuje, i nikt nie słucha zdarzenia `storage`. Dwie karty potrafią pokazywać różny motyw i różne etykiety przycisku.
- `ustawFazeOceniania()` (script.js:280-285) cicho połyka błędy zapisu — przy zablokowanym localStorage "ukryj wskaźniki" nie utrwala się i kropki wracają po każdym odświeżeniu, bez żadnego komunikatu.