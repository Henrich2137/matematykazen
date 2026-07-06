ARCHIWUM ZROBIONYCH PUNKTÓW TODO. Tu trafiają wpisy [DONE]/[ZROBIONE] przenoszone z todo.md.
Nie wczytuj tego pliku domyślnie — tylko gdy potrzebne jest szersze spojrzenie na projekt,
rozwiązanie trudniejszego problemu albo sprawdzenie, czy/jak coś już kiedyś rozwiązano.
(Zasada opisana w CLAUDE.md. Plik zaczął się jako notatki ze smoke testu.)

ZROBIONE (2026-07-04):
- [DONE] Punkt nie cofał się po złej odpowiedzi → naprawione. Usunięto flag isScoreGiven; każde zadanie ma earnedScore (0 albo maxScore), a updateTotalScore() przelicza sumę od zera. Zła odpowiedź daje 0 / X pkt i zeruje earnedScore.
- [DONE] Kruche porównywanie odpowiedzi po stringu HTML → naprawione. Dane używają teraz correctAnswerIndex (0=A, 1=B, ...; -1 = otwarte/niewypełnione), a ocena to i === correctIndex. Cały exercises.js zmigrowany.
- [DONE] defaultPlaybackRate na oderwanym tempDiv → naprawione. renderStep() zwraca czysty string, a showStep() ustawia defaultPlaybackRate i playbackRate = 0.1 na realnym.
- [DONE] Pozostałe porządki Fazy 1 (usunięcie martwego kodu, scalenie listenerów .solution-button, deklaracje globali, przeniesienie)

ZROBIONE (2026-07-04, sesja 2 — uzupełnienie arkusza + interaktywność):
- [DONE] Uzupełnione wszystkie zadania: poprawne odpowiedzi (correctAnswerIndex), podpowiedzi, rozwiązania (solutionText + solutionTextMore) i strony tablic (formulasPage) dla zadań 1-20; treści 7-20 zweryfikowane z obrazkami zadN/ (cropami z arkusza).
- [DONE] BŁĄD MERYTORYCZNY zad 2: (⁵√5 · ⅕)⁻⁵ = 5⁴, czyli odpowiedź A, nie B. Dane poprawione; klatka końcowa filmiku step6 nadal pokazuje 5⁻⁴ (patrz niżej: do przerenderowania).
- [DONE] Poprawka rozwiązania zad 3 (było "2⁴ + 2² + 2⁹⁶" w nawiasie, ma być "2⁴ + 2² + 1 = 21") oraz podpowiedzi zad 6 (była skopiowana podpowiedź o logarytmach z zad 4).
- [DONE] Nowe typy zadań w silniku: PF (prawda/fałsz z przyciskami P/F przy każdym stwierdzeniu), multiSelect (np. zad 12.2 — wybór dwóch wzorów, punkty częściowe), open z samooceną (selfScore: true → przyciski 0..maxScore pkt; realizuje flow "rozwiąż na kartce i oceń się" z CLAUDE.md).
- [DONE] 9 widżetów interaktywnych (solutionInteractive): zad 1 (oś liczbowa z przeciąganym punktem i strzałkami odległości — realizuje pomysł z sekcji "było by idealnie"), zad 5 (procent składany — suwak p i słupki kapitału; naprawia martwe rysujWykresEksponencjalny), zad 9 (parabola nierówności z przedziałem rozwiązań), zad 10 (wykres przedziałami z podświetlanym wzorem), zad 12.1 (monotoniczność paraboli), zad 15 (ciąg arytmetyczny — suwak m i różnice), zad 18 (koło trygonometryczne z przeciąganym kątem), zad 20 (kąt wpisany/środkowy z przeciąganym C), zad 30 (optymalizacja prostokąta).
- [DONE] maxTotalScore liczone automatycznie z sumy maxScore (nie trzeba już synchronizować ręcznie).
- [DONE] zad17.PNG → zad17.png (wielkość liter psuła obrazek na hostingu case-sensitive, np. GitHub Pages).
- [DONE] Przycisk "Podpowiedź" chowa się, gdy zadanie nie ma podpowiedzi.
- [DONE] Zaznaczenie tekstu jasnoniebieskie bez zmiany koloru tekstu (::selection) — z sekcji "było by idealnie".
- [DONE] Krok filmu bez komentarza dostaje wypełniacz "· · ·" (.step-comment:empty) — z sekcji "było by idealnie".
- [DONE] Migotanie przy przełączaniu stepów zmniejszone: film następnego kroku jest preloadowany (preload="auto") w showStep().
- [DONE] Spacer <br><br><br><br> pod paskiem zastąpiony paddingiem #exercises-wrapper (gotcha z CLAUDE.md).
- [DONE] Zadania 23-30 (wymyślone przez ChatGPT, odwołujące się do nieistniejących obrazków zad23-29) zastąpione spójnymi zadaniami 21-31 w stylu CKE bez obrazków; brakujące grafiki przestały być problemem.

