Dziennik ukończonych zadań, partia bieżąca (otwarta 2026-07-27). Zasady formatu i podziału na pliki: patrz DONE/README.md — najnowsze wpisy na górze.

[ZROBIONE 2026-07-28] Transkrypt tablicy wzorów dla modeli — `wybrane_wzory_matematyczne/`
(INDEX.md + 16 plików sekcji, ~780 wzorów ze stron 4–33 PDF-a CKE). Cel: model ładuje jedną
sekcję (300–800 tokenów) zamiast całego PDF-a; „Skorowidz" w INDEX.md mapuje słownictwo zadania
na ID wzoru i stronę, co ma przyspieszyć uzupełnianie `formulasPage`. Ustalenia z Henrichem:
KaTeX w konwencji `\( … \)` / `\[ … \]` identycznej jak w exercises.json (kopiowanie bez konwersji;
`$…$` NIE zadziałałoby — `renderMath` w app/state.js rejestruje tylko te dwa delimitery), pełne
zdania opisowe CKE, pozycja wzoru słownie (góra/środek/dół), sekcja 17 (tablica wartości
trygonometrycznych, s. 34) pominięta, rysunki jako legendy oznaczeń zamiast opisów figur, bez PNG,
bez znaczników podstawa/rozszerzenie. Wyciąg z PDF-a: `pdftohtml -xml` + normalizacja Unicode
Mathematical Italic (U+1D400+) na ASCII — `pdftotext` gubi zmienne i strukturę ułamków.
Weryfikacja: (1) wszystkie 782 wzory renderują się w vendorowanym KaTeX-ie, (2) 26 352 losowych
sprawdzeń numerycznych tożsamości (skrócone mnożenie, potęgi, logarytmy, Newton, Viète, ciągi,
cała trygonometria, tw. sinusów/cosinusów, Heron, pola, wariancja, pochodne) — bez błędu.
Do sprawdzenia wyrywkowego przez Henricha zostają rzeczy nieweryfikowalne liczbowo: definicje
słowne, cechy przystawania/podobieństwa, legendy oznaczeń.

[ODRZUCONE 2026-07-28] Celowanie w konkretny wzór na stronie PDF-a (`#page=N&view=FitH,<top>`
zamiast samego `#page=N`). Zbudowane i przetestowane (współrzędne wzorów z `pdftohtml -xml`,
centrowanie liczone z rozmiaru panelu), po czym wycofane: Firefox i Brave przewijają poprawnie,
ale Chrome i Edge lądują zdecydowanie za nisko — wzoru nie widać. Dodatkowo przy domyślnym
kształcie panelu (28% × 80vh) cała strona i tak mieści się w kadrze przy FitH, więc kotwica
nic by nie dawała bez zmiany proporcji panelu. Ostrzeżenie zostawione w app/panels.js i
ARCHITECTURE.md, żeby nikt nie próbował drugi raz. Pole `formulasY` w exercises.json usunięte.

[ZROBIONE 2026-07-28] Skok formularza „zgłoś błąd" (link na dole karty, formularz otwiera się wyżej,
nad Podpowiedź/Rozwiązanie) — sprawdzone, zachowanie takie samo na desktop i mobile (DOM insertBefore
bez media query), Henrich zaakceptował, bez zmian. [formularz, ui]

[ZROBIONE 2026-07-28] Analityka: GoatCounter wpięty w template.html i index.html
(`data-goatcounter="https://henrich.goatcounter.com/count"`), błąd ładowania skryptu wyciszony
w belce diagnostycznej (adblock/Privacy Badger często go blokują — to nieszkodliwe, nie powinno
straszyć banerem błędu). Potwierdzone przez Henricha na żywo w panelu goatcounter.com — dzisiejsze
odwiedziny się liczą. Do pamiętania przy czytaniu statystyk: część ruchu z adblockami nie zostanie
zliczona, więc realne liczby są wyższe niż panel pokazuje. [analityka, goatcounter]

[ZROBIONE 2026-07-28] Zadania nie renderowały się na telefonie (arkusz 2024-grudzień) — potwierdzone
przez Henricha na żywo, że fix z 2026-07-24 (`.nojekyll` w rootcie, patrz issues/zadania-nie-renderuja-sie-mobile.md)
faktycznie działa na urządzeniu. [mobile, bugfix, github-pages]

[ZROBIONE 2026-07-27] (Sonnet High) „Sprawdź wszystkie odpowiedzi" pomijało zadania z polem tekstowym
+ brak potwierdzenia kliknięcia — pełny spec z (usuniętego) issues/sprawdz-wszystkie-pola-i-komunikat.md,
v0.08. Weryfikacja: Playwright headless, oba motywy, tryb „sprawdź później", brak scrolla 360px.

- REJESTR: `fillIn` i `finalAnswer` dopisane do `oczekujaceSprawdzenia` (app/render.js) obok
  ABCD/PF/multiSelect. `fillIn` — ocena wydzielona do nazwanej `ocenFillIn()` (przycisk „Sprawdź" i
  rejestr wołają tę samą funkcję, zero duplikacji normalizacji/punktacji); `czySprawdzone` czyta klasę
  `correct`/`incorrect` z DOM pierwszego pola (nie flagę) — edycja pola kasuje tę klasę, więc zadanie
  wraca do „niesprawdzone" automatycznie. `finalAnswer` — istniejąca `ocenKoncowaOdpowiedz()` wpisana do
  rejestru z `typ: "finalAnswer"` (znacznik pod bonus niżej). Skutek uboczny świadomie zaakceptowany:
  „sprawdź wszystkie" teraz też PRZYZNAJE PUNKTY za fillIn (dawniej trzeba było kliknąć każdy „Sprawdź").
