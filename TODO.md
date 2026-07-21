Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do DONE.md — patrz CLAUDE.md.)
(Zasada: Drogi LLM, Sonnecie, Opusie, Jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole)
Zadania realizuj od góry do dołu.

<br>

NASTAŁA ERA NOWEGO MASTERA BUHAHAHAHAHA

<h3>DO REALIZACJI</h3>
Jeżeli nie masz co robić to rób stąd.

- utworzenie zmiennych css, dodanie Darkmode i zrobienie przełącznika do niego (doprecyzowane 2026-07-21). Etap 1 = sama infrastruktura:
  * Wprowadzić CSS custom properties na kolory (tło, tekst, ramki, akcenty) w :root i przepiąć na nie style.css.
  * Ciemna paleta pod `@media (prefers-color-scheme: dark)` + nadpisanie klasą na <html>/<body> (żeby przełącznik miał pierwszeństwo nad systemem).
  * Przełącznik trybu zapamiętywany w localStorage. Umiejscowienie/wygląd przełącznika do uznania Opusa.

- (tryb egzaminu) minimalistyczne pływające żółte wskaźniki nieocenionych zadań otwartych (doprecyzowane 2026-07-21). Kiedy: TYLKO po zakończeniu egzaminu (faza "egzamin zakończony, oceń się"), dla zadań otwartych (selfScore) wypełnionych, ale bez uzupełnionego self-score; znikają po ocenieniu danego zadania. W trakcie egzaminu ich nie ma. Reszta (dokładny wygląd, sticky góra/dół przy scrollu, przycisk wyłączający wszystkie) — do uznania Opusa wg oryginalnego opisu poniżej:
  * Stwórz minimalistyczne flating żółte wskaźniki po prawej stronie które pokazują otwarte zadania, które zostały wypełnione, ale wymagają zaznaczenia liczby punktów po ukończeniu egzaminu. Mają znajdować się w kolumnie. Wskaźniki powinny mieć gdzieś przycisk który wyłącza je wszystkie. Każdy z wskaźników powinien znajdować się przy danym zadaniu lub przyklejać się do góry lub dołu strony w zależności od tego gdzie trzeba przeskrolować.




<br>


NIE REALIZUJ
czyli nieskonkretyzowane

- Stworzyć przycisk "zgłoś błąd w zadaniu" i odpowiedni formularz

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


INNE NOTATKI:s

- Tryb egzaminu nie powinien być tak "schowany" w opcjach. Moze pod tytułem zrobić zamiast stałego napisu "tryb ćwiczeniowy" zrobić toggle między dwoma trybami.

- na telefonie pdfy się nie ładują (tablica i zasady oceniania). Podczas naprawy warto sprawić aby odpalały się one nie w okienku ale wypełniały całą stronę z krzyżykiem w rogu. Jeżeli nie uda się tego naprawić to należy usunąć tę funkcjonalność z wersji mobilnej.

- ZMIANA UI: Wywalić top-bar i przenieśc wszystko na rozwijany pasek boczny po lewej który można łatwo schować, aby widzieć tylko zadania i włączone elementy takie jak tablica, punktacja itd.


<br><br><br>


DO SPRAWDZENIA PRZEZ HENRICHA.
Claudzie, możesz tutaj dopisywać rzeczy które mam sprawdzić/przetestować.
- nic