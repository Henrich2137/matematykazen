# SOLUTION_TEXT_RULES.md

Jak pisać **rozwiązanie zwykłe**, czyli pole `solutionText` w `matura/<arkusz>/exercises.json`.
Zasady Henricha, ustalone 2026-08-21 na zadaniu 2 z arkusza 2024-grudzień i doprecyzowane
tego samego dnia na zadaniach 3, 4, 6, 7 i 8. Wzorce do podejrzenia, wszystkie w 2024-grudniu:

| zadanie | czego jest wzorcem |
|---|---|
| 1 | dwa tory dla dwóch przypadków (wartość bezwzględna), schodzące się w sumie na końcu |
| 2 | dwie kolumny w równych połówkach karty (`rozw-polowki`), wzór przy każdej linijce, zielony przy każdym wzorze |
| 3 | to samo w zadaniu na wykazanie, na końcu wniosek zamiast „Odpowiedź X." |
| 4 | wąskie rozwiązanie wyśrodkowane na karcie (`rozw-srodek`) |
| 6 | jedna kolumna, jeden wzór na górze, ułamki przez `\dfrac` |
| 7 | dwa tory obok siebie, które na końcu schodzą się w jeden, z komentarzami **wewnątrz** siatki |
| 8 | dwa tory **wewnątrz** rozwiązania jednokolumnowego, komentarze tylko w trudnych przejściach, przerwa między częściami, odkreślone sprawdzenie |
| 9 | to samo w zadaniu z deltą: ogniwa (\(x \cdot x - x \cdot 6\), \(-(-6)\), \(\dfrac{-2}{2}\)) mają własne linijki, a wniosek z rysunku (ramiona paraboli) stoi jako zwykłe zdanie w linijce |
| 10 | zadanie bez rachunku, sam odczyt z wykresu: cztery części z wytłuszczonym nagłówkiem wtopionym w pierwszą linijkę, przedział budowany z dwóch końców, zdanie zamykające podaje odpowiedzi w zapisie z polecenia |

Bliźniaczy plik dla filmów: `manimations/README.md`, sekcja „Zasady krok po kroku, wersja krótka".
Wygląd i nazwy klas CSS: `ARCHITECTURE_CSS.md`. Znaczenie kolorów: `COLORS.md`.

## Linijki

