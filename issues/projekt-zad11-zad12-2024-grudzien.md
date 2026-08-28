# Projekt: zadania 11 i 12, arkusz 2024-grudzień

Dokument projektowy (co ma zobaczyć uczeń), nie instrukcja techniczna. Powstał 2026-08-28,
po zad. 9 i 10. Zapis do repozytorium rządzi się osobnymi plikami: `SOLUTION_TEXT_RULES.md`,
`manimations/README.md`, `COLORS.md`.

Zadanie 12 to wiązka: 12.1, 12.2 i 12.3. Cztery rozwiązania, cztery filmy.

## Stan wyjściowy

Wszystkie cztery mają dziś jednoakapitowe `solutionText` napisane przed zasadami z sierpnia
(rachunek zbity w jedno zdanie, wynik i wniosek w tej samej linijce) i **żadnego filmu**.
Projekt zastępuje teksty w całości i dokłada cztery sceny.

## Wyniki policzone od zera i porównane z kluczem

| zadanie | mój rachunek | klucz CKE | zgodne |
|---|---|---|---|
| 11 | \(a = -2\) (P), pole \(= 4\), a nie \(8\) (F) | PF | tak |
| 12.1 | ramiona w dół, maleje w \(\langle 3,\ +\infty)\) | D | tak |
| 12.2 | \(f(x) = -(x-3)^{2} = -x^{2}+6x-9\) | BD | tak |
| 12.3 | brak miejsc zerowych (F), oś \(x = 3\) (P) | FP | tak |

