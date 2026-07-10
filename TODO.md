Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do DONE.md — patrz CLAUDE.md.)
(Zasada: Drogi LLM, Sonnecie, Opusie, Jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole)
Zadania realizuj od góry do dołu.

<br>



<h3>DO REALIZACJI</h3>
Jeżeli nie masz co robić to rób stąd.

WYSOKI PRIORYTET:
- nic

NISKI PRIORYTET (drobne porządki, dobre na krótką sesję):
- (dokańczanie arkusza 2026 przeniesione do sekcji Opusa niżej — odpowiedzi w
  exercises.json są już ZWERYFIKOWANE z kluczem CKE i rachunkiem, patrz DONE.md,
  więc reszta to robota przepisywacko-składacka)
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
   * Przycisk zakończ egzamin powinien znajdować sięna dole strony zamiastt wyczyść wszysktie punkty
- do sekcji "oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu jak to skomponować aby miało sens.


<br>

DLA UŻYTKOWNIKA:
- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.
- Punkt o widżecie zad 1 urwał się w połowie zdania: "opcjonalnie: sprawić aby przesuwanie" — dokończ myśl, to zostanie zrobione (reszta punktu o zad 1 jest już zrealizowana).

<br>

INNE NOTATKI:
- Tryb egzaminu nie powinien być tak "schowany" w opcjach. Przed rozpoczęciem arkusza powinno pytać użytkownika czy chce wejśc w tryb ćwiczeniowy czy egzaminu z checkboxem o zapamiętanie wyboru.
- Etap sprawdzania odpowiedzi po trybie egzaminacyjnym. Idealnie powinien istnieć pomiędzy skończeniem egzaminu, a jego wyników pokazaniem wyników egzaminu.
- Okno potwierdzenia chęci wyczyszczenia punktów
- przycisk wyczyść wszystkie punkty nie powinien chyba być na kończu aby nikt se przez przypadek ni wyczyścił chcąc podsumować
- analogicznie do boxów z punktacją powinny być do włączenia boxy z opisem typu zadania
- okna otwierające pdf zasad oceniania i tablicy wzorów powinny zatrzymywać się nie tylko na lewej krawędzi al równie ż na dole i u góry (zanim schowa się za top-bar)
- na telefonie pdfy się nie ładują (tablica i zasady oceniania). Podczas naprawy warto sprawić aby odpalały się one nie w okienu ale wypełniały całą stronę z krzyżykiem w rogu. Jeżeli nie uda się tego naprawić to należy usunąć tę funkcjonalność z wersji mobilnej.

<br><br><br>

<h3>DO WERYFIKACJI PRZEZ HENRICHA</h3>
- Tryb egzaminacyjny (zrealizowany 2026-07-06): sprawdzić cały przebieg — start →
  parę odpowiedzi (ramki powinny być neutralne/niebieskie) → F5 (czy egzamin dalej
  trwa) → "zakończ egzamin" → podsumowanie → samoocena zadania otwartego.
  (Automatyczny smoke-test Playwright 2026-07-06 przeszedł cały ten przebieg bez
  błędów — patrz DONE.md; to tylko na wyczucie/UX zostaje do Ciebie.)


DO REALZACJI Dopisane przez SONNETA LUB OPUSA:

SONNET DOPISAŁ:
- Naprawa odnośników po ręcznej reorganizacji na foldery matura/<arkusz>/
  (2026-07-10). NIE buduj wspólnego systemu wczytywania arkuszy — to osobne
  zadanie Opusa niżej. Tu chodzi wyłącznie o przywrócenie działania strony
  w OBECNEJ (na razie zdublowanej) strukturze:
  * zmień nazwę root matematykazen.html → template.html (może na razie zostać
    "martwy"/niepodłączony — to surowiec pod zadanie Opusa niżej, nie musi
    samodzielnie działać)
  * matura/2024-grudzien/index.html jest PUSTY (0 bajtów) — wypełnij go treścią
    starego matematykazen.html (patrz historia git) i popraw ścieżki względne:
    style.css, vendor/katex/..., script.js → ../../ ; exercises.json i
    solutionsInteractive.js zostają lokalne (są już w tym folderze)
  * matura/2026-maj/index.html ma już treść, ale ścieżki są napisane tak, jakby
    plik był w rootcie — popraw analogicznie (../../style.css, ../../vendor/...,
    ../../script.js). Ten arkusz NIE ma własnego solutionsInteractive.js —
    sprawdź czy w exercises.json są w ogóle referencje "solutionInteractive" do
    widżetów; jeśli tak, na razie odwołaj się do ../../matura/2024-grudzien/
    solutionsInteractive.js, jeśli nie — pomiń
  * popraw root index.html (landing): linki "matematykazen.html" i
    "matura-2026-maj/matematykazen.html" → matura/2024-grudzien/index.html i
    matura/2026-maj/index.html
  * zgrep'uj cały projekt (też *.md) za starymi nazwami "matematykazen.html" i
    "matura-2026-maj" i popraw bieżące odnośniki w TODO.md/ARCHITECTURE.md;
    wpisy historyczne w DONE.md możesz zostawić bez zmian (opisują przeszłość)
  Cel: oba arkusze klikalne i działające ze strony głównej — duplikacja HTML
  między arkuszami to na razie akceptowalny stan przejściowy.


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


OPUS DOPISAŁ:
- Ujednolicenie renderowania arkuszy w jeden wspólny plik. WARUNEK WSTĘPNY: wymaga
  wykonania zadania "Naprawa odnośników..." wyżej (SONNET DOPISAŁ) — root ma być
  wtedy już template.html, a oba arkusze (matura/2024-grudzien/, matura/2026-maj/)
  mają działać samodzielnie, każdy ze swoim zdublowanym HTML. Jeśli ten punkt nadal
  wisi jako niezrobiony, zapytaj zanim zaczniesz — ta praca na nim bazuje.
  * wybór arkusza przez parametr URL, np. template.html?arkusz=2024-grudzien
    (strona statyczna, brak backendu/przekierowań serwera — patrz CLAUDE.md)
  * DODAJ metadane arkusza WPROST DO KAŻDEGO exercises.json (nowe pola obok
    istniejącej tablicy zadań): tytuł strony, meta description, tekst do
    #exercises-sheet-title, ścieżka+numer strony PDF tablicy wzorów (dziś na
    sztywno jako TABLICE_PDF w script.js:17), ścieżka PDF zasad oceniania (dziś
    na sztywno w #zasady-oceniania w HTML)
  * w script.js, funkcja startSheet() (ok. linii 974-991): zamień
    fetch("exercises.json") na ścieżkę zależną od arkusza z URL
    (matura/<id>/exercises.json) i użyj nowych pól metadanych zamiast
    hardkodowanych stringów w HTML (<title>, meta description, itd.)
  * gdy template.html działa dla obu arkuszy: usuń zdublowane
    matura/2024-grudzien/index.html i matura/2026-maj/index.html; sprawdź czy
    da się scalić solutionsInteractive.js z powrotem do jednego wspólnego pliku
    w rootcie (czy arkusz 2026-maj w ogóle potrzebuje własnych widżetów)
  * popraw linki na stronie głównej (index.html) na template.html?arkusz=...
  * zaktualizuj ARCHITECTURE.md: nowy schemat pól metadanych w exercises.json +
    mechanizm wyboru arkusza (wymóg z CLAUDE.md — trzymać ARCHITECTURE.md w
    sync z tym co faktycznie opisuje)