1. **Zaczynaj od wyrażenia, które stoi w treści zadania.** Nie od fragmentu wyjętego z boku.
2. **Jedna linijka = jedno wyrażenie**, całe, po jednym przekształceniu.
3. **Jedna linijka = jeden wzór.** Dwa przekształcenia naraz rozbij na dwie linijki.
4. **Żadnych znaków `=` na początku ani na końcu linijki.** Same wyrażenia, jedno pod drugim.
5. **Ostatnia linijka idzie przez całą szerokość, wyśrodkowana.** W zadaniu zamkniętym jest
   to `Odpowiedź X.`, w zadaniu na wykazanie zdanie z wnioskiem („… więc iloczyn dzieli się
   przez 21, co należało wykazać"). Sam wynik rachunku, wytłuszczony, zostaje linijkę wyżej,
   w kolumnie rachunku.
6. **Tyle linijek, ile kroków filmu**, jeden do jednego, ale **domyślnie, a nie za wszelką
   cenę** (Henrich, 2026-08-30: „rozwiązania krok po kroku i zwykłe nie muszą być koniecznie
   ze sobą zgrane, szczególnie jeśli miałoby to zaszkodzić uczniowi w zrozumieniu któregoś
   z nich"). Zaczynasz od jeden do jednego. Rozjazd wolno zrobić wtedy, gdy trzymanie się go
   psuje którąś formę: film ma kroki, których tekst nie potrzebuje (sprzątanie kadru,
   podsumowanie z obiema postaciami wzoru), a tekst ma zdania, które w filmie są komentarzem
   pod kadrem, a nie osobną kropką. Zmieniasz tu, **przejrzyj film** i albo popraw, albo
   świadomie zostaw rozjazd.

## Który układ wybrać

Trzy układy, wybór zależy od tego, ile jest wzorów z tablicy i czy rachunek idzie
jednym torem.

- **Jedna kolumna** (`<div class="rozwiazanie-kroki">`, linijki rozdzielone `<br>`), gdy
  wzoru z tablicy nie ma wcale albo jest **jeden i stosuje się go na starcie**. Wzór stoi
  wtedy nad rachunkiem, wyśrodkowany przez `\[ … \]`, a pod nim idą same linijki.
  Wzorce: zad. 5, 6 i 8 z 2024-grudnia.
- **Dwie kolumny** (`<div class="rozw-2kol">`), gdy wzorów jest kilka i każdy należy do
  innej linijki, a rachunek jest na tyle szeroki, że wzór dopisany pod nim rozbiłby czytanie.
  Wzorce: zad. 2, 3 i 4. Ten układ jest **chciany**, nie tymczasowy (Henrich, 2026-08-23,
  na zad. 2 z 2024-grudnia): nie spłaszczaj go do jednej kolumny tylko po to, żeby wszystko
  szło jedno pod drugim. Linijki rachunku i tak stoją jedna pod drugą, wzory jadą obok nich.
- **Dwa tory** (`<div class="rozw-2kol rozw-dwatory">`), gdy zadanie każe policzyć dwie
  rzeczy niezależnie, a dopiero na końcu je połączyć: rachunki idą obok siebie, a wiersze
  wspólne (dane na starcie, wynik na końcu, odpowiedź) dostają `rozw-pelny` i rozpinają się
  na obie kolumny. Wzorzec: zad. 7, gdzie osobno liczy się \(a\), osobno \(b\), a na końcu
  ich iloczyn. Układ ma pokazywać to samo, co film.
  Krótszy tor kończy się wyżej: **pusta komórka idzie na KONIEC tej kolumny, nie w jej
  środek** (Henrich, 2026-08-21). Dziura w środku wygląda jak zgubiona linijka.

**Ostrzeżenie o telefonie, zmierzone 2026-08-27 na roboczej wersji zad. 8.** Dwie kolumny kosztują dużo
miejsca: przy oknie 390 px kolumna wzorów bierze 104 px, przerwa między kolumnami 40 px,
więc na rachunek zostaje 154 px z 298 px bloku. Linijka dłuższa niż mniej więcej
\(2x^{2} + 4x - 6 = x^{2} - x\) łamie się wtedy w przypadkowym miejscu (KaTeX nie łamie
wzoru mądrze), a ułamek rozjeżdża się na dwa wiersze i wygląda jak inne wyrażenie. Zanim
wybierzesz dwie kolumny do długiego rachunku, zrób zrzut telefonu: jeśli łamie się więcej
niż kilka linijek, oddaj kolumnę wzorów i przenieś wzory nad rachunek.

## Dwie kolumny

7. **Rachunek z lewej, użyty wzór z prawej**, na tej samej wysokości co linijka, w której się
   go stosuje.
8. **Wzór stoi przy stanie SPRZED swojego zastosowania**, nie po.
9. **Linijka bez wzoru** (sam rachunek na liczbach) ma pustą prawą komórkę. Pustej komórki
   nie wolno pominąć, bo siatka przesunie następny rachunek do prawej kolumny.
10. **Kilka linijek rachunku pod jednym wzorem** idzie w jednym `.rozw-obl`, rozdzielone `<br>`.
    Wzór stanie wtedy na środku całej grupy.

## Komentarze między linijkami (od 2026-08-27)

Zasada Henricha z 2026-08-27, wprowadzona na zad. 8. Dotyczy układu jednokolumnowego.

**Nie pod każdą linijką** (doprecyzowane 2026-08-28, znowu na zad. 8). Komentarz pod każdym
przejściem zamienia rozwiązanie w ścianę tekstu, w której rachunek ginie. Zdanie należy się
przejściu, które spełnia jeden z dwóch warunków:

- **uczeń nie zobaczy, skąd się coś wzięło** (skąd pomysł na wspólny nawias, po co dopisujemy
  jedynkę przy iksie), albo
- **zmienia się dużo naraz** (skracanie \((x-1)\) po obu stronach: znikają cztery nawiasy
  i jeden ułamek).

Przejścia oczywiste (przeniesienie składnika na drugą stronę, policzenie \(2 \cdot 3\))
zostają bez komentarza, bo widać je w samym zapisie. W zad. 8 wychodzi z tego siedem
komentarzy na dziewiętnaście linijek.

15a. **Między linijkami rachunku wolno napisać, co się w przejściu dzieje.** Jedno zdanie,
     w `<div class="rozw-komentarz">`, bledsze od rachunku (ten sam token co kolumna wzorów).
     Rachunek czyta się pierwszy, komentarz drugi.
15b. **Linijki idą wtedy w `<div class="rozw-linia">`, nie przez `<br>`.** Div sam łamie
     wiersz, a komentarz ma własny, ciaśniejszy odstęp.
15c. **Komentarz mówi o przejściu do NASTĘPNEJ linijki**, więc stoi pod tą, z której
     wychodzimy, i przykleja się do niej z góry.
15d. **Nie opisuj tego, co widać.** „Mnożymy obie strony przez \(x-1\)" ma sens tylko wtedy,
     gdy dopisuje coś ponad sam zapis (tu: że nawias dopisuje się w obu licznikach).
15e. **Komentarz nie zastępuje rozbicia kroku.** Jeśli przejście robi dwie rzeczy naraz,
     rozbij je na dwie linijki, a nie tłumacz zdaniem.
15f. **Sprawdzenie wyniku idzie w `<div class="rozw-sprawdzenie">`**, czyli pod szerszy
     odstęp, na dole (kreska stała tam do 2026-08-29; Henrich: „wygląda to jakby było
     oddzielną częścią niż rozwiązanie zwykłe", więc została sam odstęp tej samej wielkości).
     Po samym słowie **Sprawdzenie.** idzie nowa linijka, a zdanie wyjaśniające pod nim
     jest komentarzem, nie dalszym ciągiem nagłówka. Rachunek punktowany przez CKE kończy się wyżej, na wyniku, więc ma być widać,
     że zaczyna się część dobrowolna. Podstawiając liczbę ujemną, pisz ją **w nawiasie**
     (\((-6) + 3\), nie \(-6 + 3\)): to jedno z miejsc, w których uczniowie gubią znak.
15g. **Komentarz niesie OGNIWO, którego w rachunku nie widać** (dopisane 2026-08-27, po
     przerobieniu filmu do zad. 8). To, co ekspert liczy w głowie, wypisz w komentarzu jako
     jeden ciąg równości: \(2x - 2 = 2 \cdot x - 2 \cdot 1 = 2(x - 1)\),
     \(2 \cdot x = 2x\) oraz \(2 \cdot 3 = 6\), \(x\) to inaczej \(1x\). Linijka
     rachunku zostaje krótka, a uczeń, który nie widzi przejścia, ma je pod nosem.
15i. **Między zdaniem a rachunkiem musi być przerwa** (Henrich, 2026-08-28: „nie mają być
     ściśnięte"). Robi to CSS, nie `<br>`. Osobna przerwa, szersza, oddziela CAŁE części
     rozwiązania: po wyliczeniu dziedziny idzie `class="rozw-odstep"` na pierwszym elemencie
     następnej części, żeby było widać, że zaczyna się nowa rzecz.
15h. **Film i tekst tłumaczą TO SAMO, w tym samym miejscu.** Jeśli film pokazuje w kroku N
     rachunek pomocniczy (patrz `manimations/README.md`, „Wyjaśnienie w środku kroku"), to
     komentarz przy linijce N mówi to samo słowami. Dwie różne wersje tego samego przejścia
     są gorsze niż jedna.

Szkielet do przeklejania:

```html
<div class="rozwiazanie-kroki">
  <div class="rozw-linia">\(2x + 6 = x\)<span class="rozw-dzialanie">\(\big/ - 6\)</span></div>
  <div class="rozw-komentarz">Liczby zbieramy po prawej stronie. Szóstka przechodzi ze zmianą znaku.</div>
  <div class="rozw-linia">\(2x = x - 6\)</div>
</div>
```

## Komentarz w układzie dwutorowym (od 2026-08-29)

15m. **W układzie dwutorowym komentarz idzie WEWNĄTRZ siatki**, jako wiersz rozpięty na obie
     kolumny, a nie między dwoma blokami `.rozw-2kol`:

     ```html
     <div class="rozw-wiersz rozw-pelny">
       <div class="rozw-komentarz">zdanie o przejściu w OBU torach</div>
     </div>
     ```

     Powód jest mechaniczny: każdy blok `.rozw-2kol` liczy szerokość kolumn osobno
     (`width: fit-content`), więc rozbicie rachunku na kilka bloków przedzielonych zdaniami
     rozjeżdża tory w pionie. Cały blok musi zostać jeden.
15n. **Jedno zdanie opisuje przejście w obu torach naraz**, bo wiersz jest wspólny:
     „Po lewej \(3 \cdot 6 = 18\). Po prawej \(-1\) przechodzi na drugą stronę ze zmianą
     znaku". Osobne zdanie dla każdego toru zrobiłoby z komentarza trzecią kolumnę.

## Linijka, w której stoi kilka wartości naraz (od 2026-08-28)

Chodzi o linijki typu „Współczynniki: \(a = 1\), \(b = -6\), \(c = -7\)" albo o zestaw
wyników cząstkowych. To wyjątek od zasady „jedna linijka, jedno wyrażenie": wartości są
odczytane naraz, z jednego zapisu, więc rozbijanie ich na trzy linijki niczego nie tłumaczy.

15j. **Rozdziel je odstępem, nie samym przecinkiem** (Henrich, 2026-08-28, zad. 9: „rozdziel
     te współczynniki troszeczkę, aby były bardziej czytelne"). Trzy równości postawione
     blisko siebie czytają się jak jedno długie wyrażenie.
15k. **I zaraz to zmierz na telefonie.** Przy oknie 485 px linijka z trzema równościami jest
     już blisko krawędzi, a KaTeX nie łamie wzoru mądrze: rozsuwanie na oko potrafi wypchnąć
     ostatnią wartość poza kartę. Zrzut telefonu jest tu obowiązkowy, nie opcjonalny.
15l. **W filmie ta sama linijka ma być MNIEJSZA od rachunku** (`manimations/README.md`,
     punkt 41). To jest odczyt odstawiony z boku, a nie kolejny krok przekształcenia.

## Kolor

11. **Zielony to `--accent-green`**, wołany z JSON-a jako `\htmlClass{zielony}{...}` wewnątrz
    wzoru KaTeX. Nie wpisuj `\textcolor` z gotowym hexem: nie zmieni się w ciemnym motywie.
12. **Zielony zaznacza fragment, do którego odnosi się wzór, PO OBU STRONACH**: kawałek
    rachunku, który zaraz się zmieni, i tę stronę wzoru, która się do niego dopasowuje.
    Zaznaczasz **to, co się zmienia**: znika, pojawia się, zmienia wartość albo zmienia rolę.
    Co tylko wędruje w inne miejsce zapisu, a dalej znaczy to samo, zostaje bez koloru.
    Ta sama reguła obowiązuje w filmie, patrz `manimations/README.md`.
13. **Nie zaznaczaj, gdy wzór dotyczy całego wyrażenia.** Nie ma wtedy czego wskazywać.
    Tak samo linijka bez wzoru nie ma koloru: zielony zawsze idzie w parze ze wzorem obok.
14. **Nawiasów nie koloruj.** Kolor noszą liczby i litery, nawet gdy nawias właśnie
    się pojawia albo znika. To samo obowiązuje w filmie.

15. **Zielony nie znaczy „dobrze".** Zieleń poprawności to inny token, patrz `COLORS.md`.

## Wzory

16. **W prawej kolumnie stoją tylko wzory z tablicy** (`tablica-wzorow-transkrypt/`).
    Czego w tablicy nie ma, tego tam nie wpisuj: komórka zostaje pusta, a wyjaśnienie
    idzie do opisu kroku pod filmem. Zasada Henricha, 2026-08-21, na wyłączaniu
    wspólnego czynnika przed nawias.

## Znaczniki

17. Szkielet do przeklejania:

```html
<div class="rozw-2kol">
  <div class="rozw-wiersz">
    <div class="rozw-obl">\(rachunek\)</div>
    <div class="rozw-wzor">\(wzór\)</div>
  </div>
  <div class="rozw-wiersz">
    <div class="rozw-obl">\(rachunek bez wzoru\)</div>
    <div class="rozw-wzor"></div>
  </div>
  <div class="rozw-wiersz rozw-pelny">
    <div class="rozw-obl">Odpowiedź <b>A</b>.</div>
  </div>
</div>
```

18. **Ułamki pisz `\dfrac`, nie `\frac`.** W linijce `\( … \)` KaTeX składa `\frac`
    w wersji tekstowej, czyli z licznikiem i mianownikiem tak małymi, że na komputerze
    ledwo je widać (Henrich, 2026-08-21, na zad. 6).
19. Cała matematyka w **KaTeX**, `\( ... \)` w linijkach. Pamiętaj, że JSON wymaga `\\`.
20. **Bez myślników i półpauz** w tekście (zasada ogólna projektu, `CLAUDE.md`).
20a. **Bez nazw liter zapisanych słowami.** Nie „iks", tylko \(x\) (zasada ogólna projektu,
    `CLAUDE.md`). Zdanie, które musiałoby odmieniać nazwę litery, przepisz na rachunek:
    zamiast „dwa iksy bez jednego iksa to jeden iks" napisz \(2x - 1x = 1x\).
20b. **Zdania krótkie.** Wyrzuć części, które nic nie wnoszą („Wracamy do równania",
    „a o to nam chodziło"). Henrich, 2026-08-28.

## Ustawienie bloku

21a. **Przerwa między kolumnami ma wypadać na środku karty** (Henrich, 2026-08-30, zad. 2).
    Domyślne ustawienie liczy szerokość kolumn z ich treści i dosuwa całość do lewej, więc
    przy wąskiej kolumnie wzorów obie kolumny zbijają się w lewy górny róg, a prawa połowa
    karty stoi pusta. Blok dostaje wtedy `class="rozw-2kol rozw-polowki"`: każda kolumna
    bierze połowę karty, rachunek dobija do środka z lewej, wzór idzie od środka w prawo.
    Nie stosuj tego do bloku, w którym rachunek i tak jest szeroki (zad. 3): tam kolumny
    same wypełniają kartę, a wymuszona połowa tylko rozerwałaby parę.

21. **Blok stoi domyślnie przy lewej krawędzi karty.** Wąskie rozwiązanie (kilka krótkich
    linijek) wygląda przy niej na zgubione, więc dostaje `class="rozw-2kol rozw-srodek"`
    i wraca na środek. Szerokie zostawiaj bez tej klasy. Decyzja jest na oko, na zrzucie.

## Zadania otwarte

22. **Założenie (dziedzina) idzie NA GÓRĘ, nad rachunek**, razem z jednym zdaniem, skąd się
    wzięło („mianownik nie może być zerem, oba zerują się dla \(x=1\)"). CKE daje za nie
    osobny punkt, więc ma być widoczne, a nie schowane w środku rachunku.
    **Podpisz je słowem.** Sama linijka \(x \ne 1\) nie mówi uczniowi, czym jest, więc
    stoi przed nią etykieta „Założenie (dziedzina):" (Henrich, 2026-08-28, zad. 8). To jedyne
    miejsce, w którym linijka rachunku ma przy sobie zwykły tekst.
    Osobny akapit nad blokiem nie jest do tego potrzebny: założenie jest po prostu jedną
    z pierwszych linijek rachunku. W zad. 8 (wersja z 2026-08-28) idzie jeszcze dalej i samo
    **wyprowadzenie** dziedziny stoi na górze, dwoma torami, po jednym na każdy mianownik,
    a wytłuszczony wspólny warunek zamyka tę część.
23. **Ostatnia linijka sprawdza założenie i ogłasza wynik**: „wynik spełnia założenie, bo
    \(-6 \ne 1\), więc rozwiązaniem równania jest \(x=-6\)".
24. **Działanie wykonywane na obu stronach zapisuj po szkolnemu, na tej samej linijce**:
    `\big/ \cdot (x-1)`. To nie jest wzór, więc nie idzie do kolumny wzorów. Od 2026-08-27
    idzie **w osobnym `<span class="rozw-dzialanie">` obok wzoru**, nie w środku tego samego
    `\( … \)`: jest wtedy odsunięty i bledszy, a na telefonie zawija się w całości pod
    rachunek, zamiast łamać rachunek w środku ułamka.

## Praca z plikiem

25. **`exercises.json` poprawiaj tekstowo, nie przez `json.dumps`.** Plik jest formatowany
    ręcznie (elementy tablicy na tym samym wcięciu co klucz), więc przepisanie go całego
    biblioteką daje diff na tysiąc linijek zamiast na pięć. Bezpieczny sposób: wczytaj plik
    jako TEKST, znajdź w nim starą wartość zakodowaną `json.dumps(stara)` i podmień na
    `json.dumps(nowa)`, na koniec sprawdź, że `json.loads` przechodzi.

26. **Zmieniasz `solutionText`, przerenderuj film** (`tools/wgraj-kroki.sh <nr>`), i odwrotnie.
    Linijki i kroki są parami; rozjazd widać dopiero na stronie, kiedy podpis pod filmem mówi
    co innego niż zapis obok. **Zgadzać ma się nie tylko liczba**, ale i treść: ta sama droga,
    te same ogniwa pośrednie, ten sam warunek w tym samym miejscu (patrz 15g i 15h).

## Sprawdzenie

27. **Obejrzyj na zrzucie**: komputer i telefon, jasny i ciemny motyw.
28. **Strona nie ma się przewijać w bok**, a siatka nie ma się obcinać
    (`scrollWidth === clientWidth`, `el.scrollWidth - el.clientWidth === 0`).
29. **Policz linijki i kroki filmu.** Muszą się zgadzać.