Kryteria oceniania są we wszystkich czterech jednozdaniowe („1 pkt, odpowiedź poprawna"),
poza 12.2, gdzie 1 pkt należy się za jedną trafioną odpowiedź z dwóch. Nie ma tu etapów
do pokrycia, więc rozwiązanie ma po prostu dowieźć obie litery.

---

# Zadanie 11

## Metoda

Dwie niezależne części, liczone **po kolei** (`manimations/README.md`, punkt 4), tak jak
w zad. 7: najpierw cały współczynnik kierunkowy, potem całe pole. Wykres stoi w kadrze przez
cały film, rachunek rośnie obok niego, jak w zad. 10.

Współczynnik liczymy ze wzoru na prostą przez dwa punkty (\([11.5]\), s. 23 tablicy),
a nie z podstawiania do \(y = ax + b\): oba punkty są dane wprost, więc podstawienie jest
jedno zamiast dwóch, i widać na wykresie, skąd biorą się \(-4\) i \(2\).

Pole liczymy ze wzoru \(P = \tfrac{1}{2} a \cdot h_a\) (\([10.4]\), s. 16 tablicy).
Trójkąt jest prostokątny, więc podstawa i wysokość leżą na osiach.

## Ogniwa wypisane jawnie

- \(\dfrac{0 - 4}{2 - 0}\) przed \(\dfrac{-4}{2}\), bo tu uczeń najczęściej odejmuje
  w odwrotnej kolejności i wychodzi mu \(+2\),
- osobna linijka na to, **który** to trójkąt (trzy wierzchołki), zanim padnie jakikolwiek
  rachunek: „ograniczony osiami oraz wykresem" to zdanie, którego uczeń nie umie sobie
  narysować,
- osobna linijka na długości przyprostokątnych, zanim wejdą do wzoru.

## Linijki (osiem, jeden do jednego z krokami filmu)

| # | linijka | wzór z tablicy obok |
|---|---|---|
| 1 | Z wykresu: \(A = (0,\ 4)\), \(B = (2,\ 0)\) | |
| 2 | \(a = \dfrac{0 - 4}{2 - 0}\) | \(a = \dfrac{y_B - y_A}{x_B - x_A}\) |
| 3 | \(a = \dfrac{-4}{2}\) | |
| 4 | \(a = -2\), czyli tyle, ile mówi zdanie 1: **P** | |
| 5 | Trójkąt ma wierzchołki \((0,0)\), \((2,0)\), \((0,4)\) | |
| 6 | Podstawa \(2\), wysokość \(4\) | |
| 7 | \(P = \dfrac{1}{2} \cdot 2 \cdot 4\) | \(P = \dfrac{1}{2} a \cdot h_a\) |
| 8 | \(P = 4\), a w zdaniu 2 stoi \(8\): **F** | |
| — | Odpowiedź **PF**. | zdanie zamykające, nie jest krokiem |

## Kroki filmu

Kadr: po lewej układ współrzędnych z prostą (fiolet jak w arkuszu, podpis \(y = f(x)\)),
po prawej kolumna rachunku. Wykres i osie to scenografia, stoją przez cały film.

1. **Odczyt dwóch punktów.** Wjeżdża układ i prosta. Zapalają się dwa punkty na wykresie:
   \((0,\ 4)\) na osi \(y\) i \((2,\ 0)\) na osi \(x\); obok każdego pojawiają się
   współrzędne, które odjeżdżają do prawej kolumny jako \(A\) i \(B\). Bez rachunku.
2. **Wzór i podstawienie, dwutaktem** (README, punkt 37). Najpierw w kolumnie staje
   \(a = \dfrac{y_B - y_A}{x_B - x_A}\) samymi literami, potem każda litera zamienia się
   w liczbę, która przylatuje z odczytanego wcześniej punktu. Zielone są tylko litery
   zamieniane na liczby.
3. **Odejmowanie.** \(0 - 4\) zwija się w \(-4\), \(2 - 0\) w \(2\). Zielony licznik
   i mianownik.
4. **Dzielenie i werdykt.** \(\dfrac{-4}{2}\) zwija się w \(-2\). Obok zdania 1 pojawia się
   **P**. Litera jest czarna: to odpowiedź ucznia, nie ocena poprawności (`COLORS.md`).
5. **Który trójkąt.** Na wykresie zapalają się trzy wierzchołki i obrys trójkąta między
   osiami a prostą, wnętrze na słabo. Rachunek po prawej odjeżdża w górę i zostaje tam
   do końca filmu (jak wynik pierwszego toru w zad. 7).
6. **Przyprostokątne.** Odcinek na osi \(x\) od \(0\) do \(2\) i odcinek na osi \(y\)
   od \(0\) do \(4\) zapalają się po kolei, a przy nich staje \(2\) i \(4\).
7. **Wzór na pole i podstawienie, dwutaktem.** \(P = \tfrac{1}{2} a \cdot h_a\) literami,
   potem \(a\) i \(h_a\) zamieniają się w \(2\) i \(4\), które przylatują z odcinków.
8. **Wynik i werdykt.** \(\tfrac{1}{2} \cdot 2 \cdot 4\) zwija się w \(4\). Pod spodem
   staje \(4 \ne 8\) i obok zdania 2 pojawia się **F**.

## Typowy błąd, który ten projekt rozbraja

Ze sprawozdań CKE: **znak współczynnika kierunkowego przy funkcji malejącej**. Rozbrajamy go
nie ostrzeżeniem, tylko krokiem 3, w którym \(0 - 4\) ma własną klatkę, oraz tym, że na
wykresie widać jednocześnie, że prosta opada.

---

# Zadanie 12.1

## Metoda

Zadanie nic nie liczy, tylko czyta rysunek, więc jednostką kroku jest **jedna myśl**
(README, punkt 42). Rysunek robimy sami: w treści go nie ma, a bez niego zdanie
„punkt leży poniżej wierzchołka" jest pustym słowem.

Cała trudność siedzi w jednym miejscu: skąd wiadomo, że ramiona idą w dół. Stąd osobny krok
na porównanie wysokości punktu \((0,\ -9)\) z wysokością wierzchołka.

## Linijki (pięć)

| # | linijka |
|---|---|
| 1 | Wierzchołek \((3,\ 0)\), punkt na wykresie \((0,\ -9)\) |
| 2 | Punkt leży niżej niż wierzchołek, więc wierzchołek jest najwyższym punktem: ramiona w dół |
| 3 | Po lewej stronie wierzchołka wykres rośnie |
| 4 | Po prawej stronie wierzchołka wykres maleje |
| 5 | Maleje od \(x = 3\) w prawo: \(\langle 3,\ +\infty)\) |
| — | Odpowiedź **D**. |

