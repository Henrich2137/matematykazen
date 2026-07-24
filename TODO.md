Oto plik który tworzy Henrich (ja, użytkownik).

DO REALIZACJI
<br> Jeżeli nie masz co robić, to rób stąd.
Do przydzielenia:
- Przycisk "sprawdź wszystkie odpowiedzi" powinien być szary/nieaktywny w trybie egzaminu

Dla Sonneta na effort High
1. Przycisk "zgłoś błąd" → tekst "zgłoś błąd" (app/report.js:243) i wyśrodkować (`text-align: center` na `.report-error-link`, style/sheet.css:858)
2. Landing CSS używa złych zmiennych (kontrast WCAG) — `.landing-footer` (style/landing.css:90) → `var(--text-faint)` zamiast `--border-close`; `.landing-card` (style/landing.css:63) → `border: 1px solid var(--border)` zamiast `--bg-hover`. Szczegóły: issues/dark-mode-css-zmienne-landing.md
3. Kropki wskaźników „gumkują" przy scrollowaniu — wyłączyć `transition` na `.wskaznik-otwarte` (style/exam.css:213) na czas aktywnego scrolla (klasa dodawana/zdejmowana w app/indicators.js, debounce ~150ms po ostatnim scroll evencie, bez `scrollend`) i przywracać go po zatrzymaniu scrolla; szczegóły w issues/dark-mode-wskazniki-scroll.md
4. Cichy błąd zapisu w `ustawFazeOceniania()` (app/indicators.js:21-26) — w catch wywołać `pokazZglosToast("nie udało się zapisać ustawienia", true)` (istniejący toast z app/report.js). Szczegóły: issues/ocenianie-cichy-blad-zapisu.md
5. Wskaźniki „oceń się" znikają po odświeżeniu po egzaminie — `pokazWskaznikiOtwarte()` (app/indicators.js:73-76) nie powinno gasić fazy, gdy arkusz jeszcze nie wyrenderowany; strażnik `document.body.classList.contains("arkusz-wczytany")` (klasa z app/render.js:715). Szczegóły: issues/wskazniki-reload-faza-oceniania.md
6. Motyw rozjeżdża się między kartami — dodać w app/theme.js nasłuch `window.addEventListener("storage", ...)`: przy zmianie `KLUCZ_MOTYWU` w innej karcie wywołać `applyTheme(readTheme())`. Tylko to (bez ogólnego cross-tab helpera). Szczegóły: issues/motyw-rozjezdza-sie-miedzy-kartami.md
7. [niski priorytet, dziś nieszkodliwe] Numer zadania gubi podnumer (12.1 vs 12.2) — zmienić regex w app/render.js:440 na `/Zadanie\s*([\d.]+)/i`; sprawdzić, czy nic nie zakłada, że `numer` jest liczbą całkowitą. Dane w exercises.json są poprawne (podnumerowane zadania mają `type: "fillIn"`, nie wchodzą dziś do `zadaniaOtwarte`) — to łatka regexu, nie poprawka danych. Szczegóły: issues/numer-zadania-podnumer.md

Dla Opusa na effort High:
- nic

<br>


NIE REALIZUJ
<br> czyli nieskonkretyzowane

- dodanie rozwiązań do matury 2026

- Zadania otwarte powinny też mieć okienko normalizujące i sprawdzające wpisaną odpowiedź.
  * Do tego można rozpisać i dorobić do nich pytania w stylu „Czy masz opisaną długość boku BC?", które wynikają z zasad oceniania i ułatwiają ustalenie ilości punktów.
  * Przy nich można dać gwiazdkę, że trzeba każdy przypadek sprawdzić indywidualnie i autor strony nie jest egzaminatorem.

- Do sekcji „oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu, jak to skomponować, aby miało sens.

- squash grup starych commitów zrobionych automatycznie przez gitdoc



<br>


DLA HENRICHA:

