# Projekt: zadania 13 i 14, arkusz 2024-grudzień

Dokument projektowy (co ma zobaczyć uczeń), nie instrukcja techniczna. Powstał 2026-08-28,
po zad. 11 i 12. Zapis do repozytorium rządzi się osobnymi plikami: `SOLUTION_TEXT_RULES.md`,
`manimations/README.md`, `COLORS.md`.

Oba zadania są typu prawda/fałsz, po 1 pkt, po dwa zdania do oceny.

## Stan wyjściowy

Oba mają dziś jednoakapitowe `solutionText` napisane przed zasadami z sierpnia (rachunek
zbity w jedno zdanie, w zad. 13 na dodatek z półpauzą) i **żadnego filmu**. Projekt zastępuje
teksty w całości i dokłada dwie sceny.

## Wyniki policzone od zera i porównane z kluczem

| zadanie | mój rachunek | klucz CKE | zgodne |
|---|---|---|---|
| 13 | \(f(36) = \log_{6} 36 = 2\), a nie \(6\) (F); podstawa \(6 > 1\), więc rosnąca (P) | FP | tak |
| 14 | \(\tfrac{13}{7} \ne \tfrac{7}{13}\), więc nie geometryczny (F); \(S_{8} = 80\) (P) | FP | tak |

