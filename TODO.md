Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do DONE.md — patrz CLAUDE.md.)
(Zasada: Drogi LLM, Sonnecie, Opusie, Jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole)
Zadania realizuj od góry do dołu.

<br>

NASTAŁA ERA NOWEGO MASTERA BUHAHAHAHAHA

<h3>DO REALIZACJI</h3>
Jeżeli nie masz co robić to rób stąd.

- tryb egzaminu — pasek i stopka (doprecyzowane z Henrichem 2026-07-21, patrz też DONE.md po realizacji):

  * Nowy przycisk "zakończ egzamin" w pasku górnym: w #bar-right, zaraz PO #egzamin-timer (czyli przed #total-score). To DODATKOWY przycisk — istniejący #egzamin-koniec pod ostatnim zadaniem zostaje, nic się nie przenosi.
    - Styl: ramka jak #toggle-tablica (border: 2px solid #e7e7e7; border-radius: 3px; padding ok. 8px 12px; background #fff; cursor: pointer), BEZ sztywnego min-width (etykieta się nie zmienia, to nie jest toggle).
    - Widoczność: tylko gdy body ma klasę tryb-egzaminu — ten sam mechanizm co #egzamin-timer (display: none domyślnie, odkrywane regułą `body.tryb-egzaminu #id`).
    - Zachowanie po kliknięciu: identyczne jak istniejący #egzamin-koniec — ten sam tekst confirm() ("Zakończyć egzamin i zobaczyć wynik?") i to samo wywołanie finishExam(false). Najlepiej podpiąć oba przyciski pod jedną wspólną funkcję/listener, żeby zachowanie nie mogło się kiedyś rozjechać.
    - Ewentualna wąska szerokość ekranu: jeśli przycisk nie mieści się w pasku poniżej 720px, dodać mu analogiczne zmniejszenie jak #total-score dostaje w tym samym @media (max-width: 720px) (font-size: 13px) — ocenić wizualnie po wdrożeniu.

  * Przycisk #egzamin-koniec (ten w stopce, pod ostatnim zadaniem) ma dostać odstęp od góry: zmienić `margin: 0 auto 80px;` na `margin: 40px auto 80px;`.

  * Przycisk "rozpocznij próbny egzamin" ma DODATKOWO (nie zamiast) pojawić się w stopce arkusza, w tym samym miejscu co #egzamin-koniec (pod #exercises-wrapper), ale widoczny odwrotnie — tylko gdy body NIE ma klasy tryb-egzaminu (czyli w trybie ćwiczeniowym). Wersja w rozwijanym menu "⋯" (obecny #egzamin-start) zostaje bez zmian — to nie jest przeniesienie, chcemy przycisk w obu miejscach.
    - Styl: identyczny jak #egzamin-koniec w stopce (ta sama ramka, te same 40px góra / 80px dół marginesu).
    - Zachowanie po kliknięciu: identyczne jak istniejący #egzamin-start (ten sam tekst confirm(), ten sam zapis stanu do localStorage i location.reload()) — wspólna funkcja/listener dla obu przycisków, tak jak wyżej.

- Tytuł arkusza (#exercises-sheet-title) i podtytuł trybu (#exercises-mode-subtitle) mają być nieco niżej w pasku — delikatny nudge, bez zmiany wysokości #top-bar. Dodać `position: relative; top: 5px;` na #bar-center. Jeśli 5px wygląda źle (za mało/za dużo), to jedyna wartość do skorygowania.

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