Komentarz przy linijce 4: sam wierzchołek dopisujemy do przedziału, dlatego przy \(3\) stoi
nawias kątowy, a przy nieskończoności zawsze okrągły.

Wzoru w ramce nie ma. Zdanie „gdy \(a < 0\), ramiona skierowane są ku dołowi" stoi w tablicy
(s. 8) jako zwykłe zdanie, a nie wzór, więc idzie zwykłym zdaniem także tutaj.

## Kroki filmu

Kadr: układ współrzędnych na całą szerokość, bo parabola jest wysoka (od \(-9\) do \(0\)).
Zapis przedziału powstaje w prawym górnym rogu.

1. **Dwa punkty.** W pustym układzie zapala się wierzchołek \((3,\ 0)\) i punkt
   \((0,\ -9)\), oba z podpisami. Paraboli jeszcze nie ma.
2. **Ramiona w dół.** Między oboma punktami staje pionowa strzałka pokazująca, że
   \(-9\) leży niżej niż \(0\), po czym rysuje się parabola przez oba punkty. Zielona jest
   strzałka, nie parabola.
3. **Lewa gałąź rośnie.** Fragment wykresu na lewo od wierzchołka zapala się i przebiega go
   kropka od dołu do góry.
4. **Prawa gałąź maleje.** To samo na prawo od wierzchołka, kropka schodzi w dół.
   Lewa gałąź wraca do czerni, żeby w kadrze świeciło jedno miejsce.
5. **Rzut na oś \(x\).** Prawa gałąź rzutuje się na oś \(x\) jako półprosta od \(3\)
   w prawo, z zamalowaną kropką w \(3\). Po prawej stronie kadru powstaje
   \(\langle 3,\ +\infty)\).

---

# Zadanie 12.2

## Metoda

Jedyne z czterech, które naprawdę liczy, więc idzie wzorem zad. 9: pełny pas rachunku,
bez wykresu, każde ogniwo w osobnym kroku. Dwa wzory z tablicy: postać kanoniczna
(\([7.5]\), s. 8) i kwadrat różnicy (\([6.1]\), s. 7).

Zadanie ma dwie odpowiedzi i to jest jego sedno: **B i D to ten sam wzór**, raz zwinięty,
raz rozwinięty. Dlatego rozwiązanie nie kończy się na \(-(x-3)^{2}\), tylko jedzie dalej
i rozwija nawias. Litera B zapala się w połowie filmu, litera D na końcu.

## Ogniwa wypisane jawnie

- \(p = 3\), \(q = 0\) odczytane osobno, zanim cokolwiek wejdzie do wzoru,
- \(+\,0\) w postaci kanonicznej najpierw jest napisane, a dopiero potem znika,
- \((0 - 3)^{2}\) przed \((-3)^{2}\) przed \(9\), bo tu ginie znak i uczeń wpisuje \(-9\),
- \(x^{2} - 2 \cdot x \cdot 3 + 3^{2}\) przed \(x^{2} - 6x + 9\),
- minus przed nawiasem zmienia znak **każdego** składnika, więc \(-(x^{2}-6x+9)\) ma własny
  krok przed \(-x^{2}+6x-9\).

## Linijki (dwanaście)

