Oto plik który tworzy Henrich (ja, użytkownik).

DO REALIZACJI
Jeżeli nie masz co robić to rób stąd.

Dla Sonneta na effort High
(brak — wszystko zrobione, patrz DONE/)

<br>


NIE REALIZUJ
czyli nieskonkretyzowane

- squah grup starych commitów zrobionych automatycznie przez gitdoc

- dodanie rozwiązań do matury 2026

- zadania otwarte powinny też mieć okienko normalizujące i sprawdzające wpisaną odpowiedź. Do tego można rozpisać i dorobić donich pytania w stylu "Czy masz opisana długość boku BC?" które wynikają z zasad oceniania i ułatiwają ustalenie ilości punktów. przy nich można dać gwiazdkę, że trzeba każdy przypadek sprawdzić indywidualnie i autor strony nie jest egzaminatorem. 

- do sekcji "oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu jak to skomponować aby miało sens.



<br>


DLA HENRICHA:

- skonfigurować formspree (formularze) — kod „zgłoś błąd" JEST GOTOWY (app/report.js). Zostaje tylko: 
  * założyć konto na formspree.io
  * utworzyć formularz i wkleić jego endpoint (`https://formspree.io/f/xxxxxxxx`) w miejsce stałej `FORMSPREE_ENDPOINT = "TODO-WKLEJ-ENDPOINT-FORMSPREE"` na górze app/report.js. Do tego czasu wysyłka pokazuje komunikat „nie skonfigurowane".

- Obczaić analitykę czyli śledzenie ilości i zaangażowania użytkowników (moze da sięjakoś przez githuba)

- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

- Wykminić jak zrobić grafiki do dark mode, można np masowo odwrócić kolory i zmienić krzywą tak, aby zamiast czarnego tła był odpowiedni kolor szarego. (Tańszy tymczasowy fix: CSS filter na `.question img`/wideo — patrz issues/dark-mode-obrazki-wideo.md)

<br>


INNE NOTATKI:

- pokminić nad kolejnością przycisków w menu

- Poprosić claude aby zmienił czas egzaminu na absurdalnie krótki i/lub dodał toggle trybu testowego który to robi abym mógł przetestować koniec egzaminu

- dodać toggle "chowający się panel górny: włączony/wyłączony" (możesz wymyśleć lepszą nazwę), ta opcja ma być domyślnie włączona na telefonie. Top-bar powiniene się chować po scrolowaniu w dół i pojawiać przy skrolowaniu w górę lub gdy pociągnie się z górnej krawędzi.

- Tryb egzaminu nie powinien być tak "schowany" w opcjach. Moze pod tytułem zrobić zamiast stałego napisu "tryb ćwiczeniowy" zrobić toggle między dwoma trybami.

- na telefonie pdfy się nie ładują (tablica i zasady oceniania). Podczas naprawy warto sprawić aby odpalały się one nie w okienku ale wypełniały całą stronę z krzyżykiem w rogu. Jeżeli nie uda się tego naprawić to należy usunąć tę funkcjonalność z wersji mobilnej.

- ZMIANA UI: Wywalić top-bar i przenieśc wszystko na rozwijany pasek boczny po lewej który można łatwo schować, aby widzieć tylko zadania i włączone elementy takie jak tablica, punktacja itd.

- Na telefonie defaltowo:
  * wyłączone punkty
  * przyciski "Pokaż tablice wzorów" i "Pokaż zasady odeniania": pdf powinny odpalać się albo na full screen albo otwierać pdf w nowej karcie/oknie przeglądrki. Mogą też odpalać pdf w przeglądarce pdf w tel jeśli to nie zbyt skomplkowane.

- Analityka - GoatCounter

- W index.html dodać sekcję o autorze i link do patronite

- przycisk rozpocznij próbny egzamin powiniene być zablokowany a nie niewidoczny na stronie z błędem arkusz (minor thing)

<br><br><br>


<h3>DO REALZACJI Dopisane przez CLAUDA</h3>
Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.

TRYB EGZAMINU I PAMIĘĆ PRZEGLĄDARKI:

- Dwie karty tego samego arkusza blokują "zakończ egzamin" (issues/dwie-karty-tryb-egzaminu.md) — sprawdzone 2026-07-24, NADAL nie naprawione

DARK MODE — WYGLĄD:

- Dwie zmienne CSS użyte niezgodnie z przeznaczeniem na stronie głównej (issues/dark-mode-css-zmienne-landing.md)
- Kropki wskaźników "gumkują" przy scrollowaniu (issues/dark-mode-wskazniki-scroll.md)

DOKUMENTACJA:

- ARCHITECTURE.md opisuje tylko połowę trybu egzaminu (issues/dokumentacja-exam-mode-luka.md)

DROBIAZGI (niski priorytet, dziś nieszkodliwe):

- Numer zadania gubi podnumer (12.1 vs 12.2) (issues/numer-zadania-podnumer.md)
- Motyw rozjeżdża się między kartami przeglądarki (issues/motyw-rozjezdza-sie-miedzy-kartami.md)
- Cichy błąd zapisu w ustawFazeOceniania() (issues/ocenianie-cichy-blad-zapisu.md)

- Wskaźniki „oceń się" znikają po odświeżeniu strony po egzaminie (issues/wskazniki-reload-faza-oceniania.md)


ZASADY dla Ciebie Claude:
- tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod DONE/ — patrz DONE/README.md i CLAUDE.md.)
- TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo DONE/, a tu zostaje jedna linijka z odnośnikiem.
 Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole
- Zadania realizuj od góry do dołu.
- Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.