# SOLUTION_TEXT_RULES.md

Jak pisać **rozwiązanie zwykłe**, czyli pole `solutionText` w `matura/<arkusz>/exercises.json`.
Zasady Henricha, ustalone 2026-08-21 na zadaniu 2 z arkusza 2024-grudzień i doprecyzowane
tego samego dnia na zadaniach 3, 4, 6, 7 i 8. Wzorce do podejrzenia, wszystkie w 2024-grudniu:

| zadanie | czego jest wzorcem |
|---|---|
| 2 | dwie kolumny, wzór przy każdej linijce, zielony przy każdym wzorze |
| 3 | to samo w zadaniu na wykazanie, na końcu wniosek zamiast „Odpowiedź X." |
| 4 | wąskie rozwiązanie wyśrodkowane na karcie (`rozw-srodek`) |
| 6 | jedna kolumna, jeden wzór na górze, ułamki przez `\dfrac` |
| 7 | dwa tory obok siebie, które na końcu schodzą się w jeden |
| 8 | linijki przeplecione bledszymi komentarzami, dopisek działania w osobnym spanie |

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
6. **Tyle linijek, ile kroków filmu**, jeden do jednego. Zmieniasz tu, przerenderuj film.

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

Szkielet do przeklejania:

```html
<div class="rozwiazanie-kroki">
  <div class="rozw-linia">\(2x + 6 = x\)<span class="rozw-dzialanie">\(\big/ - 6\)</span></div>
  <div class="rozw-komentarz">Liczby zbieramy po prawej stronie. Szóstka przechodzi ze zmianą znaku.</div>
  <div class="rozw-linia">\(2x = x - 6\)</div>
</div>
```

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

## Ustawienie bloku

21. **Blok stoi domyślnie przy lewej krawędzi karty.** Wąskie rozwiązanie (kilka krótkich
    linijek) wygląda przy niej na zgubione, więc dostaje `class="rozw-2kol rozw-srodek"`
    i wraca na środek. Szerokie zostawiaj bez tej klasy. Decyzja jest na oko, na zrzucie.

## Zadania otwarte

22. **Założenie (dziedzina) idzie NA GÓRĘ, nad rachunek**, razem z jednym zdaniem, skąd się
    wzięło („mianownik nie może być zerem, oba zerują się dla \(x=1\)"). CKE daje za nie
    osobny punkt, więc ma być widoczne, a nie schowane w środku rachunku.
    W układzie z komentarzami wygląda to tak, że **założenie jest DRUGĄ linijką**, zaraz pod
    zapisem z treści, a zdanie o mianowniku stoi nad nim jako komentarz (Henrich, 2026-08-27,
    zad. 8). Osobny akapit nad blokiem przestaje być wtedy potrzebny.
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
    co innego niż zapis obok.

## Sprawdzenie

27. **Obejrzyj na zrzucie**: komputer i telefon, jasny i ciemny motyw.
28. **Strona nie ma się przewijać w bok**, a siatka nie ma się obcinać
    (`scrollWidth === clientWidth`, `el.scrollWidth - el.clientWidth === 0`).
29. **Policz linijki i kroki filmu.** Muszą się zgadzać.