| # | linijka | uwaga |
|---|---|---|
| 1 | Wierzchołek \((3,\ 0)\): \(p = 3\), \(q = 0\) | odczyt, mniejsze pismo w filmie |
| 2 | \(f(x) = a(x - 3)^{2} + 0\) | podstawienie do postaci kanonicznej |
| 3 | \(f(x) = a(x - 3)^{2}\) | |
| 4 | \(-9 = a(0 - 3)^{2}\) | podstawiamy \(x = 0\) i \(f(0) = -9\) |
| 5 | \(-9 = a \cdot (-3)^{2}\) | |
| 6 | \(-9 = a \cdot 9\) z dopiskiem \(\big/ : 9\) | |
| 7 | \(a = -1\) | |
| 8 | \(f(x) = -1 \cdot (x - 3)^{2}\) | |
| 9 | \(f(x) = -(x - 3)^{2}\) | **odpowiedź B** |
| 10 | \(f(x) = -(x^{2} - 2 \cdot x \cdot 3 + 3^{2})\) | kwadrat różnicy |
| 11 | \(f(x) = -(x^{2} - 6x + 9)\) | |
| 12 | \(f(x) = -x^{2} + 6x - 9\) | **odpowiedź D** |
| — | Odpowiedź **B** i **D**. | |

Komentarze (nie pod każdą linijką, tylko tam, gdzie coś nie widać):
przy 1 (skąd \(p\) i \(q\)), przy 3 (dodawanie zera nic nie zmienia, więc znika),
przy 4 (co znaczy „przechodzi przez punkt"), przy 5 (\(0-3\) to \(-3\), a kwadrat liczby
ujemnej jest dodatni), przy 9 (\(-1\) razy nawias zapisujemy samym minusem),
przy 11 (minus przed nawiasem zmienia znak każdego składnika).

## Kroki filmu

Trzy pasy jak w zad. 8: u góry odczytane \(p\) i \(q\) (mniejszym pismem, README punkt 41),
w środku rachunek, wzór z tablicy wjeżdża nad rachunek tylko na czas swojego kroku.
Po prawej stronie rośnie lista trafionych odpowiedzi: **B**, potem **D**.

Kroki idą jeden do jednego z linijkami wyżej. Trzy miejsca warte uwagi:

- **krok 2**: wzór \(a(x - p)^{2} + q\) staje literami, potem \(p\) i \(q\) zamieniają się
  w liczby, które przylatują z pasa odczytu u góry (README, punkty 37 i 38);
- **krok 4**: \(x\) w dwóch miejscach zamienia się w \(0\), a cała lewa strona staje się
  \(-9\), które przylatuje z treści zadania stojącej u góry kadru;
- **krok 10**: wzór \((a - b)^{2} = a^{2} - 2ab + b^{2}\) wjeżdża nad rachunek, a pod nim
  \(x\) wchodzi na miejsce \(a\), \(3\) na miejsce \(b\).

---

# Zadanie 12.3

## Metoda

Zadanie stoi na jednej rzeczy: **odjęcie liczby od wzoru funkcji zsuwa cały wykres w dół**.
Reszta to odczyt z tak przesuniętego wykresu. Film pokazuje więc parabolę z 12.1 i zsuwa ją.

Rozwiązanie korzysta ze wzoru wyliczonego w 12.2, i tak ma być: to jedna wiązka, a uczeń
robi te zadania po kolei.

## Linijki (pięć)

| # | linijka |
|---|---|
| 1 | \(g(x) = -(x - 3)^{2} - 1\) |
| 2 | Odejmowanie \(1\) zsuwa cały wykres o \(1\) w dół, wierzchołek ląduje w \((3,\ -1)\) |
| 3 | Ramiona idą w dół, więc \(-1\) jest największą wartością: cały wykres leży pod osią \(x\) |
| 4 | Wykres nigdzie nie dotyka osi \(x\), więc miejsc zerowych nie ma: zdanie 1 **F** |
| 5 | Zsunięcie w dół nie przesuwa wykresu w bok, więc osią symetrii nadal jest \(x = 3\): zdanie 2 **P** |
| — | Odpowiedź **FP**. |