Zasady oceniania w obu są jednozdaniowe („1 pkt, odpowiedź poprawna"), więc nie ma etapów
do pokrycia: rozwiązanie ma po prostu dowieźć obie litery.

---

# Zadanie 13

## Metoda

Dwie części liczone **po kolei** (`manimations/README.md`, punkt 4): najpierw całe zdanie 1,
potem całe zdanie 2. Druga część korzysta z wyniku pierwszej, więc kolejność jest wymuszona
treścią, a nie tylko konwencją.

Zdanie 1 idzie wprost z definicji logarytmu (\([3.1]\), s. 5 tablicy): \(\log_{6} 36\) to
wykładnik \(c\), dla którego \(6^{c} = 36\). Trzymam literę \(c\) z tablicy, żeby uczeń
widział ten sam zapis w rozwiązaniu i w tablicy.

Zdanie 2 idzie dwutorowo: najpierw konkret (trzy policzone wartości), potem reguła
(podstawa większa od jedynki). Taka kolejność wynika z zasad tekstowych, punkt „najpierw
liczba, potem litera": uczeń celujący w 30% blokuje się na regule, a nie na rachunku.

## Pułapka, pod którą zadanie jest napisane

W zdaniu 1 stoi liczba \(6\), czyli **podstawa** logarytmu. Uczeń, który myli podstawę
z wykładnikiem, odpowie „prawda". Rozbrajam to nie ostrzeżeniem, tylko krokiem 2: zapis
\(6^{c} = 36\) stawia podstawę i wykładnik na dwóch różnych miejscach, a szukane jest \(c\),
i to \(c\) jako jedyne jest zielone.

## Ogniwa wypisane jawnie

- \(6^{c} = 36\) przed \(6^{2} = 36\), bo bez tego „logarytm to wykładnik" zostaje samym słowem,
- \(6^{0} = 1\) i \(6^{1} = 6\) jako uzasadnienia dwóch dodatkowych wartości, a nie same wyniki,
- osobna linijka na to, że argumenty i wartości rosną razem, zanim padnie reguła o podstawie.

## Linijki (siedem, jeden do jednego z krokami filmu)

| # | linijka |
|---|---|
| 1 | \(f(36) = \log_{6} 36\) |
| 2 | \(6^{c} = 36\) |
| 3 | \(6^{2} = 36\) |
| 4 | \(f(36) = 2\), a w zdaniu 1 stoi \(6\): **F** |
| 5 | \(6^{0} = 1\), więc \(f(1) = 0\); \(6^{1} = 6\), więc \(f(6) = 1\) |
| 6 | \(1 < 6 < 36\) oraz \(0 < 1 < 2\): większy argument, większa wartość |
| 7 | podstawa \(6 > 1\), więc \(f\) jest rosnąca. Zdanie 2: **P** |
| — | Odpowiedź **FP**. | zdanie zamykające, nie jest krokiem |

Układ: jedna kolumna z komentarzami. Wzór z tablicy jest jeden i stosuje się go na starcie,
więc stoi nad rachunkiem, a nie w drugiej kolumnie (`SOLUTION_TEXT_RULES.md`, „Który układ
wybrać").

## Kroki filmu

Kadr do kroku 5: sam rachunek na środku. Od kroku 6 kadr dzieli się na dwie części: po lewej
lista trzech policzonych wartości, po prawej układ współrzędnych.

1. **Podstawienie.** W kadrze staje wzór z treści \(f(x) = \log_{6} x\). Obie litery \(x\)
   zamieniają się w \(36\), które wjeżdża na ich miejsca. Zielone: dwie trzydziestki szóstki,
   bo to one są nowe.
2. **Definicja logarytmu.** Szóstka spod \(\log\) **przesuwa się** na miejsce podstawy potęgi
   (czarna, dalej ta sama szóstka), \(36\) **przejeżdża** na prawą stronę (czarne, ta sama
   liczba), znak równości **leci** za nim, a nad szóstką **pojawia się** zielone \(c\).
   Napis \(\log\) oraz lewa strona \(f(36)\) **znikają**. Zielone tylko \(c\).
3. **Znalezienie wykładnika.** \(c\) **zamienia się** w \(2\). Zielona dwójka.
4. **Werdykt zdania 1.** Wraca zapis \(f(36) = 2\): \(f(36)\) **wjeżdża** z lewej,
   dwójka **zjeżdża** z wykładnika na miejsce wyniku. Pod spodem pojawia się liczba \(6\)
   ze zdania 1 i obok niej litera **F**. Zielone: nic, to jest odczyt.
5. **Dwie dodatkowe wartości.** Rachunek **zjeżdża** na dolny wiersz listy, a obok niego
   **wraca** \(6^{2} = 36\) z kroku 3. Nad nimi **wjeżdżają** dwa wiersze: \(6^{0} = 1\)
   z \(f(1) = 0\) oraz \(6^{1} = 6\) z \(f(6) = 1\). Zielone: same wyniki \(0\) i \(1\).
6. **Wykres.** Lista wartości najpierw **przesuwa się** przy lewą krawędź, gubiąc kolumnę
   potęg (drobny ruch, żeby krok nie zaczynał się od największego przejazdu w scenie),
   potem po prawej
   **wjeżdża** układ współrzędnych z zaznaczonymi \(1\), \(6\), \(36\) na osi poziomej.
   Z listy **wylatują** trzy punkty i siadają na swoich miejscach: \((1,\ 0)\), \((6,\ 1)\),
   \((36,\ 2)\), a przez nie **rysuje się** krzywa, od lewej do prawej, cały czas w górę
   (fiolet, rola „wykres funkcji" z `COLORS.md`). To jest jedna myśl: wartości układają się
   w wykres, który rośnie.
7. **Reguła i werdykt zdania 2.** Pod wykresem **pojawia się** \(6 > 1\), a obok litera **P**.
   Zielona jest podstawa \(6\), bo to ona rozstrzyga.

Opis pod filmem niesie w kroku 2 wzór \([3.1]\) w ramce (jest w tablicy), a w kroku 7
zwykłym zdaniem regułę o podstawie (jej w tablicy nie ma).

---

# Zadanie 14

## Metoda

Wszystko stoi na jednej rzeczy: \((-1)^{n}\) przyjmuje tylko dwie wartości, na przemian
\(-1\) i \(1\). Dlatego dwa pierwsze wyrazy liczę **pełnym rachunkiem**, bez skracania,
a trzeciego już nie liczę: zamiast tego pokazuję, dlaczego wyrazy muszą się powtarzać.

Zdanie 1 obalam ilorazem kolejnych wyrazów: \(\tfrac{a_2}{a_1} = \tfrac{13}{7}\),
\(\tfrac{a_3}{a_2} = \tfrac{7}{13}\). Jeden jest większy od jedynki, drugi mniejszy, więc
różnicy nie trzeba nawet liczyć.

**Wzoru z tablicy w tym zadaniu nie ma i to jest świadome.** Definicji ilorazu tablica nie
podaje, a \([8.5]\) (suma ciągu geometrycznego) tu nie działa, bo ciąg geometryczny nie jest.
Kolumna wzorów zostaje więc pusta, a wyjaśnienia idą komentarzami
(`SOLUTION_TEXT_RULES.md`, punkt 16).

Zdanie 2 liczę wprost, przez wypisanie ośmiu wyrazów i sparowanie ich. Wzór na sumę nie
istnieje dla tego ciągu, a parowanie \(7 + 13\) jest tym, co uczeń realnie zrobi na kartce.

## Pułapka, pod którą zadanie jest napisane

Dwa miejsca, w których gubi się znak, i oba dostają własny krok:

- \((-1)^{1}\) kontra \((-1)^{2}\): potęga liczby ujemnej. Kroki 6 i 7 rozbijają to na
  dwoje: najpierw w kadrze staje \((-1) \cdot (-1)\), i dopiero z tego rodzi się \(1\).
- \(3 \cdot (-1) = -3\): mnożenie przez liczbę ujemną. To osobny krok 3, a nie część
  poprzedniego.

## Linijki (osiemnaście, jeden do jednego z krokami filmu)

| # | linijka |
|---|---|
| 1 | \(a_{1} = 3 \cdot (-1)^{1} + 10\) |
| 2 | \(a_{1} = 3 \cdot (-1) + 10\) |
| 3 | \(a_{1} = -3 + 10\) |
| 4 | \(a_{1} = 7\) |
| 5 | \(a_{2} = 3 \cdot (-1)^{2} + 10\) |
| 6 | \(a_{2} = 3 \cdot (-1) \cdot (-1) + 10\) |
| 7 | \(a_{2} = 3 \cdot 1 + 10\) |
| 8 | \(a_{2} = 3 + 10\) |
| 9 | \(a_{2} = 13\) |
| 10 | \((-1)^{1} = -1\), \((-1)^{2} = 1\), \((-1)^{3} = -1\), \((-1)^{4} = 1\) |
| 11 | osiem pierwszych wyrazów: \(7,\ 13,\ 7,\ 13,\ 7,\ 13,\ 7,\ 13\) |
| 12 | \(\dfrac{a_{2}}{a_{1}} = \dfrac{13}{7}\) |
| 13 | \(\dfrac{a_{3}}{a_{2}} = \dfrac{7}{13}\) |
| 14 | \(\dfrac{13}{7} \ne \dfrac{7}{13}\), iloraz nie jest stały. Zdanie 1: **F** |
| 15 | \(S_{8} = 7 + 13 + 7 + 13 + 7 + 13 + 7 + 13\) |
| 16 | \(S_{8} = (7 + 13) + (7 + 13) + (7 + 13) + (7 + 13)\) |
| 17 | \(S_{8} = 20 + 20 + 20 + 20\) |
| 18 | \(S_{8} = 80\), a w zdaniu 2 też stoi \(80\): **P** |
| — | Odpowiedź **FP**. | zdanie zamykające, nie jest krokiem |

Układ: jedna kolumna z komentarzami, bez kolumny wzorów.

## Kroki filmu

Kadr: rachunek na środku, a nad nim pas policzonych wartości, do którego odjeżdżają wyniki
(wzorzec z zad. 7 i 9). Od kroku 11 pas zastępuje lista ośmiu wyrazów, która zostaje do końca
filmu, bo z niej biorą się i ilorazy, i suma.

1. **Podstawienie \(n = 1\).** W kadrze staje wzór z treści \(a_{n} = 3 \cdot (-1)^{n} + 10\).
   Obie litery \(n\) zamieniają się w \(1\), które **wjeżdża** na ich miejsca. Zielone: dwie
   jedynki.
2. **Pierwsza potęga.** Wykładnik \(1\) **znika**, nawias z minusem zostaje. Zielony jest
   znikający wykładnik.
3. **Mnożenie przez liczbę ujemną.** Minus **wysuwa się** przed trójkę, trójka **przejeżdża**
   za niego, a nawias, kropka i jedynka **znikają**. Zielony jest minus, bo to on decyduje
   o wyniku; trójka zostaje czarna, bo dalej jest tą samą trójką.
4. **Dodawanie.** \(-3 + 10\) **zwija się** w \(7\). Zielona siódemka.
5. **Drugi wyraz.** \(a_{1} = 7\) **odjeżdża** do pasa nad rachunkiem, a w środek
   **wjeżdża** \(a_{2} = 3 \cdot (-1)^{2} + 10\). Bez koloru: nic się tu nie przelicza.
6. **Co znaczy druga potęga.** Wykładnik \(2\) **znika**, a obok pierwszego nawiasu
   **pojawia się** drugi taki sam: \((-1) \cdot (-1)\). Ogniwo dostaje własny krok, a nie
   rachunek na boku (`manimations/README.md`, „Wyjaśnienie w środku kroku"). Zielone: minus
   i jedynka nowego czynnika, bez nawiasów.
7. **Dwa minusy.** Oba nawiasy **zjeżdżają** w jedną jedynkę. Zielone: dwa minusy przed
   ruchem i powstająca z nich jedynka.
8. **Mnożenie przez jedynkę.** Kropka i jedynka **znikają**.
9. **Dodawanie.** \(3 + 10\) **zwija się** w \(13\). Zielona trzynastka.
10. **Naprzemienność.** \(a_{2} = 13\) **odjeżdża** do pasa. W środku **pojawiają się**
    cztery równości \((-1)^{1} = -1\), \((-1)^{2} = 1\), \((-1)^{3} = -1\),
    \((-1)^{4} = 1\), po dwie w wierszu. Zielone: same wyniki, żeby widać było, że skaczą.
11. **Lista wyrazów.** Równości **znikają**, a z pasa **wylatują** \(7\) i \(13\) na dwa
    pierwsze miejsca rzędu ośmiu liczb; pozostałe sześć **pojawia się** na zielono. Nad każdą
    liczbą stoi numer wyrazu. Rząd zostaje w kadrze do końca filmu.
12. **Pierwszy iloraz.** Z listy **wylatują** \(a_{2}\) i \(a_{1}\) i siadają w ułamku
    \(\tfrac{13}{7}\). Zielone: dwie liczby, które przyleciały.
13. **Drugi iloraz.** To samo dla \(a_{3}\) i \(a_{2}\): \(\tfrac{7}{13}\).
14. **Werdykt zdania 1.** Lewe strony **znikają**, oba wyniki **zjeżdżają** w jedną linijkę,
    a między nimi **pojawia się** przekreślony znak równości. Zielony: sam znak \(\ne\).
15. **Suma ośmiu.** Ułamki **znikają**, a z listy **zjeżdża** osiem liczb w jeden zapis
    \(S_{8} = 7 + 13 + \ldots\), między nimi **pojawiają się** plusy. Bez koloru.
16. **Parowanie.** Wokół kolejnych par **pojawiają się** nawiasy. Krok idzie bez koloru,
    bo nawiasów się nie koloruje (`SOLUTION_TEXT_RULES.md`, punkt 14), a samo pojawienie się
    czterech nawiasów wystarczy za wskazówkę.
17. **Wartość pary.** Każdy nawias **zwija się** w \(20\). Zielone: cztery dwudziestki.
18. **Wynik i werdykt zdania 2.** \(20 + 20 + 20 + 20\) **zwija się** w \(80\), a obok
    **pojawia się** litera **P**. Zielona osiemdziesiątka.

---

## Czego nie ustalono

- **Czy wykres w krokach 6 i 7 zadania 13 przejdzie styk klatek bez walki.** Sceny
  z wykresem schodzą poniżej progu 0,999 z powodu samego kodera (`manimations/README.md`,
  punkty 46 do 50). Skala poziomej osi jest tu nietypowa (od \(0\) do \(40\)), więc krzywa
  jest przy lewej krawędzi bardzo stroma. Zmierzone po renderze 2026-08-28: oba styki
  z wykresem przechodzą (0,99972 i 0,99992), więc żaden z zabiegów z punktów 46 do 49
  nie był potrzebny.
- **Czy rząd ośmiu liczb w zadaniu 14 zmieści się w kadrze razem z rachunkiem.** Sprawdzone
  na gotowym pliku 2026-08-28: mieści się, rząd zajmuje około dwóch trzecich szerokości kadru.
