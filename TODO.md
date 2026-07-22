Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod DONE/ — patrz DONE/README.md i CLAUDE.md.)
(Zasada: Drogi LLM, Sonnecie, Opusie, Jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole)
Zadania realizuj od góry do dołu.
Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

<br>

<h3>DO REALIZACJI</h3>
Jeżeli nie masz co robić to rób stąd.
- Naprawić włącznie trybu egzaminu który działa tylko raz a potem się blokuje.

- Plan podziału plików (.claude/plans/czy-my-lisz-e-mam-tingly-hamster.md): kroki 1, 1b, 2 i 3 zrobione i zautomatyzowanie zweryfikowane (patrz DONE TODO/03-biezace.md) — zostaje tylko wizualny przegląd kroku 3 przez Henricha (jasny/ciemny motyw, okno ~500px, landing), patrz sekcja „DO SPRAWDZENIA PRZEZ HENRICHA" niżej. Krok 4 zrobiony wcześniej inaczej (katalog nazwano "DONE TODO", nie "DONE"). Krok 5 (script.js → js/) świadomie odłożony, poza zakresem.

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
- Krok 3 podziału plików: style.css → style/ (base/sheet/landing/exam/responsive.css).
  Wszystko co dało się zautomatyzować jest zweryfikowane (node/grep, Playwright: liczba
  zadań, wszystkie widżety, klik ABCD/PF/fillIn, kaskada — computed styles dla jasny/ciemny
  motyw, grid #bar-container na 500px i 1280px, tryb egzaminu, landing). Zostaje sam wygląd —
  otwórz template.html?arkusz=2024-grudzien i sprawdź: jasny i ciemny motyw (⋯ → motyw),
  okno zwężone do ~500px (pasek, karta zadania, przyciski), oraz index.html (landing). Nie
  spodziewam się różnic względem starego style.css — to czysty podział plików (diff to
  potwierdził), ale to jedyna rzecz, której sam nie zweryfikuję.

<br><br><br>


<h3>DO REALZACJI Dopisane przez CLAUDA</h3>

OPUS DOPISAŁ PODCZAS ROBIENIA CODE-REVIEW:
(code review gałęzi claude/do-sprawdzenia-yfi2mu, 2026-07-22 — dark mode + podwojone przyciski egzaminu + żółte wskaźniki. Punkty oznaczone [POTWIERDZONE] odtworzyłem realnie w przeglądarce, reszta z czytania kodu.)

NAJPILNIEJSZE — strona kasuje pracę ucznia:

- [POTWIERDZONE] Znika wpisany tok rozwiązania zadania otwartego. W bloku przywracania postępu (script.js ~1224-1251) `stan.open = zap.open` stoi PO `selfButtons[zap.self].click()`, a ten klik woła `zapiszPostep()`, który serializuje zadanie z jeszcze pustym `stan.open`. Test (2024-grudzien, zadanie 30 = indeks 34, seed `{open:"...", self:3}`): po 1. odświeżeniu w localStorage zostaje samo `{"self":3}` (na ekranie tekst jeszcze jest, więc nikt nie zauważy), po 2. odświeżeniu okienko jest puste. Komentarz dopisany w script.js:1241-1244 opisuje dokładnie ten problem — poprawka wylądowała tylko 8 linijek za nisko.
  * Szerszy wariant tego samego: `zapiszPostep()` zapisuje CAŁĄ tablicę `stanOdpowiedzi`, więc każdy odtwarzający klik utrwala puste stany wszystkich zadań o wyższym indeksie. Traci dane każde zadanie otwarte leżące poniżej ostatniego zadania odtwarzanego kliknięciem.
  * Naprawa obu naraz: wypełnić `stan` danymi z `zap` ZANIM ruszy blok odtwarzających klików (albo wysłać na textarea `new Event("input")` zamiast przypisywać `.value` + `stan.open` ręcznie).

ŻÓŁTE WSKAŹNIKI — nie działają w głównym scenariuszu:

- [POTWIERDZONE] Wskaźniki nie pokazują się, gdy uczeń liczył na kartce. `czyNieoceniony()` (script.js:288-291) wymaga niepustego `stan.open`, ale okienko na tok rozwiązania jest opcjonalne — etykieta pod zadaniem wprost mówi "Rozwiąż na kartce, porównaj z rozwiązaniem i oceń się". Test: egzamin zakończony bez ani jednego wpisu w textarea → zero kropek, `KLUCZ_OCENIANIA` od razu skasowany, mimo że w 2024-grudzien nieocenionych zostaje 7 zadań otwartych. Czyli funkcja nie odpala się dokładnie w tej sytuacji, dla której powstała.

- [POTWIERDZONE] Wskaźniki gubią zadania wypełnione w trakcie fazy "oceń się". Lista liczona jest raz w `pokazWskaznikiOtwarte()` i może już tylko maleć — handler `input` textarea (script.js:850) nie woła `odswiezWskaznikiOtwarte()`, a ta funkcja wyłącznie filtruje. Test: kropka ["26"] → uczeń dopisuje rozwiązanie do zad. 30 → kropki nadal ["26"] → ocenia zad. 26 → kropki [] i `KLUCZ_OCENIANIA` skasowany na stałe. Zad. 30 zostaje wypełnione i nieocenione, bez kropki, a odświeżenie już fazy nie przywróci.

PRZYCISKI W ZŁYCH MIEJSCACH:

- [POTWIERDZONE] Przycisk "rozpocznij próbny egzamin" widoczny na stronie błędu. `#egzamin-start-stopka` nie dostał domyślnego `display: none` (style.css ~1205), w odróżnieniu od `#egzamin-koniec` i `#egzamin-koniec-bar` z grupy w style.css:1167. Test: `template.html?arkusz=nie-ma-takiego` → pod komunikatem "Błędny link" siedzi duży przycisk startu egzaminu; klik kasuje `matematykazen-postep-null` i startuje egzamin na stronie bez zadań. Widoczny też przez cały czas wczytywania exercises.json.

- [POTWIERDZONE] Na telefonie nowy "zakończ egzamin" w pasku wypycha menu ⋯ poza ekran. `#bar-right` ma `flex-wrap: nowrap`, a breakpointy ≤720px/≤560px zmniejszają nowemu przyciskowi tylko font i padding. Test różnicowy przy 360px w trybie egzaminu: prawa krawędź `#menu-button` = 430px przy oknie 360px; po ukryciu samego `#egzamin-koniec-bar` = 328px, czyli mieści się. (Poziome przepełnienie strony przy 360px istniało już wcześniej — ale to ten przycisk wypycha menu poza widok.)

- [POTWIERDZONE] Przełącznik motywu wygląda inaczej niż reszta menu ⋯. `#theme-toggle` nie został dopisany do listy selektorów w style/sheet.css:103 (`#score-switch-button, #show-all-solutions, #reset-scores, #egzamin-start`), a `#bar-menu button` ustawia tylko layout. Zmierzone: `#theme-toggle` → `border: 2px outset`, tło `rgb(240,240,240)`; sąsiedni `#reset-scores` → `border: 2px solid`, tło białe. Czyli szary systemowy przycisk pośród czterech białych z ramką.

TRYB EGZAMINU I PAMIĘĆ PRZEGLĄDARKI:

- Prawdopodobna przyczyna punktu "egzamin działa tylko raz a potem się blokuje" z sekcji DO REALIZACJI. Zwykły cykl start → koniec → start sprawdziłem i działa poprawnie, więc to nie ta ścieżka. Natomiast przy DWÓCH kartach tego samego arkusza: karta A kończy egzamin i usuwa `KLUCZ_EGZAMINU`, po czym karta B zostaje na zawsze w `body.tryb-egzaminu` — `finishExam()` wychodzi od razu na `if (!stan) return;` (script.js:227), więc zegar stoi, rozwiązania/punkty są ukryte, a klik "zakończ egzamin" nic nie robi i nie daje żadnego komunikatu. Ratuje tylko ręczne odświeżenie. Warto sprawdzić, czy tak właśnie to u Ciebie wygląda.

- Nieudany start egzaminu i tak kasuje postęp. `startExamPrompt()` (script.js:202-209) najpierw kasuje `KLUCZ_POSTEPU` i `KLUCZ_OCENIANIA`, a dopiero potem zapisuje `KLUCZ_EGZAMINU`. Gdy `setItem` rzuci (pełna pamięć, tryb prywatny), alert mówi "egzamin nie wystartował", ale postęp jest już bezpowrotnie skasowany. Naprawa: odwrócić kolejność — zapis egzaminu pierwszy, kasowanie dopiero po jego sukcesie.

- "Resetuj punktację" nie kasuje trwającego egzaminu. Handler (script.js:102-109) czyści `KLUCZ_POSTEPU` + `KLUCZ_OCENIANIA`, ale nie `KLUCZ_EGZAMINU`. Przy dwóch kartach można kliknąć reset i po przeładowaniu wylądować w trwającym egzaminie na wyczyszczonym arkuszu, z częściowo zużytym zegarem — czego tekst confirm() w ogóle nie zapowiada.

DARK MODE — WYGLĄD:

- Obrazki CKE i filmy z Manima świecą na biało w ciemnym motywie. Migracja świadomie przypięła `--canvas-bg: #fff` dla płócien widgetów, ale `.question img` (style/sheet.css:293), obrazki kroków i `<video>` nie dostały żadnej reguły tła/filtra — wszystkie PNG w matura/**/ są nieprzezroczyste białe, więc renderują się jako jaskrawe prostokąty na karcie #1b1b1b.

- Dwie zmienne CSS użyte niezgodnie z przeznaczeniem na stronie głównej:
  * `.landing-footer` (style/landing.css:90) bierze kolor tekstu z `--border-close` — tokena ramki krzyżyka paneli. Jego ciemna wartość to #666 na tle #1b1b1b, czyli kontrast 3.0:1, poniżej progu WCAG AA 4.5:1 dla tekstu 13px. Powinien iść przez `--text-faint-*`.
  * `.landing-card` (style/landing.css:63) bierze ramkę z `--bg-hover` — tokena tła hoveru. Powinna iść przez któryś `--border*`.
  * Skutek uboczny obu: przestrojenie krzyżyka paneli PDF po cichu zmienia wygląd strony głównej, a testowany będzie panel, nie landing.

- Kropki "gumkują" przy scrollowaniu. `.wskaznik-otwarte` ma `transition: top 0.12s ease` (style/exam.css:164), a `repozycjonujWskazniki()` przepisuje `top` w każdej klatce rAF — tranzycja restartuje się co klatkę i nigdy nie kończy, więc kropki wloką się za zadaniami i drgają jeszcze ~120ms po zatrzymaniu scrolla. Animacja ma sens tylko dla skokowej repozycji po ocenieniu zadania.

DOKUMENTACJA:

- ARCHITECTURE.md opisuje tylko połowę tej gałęzi. Dark mode udokumentowany wzorowo, ale sekcja "Exam mode" (ARCHITECTURE.md ~80) nadal opisuje kończenie egzaminu wyłącznie przez `#egzamin-koniec` i wymienia dwa klucze localStorage — brak `#egzamin-koniec-bar`, `#egzamin-start-stopka`, trzeciego klucza `KLUCZ_OCENIANIA` i całej fazy "oceń się" ze wskaźnikami. Lista ID "referenced by the inline JS, so keep the IDs stable" (ARCHITECTURE.md ~97) nie zawiera `#egzamin-koniec-bar` ani `#theme-toggle`, więc ktoś restylujący pasek może je skasować jako niepodpięte.

DROBIAZGI (niski priorytet, dziś nieszkodliwe):

- Numer zadania wyciągany regexem `/Zadanie\s*(\d+)/i` (script.js:891) gubi część po kropce — gdyby kiedyś zadanie 12.1 i 12.2 były otwarte (selfScore), dostałyby dwie identyczne kropki "12" z identycznym tooltipem. Dziś nieosiągalne: w obu arkuszach żadne zadanie otwarte nie ma podnumeru. Docelowo lepsze byłoby pole `numer` w exercises.json (przydałoby się też w console.warn w script.js:695 i :1004, które nadal drukują mylące `index + 1`).
- Motyw rozjeżdża się między kartami: `readTheme()` czyta localStorage zamiast stanu, który ta karta faktycznie renderuje, i nikt nie słucha zdarzenia `storage`. Dwie karty potrafią pokazywać różny motyw i różne etykiety przycisku.
- `ustawFazeOceniania()` (script.js:280-285) cicho połyka błędy zapisu — przy zablokowanym localStorage "ukryj wskaźniki" nie utrwala się i kropki wracają po każdym odświeżeniu, bez żadnego komunikatu.