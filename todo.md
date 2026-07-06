Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do todoDONE.md — patrz CLAUDE.md.)

Zadania realizuj od góry do dołu.

<br>



<h3>DO REALIZACJI DLA FABLE</h3>
Opus, nie ruszaj tego chyba, że cię poproszę w promptcie, możesz zapytać czy to zrobić jeśli nie masz co robić

WYSOKI PRIORYTET:
- zad 29 nie akceptuje liczby 6,50 a powinno. Sprawdzić również w zasadach oceniania czy mozna wpisywać ułamki mieszane, jeśli tak to dorobić system odczytu zapisów 6 1/2 (sześć i jedna druga czyli 6,5)

- Strona wydaje się klatkowac podczas przewijania i trwania filmiku. Poszukaj przyczyny. Podejrzewam, że to kwestia płynnego paska postępu filmu to usuń ten bajer lub jeśli masz pomysł jak go łatwo zoptymalizowac to zrób to nie rób kombinacji alpejskich aby to zoptymalizować, nie warto. Dzieje siętak tylko w firefox, moze to jest związane z ustawieniami prywatnosci/bezpieczenstwa jakie tam mam idk.

- przerestrukturyzowanie projektu było to łatwiejsze do pracy. Domyślam się, że wartoby zrobić oddzielny pliki script.js, solutionsInteractive.js,


NISKI PRIORYTET (drobne porządki, dobre na krótką sesję):
- Stworzyć nową stronę z nowym arkuszem matury 2026
- Stworzyć nową stronę z nowym arkuszem matury 2027




<br>



<h3>DO REALIZACJI DLA OPUSA</h3>
Fable, nie ruszaj tego chyba, że nie masz co robić.

WYSOKI PRIORYTET:
- w zad 1 przekleić "Geometrycznie: ∣x+4∣=7∣x+4∣=7 to wszystkie liczby odległe o 7 od liczby −4−4, czyli x1=3x1​=3 i x2=−11x2​=−11. Suma: 3+(−11)=−83+(−11)=−8 — odpowiedź B." do rozwijalnego tekstu ("Pokaż więcej") lub wywalić całkiem albo najlepiej jakoś lepiej opisać pod interaktywnym rozwiązaniem.

- wyciągnięcie tekstu z PDF-ów:
  * matematyka-2026-maj-matura-podstawowa.pdf
  * matematyka-2026-maj-matura-podstawowa-odpowiedzi.pdf

- pozmieniaj nazewnictwo na anglojęzyczne w miejscach takich jak: renderujMatematyke, odczytajEgzamin. Elementy typowo związane z maturą takie jak nazwa folderu arkusze, które i tak w środku są po polsku, możesz zostawić. Nie tłumacz bezpośrednio tylko nazwij to jak programista, podobnie możesz zrobić z innymi amatorskimi nazwami nawet jeśli są jużpo angielsku, w szczególności jeżeli wiesz, że ułatwią pracę LLM.




- w miescach takich jak zad 10 lub 29 dopisać w treści zadania krótki dopisek np. "Odpowiedź podaj jako ułamek dziesiętny z dwiema liczbami po przeciku 3,53"

NISKI PRIORYTET:
- wyciągnięcie tekstu z PDF-ów:
  * matematyka-2025-maj-matura-podstawowa.pdf
  * matematyka-2025-maj-matura-podstawowa-odpowiedzi.pdf
- zmień w css przyciski wyboru ilości punktów ("oceń się") tak aby nie były wiele mniejsze od zwykłych przycisków odpowiedzi
- na bieżąco obliczany procent obok sumy punktów, który świeci się na zielono gdy jest conajmniej 30%, poa najechaniu myszką pokazuje się, zdałeś/nie zdałeś (jeszcze)
- utworzenie zmiennych css i zrobienie przełącznika na darkmode
<br>


NAJNIŻSZY PRIORYTET, NA POTEM:

- DOTYCZĄCE TRYBU PRÓBNY EGZAMIN
   * Przycisk pokaż potrzebne wzory nie powinien się pokazywać, zrób też tak, aby nie było tam przerwy zadużej można wyłączyć div który jest gdzieś wyżej w hierarchi czy coś
   * przycisk opcji "..." po kliknięciu pokazuje pustą ramkę, dobrze aby albo nie było go w ogóle albo był szary lub po rozwinięciu pokazywał zaszarzone te przyciski które nie powinny działać podczas egzaminu.
   * Zadania otwarte np. 30 powinny mieć pole do zanotowania odpowiedzi do samodzielnego sprawdzenia potem.
   * na przycisku "wróć do arkusza
- do sekcji "oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu jak to skomponować aby miało sens.


<br>

DLA UŻYTKOWNIKA:
- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.
- Punkt o widżecie zad 1 urwał się w połowie zdania: "opcjonalnie: sprawić aby przesuwanie" — dokończ myśl, to zostanie zrobione (reszta punktu o zad 1 jest już zrealizowana).

INNE NOTATKI:
- Tryb egzaminu nie powinien być tak "schowany" w opcjach. Przed rozpoczęciem arkusza powinno pytać użytkownika czy chce wejśc w tryb ćwiczeniowy czy egzaminu z checkboxem o zapamiętanie wyboru.
<br><br><br>

<h3>DO WERYFIKACJI PRZEZ HENRICHA</h3>
- Tryb egzaminacyjny (zrealizowany 2026-07-06): sprawdzić cały przebieg — start →
  parę odpowiedzi (ramki powinny być neutralne/niebieskie) → F5 (czy egzamin dalej
  trwa) → "zakończ egzamin" → podsumowanie → samoocena zadania otwartego.
