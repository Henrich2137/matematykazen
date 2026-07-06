Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do todoDONE.md — patrz CLAUDE.md.)

Zadania realizuj od góry do dołu.

<br>



<h3>DO REALIZACJI DLA FABLE</h3>
Opus, nie ruszaj tego chyba, że cię poproszę w promptcie, możesz zapytać czy to zrobić jeśli nie masz co robić

WYSOKI PRIORYTET:
- zad 29 nie akceptuje liczby 6,50 a powinno. Sprawdzić również w zasadach oceniania czy mozna wpisywać ułamki mieszane, jeśli tak to dorobić system odczytu zapisów 6 1/2 (sześć i jedna druga czyli 6,5)

- Strona wydaje się klatkowac podczas przewijania i trwania filmiku. Poszukaj przyczyny. Podejrzewam, że to kwestia płynnego paska postępu filmu to usuń ten bajer lub jeśli masz pomysł jak go łatwo zoptymalizowac to zrób to nie rób kombinacji alpejskich aby to zoptymalizować, nie warto. Dzieje siętak tylko w firefox, moze to jest związane z ustawieniami prywatnosci/bezpieczenstwa jakie tam mam idk.


NISKI PRIORYTET (drobne porządki, dobre na krótką sesję):
- Stworzyć nową stronę z nowym arkuszem matury 2026 — szkielet danych już gotowy:
  matura-2026-maj/exercises.json (41 wpisów, wszystkie 33 zadania, suma punktów = 50,
  wszystkie wzory KaTeX zweryfikowane przez katex.renderToString, patrz todoDONE.md).
  Brakuje: hint/solutionText/solutionStepByStep/solutionInteractive (celowo puste —
  do dorobienia), formulasPage (numery stron w wybrane_wzory_matematyczne.pdf), oraz
  obrazki/wykresy dla zadań 12 (wykres funkcji łamanej), 13 (wykres funkcji liniowej
  z kątem α), 19 (okrąg z punktami A,B,C,D), 20 (proste równoległe k,l,m,n) i 31
  (dwa diagramy słupkowe klasa IVA/IVB — dane WYŁĄCZNIE na obrazku, bez niego zadanie
  31 nie da się zweryfikować/rozwiązać) — trzeba je wyciąć z arkusze PDF/matematyka-
  2026-maj-matura-podstawowa.pdf (wzorem zad30 z arkusza 2024: pdftoppm -x/-y/-W/-H).
  Brakuje też matematykazen.html/script.js/style.css dla tej strony (folder ma na
  razie tylko exercises.json).
- Stworzyć nową stronę z nowym arkuszem matury 2027




<br>



<h3>DO REALIZACJI DLA OPUSA</h3>
Fable, nie ruszaj tego chyba, że nie masz co robić.

WYSOKI PRIORYTET:
- (puste — patrz todoDONE.md, sesja 2026-07-06: ekstrakt PDF 2026 + szkielet
  matura-2026-maj/exercises.json + dopisek formatu w zad 10/29 zrobione)

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