## Kroki filmu

Kadr taki jak w 12.1, żeby uczeń rozpoznał ten sam wykres.

1. **Wzór.** W kadrze stoi \(f(x) = -(x-3)^{2}\) i jego parabola. Pod wzorem dopisuje się
   \(-\,1\) i powstaje \(g(x) = -(x-3)^{2} - 1\). Zielona jest dopisana jedynka.
2. **Zsunięcie.** Cała parabola zjeżdża o jedną kratkę w dół, wierzchołek ląduje
   w \((3,\ -1)\) i tam zostaje podpisany. Stara pozycja zostaje przez chwilę jako
   przerywana, żeby widać było, o ile to jest.
3. **Najwyższy punkt.** Przez wierzchołek przechodzi pozioma przerywana \(y = -1\)
   i zapala się cały wykres: leży pod nią, a ona leży pod osią \(x\).
4. **Brak miejsc zerowych.** Oś \(x\) zapala się, a między nią a wierzchołkiem staje odstęp
   \(1\). Zdanie 1 dostaje **F**.
5. **Oś symetrii.** Pionowa prosta \(x = 3\) przez wierzchołek; lewa i prawa gałąź
   przez chwilę odbijają się względem niej. Zdanie 2 dostaje **P**.

---

## Co się zmieniło przy realizacji (dopisane 2026-08-28, po renderze)

- **Liczba kroków wyszła zgodnie z projektem**: 8 + 5 + 12 + 5, jeden do jednego z linijkami
  rozwiązań opisowych. Sprawdzone maszynowo.
- **Katalogi filmów dla podnumerów**: `media/zad12_1`, `zad12_2`, `zad12_3` (podkreślnik,
  nie kropka). Pierwszy taki przypadek w repo, opisany w `matura/README.md`.
- **W 12.3 kolejność kroku 2 jest odwrotna niż w projekcie**: najpierw strzałka „o ile",
  dopiero potem zsuwa się wykres. Wyszło z pomiaru styku klatek (punkt 48
  w `manimations/README.md`), ale jest też lepsze dydaktycznie: uczeń widzi miarę
  przesunięcia, zanim cokolwiek pojedzie.
- **Kroki 3 i 4 w 12.1 zostawiają w kadrze napisy „rośnie" i „maleje"** (czarne), zamiast
  je gasić. Bez tego obraz spoczynkowy kroków 2, 3 i 4 byłby identyczny i uczeń
  zatrzymany na kropce nie widziałby żadnej różnicy.
- **Cztery sceny z wykresem wymusiły cztery nowe reguły techniczne** (podświetlenie krzywej
  tylko kolorem, przytrzymanie 0,45 s, krok nie zaczyna się od największego ruchu, siatka
  `#e0e0e0`). Spisane z pomiarami w `manimations/README.md`, sekcja „Sceny z wykresem".

## Czego nie ustalono

- **Czy wykres w kadrze jest czytelny na telefonie.** Kadr 16:9 przy oknie 485 px daje
  wykresowi jakieś 180 px szerokości, a liczby przy osiach zostały z tego powodu podbite
  (zad. 11 z 28 na 34, 12.1 z 26 na 32, 12.3 z 24 na 34). Tego nie sprawdzę zrzutem
  z przeglądarki tak, żeby ocenić czytelność okiem na małym ekranie; wpis jest w TODO.md,
  sekcja TESTOWANIE HENRICH.
- **Jak siatka wykresu wygląda w ciemnym motywie.** Film jest odwracany filtrem CSS, więc
  jasnoszara siatka robi się ciemnoszara na prawie czarnym tle. Na zrzucie widać ją słabo,
  ale to nie to samo co ocena na telefonie. Też w TESTOWANIE HENRICH.