- BONUS (domyka wpis z TODO.md „ostateczna odpowiedź sprawdza się sama po egzaminie"): `finishExam()`
  (app/exam.js) po zakończeniu egzaminu przelatuje rejestr i woła `ocen()` tylko dla wpisów
  `typ: "finalAnswer"` z niepustą, jeszcze nieodsłoniętą wartością — nie odsłania przy okazji zadań
  zamkniętych, których uczeń nie zdążył sprawdzić.
- KOMUNIKAT „sprawdzono ✓": nowy `<span role="status" aria-live="polite">` przy obu kopiach przycisku.
  Stopka — komunikat `position: absolute` względem nowego `#sprawdz-wszystkie-stopka-wrap` (jak
  `.answer-check-floating`), więc nigdy nie przesuwa przycisku; pod 720px przesuwa się pod przycisk
  (wycentrowany), ale ZOSTAJE `position: absolute` — zmieniają się tylko `left`/`top`/`transform`.
  Panel boczny — tylko glif „✓" (`margin-left: auto` we flexowym `.sidebar-akcja`), bo 260px
  nie mieści zdania; prawdziwy tekst leci do `aria-label`, nie do widocznej treści. Zielony (`--correct`)
  gdy jest cokolwiek zaznaczone (czy to właśnie ocenione, czy już wcześniej sprawdzone), przygaszony
  (`--text-faint`) przy pustym arkuszu — inaczej „sprawdzono" kłamałoby. Znika po ~2,5s przez `opacity`;
  kolejny klik resetuje timer; `prefers-reduced-motion: reduce` bez animacji (dopisane do wspólnego
  bloku w sheet.css). Egzamin: bez zmian — przyciski zostają `disabled` jak dotychczas, więc handler
  (i komunikat) w ogóle się nie odpala.
- POPRAWKA tego samego dnia (zgłoszone przez Henricha na żywo): pierwsza wersja mobilnego fallbacku
  (pod 720px) przełączała komunikat z `position: absolute` na `position: static; display: block` —
  wciągnęło go to z powrotem do flow `#sprawdz-wszystkie-stopka-wrap`, więc nawet PUSTY/niewidoczny
  komunikat (opacity: 0, bez treści) dokładał ~6px wysokości pod przyciskiem przez `margin-top` +
  wysokość pustej linii („sprawdź wszystkie" wyglądało na stałe za grubo na telefonie, nie tylko po
  kliknięciu). Naprawione: mobilny fallback zostaje `position: absolute`, tylko przesunięty pod
  przycisk (`left: 50%; top: 100%; transform: translateX(-50%)`) — zero wysokości w layoucie, kiedy
  komunikat jest pusty. Zweryfikowane Playwright: `bottomDiff` wrappera i przycisku 0px (było 6px).

[ZROBIONE 2026-07-27] (wpis Henricha, przeniesiony z TODO.md 2026-07-27) W trybie ćwiczeń przycisk
„sprawdź wszystkie odpowiedzi" na dole arkusza obok „rozpocznij egzamin", zostaje też w panelu bocznym.
W trybie egzaminu ostatecznie NIE jest niewidoczny, a wyszarzony — zmiana decyzji z 2026-07-26
(znikający przycisk mylił, jakby zniknęła sama funkcja; patrz komentarz przy #sprawdz-wszystkie-stopka
w style/exam.css). Wygląd obu przycisków stopki ujednolicony w sesji „spójność UI" (wpis niżej).

[ZROBIONE 2026-07-27] (Opus High, lokalnie) Trzy drobnice po przeglądzie sesji 1 przez Henricha — v0.07.
Weryfikacja: Playwright, zrzuty light/dark × 1440/1280/390 + pomiary computed style.

- CIENIE: #sidebar traci box-shadow (Henrich: „nie współgrają z logiem ani z kreską"). Panel jest przypięty
  do krawędzi i ma własną kreskę #sidebar-linia, więc cień dublował tę granicę. Panele PDF i toast cień
  ZOSTAWIAJĄ — pływają nad treścią i nie mają żadnej kreski (decyzja Henricha: „tylko panel boczny").
  Token --shadow-panel zostaje w użyciu, tylko bez sidebara.
- STOPKA: #sprawdz-wszystkie-stopka z --text-muted na pełne --text — oba przyciski stopki są teraz
  identyczne, o kolejności czytania decyduje pozycja, nie kontrast (zmierzone: rgb(17,17,17) w light,
  rgb(230,230,230) w dark, oba przyciski).
- TYTUŁ ARKUSZA: .sheet-title-heading dostał max-width: 32% (456px przy 1440px) + margin: 0 auto —
  typowy tytuł CKE zawija się na dwie wyśrodkowane linie zamiast ciągnąć się przez cały ekran.
  Pod 720px ograniczenie zdjęte (max-width: none), bo 32% z 390px zostawiłoby po dwa słowa w linii.
