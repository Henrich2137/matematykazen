# SOLUTION_TEXT_RULES.md

Jak pisać **rozwiązanie zwykłe**, czyli pole `solutionText` w `matura/<arkusz>/exercises.json`.
Zasady Henricha, ustalone 2026-08-21 na zadaniu 2 z arkusza 2024-grudzień i doprecyzowane
tego samego dnia na zadaniu 3. Wzorce do podejrzenia: te dwa zadania (2 zamknięte, 3 otwarte).

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
  innej linijki. Wzorce: zad. 2, 3 i 4.
- **Dwa tory** (`<div class="rozw-2kol rozw-dwatory">`), gdy zadanie każe policzyć dwie
  rzeczy niezależnie, a dopiero na końcu je połączyć: rachunki idą obok siebie, a wiersze
  wspólne (dane na starcie, wynik na końcu, odpowiedź) dostają `rozw-pelny` i rozpinają się
  na obie kolumny. Wzorzec: zad. 7, gdzie osobno liczy się \(a\), osobno \(b\), a na końcu
  ich iloczyn. Układ ma pokazywać to samo, co film.

## Dwie kolumny

7. **Rachunek z lewej, użyty wzór z prawej**, na tej samej wysokości co linijka, w której się
   go stosuje.
8. **Wzór stoi przy stanie SPRZED swojego zastosowania**, nie po.
9. **Linijka bez wzoru** (sam rachunek na liczbach) ma pustą prawą komórkę. Pustej komórki
   nie wolno pominąć, bo siatka przesunie następny rachunek do prawej kolumny.
10. **Kilka linijek rachunku pod jednym wzorem** idzie w jednym `.rozw-obl`, rozdzielone `<br>`.
    Wzór stanie wtedy na środku całej grupy.

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

## Praca z plikiem

22. **`exercises.json` poprawiaj tekstowo, nie przez `json.dumps`.** Plik jest formatowany
    ręcznie (elementy tablicy na tym samym wcięciu co klucz), więc przepisanie go całego
    biblioteką daje diff na tysiąc linijek zamiast na pięć. Bezpieczny sposób: wczytaj plik
    jako TEKST, znajdź w nim starą wartość zakodowaną `json.dumps(stara)` i podmień na
    `json.dumps(nowa)`, na koniec sprawdź, że `json.loads` przechodzi.

23. **Zmieniasz `solutionText`, przerenderuj film** (`tools/wgraj-kroki.sh <nr>`), i odwrotnie.
    Linijki i kroki są parami; rozjazd widać dopiero na stronie, kiedy podpis pod filmem mówi
    co innego niż zapis obok.

## Sprawdzenie

24. **Obejrzyj na zrzucie**: komputer i telefon, jasny i ciemny motyw.
25. **Strona nie ma się przewijać w bok**, a siatka nie ma się obcinać
    (`scrollWidth === clientWidth`, `el.scrollWidth - el.clientWidth === 0`).
26. **Policz linijki i kroki filmu.** Muszą się zgadzać.