ZROBIONE (2026-07-05, sesja 3 — oryginalne zadania 21-30 + strona główna):
- [DONE] Zadania 21-30 podmienione na ORYGINAŁY z arkusza CKE (treści i klucz odpowiedzi wklejone przez autora; wszystkie odpowiedzi przeliczone i zgodne z kluczem). Suma punktów arkusza = 50 pkt — zgadza się z oficjalną, co potwierdza też punktację zadań otwartych 8 (3 pkt), 10 (4 pkt), 19 (4 pkt).
- [DONE] Zweryfikowane z kluczem zadania 18 (A), 19 (22,14), 20 (B) — były poprawne.
- [DONE] Widżet zad 30 przerobiony z prostokąta na prostopadłościan z arkusza (P(x) = −26x² + 96x, dziedzina (0,3), maksimum x = 24/13) — widgetProstopadloscian.
- [DONE] Strona główna index.html (przeniesiona z gałęzi claude/practical-rubin-t7g7ya, style .landing-* w style.css) + logo w arkuszu jest teraz linkiem do index.html.
- [DONE] Tabelka danych zad 29 jako HTML (.data-table), nie obrazek.




Sugestie WYGLĄD / DESIGN:

ZROBIONE WYGLĄD/DESIGN (2026-07-04):
- [DONE] "pokaż więcej" za bardzo przyklejone do lewej → .solution-text-more ma teraz padding 0 40px, treść odsunięta od krawędzi.
- [DONE] Zbędny separator pod rozwiązaniem tylko-tekstowym → loadExercises() zdejmuje border-bottom z ostatniego widocznego bloku rozwiązania (na podstawie hasText/hasSteps/hasInteractive/hasMore).
- [DONE] Przycisk "Pokaż/Schowaj tablice wzorów" zmieniał szerokość → #toggle-tablica ma min-width: 200px.
- [DONE] Skakała wysokość diva step-by-step → podpis kroku owinięty w .step-comment (min-height ~2 linijki), .steps-content min-height 250px; wysokość stała do ~2 linijek komentarza.
- [DONE] Litery A, B w przyciskach na dole → vertical-align: middle na przyciskach i obrazkach w nich (bez flexa, żeby nie zepsuć sup/sub).
- [DONE] Grafika w zad 10 nierówna / przesunięta w prawo → .question img jako blok wyśrodkowany; inline obrazek w zad2 nadpisany display:inline-block.
- [DONE] Przycisk "Rozwiązanie" tylko gdy istnieje jakiekolwiek rozwiązanie → loadExercises() chowa .solution-button, gdy brak tekstu/kroków/interaktywnego/"pokaż więcej".
- [DONE] Klik w filmik zatrzymuje/wznawia + ikonka ▶ gdy zatrzymany → mała .video-overlay-icon w lewym dolnym rogu (nie na środku, nie zasłania filmu).
- [DONE] Pasek postępu filmu → cienki (2px) szary .video-progress-bar aktualizowany w timeupdate, płynne przejście width (pełny = skończony).
- [DONE] Krzyżyk zamykający tablicę wzorów → #tablica-close (✕) w prawym GÓRNYM rogu #tablica-wzorow-panel, chowa panel przez schowajTablice().

