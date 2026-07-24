Oto plik który tworzy Henrich (ja, użytkownik).

DO REALIZACJI
<br> Jeżeli nie masz co robić, to rób stąd.
Do przydzielenia:
- Przycisk "sprawdź wszystkie odpowiedzi" powinien być szary/nieaktywny w trybie egzaminu

Dla Sonneta na effort High:
- Dwie karty tego samego arkusza blokują „zakończ egzamin" (issues/dwie-karty-tryb-egzaminu.md) — sprawdzone 2026-07-24, NADAL nie naprawione
- ARCHITECTURE.md opisuje tylko połowę trybu egzaminu (issues/dokumentacja-exam-mode-luka.md)

Dla Opusa na effort High:
- Arkusz 2024 (demonstracyjny) nie wczutuje się na telefonie w ogóle.
- Na telefonie domyślnie:
  - wyłączone punkty
  - przyciski „Pokaż tablice wzorów" i „Pokaż zasady oceniania": pdf powinny odpalać się albo na fullscreen, albo otwierać pdf w nowej karcie/oknie przeglądarki. Mogą też odpalać pdf w przeglądarce pdf w telefonie, jeśli to nie jest zbyt skomplikowane.
-  i/lub dodać toggle tryb testowy, który zmienia czas egzaminu na absurdalnie krótki , abym mógł przetestować koniec egzaminu

- Zadania otwarte z serii "oceń się", dodać do nich:
  - Okienko normalizujące i sprawdzające wpisaną odpowiedź oprócz miejsca na notatki.
  - Mini-formularz z pytaniami w stylu „Czy masz zapisane, żę długość boku BC to 5cm", które wynikają z zasad oceniania i ułatwiają ustalenie ilości punktów. Może wyglądać to podobnie do zadań otwartych w których uzupełnia się odpowiedzi np przedziałami.
  - Można dać gwiazdkę, że trzeba każdy przypadek sprawdzić indywidualnie i autor strony nie jest egzaminatorem.

<br>


NIE REALIZUJ
<br> czyli nieskonkretyzowane

- dodanie rozwiązań do matury 2026

<br>


DLA HENRICHA:

- Skonfigurować formspree (formularze błędów) - kod JS „zgłoś błąd" jest gotowy(app/report.js). Zostaje tylko:
  * założyć konto na formspree.io
  * utworzyć formularz i wkleić jego endpoint (`https://formspree.io/f/xxxxxxxx`) w miejsce stałej `FORMSPREE_ENDPOINT = "TODO-WKLEJ-ENDPOINT-FORMSPREE"` na górze app/report.js. Do tego czasu wysyłka pokazuje komunikat „nie skonfigurowane".

- Obczaić analitykę, czyli śledzenie ilości i zaangażowania użytkowników. Warto rozważyć GoatCounter.

- Wykminić, jak zrobić grafiki do dark mode, można np. masowo odwrócić kolory i zmienić krzywą tak, aby zamiast czarnego tła był odpowiedni kolor szarego. (Tańszy tymczasowy fix: CSS filter na `.question img`/wideo — patrz issues/dark-mode-obrazki-wideo.md)

- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

<br>


INNE NOTATKI, DO PRZEKMINIENIA:

- Na telefonie pdfy się nie ładują (tablica i zasady oceniania). (to nie będzie problem po zmianie na pdf otwierane na zewnątrz stronki, jeśli tamto będzie działać to można usunąć ten wpis)
  - Podczas naprawy warto sprawić, aby odpalały się one nie w okienku, ale wypełniały całą stronę z krzyżykiem w rogu.
  - Jeżeli nie uda się tego naprawić, to należy usunąć tę funkcjonalność z wersji mobilnej.

- Tryb egzaminu nie powinien być tak „schowany" w opcjach. Może pod tytułem zrobić zamiast stałego napisu „tryb ćwiczeniowy" toggle między dwoma trybami.

- Propozycje zmiany UI:
  - Albo: Wywalić top-bar i przenieść wszystko na rozwijany pasek boczny po lewej, który można łatwo schować, aby widzieć tylko zadania i włączone elementy takie jak tablica, punktacja itd.
  - Albo: Dodać toggle „chowający się panel górny: włączony/wyłączony" (możesz wymyśleć lepszą nazwę).
    - Ta opcja ma być domyślnie włączona na telefonie.
    - Top-bar powinien się chować po scrollowaniu w dół i pojawiać przy scrollowaniu w górę lub gdy pociągnie się z górnej krawędzi.

- Do sekcji „oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu, jak to skomponować, aby miało sens.

- Pokminić nad kolejnością przycisków w menu

- W index.html dodać sekcję o autorze i link do Patronite

<br><br>


<h3>DO REALIZACJI Dopisane przez CLAUDA</h3>
Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.

(wszystkie punkty przeniesione do „Dla Sonneta na effort High" wyżej, ze skonkretyzowanym kierunkiem naprawy)


ZASADY dla Ciebie Claude:
- tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod DONE/ — patrz DONE/README.md i CLAUDE.md.)
- TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo DONE/, a tu zostaje jedna linijka z odnośnikiem.
 Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole
- Zadania realizuj od góry do dołu.
- Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.
