Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do todoDONE.md — patrz CLAUDE.md.)

Zadania realizuj od góry do dołu.

<br>



<h3>DO REALIZACJI DLA FABLE</h3>
Opus, nie ruszaj tego chyba, że cię poproszę w promptcie, możesz zapytać czy to zrobić jeśli nie masz co robić

WYSOKI PRIORYTET:
- (puste — zad 29 „6,50", klatkowanie w Firefoksie i strona arkusza 2026
  zrobione 2026-07-06, patrz todoDONE.md)


NISKI PRIORYTET (drobne porządki, dobre na krótką sesję):
- (dokańczanie arkusza 2026 przeniesione do sekcji Opusa niżej — odpowiedzi w
  exercises.json są już ZWERYFIKOWANE z kluczem CKE i rachunkiem, patrz todoDONE.md,
  więc reszta to robota przepisywacko-składacka)




<br>



<h3>DO REALIZACJI DLA OPUSA</h3>
Fable, nie ruszaj tego chyba, że nie masz co robić.

WYSOKI PRIORYTET:
- (puste — patrz todoDONE.md, sesja 2026-07-06: ekstrakt PDF 2026 + szkielet
  matura-2026-maj/exercises.json + dopisek formatu w zad 10/29 zrobione)

NISKI PRIORYTET:
- Dokończenie arkusza 2026 (strona działa: matura-2026-maj/matematykazen.html;
  odpowiedzi i punktacja w exercises.json zweryfikowane 2026-07-06 z kluczem CKE
  Wersja A + rachunkiem — NIE zmieniaj correctAnswerIndex/blanks/statements/maxScore):
  * hint + solutionText dla 41 wpisów — przepisz/zredaguj z gotowych rozwiązań w
    arkusze PDF/matematyka-2026-maj-matura-podstawowa-odpowiedzi.txt (klucz zawiera
    pełne rozwiązania zadań otwartych; wzory w KaTeX, konwencje jak w arkuszu 2024)
  * obrazki zad 12 (wykres łamanej), 13 (prosta z kątem α), 19 (okrąg A,B,C,D),
    20 (proste równoległe), 31 (diagramy IVA/IVB — dane TYLKO na obrazku) — wyciąć
    z arkusze PDF/matematyka-2026-maj-matura-podstawowa.pdf wzorem zad30
    (pdftoppm -x/-y/-W/-H); docelowe ścieżki matura-2026-maj/zadN/zadNrys.png już są
    w exercises.json. UWAGA: sesja zdalna nie ma pdftoppm/mutool/gs — tylko lokalnie.
- Stworzyć nową stronę z arkuszem matury 2027 (wzorem 2026: folder, exercises.json,
  matematykazen.html z window.SHEET_ID/TABLICE_PDF, link na stronie głównej)
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
  (Automatyczny smoke-test Playwright 2026-07-06 przeszedł cały ten przebieg bez
  błędów — patrz todoDONE.md; to tylko na wyczucie/UX zostaje do Ciebie.)