Uwaga: wyśrodkowanie liter A/B w odpowiedziach jest w style.css (ogólne, wszystkie zadania), nie w exercises.js. Zmiana w exercises.js dotyczyła tylko grafiki w treści zad2.




Byłoby idealnie:
- [DONE 2026-07-04] zad 2 (=zad 1?) > interactiveSolution: przesuwanie punktu na osi liczbowej + strzałki od środka — zrealizowane w widgetOsLiczbowa (zad 1).
- [DONE 2026-07-04] zaznaczenie jasnoniebieskie bez białego tekstu (::selection).
- [DONE 2026-07-04] gdyby nie było tekstu/komentarza pod video to pojawia się wypełniacz "· · ·" w jego miejsce.


=== PRZENIESIONE Z todo.md (2026-07-05, porządkowanie: zrobione wpisy trafiają tutaj) ===

--- Weryfikacja zgodności z arkuszem PDF (2026-07-05, sesja: sprawdzenie exercises.js vs "arkusze PDF/") ---
Porównałem cały exercises.js z arkuszem (matematyka-2024-grudzien-probna-podstawowa.pdf)
i kluczem (…-odpowiedzi.pdf). Tekst obu PDF-ów wyciągnąłem przez `pdftotext -layout`
do arkusze PDF/arkusz.txt oraz arkusze PDF/odp.txt (zostawione na przyszłość).

WYNIK: wszystkie 30 odpowiedzi zgadza się z oficjalnym kluczem CKE. Treści też się zgadzają.

- [ZROBIONE 2026-07-05] Zad 29 — tabela podmieniona na oryginał CKE (5 kolumn:
  książki 4,5,6,7,8, uczniowie 5,8,12,13,12; suma 50). solutionText zsynchronizowany
  (rozpiska średniej 4·5 + 5·8 + 6·12 + 7·13 + 8·12 = 319/50 = 6,38; mediana 6,5 bez zmian).
  (Wcześniej w exercises.js była tabela ODTWORZONA: 6 kolumn, książki 4-9,
  uczniowie 7,8,10,14,6,5 — dawała te same wyniki, ale była zmyślona.)
- [OK, potwierdzone z kluczem] Toki ROZWIĄZAŃ (solutionText + solutionTextMore) sprawdzone
  z modelowymi rozwiązaniami / "Zasadami oceniania" w odp.txt — wszystkie merytorycznie
  poprawne. Zadania otwarte 3, 8, 9, 10, 19, 26, 28, 30 mają metodę zgodną z modelową
  (zad 19 to poprawny wariant trygonometryczny zamiast podobieństwa — klucz akceptuje
  każdą poprawną metodę). Uzasadnienia zadań zamkniętych prowadzą do litery z klucza.
  Znany wyjątek (nie nowy błąd): zad 2 krok 6 filmu ma błędną klatkę 5⁻⁴, ale tekst
  rozwiązania jest poprawny (film do przerenderowania — punkt otwarty w todo.md).
- [OK, potwierdzone z kluczem] Punktacja zadań otwartych zgadza się z arkuszem:
  zad 3 (0-2), 8 (0-3), 9 (0-2), 10 (0-4), 19 (0-4), 26 (0-2), 28 (0-2), 29 (0-2), 30 (0-4).
  Suma całego arkusza = 50 pkt. Zgadza się z maxTotalScore liczonym z maxScore.
