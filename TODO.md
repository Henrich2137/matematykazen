Oto plik który tworzy Henrich (ja, użytkownik).

DO REALIZACJI
<br> Jeżeli nie masz co robić, to rób stąd.

Do przydzielenia:

- W zadaniach otwartych: zamiast checkboxów powinny być przyciski z punktami do każdego zdania typu "Nierówność zapisana w postaci x2−6x−7≤0x2−6x−7≤0" (przykład z zad 9.) Dokładna punktacja jest w zasadach oceniania w pdf i od tego powinna zależeć ilość przycisków. (czeka na decyzję merytoryczną Henricha o punktacji za poszczególne przyciski, potem do przydzielenia modelowi)

- w zadaniach z oknem z ostateczną odpowiedzią (jak 8 czy 9), po zrobieniu egzaminu ostateczna odpowiedź powinna się samodzielnie sprawdzić.

- Tło w niektórych widżetach jest białe w motywie darkmode. Należy zmienić kolory na taki które będą się zgadzać z motywem.

- Tylko w trybie ćwiczeń przycisk "sprawdź wszystkie odpowiedzi" powinien znajdować się na dole arkusza, obok "rozpocznij egzamin". Ma zostać też w menu (i tu, i tu). W trybie egzaminu na dole arkusza ma być niewidoczny (nie tylko wyszarzony jak w menu).

SESJA 2 — redesign chrome (Opus High, LOKALNIE, nie cloud: potrzebna iteracja wizualna).
Szczegóły techniczne w issues/sidebar-nawigacji.md + issues/likwidacja-top-bara.md — tu tylko UX.

- Górny pasek znika. W lewym górnym rogu zostaje samo logo + strzałka rozwijająca panel boczny, w prawym — sama suma punktów (w trakcie egzaminu obok niej zegar i „zakończ egzamin"). Bez wspólnego paska, bez „⋯", bez podtytułu „tryb ćwiczenia".

- Panel boczny po lewej, otwierany i zamykany tą samą strzałką (plus Esc). Arkusz się nie rusza, a na komputerze nie jest niczym zasłaniany — panel mieści się w marginesie. Na wąskim ekranie nachodzi na zadania: wtedy lekko je przygasza i zamyka się kliknięciem w arkusz. Otwiera się nad oknami z PDF-ami.

- Kolejność i nazwy pozycji w panelu:
  - Tytuł arkusza (nagłówek, nie przycisk)
  - tryb ćwiczenie / tryb egzaminu
  - Otwórz tablicę wzorów
  - Otwórz zasady oceniania
  - Rozpocznij egzamin
    - Zegar: na wierzchu w menu / wył.
    - Wskaźniki samooceny zad. otwartych: wszystkie/wypełnione/wył.
  - Sprawdź wszystkie odpowiedzi
  - Pokaż wszystkie rozwiązania
  - Zresetuj arkusz (zamiast „resetuj punktację" — działanie bez zmian, sama nazwa)
  - ------------- (mała przerwa na pół przycisku)
  - Motyw: jasny/ciemny/auto
  - Punktacja: wł./tylko suma/wył.
  - Pokaż poprawność odpowiedzi: natychmiast/po kliknięciu "sprawdź"
  - Przycisk "zgłoś błąd" pod zadaniem: wł./wył.
  (sub-opcje zegara i wskaźników zawsze widoczne, wcięte pod „Rozpocznij egzamin")

- Wygląd: spójny z resztą strony, ale nowocześniejszy — płynne wysuwanie panelu, obracająca się strzałka, wyraźne grupy. Ikony robię sam jako inline SVG (kreskowe, dziedziczą kolor motywu) — nie musisz nic przygotowywać.
<br>



<br>

TESTOWANIE HENRICH:
- telefon 2024 - wczytuje zadania ale wyświetla błąd. ( issues/zadania-nie-renderuja-sie-mobile.md)

DLA HENRICHA:

- Obczaić analitykę, czyli śledzenie ilości i zaangażowania użytkowników. Warto rozważyć GoatCounter.

- Wykminić, jak zrobić grafiki do dark mode, można np. masowo odwrócić kolory i zmienić krzywą tak, aby zamiast czarnego tła był odpowiedni kolor szarego. (Tańszy tymczasowy fix: CSS filter na `.question img`/wideo — patrz issues/dark-mode-obrazki-wideo.md)

- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

<br>


INNE NOTATKI, DO PRZEKMINIENIA:
- wskaźniki "oceń się" na telefonie powinny być:
  - ALBO: niewidzialne, wtedy opcja w menu powinna być szara z wybranym
  - ALBO: widoczne przyklejone do prawej strony z lekkim marginesem. powinny też być odpowiednio małe aby nie zasłaniały treści.

- Przekminić i dodać zasadę dotyczącą tłumaczenia mi (Henrichowi) rzeczy (jak mam przeprowadzić test, jak wygląda projekt itd.)

- dodanie rozwiązań do matury 2026

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

SONNET DOPISAŁ:
- Uzupełnić `formulasPage` w 2024-grudzień — brakuje w zad. 7, 8, 10, 11, 12, 20 (6 z 35), więc nie mają przycisku „Pokaż potrzebne wzory". Do decyzji merytorycznej: część pewnie faktycznie nie wymaga tablic, ale zad. 8 (otwarte) warto sprawdzić.

- Tryb testowy dla zgłaszania błędów (app/report.js): przycisk „Wyślij zgłoszenie" zamieniony na „Wyślij zgłoszenie lokalnie" (np. pod `?test-zgloszenie=1`, wzorem `?test-egzamin=1`), który loguje payload do konsoli/localStorage zamiast robić fetch do Formspree — żeby testować całą ścieżkę (walidacja, honeypot, throttling, toast) bez zużywania miesięcznego limitu 50 zgłoszeń.

- `#top-bar` powoduje 13 px poziomego scrolla przy szerokości 360 px (pasek ma 373 px). Defekt zastany, potwierdzony pomiarem — znika razem z paskiem w Sesji 2, wpisany jako kryterium akceptacji w issues/likwidacja-top-bara.md.

- Formularz zgłoszenia na telefonie jest wysoki: 8 pigułek kategorii idzie po jednej na wiersz (~340 px), więc obowiązkowe pole opisu jest daleko w dole. Do rozważenia: dwie pigułki w rzędzie, skrócone nazwy albo opis nad kategoriami.

- Link „zgłoś błąd" jest na samym dole karty, a formularz otwiera się nad przyciskami Podpowiedź/Rozwiązanie — czyli powyżej miejsca kliknięcia. Działa, ale warto sprawdzić na żywo, czy ten skok nie dezorientuje; ewentualnie doscrollować formularz do widoku po otwarciu.


ZASADY dla Ciebie Claude:

- tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod DONE/ — patrz DONE/README.md i CLAUDE.md.)

- TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo DONE/, a tu zostaje jedna linijka z odnośnikiem.
 Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole

- Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

- Zadania powinny być oddzielone pustą linijką, chyba, że są to podzadania i składają się na jedno duże zadanie.