- Skonfigurować formspree (formularze błędów) - kod JS „zgłoś błąd" jest gotowy(app/report.js). Zostaje tylko:
  * założyć konto na formspree.io
  * utworzyć formularz i wkleić jego endpoint (`https://formspree.io/f/xxxxxxxx`) w miejsce stałej `FORMSPREE_ENDPOINT = "TODO-WKLEJ-ENDPOINT-FORMSPREE"` na górze app/report.js. Do tego czasu wysyłka pokazuje komunikat „nie skonfigurowane".

- Obczaić analitykę, czyli śledzenie ilości i zaangażowania użytkowników. Warto rozważyć GoatCounter.

- Wykminić, jak zrobić grafiki do dark mode, można np. masowo odwrócić kolory i zmienić krzywą tak, aby zamiast czarnego tła był odpowiedni kolor szarego. (Tańszy tymczasowy fix: CSS filter na `.question img`/wideo — patrz issues/dark-mode-obrazki-wideo.md)

- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

<br>


INNE NOTATKI:

- Na telefonie pdfy się nie ładują (tablica i zasady oceniania).
  * Podczas naprawy warto sprawić, aby odpalały się one nie w okienku, ale wypełniały całą stronę z krzyżykiem w rogu.
  * Jeżeli nie uda się tego naprawić, to należy usunąć tę funkcjonalność z wersji mobilnej.

- Na telefonie domyślnie:
  * wyłączone punkty
  * przyciski „Pokaż tablice wzorów" i „Pokaż zasady oceniania": pdf powinny odpalać się albo na full screen, albo otwierać pdf w nowej karcie/oknie przeglądarki. Mogą też odpalać pdf w przeglądarce pdf w telefonie, jeśli to nie zbyt skomplikowane.

- ZMIANA UI: Wywalić top-bar i przenieść wszystko na rozwijany pasek boczny po lewej, który można łatwo schować, aby widzieć tylko zadania i włączone elementy takie jak tablica, punktacja itd.

- Tryb egzaminu nie powinien być tak „schowany" w opcjach. Może pod tytułem zrobić zamiast stałego napisu „tryb ćwiczeniowy" toggle między dwoma trybami.

- Dodać toggle „chowający się panel górny: włączony/wyłączony" (możesz wymyśleć lepszą nazwę).
  * Ta opcja ma być domyślnie włączona na telefonie.
  * Top-bar powinien się chować po scrollowaniu w dół i pojawiać przy scrollowaniu w górę lub gdy pociągnie się z górnej krawędzi.

- Poprosić Claude, aby zmienił czas egzaminu na absurdalnie krótki i/lub dodał toggle trybu testowego, który to robi, abym mógł przetestować koniec egzaminu

- Pokminić nad kolejnością przycisków w menu

- W index.html dodać sekcję o autorze i link do Patronite

- Przycisk „rozpocznij próbny egzamin" powinien być zablokowany, a nie niewidoczny na stronie z błędem arkusza (minor thing)

<br><br><br>


<h3>DO REALIZACJI Dopisane przez CLAUDA</h3>
Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.

TRYB EGZAMINU I PAMIĘĆ PRZEGLĄDARKI:

- Dwie karty tego samego arkusza blokują „zakończ egzamin" (issues/dwie-karty-tryb-egzaminu.md) — sprawdzone 2026-07-24, NADAL nie naprawione

DOKUMENTACJA:

- ARCHITECTURE.md opisuje tylko połowę trybu egzaminu (issues/dokumentacja-exam-mode-luka.md)

(dark mode CSS-zmienne na landing, wskaźniki po odświeżeniu, cichy błąd zapisu, motyw między kartami i numer-podnumer — przeniesione do „Dla Sonneta na effort High" wyżej, ze skonkretyzowanym kierunkiem naprawy)


ZASADY dla Ciebie Claude:
- tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod DONE/ — patrz DONE/README.md i CLAUDE.md.)
- TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo DONE/, a tu zostaje jedna linijka z odnośnikiem.
 Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole
- Zadania realizuj od góry do dołu.
- Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.