- [ZROBIONE 2026-07-05] Zad 12 — wspólne wprowadzenie pokazywane raz (nagłówek
  „Zadanie 12." na górze wpisu 12.1), 12.2 tylko krótko odwołuje się do tej samej
  funkcji f — wzorem na zad 17.

--- Sesja 2026-07-05: realizacja punktów „do zrobienia / do poprawki" z góry todo.md ---
Zrobione:
- [ikonka w title] Usunąłem 🧘. W <head> matematykazen.html jest teraz prosta,
  czarna ikonka „M" (serif, data-URI SVG) — włączona. Jeśli nie pasuje, wystarczy
  usunąć jedną linię <link rel="icon"> (komentarz obok o tym mówi). Zrób własne logo,
  gdy zechcesz — łatwo podmienić.
- [zad 12 oddzielone od 12.1] Zrobione tak jak w zad 17: wpis 12.1 zaczyna się teraz
  od nagłówka „Zadanie 12." + wspólne wprowadzenie o paraboli, a pod nim „Zadanie 12.1."
  z samym pytaniem. 12.2 nie powtarza już całego wprowadzenia — krótkie „Dana jest ta
  sama funkcja f (...)", jak „Dany jest ten sam trójkąt" w 17.2. 12.3 bez zmian
  (buduje na f). To układ czysto w treści (question HTML) — pól number/numberSection
  nadal nie ma.
- [przyciski 12.2 nieintuicyjne] multiSelect: gdy komplet już zaznaczony, klik nowej
  odpowiedzi podmienia teraz najdawniej wybraną (okno przesuwne) zamiast nic nie robić —
  nie trzeba już ręcznie odklikiwać. Kod: obsługa kliknięcia w bloku multiSelect
  w matematykazen.html.
  (Wybrałem podmianę NAJSTARSZEGO wyboru, nie ostatniego jak proponowałeś — przy
  poprawianiu dwóch typowań daje płynniejsze „przesuwane okno ostatnich 2 klików".
  Jak wolisz jednak LIFO, powiedz — to jedna linijka.)
- [zad 29 tabela] Patrz wyżej — [ZROBIONE 2026-07-05].

Zostawione bez zmian (za decyzją Henricha):
- [zad 17.1] Zweryfikowane z kluczem CKE i rysunkiem: odpowiedź D (√15/8) oraz całe
  rozwiązanie są poprawne (kąt ABC przy wierzchołku B, sin = AC/BC = √15/8). Na prośbę
  Henricha zostawione bez zmian.

--- Sesja 2026-07-05: odchudzenie CLAUDE.md (mniej tokenów na start sesji) ---
- [ZROBIONE] CLAUDE.md skrócony z ~125 do ~35 linii: zostały tylko rzeczy potrzebne
  w każdej sesji (kontekst produktu, 4 główne pliki, zasady todo.md, uruchamianie,
  notatki o treści). Cała szczegółowa dokumentacja (model renderowania, schemat
  exercises.js, konwencja zadN/, pełny opis CSS/layout z gotchami) przeniesiona
  do NOWEGO pliku ARCHITECTURE.md — CLAUDE.md odsyła do niego i każe go czytać
  przed zmianami w renderowaniu/schemacie/CSS oraz utrzymywać w synchronizacji.
- [ZROBIONE przy okazji] CLAUDE.md wskazywał na nieistniejące pliki todo3.md /
  todo2.md / todo1DONE.md — poprawione na faktyczne todo.md (aktywny) i todoDONE.md
  (archiwum). Usunięty też nieaktualny "known open task" o tabeli zad 29 (podmiana
  była już zrobiona 2026-07-05 — potwierdzone w exercises.js).
- [ZROBIONE 2026-07-05] Nowa zasada w CLAUDE.md: wpisy [DONE]/[ZROBIONE] przenoszone
  są z todo.md do todoDONE.md, a todoDONE.md NIE jest wczytywany domyślnie — tylko
  przy szerszym spojrzeniu na projekt / trudniejszym problemie. Ten blok wpisów to
  pierwsze zastosowanie tej zasady.
--- Sesja 2026-07-05 (Fable): realizacja todo.md — wysoki priorytet + "cięższe rzeczy" ---
- [ZROBIONE 2026-07-05] Zad 12 i 17 oddzielone od podzadań: wspólny wstęp każdego z nich
  to teraz osobny, "pusty" element exercises (maxScore: 0 — bez odpowiedzi, rozwiązań
  i badge'a punktów; badge jest usuwany z DOM, żeby przełącznik widoku punktów go nie
  przywracał). Z 12.2 i 17.2 usunięte powtórki treści ("Dana jest ta sama funkcja...").
- [ZROBIONE 2026-07-05] Rysunek do zad 30: zad30/zad30.png wycięty ze strony 28 arkusza
  CKE (pdftoppm -x/-y/-W/-H, 150 dpi) i wstawiony do treści zadania.
- [ZROBIONE 2026-07-05] Przycisk ✕ tablicy wzorów powiększony (40px), pogrubiony,
  z ramką i mocniejszym cieniem; ten sam styl dostał ✕ panelu zasad oceniania.
- [ZROBIONE 2026-07-05] Komentarze ✓/✗ w widżetach (np. "✓ największe pole przy
  x = 24/13" w zad 30) są teraz w osobnej linijce (po <br>); .widget-readout ma
  min-height na 2 linijki, żeby nic nie skakało. Dotyczy widżetów 1, 5, 9, 10,
  12.1, 15, 18, 20, 30.
- [ZROBIONE 2026-07-05] "Płynne przewijanie" paska postępu wideo: zamiast zdarzeń
  timeupdate (~4/s) + transition w CSS (to dawało gumowate ruchy) pasek rysuje pętla
  requestAnimationFrame działająca tylko podczas odtwarzania. Transition usunięty.
- [ZROBIONE 2026-07-05] Widżet zad 1 (oś liczbowa): niebieskie strzałki odległości b
  na dwóch różnych wysokościach i skrócone z obu końców (już się nie zlewają);
  etykieta "−a" usunięta; okienko a ma zieloną ramkę (jak punkt środka −a na osi),
  okienko b niebieską (jak strzałki); punkt testowy x jest ciemnożółty, po trafieniu
  dostaje zieloną obwódkę; dodany przycisk "↺ reset" (a=4, b=7, x=0).
- [ZROBIONE 2026-07-05] Snap (przyklejanie) w widżetach z przeciąganym punktem:
  wspólny helper wgPrzyciagnij; zad 1 (rozwiązania i środek), zad 9 (−1 i 7),
  zad 12.1 (wierzchołek x=3), zad 18 (kąt z sin α = √3/4 po obu stronach).
- [ZROBIONE 2026-07-05] Przycisk "Pokaż zasady oceniania" po lewej stronie paska +
  panel z oficjalnym PDF-em CKE (arkusze PDF/...-odpowiedzi.pdf, spacja w ścieżce
  zakodowana jako %20). Działa jak tablica wzorów, tylko przypięty do lewej.
- [ZROBIONE 2026-07-05] Zaznaczone/ocenione odpowiedzi mają optycznie 2× grubszą ramkę:
  box-shadow inset w kolorze ramki (prawdziwe pogrubienie border przesuwałoby layout).
  Dotyczy .correct/.incorrect/.selected w ABCD, PF, multiSelect, samoocenie i fillIn.
- [ZROBIONE 2026-07-05] Zapisywanie postępu: localStorage (klucz
  matematykazen-postep-grudzien2024) trzyma "co użytkownik kliknął/wpisał"; przy
  wczytaniu strony postęp wraca przez SYMULACJĘ tych samych kliknięć (ta sama ścieżka
  oceniania, zero drugiej logiki). Zapis o innej liczbie zadań jest ignorowany.
  Na dole arkusza przycisk "wyczyść zapisany postęp".
- [ZROBIONE 2026-07-05] Przycisk "pokaż wszystkie rozwiązania" w pasku — przełącznik
  (pokaż/schowaj), klika przyciski "Rozwiązanie" poszczególnych zadań, pomijając te
  już w docelowym stanie (na prośbę Henricha działa też w drugą stronę — chowa).
- [ZROBIONE 2026-07-05] Tablica wzorów (i panel zasad) "odblokowana": przesuwanie za
  górny pasek-uchwyt, zmiana rozmiaru za narożnik ◢; pointer capture na uchwytach,
  bo <object> z PDF-em połyka zdarzenia myszy.
- [ZROBIONE 2026-07-05] Pola na własny tekst (punkt z sekcji "sprawdź czy zrobione"):
  nowy typ zadania fillIn (pole blanks w exercises.js) z przyciskiem "Sprawdź"
  i zielonymi/czerwonymi ramkami pól; zad 10 (4 przedziały) i zad 29 (średnia,
  mediana) przełączone z samooceny na fillIn. Odpowiedzi porównywane po normalizacji
  (spacje, ⟨⟩/<>/[], minus typograficzny, ; vs ,; warianty 6,38/6.38/319/50).
- [ZROBIONE 2026-07-05] Audyt sekcji "SPRAWDŹ CZY PONIŻSZE SĄ ZROBIONE": rysunki
  zad 19 i 20 były już na miejscu (zad19/zad19.png, zad20/zad20.png), tabela zad 29
  poprawna, crop do zad 30 dodany w tej sesji (patrz wyżej) — punkt zamknięty.
- [ODNOTOWANE] Pozytywny feedback od Henricha: rozwiązanie zad 5 (procent składany)
  i kolorowanie punktów w zależności od wyniku — zostawione jak jest. Pytanie
  o ujemny playback rate: pola prędkości nie ma już w UI (playbackRate na sztywno 1),
  przeglądarki i tak nie odtwarzają wstecz — nic do roboty.

--- FEEDBACK FABLE (2026-07-05) do prośby "sprawdź poprawność rozwiązań i oceń" ---
- [OPUS DID WELL] zad 17.1: treść, rysunek (zad17/zad17.png) i rozwiązanie są ZGODNE.
  Kąt prosty jest przy A (AB i AC to przyprostokątne), przeciwprostokątna to BC = 8,
  więc sin(∠ABC) = AC/BC = √15/8 — odp. D, potwierdzona w oficjalnym kluczu CKE
  (odp.txt: "Rozwiązanie D"). Nie było czego poprawiać.
- [OPUS DID POORLY, POPRAWIONE PRZEZ FABLE] zad 12 i 17 oddzielenie od podzadań: wstęp 12
  był wklejony w treść 12.1, a wstęp 17 (z rysunkiem) w 17.1. Poprawione: 12 i 17 są
  teraz osobnymi, "pustymi" elementami exercises (maxScore: 0 — bez odpowiedzi, punktów,
  podpowiedzi i rozwiązań), a 12.1/12.2/17.1/17.2 zaczynają się od własnego numeru jak
  w arkuszu (usunięte też powtórki treści "Dana jest ta sama funkcja/trójkąt").
- [OPUS DID WELL] przyciski w 12.2: okno przesuwne już działa: gdy komplet odpowiedzi
  jest zaznaczony, klik nowej odpowiedzi automatycznie podmienia najdawniej wybraną,
  więc nic nie trzeba ręcznie odklikiwać. Osobne pole numberOfCorrectAnswers nie jest
  potrzebne — liczbę wymaganych odpowiedzi wyznacza długość correctAnswerIndices
  i skrypt obsługuje dowolną ich liczbę.
- [OPUS DID WELL] zad 29 tabela: tabela w exercises.js jest zgodna z oryginałem CKE:
  książki 4–8, liczby uczniów 5, 8, 12, 13, 12 (średnia 6,38, mediana 6,5 jak w kluczu).

--- Sesja 2026-07-06 (Fable): KaTeX offline + menu ⋯ + reset punktacji + anty-migotanie wideo ---
- [ZROBIONE 2026-07-06] KaTeX zvendorowany do repo (vendor/katex/: katex.min.js/css,
  auto-render.min.js, fonty woff2, LICENSE; wersja 0.16.11) — matematyka renderuje
  się w pełni offline. Ładowany synchronicznie w <head>; renderujMatematyke(el)
  (wrapper na renderMathInElement, delimitery \( \) i \[ \], throwOnError: false,
  guard na brak biblioteki) wołany na klonie każdego zadania oraz na każdym kroku
  step-by-step w showStep().
- [ZROBIONE 2026-07-06] Migracja CAŁEJ matematyki w exercises.js na KaTeX:
  <sub>/<sup>, unicode (𝑥₁, ⁵√5, ⅕, ²⁄₃...), spany .mathText → \( \) / \[ \]
  (wieloliniowe wyprowadzenia jako \[\begin{aligned}...\]). 422 wzory zweryfikowane
  automatycznie przez katex.renderToString — 0 błędów; suma punktów arkusza nadal 50.
  Konwencje: 6{,}38 (polski przecinek), \operatorname{tg}, przedziały \langle\rangle,
  wyniki \boldsymbol{} — opisane w komentarzu nagłówkowym exercises.js.
- [ZROBIONE 2026-07-06, bonus] Wzory-obrazki zastąpione KaTeXem: zad 2 (potęga
  z pierwiastkiem), zad 6 (wyrażenie + wszystkie 4 odpowiedzi), zad 7 (układ równań,
  \begin{cases}), zad 8 (równanie wymierne), zad 10 (definicja funkcji przedziałami,
  \begin{cases}) — przepisane 1:1 z PNG. W treściach zostały tylko prawdziwe rysunki
  (zad 10 wykres, 11, 17, 19, 20, 30). Nieużywane PNG zostają na dysku (prowieniencja).
- [ZROBIONE 2026-07-06] Przycisk ⋯ (#menu-button) w prawej strefie paska + okienko
  #bar-menu (fixed, pod paskiem, zamykane klikiem poza): przeniesione tam
  "pokaż/schowaj wszystkie rozwiązania" i "widok punktów" (te same ID, ta sama
  logika) + NOWY "resetuj punktację" (#reset-scores: localStorage.removeItem +
  reload — jedna wspólna ścieżka zerowania ze świeżym renderem).
- [ZROBIONE 2026-07-06, do testu wzrokowego] Migotanie przy przełączaniu kroków:
  podwójny bufor w showStep() — nowy krok budowany w odłączonym divie, a gdy
  poprzedni krok jest na ekranie i nowy ma film, podmiana (replaceChildren) czeka
  na loadeddata nowego filmu (skrót readyState>=2 dla cache, fallback setTimeout
  1,5 s); autoplay zdjęty, video.play() dopiero po wstawieniu; stepSwapToken +
  flaga krokWstawiony chronią przed wyścigami (szybkie ◄/►, loadeddata+timeout).
  Nawigacja (licznik, strzałki, markCorrectAnswer) aktualizuje się od razu.
- [ZROBIONE 2026-07-06] Przyciski odpowiedzi: width → min-width (22% ABCD / 30%
  multiSelect) + white-space: nowrap — dłuższy wzór poszerza przycisk zamiast
  łamać "A." nad wzór; krótkie odpowiedzi trzymają równą siatkę. Rozmiar wzorów:
  .katex { font-size: 1.08em }.
- [SPRAWDZONE 2026-07-06] Test Playwright (chromium): ABCD/PF/multiSelect/fillIn,
  punktacja i suma, zapis/odczyt postępu, menu ⋯ (otwieranie, zamykanie klikiem
  poza, wszystkie 3 akcje), reset punktacji (0/50 po resecie), kroki wideo
  z podwójnym buforem, KaTeX w komentarzach kroków. Jedyne błędy konsoli to
  fonts.googleapis.com (brak internetu w sandboksie testowym) — nie dotyczy zmian.
- [ZROBIONE 2026-07-06, własna inwencja] Responsywność (wąskie ekrany): sekcja
  RESPONSYWNOŚĆ na końcu style.css. Breakpointy: 1024px (badge punktów wraca do
  wnętrza karty — poza kartą mieści się dopiero od ~1010px okna), 900px (tytuł
  arkusza w pasku znika), 720px (kompaktowy pasek, płynna szerokość karty,
  skalowanie filmów przez aspect-ratio, przyciski odpowiedzi 38% z wyjątkiem
  P/F 44px, panele PDF 94%), 560px (pasek w dwóch rzędach: logo+zasady /
  punkty+tablica+⋯). Szerokie wzory blokowe: .katex-display { overflow-x: auto }.
  Zweryfikowane sweepem Playwright: zero poziomego scrolla przy 360-1280px,
  desktop bez zmian. Ikonka "M" dodana też do index.html.
