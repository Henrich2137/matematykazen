BIEZACA PARTIA ZROBIONYCH PUNKTOW TODO (otwarta). Tu trafiaja wpisy [DONE]/[ZROBIONE]
przenoszone z TODO.md. Nie wczytuj tego pliku domyslnie - tylko gdy potrzebne jest szersze
spojrzenie na projekt, rozwiazanie trudniejszego problemu albo sprawdzenie, czy/jak cos juz
kiedys rozwiazano. Zasada podzialu i indeks: DONE/README.md.
Zakres: 2026-07-13 (WYSOKI PRIORYTET) - 2026-07-21. Partia jeszcze niezmergowana do mastera.

[ZROBIONE] (2026-07-24, Sonnet) — dwie karty tego samego arkusza blokujące „zakończ egzamin"
(issues/dwie-karty-tryb-egzaminu.md): dodano nasłuch zdarzenia `storage` w app/exam.js — gdy
karta A usunie KLUCZ_EGZAMINU (koniec egzaminu), inne otwarte karty tego samego arkusza dostają
zdarzenie `storage` (odpala się tylko w INNYCH kartach), przestają tykać zegar i pokazują nakładkę
„Egzamin zakończony w innej karcie" z przyciskiem `location.reload()` zamiast próbować dorenderować
podsumowanie z własnych (mogących się różnić) danych w pamięci. CSS: #egzamin-odswiez dopisany do
selektora stylującego przycisk w style/exam.css. Zweryfikowane Playwrightem (dwie karty w jednym
kontekście przeglądarki: start w karcie A → reload karty B → koniec w karcie A → karta B bez
odświeżenia pokazuje komunikat → klik „odśwież" wyprowadza z trybu egzaminu, 0 błędów JS w konsoli).
Przy okazji uzupełniono ARCHITECTURE.md (sekcja „Exam mode"): #egzamin-koniec-bar,
#egzamin-start-stopka, KLUCZ_OCENIANIA, faza „oceń się" i mechanizm synchronizacji między kartami
(issues/dokumentacja-exam-mode-luka.md — lista „stabilnych ID" wspomniana w issue już nie istnieje
w pliku, więc ten podpunkt issue jest nieaktualny/pominięty).

[ZROBIONE] (2026-07-24, Sonnet) — 7 POPRAWEK Z „DLA SONNETA NA EFFORT HIGH" (TODO.md), zrealizowane
po kolei w jednej sesji, node --check na wszystkich zmienionych plikach JS (report.js, indicators.js,
theme.js, render.js) — build/testów brak w projekcie, dalsza weryfikacja wizualna w przeglądarce
zalecana Henrichowi:
1. Link „zgłoś błąd w tym zadaniu” → tekst skrócony do „zgłoś błąd” (app/report.js) i wyśrodkowany
   (text-align: center na .report-error-link, style/sheet.css).
2. Landing CSS: .landing-card border → var(--border) (było var(--bg-hover), token hover-tła nie do
   ramek); .landing-footer color → var(--text-faint) (było var(--border-close), 3.0:1 w dark mode,
   poniżej WCAG AA) [css, kontrast, landing] — issues/dark-mode-css-zmienne-landing.md.
3. Kropki wskaźników „oceń się” gumkowały przy scrollu — transition: top restartował się co klatkę
   rAF w repozycjonujWskazniki(). Nowa klasa body.wskazniki-scroll-aktywny (style/exam.css) wyłącza
   transition na czas aktywnego scrolla; dodaje/zdejmuje ją app/indicators.js (oznaczScrollAktywny(),
   debounce 150ms po ostatnim scroll evencie, celowo bez scrollend dla zgodności przeglądarek)
   [css, egzamin, scroll] — issues/dark-mode-wskazniki-scroll.md.
4. Cichy błąd zapisu w ustawFazeOceniania() (app/indicators.js) — catch teraz woła
   pokazZglosToast("nie udało się zapisać ustawienia", true) zamiast połykać błąd localStorage
   [localStorage, ui] — issues/ocenianie-cichy-blad-zapisu.md.
5. Wskaźniki „oceń się” znikały po odświeżeniu strony w trakcie fazy oceniania — pokazWskaznikiOtwarte()
   gasiło fazę zanim zadaniaOtwarte zdążyło się wypełnić przy starcie strony (lista pusta na starcie).
   Teraz gasi fazę tylko gdy body.arkusz-wczytany (klasa z app/render.js) — inaczej zwraca bez gaszenia,
   a startSheet() odtwarza wskaźniki poprawnie po renderze [egzamin, bugfix] —
   issues/wskazniki-reload-faza-oceniania.md.
6. Motyw jasny/ciemny rozjeżdżał się między kartami przeglądarki tej samej strony — app/theme.js
   nasłuchuje teraz window "storage" (KLUCZ_MOTYWU) i przy zmianie w innej karcie woła
   applyTheme(readTheme()) [motyw, cross-tab] — issues/motyw-rozjezdza-sie-miedzy-kartami.md. Zakres
   celowo zawężony do motywu (bez ogólnego cross-tab helpera) — analogiczny problem dla trybu
   egzaminu (issues/dwie-karty-tryb-egzaminu.md) NIE ruszony.
7. Numer zadania gubił podnumer (12.1 vs 12.2 → oba „12”) — regex w app/render.js zmieniony z
   /Zadanie\s*(\d+)/i na /Zadanie\s*([\d.]+)/i (łapie pełny numer z podnumerem). Dodana funkcja
   numerZadania(exercise, index), użyta też w dwóch console.warn (correctAnswerIndex poza zakresem,
   nieznany widżet), które wcześniej mylnie drukowały index+1 zamiast prawdziwego numeru CKE.
   Sprawdzone: nic w app/indicators.js ani app/report.js nie zakłada, że numer jest liczbą całkowitą
   (używany wyłącznie do wyświetlania) — bez zmian w exercises.json [bugfix, regex] —
   issues/numer-zadania-podnumer.md.

[ZROBIONE] (2026-07-24, Opus) — „ZGŁOŚ BŁĄD W ZADANIU" (TODO.md, „Dla Opusa na effort High").
Nowy plik app/report.js (ładowany w template.html tuż PRZED render.js, bo loadExercises woła
z niego dodajLinkZgloszenia). Pod każdym zadaniem dyskretny link tekstowy .report-error-link
(„zgłoś błąd w tym zadaniu", numer zadania z treści przez /Zadanie (\d+)/, jak wskaźniki
„oceń się"). Klik otwiera JEDEN wspólny modal (#zglos-blad-overlay, statyczny w template.html,
styl jak #egzamin-podsumowanie; JS wypełnia numer zadania i podgląd danych). Toggle w menu ⋯
(#zglos-blad-toggle) — globalny (localStorage matematykazen-zglaszanie-bledow, bez sufiksu
arkusza, tylko „0" wyłącza; wzorem #natychmiastowa-toggle), chowa linki przez body.bez-zglaszania.
Wysyłka do Formspree fetchem (AJAX, bez reloadu). BLOKER: FORMSPREE_ENDPOINT na górze report.js
to PLACEHOLDER „TODO-WKLEJ-ENDPOINT-FORMSPREE" — Henrich musi założyć konto na formspree.io i
wkleić adres https://formspree.io/f/xxxxxxxx; do tego czasu submit pokazuje jasny toast „nie
skonfigurowane" (regex na endpoint), NIE ustawia throttlingu. Wszystkie pola OPCJONALNE (opis +
e-mail, oba oznaczone „(opcjonalnie)"), pusty submit z samymi auto-danymi też działa. Auto-dane
(user nic nie wpisuje): numer zadania, SHEET_ID, location.href, efektywny motyw (aktualnyMotyw:
rozróżnia ręczny jasny/ciemny od auto i co auto realnie znaczy), tryb egzamin/ćwiczenia,
navigator.userAgent, cała zawartość localStorage (JSON.stringify wszystkich kluczy) — pokazane
w rozwijanym <details> dla transparentności. Antyspam: honeypot input[name=_gotcha] (natywny w
Formspree), ukryty off-screen przez CSS (.zglos-blad-hp left:-9999px, NIE display:none, żeby
boty go wypełniały) — wypełniony = udajemy sukces i nic nie wysyłamy; + throttling raz/min
(matematykazen-zglos-ostatnia, chroni limit 50/mies. free tier), znacznik ustawiany tylko gdy
żądanie DOTARŁO do serwera (nie przy błędzie sieci ani placeholderze). Toast (.zglos-toast,
zielona ramka --correct = sukces „Dziękujemy, zgłoszenie wysłane", czerwona --incorrect = błąd)
— osobne komunikaty dla res.ok, non-ok (np. 429 = limit), błędu sieci, throttlingu i placeholdera;
nigdy cicha porażka. Cały nowy CSS (sekcja na dole style/sheet.css) używa WYŁĄCZNIE zmiennych z
base.css → jasny i ciemny motyw działają automatycznie. Testy Playwright (2024-grudzien, 28
asercji): link pod każdym zadaniem, modal, auto-dane, honeypot off-screen + wypełniony,
placeholder-submit, Escape, toggle+persist+reload, throttling, dark mode (kolor z var), tryb
egzaminu (link działa, tryb w danych), oraz z zamockowanym endpointem: POST z właściwymi polami
+ toast sukcesu + throttle set, oraz 429 → toast błędu, modal zostaje otwarty. Do zweryfikowania
przez Henricha po wklejeniu prawdziwego endpointu: realna wysyłka i e-mail powiadomienia.
Dokumentacja: ARCHITECTURE.md (nowa sekcja „Zgłaszanie błędów"), ARCHITECTURE_CSS.md, CLAUDE.md
(kolejność ładowania app/*.js).

[ZROBIONE] (2026-07-24, Sonnet) — TOGGLE „WIDOCZNOŚĆ ZEGARA" W MENU EGZAMINU (TODO.md
„Dla Sonneta" → tryb egzaminu; issues/egzamin-zegar-toggle.md, teraz usunięty). Nowy
przycisk `#zegar-toggle` w `#bar-menu` (template.html), wzorowany 1:1 na
`#natychmiastowa-toggle`: `KLUCZ_ZEGAR_WIDOCZNY` + `czyZegarWidoczny()` w app/state.js
(GLOBALNE ustawienie w localStorage, bez sufiksu SHEET_ID — brak wpisu = domyślnie
widoczny, tylko jawne "0" wyłącza). `odswiezWidocznoscZegara()` w app/exam.js przełącza
klasę `.zegar-ukryty` na `#egzamin-timer` i etykietę przycisku; wołana raz na starcie i po
kliknięciu. CSS: `body.tryb-egzaminu #egzamin-timer.zegar-ukryty { display: none; }`
(exam.css) — sam zegar (tickExam) dalej tyka i kończy egzamin po czasie w tle, toggle
zmienia tylko widoczność spana. W odróżnieniu od reszty opcji menu (`OPCJE_MENU_EGZAMIN`),
`#zegar-toggle` NIE jest blokowany w trakcie egzaminu — to jedyny sensowny moment na jego
użycie. Sprawdzone Playwright: etykieta przed/po starcie egzaminu, toggle chowa/pokazuje
`#egzamin-timer` (computed display), zegar dalej tyka (tekst zmienia się mimo ukrycia),
ustawienie przetrwało reload strony.

[ZROBIONE] (2026-07-24, Sonnet) — „ROZPOCZNIJ PRÓBNY EGZAMIN" W MENU UKRYTY PRZED
WCZYTANIEM ARKUSZA (TODO.md „Dla Sonneta" → tryb egzaminu, „minor thing"). Kopia przycisku
w stopce (`#egzamin-start-stopka`) już była gated przez `body.arkusz-wczytany`, ale wersja
w menu ⋯ (`#egzamin-start`) nie — pokazywała się nawet na stronie „Błędny link" (zły
`?arkusz=`). Dodano w exam.css `#bar-menu #egzamin-start { display: none; }` + `body.
arkusz-wczytany #bar-menu #egzamin-start { display: block; }`. Podwójny `#id` w selektorze
celowy: samo `#egzamin-start` ma niższą specyficzność niż `#bar-menu button` (sheet.css,
`display: block`) i przegrywało mimo że exam.css ładuje się później — specyficzność liczy
się przed kolejnością źródłową. Przycisk zostaje widoczny (wyszarzony) W TRAKCIE egzaminu,
tak jak wcześniej (setExamMenuDisabled() w app/exam.js) — reguła ujawnienia nie ma
`:not(.tryb-egzaminu)`. Sprawdzone Playwright: strona błędnego linku (menu bez przycisku),
normalny arkusz (przycisk widoczny), w trakcie egzaminu (widoczny, disabled=true).

[ZROBIONE] (2026-07-24, Sonnet) — TABLICA WZORÓW ZAMYKA SIĘ AUTOMATYCZNIE PO EGZAMINIE
(TODO.md „Dla Sonneta" → tryb egzaminu; issues/egzamin-tablica-auto-zamkniecie.md, teraz
usunięty). Panel `#tablica-wzorow-panel` zostawał otwarty (i przycisk z etykietą „▲
Schowaj…") także w fazie „oceń się" po zakończeniu egzaminu, mimo że sam tryb egzaminu
się kończył. `finishExam()` (app/exam.js) dostał, tuż po zdjęciu klasy
`body.tryb-egzaminu`, sprawdzenie `tablicaPanel.style.display === "block"` i wywołanie
`hideFormulasPanel()` (z app/panels.js — mimo że panels.js ładuje się PO exam.js,
finishExam() wykonuje się dopiero po kliknięciu użytkownika, długo po tym jak wszystkie
skrypty się już załadowały, więc funkcja jest dostępna). Sprawdzone Playwright: start
egzaminu → otwarcie tablicy z menu → „zakończ egzamin” → panel `display:none`, a etykieta
przycisku wraca do „▼ Pokaż tablice wzorów” (nie tylko display, cały stan przez
hideFormulasPanel, nie ręczny reset style.display).

[ZROBIONE] (2026-07-24, Sonnet) — #toggle-tablica/#toggle-zasady NA STAŁE W MENU ⋯
(TODO.md „Dla Sonneta"; issues/pasek-przyciski-do-menu.md, teraz usunięty). Oba przyciski
przeniesione z #bar-left/#bar-right (template.html) do #bar-menu, zawsze — bez różnicy
desktop/telefon, bez media query. app/panels.js odwołuje się do nich przez
getElementById, więc przeniesienie w DOM nie wymagało zmian w JS. CSS: dopisane do
wspólnego selektora przycisków menu (sheet.css, obok #theme-toggle itd.), usunięta stara
reguła #toggle-tablica/#toggle-zasady z min-width:200px (zbędna — #bar-menu button ma
width:100%) oraz odpowiadający jej reset w responsive.css (@720px). To zastępuje też
ogólniejszy punkt „przyciski niemieszczące się na pasku trafiają do menu" — po tej
zmianie na pasku zostały tylko tytuł/wynik/⋯, które się zawsze mieszczą. Sprawdzone
Playwright na desktop (1280px) i telefonie (400px): pasek bez zbędnych przycisków, menu
otwiera oba toggle'e ze spójnym stylem, kliknięcie „pokaż tablice wzorów" z menu nadal
otwiera panel PDF. Zaktualizowano ARCHITECTURE_CSS.md (opis #bar-left/#bar-right/#bar-menu,
usunięte nieaktualne wzmianki o min-width:200px).

[ZROBIONE] (2026-07-24, Sonnet) — STYL PRZYCISKÓW MENU + WYRÓWNANIE „SPRAWDŹ" (TODO.md
„Dla Sonneta"). (1) #natychmiastowa-toggle i #sprawdz-wszystkie brakowały we wspólnym
selektorze stylującym przyciski #bar-menu (sheet.css ~103-110 obok #theme-toggle itd.) i
renderowały się jako gołe przyciski przeglądarki — dopisane do tego selektora. (2)
.button-container .answer-check-floating (pływający przycisk „sprawdź") miał top:0
względem .answers-container, a przyciski odpowiedzi mają margin-top:8px — przez to
„sprawdź" wisiał 8px wyżej. Zmiana top:0 → top:8px wyrównuje górne krawędzie (sprawdzone
bounding-boxami w Playwright, desktop i ≤900px flow-layout).

[ZROBIONE] (2026-07-23, Opus) — TOGGLE „natychmiastowa poprawność" + przyciski „sprawdź"
(TODO.md: „dodać w opcjach toggle …"). Nowe ustawienie GLOBALNE (localStorage
`matematykazen-natychmiastowa-poprawnosc`, bez sufiksu arkusza; state.js:
czyNatychmiastowaPoprawnosc/natychmiastowaOcenaAktywna + rejestr oczekujaceSprawdzenia).
Dotyczy TYLKO zadań zamkniętych ABCD/PF/multiSelect (fillIn ma swój „Sprawdź" — nietknięty).
ON (domyślnie) = klik odpowiedzi od razu koloruje (dawne zachowanie). OFF = klik daje tylko
neutralne .selected, a po prawej ramki odpowiedzi pojawia się pływający przycisk „sprawdź"
(render.js: utworzPrzyciskSprawdz — position:absolute względem .answers-container, left:100%,
nie zmienia wysokości zadania; na ≤900px wraca do flow). Klik „sprawdź" odsłania ocenę i
znika. Każda gałąź zamknięta ma teraz ocen*(): idempotentne odsłonięcie na podstawie
zapisanego wyboru; w trybie egzaminu natychmiastowaOcenaAktywna() wymusza ON (kolory i tak
schowane przez exam.css), więc przycisków „sprawdź" na egzaminie nie ma. Zapis stan.sprawdzone
w localStorage → po reloadzie odsłonięte zadania zostają pokolorowane i z punktami, a
zaznaczone-lecz-niesprawdzone wracają jako neutralne z przyciskiem „sprawdź" (bez fałszywych
punktów). „Sprawdź wszystkie odpowiedzi" w menu ⋯ i w stopce arkusza (bootstrap.js:
sprawdzWszystkieOdpowiedzi) — odsłania wszystkie zaznaczone-a-niesprawdzone; oba przyciski
widoczne tylko w trybie OFF (body.reczne-sprawdzanie) i poza egzaminem. Testy Playwright
(2024-grudzien): ON/OFF ABCD, zmiana wyboru bez kolorowania, „sprawdź" indywidualny, „sprawdź
wszystkie" na ABCD+PF+multi (3 pending → wszystkie pokolorowane), fillIn nietknięty, brak
kolizji z egzaminem, reload w obu stanach — wszystko OK.

[ZROBIONE] (2026-07-23, Opus) — POZYCJA/WARSTWY WSKAŹNIKÓW „OCEŃ SIĘ" (TODO.md: „wskaźniki
zadań do samodzielnej oceny"). (1) Kolumna kropek odsunięta od krawędzi: .wskaznik-otwarte
right 14px → 70px (nie nachodzi na scrollbar ani na typowych szerokościach na kolumnę
punktacji). (2) Przycisk „ukryj" przeniesiony z lewego dolnego rogu w prawy dolny róg,
OBOK kolumny kropek: #wskazniki-ukryj left:10px → right:96px (na lewo od kropek przy
right:70px, więc bez nakładania — sprawdzone bounding-boxami), bottom:10px bez zmian; logika
pionowego rozstawiania (declutter + `dol`) w repozycjonujWskazniki() NIETKNIĘTA, kropki dalej
schodzą blisko dołu. (3) z-index kropek i przycisku 15 → 8: CELOWO poniżej panelu tablicy
wzorów (#tablica-wzorow-panel z-index 9), więc otwarta tablica przykrywa kropki. UWAGA: TODO
zakładało panel z-index 11 nad paskiem — realnie panel to 9, „tuż pod paskiem" (top-bar 10,
udokumentowane w ARCHITECTURE_CSS.md), więc „kropki nad paskiem, pod panelem" jest
niewykonalne bez ruszania warstw paska/menu; że kropki są też pod paskiem (10) nie ma
znaczenia wizualnego — declutter i tak klamruje każdą kropkę do pasa POD paskiem. (4) Tekst
przycisku skrócony na „Ukryj wskaźniki" (indicators.js). Testy Playwright: pełny próbny
egzamin → faza „oceń się" (7 kropek), brak nakładania przycisk↔kropki, tablica przykrywa
kropki, scroll/resize dalej repozycjonuje (bug „gumkowania" z issues/ NIE pogłębiony —
transition bez zmian).

[ZROBIONE] (2026-07-23, Opus) — PODZIAŁ script.js NA app/*.js (wariant C z planu
"joyful-river"). Stary script.js (1446 linii) rozbity na 9 klasycznych skryptów w
nowym katalogu app/ (nazwy angielskie, jak style/*.css): state.js (globalne +
mediaPath/renderMath + rejestry wszystkieRozwiazania/zadaniaOtwarte), theme.js,
exam.js (tryb egzaminu + timer, wraz z „if readExamState → enableExamMode"),
indicators.js (wskaźniki „oceń się"), panels.js (panele PDF + openFormulasAtPage),
answers.js (normalizeAnswer + markCorrectAnswer), steps.js (podsystem kroków —
renderStep/showStep/podepnijSterowanieWideo wydzielony z loadExercises; wspólny stan
currentStep/stepSwapToken i refy DOM przekazywane JAWNIE w obiekcie krokiCtx, nie
kopią wartości), render.js (loadExercises), bootstrap.js (chrome menu ⋯ + startSheet,
ładowany OSTATNI). template.html: <script src="script.js"> → ciąg app/*.js
(state pierwszy, bootstrap ostatni), kolejność widgetów bez zmian. Zachowanie ciała
funkcji bez zmian (czysty wytnij-wklej). Weryfikacja: node --check ×9 OK; Playwright
headless (2024-grudzien) przeklikane — ABCD/PF/multiSelect/open-self/fillIn (ocena,
kolory badge'y high/mid/low, suma w pasku), kroki wideo z szybkim ◄/► (brak wyścigu,
licznik i treść spójne), panel wzorów PDF, motyw jasny/ciemny, widok punktów,
tryb egzaminu (start/timer/koniec/podsumowanie), przywrócenie postępu po reload;
0 pageerror, 0 console.error, 0×404. UWAGA — znaleziony pre-existing bug (patrz
TODO.md, OPUS DOPISAŁ): reload w fazie „oceń się" po egzaminie. W oryginale
crashował (ReferenceError: zadaniaOtwarte w TDZ — deklaracja poniżej wywołania na
load); po podziale nie crashuje, ale wskaźniki znikają i faza jest czyszczona.
Świadomie NIE naprawiane w tym refaktorze (poza zakresem) — zgłoszone do decyzji.

ZWERYFIKOWANE PRZEZ HENRICHA (2026-07-23): przetestowane ręcznie na gałęzi
claude/do-sprawdzenia-yfi2mu — wszystkie 7 poprawek z code-review Opusa (patrz
niżej) oraz wizualny przegląd kroku 3 podziału plików (style.css → style/*.css:
jasny/ciemny motyw, okno ~500px, landing) — wszystko działa bez zastrzeżeń.
Usunięto z TODO.md sekcję „DO SPRAWDZENIA PRZEZ HENRICHA" i wpis o kroku 3
podziału plików. Przy okazji: reset punktacji będąc wyszarzony w trakcie
egzaminu (w tej samej karcie) to zachowanie uznane za dobre — nie trzeba
dodatkowego ostrzeżenia confirm() w tym przypadku (dotyczy tylko scenariusza
z dwiema kartami, patrz nienaprawiony bug w TODO.md).

ZROBIONE PRZEZ SONNETA (2026-07-22) — naprawy z code-review Opusa (gałąź
claude/do-sprawdzenia-yfi2mu → claude/po-review), punkty 1-7 sekcji „DO REALZACJI
Dopisane przez CLAUDA" w TODO.md:
- [ZROBIONE] [1+2] Znikanie wpisanego toku rozwiązania zadania otwartego po
  odświeżeniu. Przyczyna: zapiszPostep() serializuje CAŁĄ tablicę stanOdpowiedzi,
  a odtwarzające kliki (przywracanie postępu) zapisywały ją, gdy zadania o
  wyższym indeksie miały jeszcze puste {}. Naprawa: cały zapisany stan (zapis.stany)
  jest teraz kopiowany do stanOdpowiedzi ZANIM ruszą odtwarzające kliki (script.js,
  zaraz po utworzeniu stanOdpowiedzi) — usunięty też zbędny drugi zapis
  `stan.open = zap.open` z bloku przywracania. Zweryfikowane Playwrightem: seed
  stany[34]={open:"DLUGI TEKST",self:3} + DWA przeładowania → textarea i
  localStorage zachowują "DLUGI TEKST" po obu.
- [ZROBIONE] [3] Żółte wskaźniki nie pokazywały się dla zadań liczonych na
  kartce (czyNieoceniony() wymagał niepustego stan.open, a to okienko jest
  opcjonalne). Dodany przełącznik w menu "⋯" (#wskazniki-tryb-toggle,
  localStorage matematykazen-tryb-wskaznikow, globalny): domyślny tryb
  "wszystkie" pokazuje kropkę przy KAŻDYM nieocenionym zadaniu otwartym; tryb
  "wypelnione" to dawne zachowanie (kropka tylko przy wypełnionym okienku).
  Zweryfikowane Playwrightem: egzamin zakończony bez wpisania niczego → 7
  kropek (tyle ile zadań otwartych bez samooceny w 2024-grudzien) i klucz
  ocenianie ustawiony.
- [ZROBIONE] [4] Wskaźniki gubiły zadania wypełnione W TRAKCIE fazy „oceń się"
  (lista liczona raz, mogła tylko maleć). odswiezWskaznikiOtwarte() przelicza
  teraz cały zestaw od nowa przez pokazWskaznikiOtwarte() (idempotentne) zamiast
  filtrować; textarea zadania otwartego woła ją też przy wpisywaniu tekstu (nie
  tylko klik samooceny). Zweryfikowane Playwrightem: wpis w trakcie fazy nie
  gubi kropek innych zadań, liczba kropek zawsze zgodna ze stanem, faza kończy
  się dopiero gdy wszystkie zadania otwarte mają samoocenę.
- [ZROBIONE] [5] Przycisk „rozpocznij próbny egzamin" w stopce
  (#egzamin-start-stopka) widoczny bezwarunkowo (dzielił regułę CSS z
  #egzamin-koniec i dostawał display:block bez warunku trybu) — widoczny nawet
  na stronie „Błędny link" i podczas wczytywania danych; klik kasował postęp i
  startował egzamin bez zadań. Naprawa: nowa klasa body.arkusz-wczytany,
  dodawana dopiero na końcu loadExercises(), oraz rozdzielone reguły CSS
  wyglądu i widoczności w style/exam.css. Zweryfikowane Playwrightem:
  ?arkusz=nie-ma-takiego → wysokość przycisku 0; poprawny arkusz w trybie
  ćwiczeniowym → widoczny normalnie.
- [ZROBIONE] [6] Na telefonie (≤~430px) nowy przycisk „zakończ egzamin" w
  pasku (#egzamin-koniec-bar) wypychał menu „⋯" poza ekran. Chowany teraz w
  breakpoincie ≤560px (style/responsive.css) — pełnowymiarowy odpowiednik w
  stopce arkusza zostaje. Zmierzone Playwrightem przy 360px: prawa krawędź
  #menu-button z 429px (poza oknem) na 330px (mieści się).
- [ZROBIONE] [7] #theme-toggle nie był dopisany do wspólnej listy selektorów
  stylujących przyciski menu „⋯" (style/sheet.css) — dostawał domyślny wygląd
  przycisku przeglądarki (szare tło, ramka outset) zamiast białego z cienką
  ramką jak reszta. Dopisany do listy. Zweryfikowane Playwrightem:
  getComputedStyle #theme-toggle i #reset-scores identyczne (border/tło/kolor).
- PRZY OKAZJI (sekcja „TRYB EGZAMINU I PAMIĘĆ PRZEGLĄDARKI", oceniono jako
  małe i bezpieczne poprawki warte zrobienia od razu): (a) nieudany start
  egzaminu (setItem rzuca przy pełnym/zablokowanym localStorage) i tak kasował
  zapisany postęp mimo alertu „egzamin nie wystartował" — kolejność zapisu w
  startExamPrompt() odwrócona, postęp kasuje się dopiero PO udanym zapisie
  stanu egzaminu; (b) „resetuj punktację" nie czyścił trwającego egzaminu w
  innej karcie — reset kasuje teraz też KLUCZ_EGZAMINU, a confirm() ostrzega o
  tym wprost. Problem „dwie karty blokują finishExam" (ten sam opis w
  TODO.md) wymaga większej przebudowy (nasłuch zdarzenia `storage` albo inna
  architektura) — zostawiony w TODO.md dla Henricha, NIE naprawiony w tej
  sesji.
- Weryfikacja: Playwright headless (arkusz 2024-grudzien, python3 -m http.server),
  7 scenariuszy a-g z promptu (zachowanie tekstu po 2 reloadach, kropki bez
  wpisanego tekstu, kropki podczas fazy oceniania, przycisk na stronie błędu,
  360px w trybie egzaminu, computed style theme-toggle vs reset-scores, pełny
  cykl egzamin start→koniec→start + zwykłe odpowiedzi ABCD/PF/fillIn) — wszystkie
  PASS, bez regresji.

ZROBIONE PRZEZ SONNETA (2026-07-22) — podział dużych plików, kroki 1/1b/2 z .claude/plans/czy-my-lisz-e-mam-tingly-hamster.md:
- [ZROBIONE] Krok 1 (wariant A): solutionsInteractive.js (958 linii, 43 KB) rozbity na
  katalog widgets/ — plik na widżet (widgets/osLiczbowa.js … widgets/prostopadloscian.js,
  9 plików), widgets/_helpers.js (wg* helpery + WG_KOLORY) i widgets/_registry.js (rejestr
  WIDZETY). Ciała funkcji przeniesione 1:1 (czysty przenos, bez zmiany logiki). template.html
  dostał 11 tagów `<script>` w kolejności _helpers → 9 widżetów → _registry → script.js
  (zamiast dawnych dwóch: solutionsInteractive.js → script.js) — kolejność wymuszona przez
  globalny scope (WIDZETY musi widzieć już zdefiniowane funkcje widget*, script.js musi
  widzieć już zbudowany WIDZETY).
- [ZROBIONE] Krok 1b: pole danych `solutionInteractive` → `solutionWidget` w obu
  exercises.json (35 + 41 wystąpień), w script.js (`exercise.solutionInteractive` → 5 miejsc),
  w ARCHITECTURE.md, CLAUDE.md i komentarzu w style.css. Celowo NIE ruszone: zmienna lokalna
  `solutionInteractiveContainer` w script.js i klasa CSS `.solution-interactive-container` —
  to osobna warstwa (nazwa slotu DOM), zgodnie z planem.
- [ZROBIONE] Krok 2: sekcja „CSS & layout reference" ARCHITECTURE.md (14 KB z 40 KB)
  wydzielona do nowego ARCHITECTURE_CSS.md; w ARCHITECTURE.md został nagłówek + link.
  CLAUDE.md zaktualizowany (odsyła do obu plików).
- Weryfikacja: `node --check` na wszystkich 11 nowych/zmienionych plików JS + walidacja
  JSON obu exercises.json — czysto. `grep -r solutionInteractive` po zmianie zwraca
  wyłącznie archiwalne DONE/STARY_PRZENIESIONY_DONE.md i `.solution-interactive-
  container` (zgodnie z planem). Playwright headless (oba arkusze, `?arkusz=2024-grudzien`
  i `?arkusz=2026-maj`): liczba zadań 35/41 OK, wszystkie 9 widżetów renderują
  `canvas.widget-canvas` po kliknięciu „Rozwiązanie" i reagują na przeciąganie/suwak,
  klik ABCD/PF/fillIn działa, zero page error / console error (poza znanymi, oczekiwanymi
  404 obrazków 2026-maj opisanymi w ARCHITECTURE.md) / response >= 400.
- [ZROBIONE] Krok 3: style.css (1470 linii, 60 KB) rozbity na katalog style/ wg
  istniejących granic `/* ===== ... ===== */` — style/base.css (zmienne CSS, palety
  jasna/ciemna, KaTeX, reset, 1-249), style/sheet.css (pasek górny, panele PDF, karta
  zadania, typy odpowiedzi, widżety, tabelki, 250-1057), style/landing.css (`.landing-*`,
  1058-1158), style/exam.css (tryb egzaminacyjny + wskaźniki nieocenionych, 1159-1350),
  style/responsive.css (breakpointy 1024/900/720/560, 1351-1470). Czysty przenos —
  `diff` skonkatenowanych 5 plików ze starym style.css pokazał tylko różnice w białych
  znakach plus jedną celową poprawkę (odsyłacz „CSS & layout reference w CLAUDE.md" →
  ARCHITECTURE_CSS.md w komentarzu nad #top-bar). template.html dostał 5 tagów `<link>`
  w kolejności base→sheet→landing→exam→responsive (kaskada, responsive musi być
  ostatni); index.html tylko base+landing. Poprawione linki z numerami linii do
  starego style.css w TODO.md (4 miejsca) na nowe pliki/linie w style/.
- Weryfikacja kroku 3: `grep href="style.css"` — zero trafień. Playwright: response 200
  dla wszystkich 5 plików CSS na obu arkuszach i dla base+landing na index.html; ponowny
  smoke test (35/41 zadań, 9 widżetów, klik ABCD/PF/fillIn) bez regresji. Dodatkowo
  computed-style sprawdzenie kaskady (bo to jedyne realne ryzyko podziału CSS): jasny
  motyw body bg rgb(255,255,255), wymuszony ciemny (localStorage) rgb(27,27,27),
  #bar-container 3 kolumny na 1280px / 1 kolumna na 500px (responsive.css > sheet.css),
  tryb egzaminu chowa #total-score i pokazuje #egzamin-timer (exam.css), landing
  .landing-hero wyśrodkowany (landing.css) — wszystko zgodne. Wizualny przegląd
  (jasny/ciemny, ~500px, landing) zostawiony Henrichowi — patrz DO SPRAWDZENIA w TODO.md.
  Krok 4 zrobiony wcześniej przez Henricha inaczej (katalog nazwano „DONE TODO"; od
  2026-07-22 zmieniony na „DONE").
  Krok 5 (script.js → js/) odłożony, poza zakresem tej sesji.

ZROBIONE PRZEZ OPUSA (2026-07-21) — poprawki żółtych bombli (zgłoszone przez Henricha) z TODO.md:
- [ZROBIONE] Złe liczby na kropkach (np. „24" dotyczyła zad 19). Przyczyna: numer
  brany z index+1, a indeksy w tablicy rozjeżdżają się z numeracją CKE przez zadania
  nadrzędne (maxScore:0) i wieloczęściowe (kilka wpisów „Zadanie 12/17"). Teraz numer
  parsowany z treści zadania (.question textContent, regex „Zadanie N"), z fallbackiem
  do index+1. Zweryfikowane: wypełnione zad otwarte idx 2/23/34 dają kropki 3/19/30
  (a nie 3/24/35); kropka „19" wskazuje #exercise-23, którego treść to „Zadanie 19".
- [ZROBIONE] Przycisk „ukryj": tekst zmieniony z „× ukryj" na „✕ Ukryj wskaźniki
  nieocenionych zadań", przeniesiony do lewego dolnego rogu (kropki są po prawej, więc
  się nie zasłaniają) i dostał żółtą ramkę (2px var(--wskaznik-border)) wiążącą go
  wizualnie z kropkami. Kolumnie kropek zdjęto rezerwę na przycisk u dołu prawej (mogą
  schodzić prawie do dołu). Zweryfikowane wizualnie w jasnym i ciemnym.
- PRZY OKAZJI naprawiony zastany bug: restore postępu ustawiał tylko openTextarea.value,
  a nie stan.open — po reloadzie kolejny zapis kasował zapisany tok rozwiązania zadania
  otwartego. Teraz restore ustawia też stan.open (zrobione już w commicie z wskaźnikami).

ZROBIONE PRZEZ OPUSA (2026-07-21) — pływające żółte wskaźniki nieocenionych zadań otwartych z TODO.md:
- [ZROBIONE] Po zakończeniu próbnego egzaminu (faza „oceń się") każde zadanie
  otwarte (selfScore) WYPEŁNIONE (jest wpisany tok rozwiązania w textarea), ale bez
  przyznanej samooceny, dostaje pływającą żółtą kropkę z numerem zadania po prawej
  krawędzi (klasa .wskaznik-otwarte, style w style.css; kolory przez nowe zmienne
  motywu --wskaznik-* — działają w jasnym i ciemnym). Klik kropki przewija do
  zadania (scrollIntoView center). W trakcie egzaminu kropek nie ma.
- [ZROBIONE] Pozycjonowanie zależne od scrolla (repozycjonujWskazniki w script.js):
  środek kropki = środek jej zadania w viewport, zaklamowany do pasa pod paskiem
  górnym … nad przyciskiem „ukryj"; kropki są rozsuwane (declutter przód/tył), więc
  gdy zadanie jest poza ekranem, kropka przykleja się do góry lub dołu w zwartej
  kolumnie. Nasłuch scroll/resize przez requestAnimationFrame.
- [ZROBIONE] Wspólny przycisk „× ukryj" (#wskazniki-ukryj, prawy dolny róg) chowa
  wszystkie kropki naraz i kończy fazę. Kropka pojedynczego zadania znika po jego
  ocenieniu (klik samooceny woła odswiezWskaznikiOtwarte()); gdy zniknie ostatnia,
  faza się kończy.
- Faza „oceń się" trzymana w localStorage (KLUCZ_OCENIANIA = matematykazen-ocenianie-
  <sheet>), więc kropki przetrwają odświeżenie strony aż do ocenienia wszystkich albo
  „ukryj". Nowy egzamin i „resetuj punktację" kasują tę fazę. Rejestr zadań otwartych
  (zadaniaOtwarte) zbierany przy renderowaniu; wskaźniki odtwarzane w startSheet po
  loadExercises (tylko gdy NIE trwa egzamin).
- PRZY OKAZJI naprawiony zastany bug: przy przywracaniu postępu ustawiane było tylko
  openTextarea.value, ale NIE stan.open (input nie odpala się przy .value). Przez to
  po reloadzie stan.open był pusty i kolejny zapis (np. klik samooceny) kasował
  zapisany tok rozwiązania zadania otwartego. Teraz restore ustawia też stan.open.
- Zweryfikowane Playwrightem: brak kropek w trakcie egzaminu; po zakończeniu kropki
  dla wypełnionych nieocenionych zadań (3, 8) i przycisk „ukryj"; pozycja kropki
  zmienia się przy scrollu (711px→87px, przyklejenie do góry); ocenienie zad 3 usuwa
  jego kropkę; trwałość po reload; „ukryj" chowa wszystkie i kasuje fazę (po reload 0).
  Wizualnie sprawdzone w jasnym i ciemnym. Bez błędów w konsoli.

ZROBIONE PRZEZ OPUSA (2026-07-21) — zmienne CSS + dark mode (Etap 1 infrastruktura) z TODO.md:
- [ZROBIONE] Wprowadzone CSS custom properties na wszystkie kolory (tło, tekst,
  ramki, akcenty, stany poprawne/błędne, badge punktacji, komunikat błędu) w :root
  (style.css). Wartości w :root = dokładnie dotychczasowe kolory jasnego motywu,
  więc jasny wygląda 1:1 jak wcześniej (zweryfikowane computed: body bg
  rgb(255,255,255), tekst rgb(17,17,17), #total-score rgb(133,133,133)). Cały
  style.css (~136 użyć) przepięty na var(--...). Canvas ma własne --canvas-bg,
  które NIE ciemnieje (widżety rysują ciemnym po jasnym — inaczej wykresy
  zniknęłyby). Landing-cta odwraca kolory przez var(--text)/var(--bg), więc hover
  działa w obu motywach.
- [ZROBIONE] Ciemna paleta w dwóch bliźniaczych blokach: @media
  (prefers-color-scheme: dark) :root:not(.theme-light) (motyw systemowy/auto) oraz
  html.theme-dark (ręczne wymuszenie — pierwszeństwo nad systemem). Ręczny jasny =
  html.theme-light (wyłącza regułę systemową przez :not, zostają wartości :root).
- [ZROBIONE] Przełącznik #theme-toggle w menu „⋯" (template.html) cyklujący
  auto → jasny → ciemny → auto; wybór ≠ auto zapisywany w localStorage pod
  GLOBALNYM kluczem matematykazen-motyw (wspólny dla wszystkich arkuszy). Klasę na
  <html> ustawia mały inline-skrypt w <head> template.html (bez mignięcia motywu /
  FOUC), logika i etykieta w script.js. Ten sam snippet dodany do index.html, żeby
  landing honorował zapamiętany motyw (landing nie ma własnego przełącznika — bez
  zapisu idzie za systemem). Zweryfikowane Playwrightem: cykl stanów, klasy na
  <html> (theme-light/theme-dark), zapis/kasowanie w localStorage, trwałość po
  reload bez FOUC, brak błędów w konsoli; wizualnie sprawdzone dark: pasek, treść
  zadania + KaTeX, błędna odpowiedź (przygaszona czerwona ramka), blok rozwiązania,
  nakładka podsumowania egzaminu, landing.

ZROBIONE PRZEZ OPUSA (2026-07-21) — nudge #bar-center z TODO.md:
- [ZROBIONE] Tytuł arkusza (#exercises-sheet-title) i podtytuł trybu
  (#exercises-mode-subtitle) delikatnie niżej w pasku: na #bar-center dodane
  position: relative; top: 5px; (style.css). Wysokość #top-bar bez zmian
  (zmierzone Playwrightem: 64px, position=relative/top=5px, tytuł opuszczony
  o 5px). 5px wizualnie w porządku.

ZROBIONE PRZEZ OPUSA (2026-07-21) — "tryb egzaminu — pasek i stopka" z TODO.md:
- [ZROBIONE] Dodatkowy przycisk "zakończ egzamin" w pasku górnym (#egzamin-koniec-bar
  w template.html, w #bar-right zaraz po #egzamin-timer, przed #total-score). Styl jak
  #toggle-tablica (border 2px #e7e7e7, radius 3px, padding 8px 12px, bg #fff, cursor
  pointer) ale BEZ min-width. Widoczny tylko pod body.tryb-egzaminu (domyślnie display:
  none, odkrywany regułą body.tryb-egzaminu #egzamin-koniec-bar). W @media <=720px dostaje
  font-size:13px i padding:8px jak #total-score. Istniejący #egzamin-koniec pod ostatnim
  zadaniem został na miejscu.
- [ZROBIONE] #egzamin-koniec (stopka) dostał odstęp od góry: margin 0 auto 80px → 40px
  auto 80px (style.css).
- [ZROBIONE] Dodatkowy przycisk "rozpocznij próbny egzamin" w stopce arkusza
  (#egzamin-start-stopka w template.html, tuż obok #egzamin-koniec pod #exercises-wrapper),
  widoczny odwrotnie — tylko w trybie ćwiczeniowym (znika pod body.tryb-egzaminu). Styl
  identyczny jak #egzamin-koniec w stopce (ta sama ramka, 40px góra / 80px dół). Wersja
  w menu "⋯" (#egzamin-start) została bez zmian.
- Zachowanie: obie pary przycisków wiszą na wspólnych funkcjach w script.js
  (startExamPrompt / finishExamPrompt), podpiętych pętlą do obu id, żeby kopie nie mogły
  się kiedyś rozjechać. Zweryfikowane Playwrightem w obu trybach: w ćwiczeniowym widać tylko
  stopkowy start (total-score widoczny), w egzaminie widać oba "zakończ" + timer (total-score
  i stopkowy start ukryte); klik "zakończ egzamin" w pasku czyści stan egzaminu i pokazuje
  podsumowanie (identycznie jak przycisk w stopce). Wizualnie sprawdzony układ paska (1280px
  i 700px) oraz przyciski w stopce.

ZROBIONE PRZEZ OPUSA (2026-07-17) — NISKI PRIORYTET z TODO.md:
- [ZROBIONE] Przeciąganie paneli PDF ograniczone do widocznego viewportu
  (makePanelDraggable w script.js). Wcześniej dół/boki były swobodne i pasek
  tytułowy (.panel-uchwyt) mógł zjechać pod dolną krawędź ekranu (za pasek zadań
  Windows). Teraz w funkcji move() klampujemy: top ∈ [minTop, innerHeight −
  uchwytH] (uchwyt zawsze w pełni widoczny, nie chowa się pod top-barem ani pod
  dolną krawędzią), left ∈ [minWidoczne − szer, innerWidth − minWidoczne]
  (min. 60px panelu zostaje na ekranie w bok). ŚWIADOMA ZMIANA wcześniejszej
  decyzji z 2026-07-13 (wtedy celowo BEZ klampu dołu/boków) — użytkownik
  poprosił o ograniczenie do viewportu. Zweryfikowane Playwrightem: drag daleko
  w dół+prawo → uchwyt zostaje przy dolnej krawędzi i 60px w prawym rogu; drag
  daleko w lewo → panel left=-298px, czyli 60px widoczne po lewej.
- [ZROBIONE] Wcięcie treści zadania (.question padding-left: 16px w style.css) —
  tekst nie klei się już do lewej krawędzi karty i nie wygląda na przeciągnięty
  w lewo względem wyśrodkowanych odpowiedzi. Zweryfikowane (computed
  padding-left=16px, wizualnie treść przesunięta w prawo).
- [ZROBIONE] Wyrównanie badge'a punktacji zadania w pionie (.exercise-score
  margin-top: 16px w style.css) — wcześniej siedział optycznie ~16px za wysoko
  względem numeru zadania. Zmierzone Playwrightem: środek badge'a przesunięty
  z y≈172 na y≈188, zrównany ze środkiem pierwszej linii treści (≈188). W media
  query <=1024px (badge w rogu karty) margin-top wyzerowany, żeby trzymał się
  górnej krawędzi.
- [ZROBIONE] Procent zdobytych punktów obok sumy w pasku (tryb ćwiczeniowy).
  updateTotalScore() (script.js) dokłada do #total-score <span.total-percent>
  z bieżącym procentem (round(pkt/max*100)); od progu zdawalności 30% dostaje
  klasę .zdane (zielony #0AB32F, bold) i title="zdałeś", poniżej szary +
  title="nie zdałeś (jeszcze)" (CSS w style.css, cursor: help). Ponieważ procent
  jest WEWNĄTRZ #total-score, automatycznie znika w trybie egzaminu i w widoku
  punktów "nic". Zweryfikowane Playwrightem: 24% → szary/"nie zdałeś (jeszcze)";
  38% → zielony bold/"zdałeś".
- [ZROBIONE] Normalizacja odpowiedzi fillIn (normalizeAnswer w script.js) —
  dołożony .replace(/[xye∈]/gi, "") wycina znaki zmiennej/przynależności
  (x, y, E/∈), więc "x∈(-4,4]", "y ∈ [-1,3]", "X E (1,3)" pasują do samego
  przedziału z klucza. Sprawdzone, że żadna accepted w obu exercises.json nie
  zawiera x/y/e/∈, więc usunięcie z obu stron porównania jest bezpieczne.
  Zweryfikowane Playwrightem: normalizeAnswer(warianty) → czysty przedział;
  realne pole fillIn (zad 17, exercise-9) z wpisami "x∈(-4, 4]" itd. → wszystkie
  4 pola .correct.
- [ZROBIONE] TRYB PRÓBNY EGZAMIN — trzy poprawki (style.css + script.js):
  * (6a) Cały wiersz light-buttonów chowany w trybie egzaminu przez
    `body.tryb-egzaminu .light-button-container { display:none }` (wcześniej
    ukrywane były tylko .hint-button/.solution-button, a "Pokaż potrzebne wzory"
    zostawał sam z pustym odstępem). TABLICA wzorów CKE i #toggle-tablica nadal
    widoczne; #toggle-zasady (klucz odpowiedzi) nadal ukryty.
  * (6b) Opcje w menu "..." (pokaż rozwiązania / widok punktów / reset / start
    egzaminu) NIE znikają już w egzaminie — zostają widoczne, ale disabled
    (wyszarzone, nieklikalne), więc menu nie jest pustą ramką. setExamMenuDisabled()
    w script.js ustawia atrybut disabled na tych 4 przyciskach w enableExamMode()
    i zdejmuje go w finishExam(); CSS `#bar-menu button:disabled` daje opacity 0.4
    + cursor not-allowed. Usunięte te 4 id z listy display:none w bloku egzaminu.
  * (6c) Zadania otwarte (selfScore) dostają textarea "Twoja odpowiedź / tok
    rozwiązania" w OSOBNYM kontenerze .open-answer-container (poza
    .self-score-container, którą egzamin chowa) — dzięki temu textarea jest
    widoczna i podczas egzaminu (samoocena schowana), i po nim (samoocena wraca).
    Zapis do localStorage tą samą drogą co reszta (stan.open w zapiszPostep,
    przywracane w bloku "Przywrócenie postępu" gdy typeof zap.open === "string").
    Zweryfikowane Playwrightem: NORMAL → textarea+samoocena+light-buttony widoczne;
    EXAM → light-buttony ukryte, textarea widoczna, samoocena ukryta,
    #toggle-tablica widoczny, #toggle-zasady ukryty, 4 opcje menu disabled=true;
    wpis w textarea przetrwał reload; po "zakończ egzamin" — samoocena wraca,
    treść textarea zachowana, opcje menu disabled=false.

ZROBIONE PRZEZ OPUSA (2026-07-13) — cały WYSOKI PRIORYTET z TODO.md:
- [ZROBIONE] Powiększone UMIARKOWANIE przyciski "oceń się" (.self-score-container button
  w style.css): padding 6px 10px → 8px 11px, font-size 15px → 17px, min-width 56px → 62px.
  Zwarty poziomy rząd przycisków punktowych zostaje — nie robią się pełnowymiarowymi
  przyciskami odpowiedzi. Zweryfikowane Playwrightem (computed font-size=17px, padding=8px 11px).
- [ZROBIONE] Panele PDF (makePanelDraggable w script.js): jedyne ograniczenie przeciągania
  to top — uchwyt (.panel-uchwyt) nie zjedzie pod top-bar (minTop = dolna krawędź #top-bar,
  liczona z getBoundingClientRect przy każdym pointerdown, więc panel zawsze da się złapać).
  Usunięty Math.max(0,...) na left — lewo/prawo/dół całkowicie swobodne (panel może wyjechać
  poza brzeg ekranu). Zmiana rozmiaru (.panel-rozmiar) bez zmian. Zweryfikowane Playwrightem:
  drag w górę klampuje top do dolnej krawędzi paska, drag w lewo daje left=-821px (bez klampu).
  UWAGA/decyzja: prompt mówił "by CAŁY pasek uchwytu się nie schował"; wybrałem ostrzejszy,
  pewniejszy wariant — cały uchwyt zostaje pod paskiem (zawsze w pełni chwytalny), zamiast
  dopuszczać częściowe wsunięcie z pozostawionym skrawkiem. Efekt (uchwyt zawsze chwytalny)
  jest ten sam, a zachowanie czytelniejsze.
- [ZROBIONE] Błędny/pusty/brakujący ?arkusz= → komunikat "Błędny link" z hiperłączem do
  index.html zamiast cichego fallbacku. Usunięty `|| "2024-grudzien"` w script.js (SHEET_ID).
  startSheet() rozróżnia: brak/pusty param → od razu błędny link (bez fetchu); fetch 404 →
  błędny link; brak odpowiedzi (file:// / sieć) → dawny komunikat o serwerze; zły JSON →
  komunikat o uszkodzonym pliku. Zweryfikowane Playwrightem (brak param / ?arkusz= / nieznane
  id → "Błędny link" + link do index.html + zero wyrenderowanych zadań; poprawne id → render OK).
- [ZROBIONE] Stały, szarawy podtytuł trybu pod nazwą arkusza w pasku
  (#exercises-mode-subtitle w #bar-center, template.html; CSS 12px #999). Domyślnie
  "tryb ćwiczenia", przełącza się na "tryb egzaminu" pod body.tryb-egzaminu przez
  updateModeSubtitle() wołane w enableExamMode() i finishExam(). Chowany <900px razem
  z tytułem. Zweryfikowane Playwrightem (ćwiczenie → "tryb ćwiczenia", start egzaminu →
  "tryb egzaminu").
- [ZROBIONE] Krótkie confirm() przed "resetuj punktację" (#reset-scores, script.js):
  "Wyczyścić zapisane odpowiedzi i punkty? Tej operacji nie można cofnąć." Anulowanie
  przerywa akcję. Zweryfikowane Playwrightem (klik pokazuje dialog z tym tekstem).

