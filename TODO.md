Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do DONE.md — patrz CLAUDE.md.)
(Zasada: Drogi LLM, Sonnecie, Opusie, Jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole)
Zadania realizuj od góry do dołu.

<br>

NASTAŁA ERA NOWEGO MASTERA BUHAHAHAHAHA

<h3>DO REALIZACJI</h3>
Jeżeli nie masz co robić to rób stąd.


WYSOKI PRIORYTET:
- Przycisk "zakończ egzamin" powinien znajdować się również na pasku, przy zegarze, nie tylko przy stopce.

- Przycisk "zakończ egzamin" przy stopce powinien mieć margines z góry.

- Przycisk rozpocznij próbny egzamin powinien znajdować na dole ale tylko w trybie ćiwczeniowym

- Spraw aby Tytuł egzaminu oraz podtytuł "tryb ćwiczenia"/"tryb egzaminu" oba były nieco niżej




NISKI PRIORYTET:
- nic (cały poprzedni NISKI PRIORYTET zrobiony przez Opusa 2026-07-17 — patrz DONE.md)


NAJNIŻSZY PRIORYTET, NA POTEM:
Tutaj będą już skonkretyzowane.

- nic

<br>


NIE REALIZUJ:
Nieskonkretyzowane.

- flating żółte wskaźniki po prawej stronie które pokazują otwarte zadania, które zostały wypełnione, ale wymagają zaznaczenia liczby punktów po ukończeniu egzaminu. Wskaźniki powinny mieć gdzieś przycisk który wyłącza je wszystkie. Każy z wskaźników powinien znajdować się przy danym zadaniu lub przyklejać się do góry lub dołu strony w zależniści od tego gdzie trzeba przeskrolować.

- zadania otwarte powinny też mieć okienko normalizujące i sprawdzające wpisaną odpowiedź. Do tego można rozpisać i dorobić donich pytania w stylu "Czy masz opisana długość boku BC?" które wynikająz zasad oceniania i ułatiwają ustalenie ilości punktów. przy nich można dać gwiazdkę, że trzeba każdy przypadek sprawdzić indywidualnie i autor strony nie jest egzaminatorem. 

- utworzenie zmiennych css i zrobienie przełącznika na darkmode

- dodanie rozwiązań do matury 2026

- wyciągnięcie tekstu z PDF-ów:
  * matematyka-2025-maj-matura-podstawowa.pdf
  * matematyka-2025-maj-matura-podstawowa-odpowiedzi.pdf

- do sekcji "oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu jak to skomponować aby miało sens.

- dodać w opcjach toggle "pokaż poprawnośc odpowiedzi natychmiast po zaznaczeniu" oraz gdy jest wyłączony to musi być widać
  * przycisk sprawdź po wybraniu odpowiedzi po prawej stronie, tak aby nie zmieniało wysokości diva/strony. Przycisk po kliknięciu powinien: włączyć kolory ramek w zależności od odpowiedzi takie jakie są obecnie, zniknąć.  
  * przycisk "sprawdź wszystkie odpowiedzi" na dole arkusza oraz w ustawieniach powinien widnieć.




<br>

DLA UŻYTKOWNIKA:

- POTESTOWAĆ TO CO POZMIENIAŁ OPUS (ZAPISANE W DONE.md) i ZMERGOWAĆ Z MASTEREM 

- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

- Punkt o widżecie zad 1 urwał się w połowie zdania: "opcjonalnie: sprawić aby przesuwanie" — dokończ myśl, to zostanie zrobione (reszta punktu o zad 1 jest już zrealizowana).

<br>

INNE NOTATKI:

- Obczaić analitykę czyli śledzenie ilości i zaangażowania użytkowników (moze da sięjakoś przez githuba)

- Stworzyć przycisk "zgłoś błąd w zadaniu" i odpowiedni formularz

- Tryb egzaminu nie powinien być tak "schowany" w opcjach. Przed rozpoczęciem arkusza powinno pytać użytkownika czy chce wejść w tryb ćwiczeniowy czy egzaminu z checkboxem o zapamiętanie wyboru.

- Etap sprawdzania odpowiedzi po trybie egzaminacyjnym. Idealnie powinien istnieć pomiędzy skończeniem egzaminu, a jego wyników pokazaniem wyników egzaminu.

- analogicznie do boxów z punktacją powinny być do włączenia boxy z opisem typu zadania

- na telefonie pdfy się nie ładują (tablica i zasady oceniania). Podczas naprawy warto sprawić aby odpalały się one nie w okienku ale wypełniały całą stronę z krzyżykiem w rogu. Jeżeli nie uda się tego naprawić to należy usunąć tę funkcjonalność z wersji mobilnej.

<br><br><br>


<h3>DO WERYFIKACJI PRZEZ HENRICHA</h3>
- Tryb egzaminacyjny (zrealizowany 2026-07-06): sprawdzić cały przebieg — start →
  parę odpowiedzi (ramki powinny być neutralne/niebieskie) → F5 (czy egzamin dalej
  trwa) → "zakończ egzamin" → podsumowanie → samoocena zadania otwartego.
  (Automatyczny smoke-test Playwright 2026-07-06 przeszedł cały ten przebieg bez
  błędów — patrz DONE.md; to tylko na wyczucie/UX zostaje do Ciebie.)


DO REALZACJI Dopisane przez SONNETA LUB OPUSA:

SONNET DOPISAŁ:
- Dokończenie arkusza 2026 (otwórz przez template.html?arkusz=2026-maj; dane w
  matura/2026-maj/exercises.json — teraz obiekt { meta, exercises }; odpowiedzi i
  punktacja zweryfikowane 2026-07-06 z kluczem CKE Wersja A + rachunkiem — NIE
  zmieniaj correctAnswerIndex/blanks/statements/maxScore):
  * hint + solutionText dla 41 wpisów — przepisz/zredaguj z gotowych rozwiązań w
    matura/2026-maj/matematyka-2026-maj-matura-podstawowa-odpowiedzi.txt (klucz
    zawiera pełne rozwiązania zadań otwartych; wzory w KaTeX, konwencje jak w 2024)
  * obrazki zad 12 (wykres łamanej), 13 (prosta z kątem α), 19 (okrąg A,B,C,D),
    20 (proste równoległe), 31 (diagramy IVA/IVB — dane TYLKO na obrazku) — wyciąć
    z matura/2026-maj/matematyka-2026-maj-matura-podstawowa.pdf wzorem zad30
    (pdftoppm -x/-y/-W/-H). Docelowe ścieżki (już w exercises.json, konwencja media/):
    matura/2026-maj/media/zadN/zadNrys.png. UWAGA: sesja zdalna nie ma
    pdftoppm/mutool/gs — tylko lokalnie.



