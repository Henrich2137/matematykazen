Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do DONE.md — patrz CLAUDE.md.)
(Zasada: Drogi LLM, Sonnecie, Opusie, Jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole)
Zadania realizuj od góry do dołu.

<br>

<h3>DO REALIZACJI</h3>
Jeżeli nie masz co robić to rób stąd.
- Naprawić włącznie trybu egzaminu który działa tylko raz a potem się blokuje.

- Flaotujące żółte bomble z numerami zadań do sprawdzenia
  * Mają na sobie złe liczby czasem. Była 24 która dotyczyłą 19stki.
  * przycisk "Ukryj" w lewym dolnym rogu powinien mieć tekst w stylu "Ukryj wskaźniki nieocenionych zadań" i powinien mieć żółty border czy coś

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
- nic