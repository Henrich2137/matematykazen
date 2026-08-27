# Projekt: zadania 9 i 10, arkusz 2024-grudzień

Dokument projektowy (co ma zobaczyć uczeń), nie instrukcja techniczna. Powstał 2026-08-27,
po przerobieniu zad. 7 i 8 „na wzór zadania 7". Oba zadania idą tym samym wzorcem:
ogniwo pośrednie dostaje własną linijkę i własny krok filmu, komentarze wybiórczo,
kadr czysty na styku kroków.

Zapis do repozytorium rządzi się osobnymi plikami: `SOLUTION_TEXT_RULES.md`,
`manimations/README.md`, `COLORS.md`.

---

# Zadanie 9

## Stan wyjściowy

Zadanie **ma już** rozwiązanie opisowe i film (osiem kroków, `media/zad9/solution-step-by-step/`),
napisane przed zasadami z 26 i 27 sierpnia. Trzy rzeczy się nie zgadzają:

- **liczba linijek nie równa się liczbie kroków** (siedem linijek, osiem kroków),
- **ogniwa liczone są w głowie**: z \(x(x-6)\) robi się od razu \(x^{2}-6x\), z podstawienia
  do delty od razu \(36+28\), z \(\dfrac{6-8}{2}\) od razu \(-1\),
- **wniosku nie widać w filmie**: paraboli nie ma w kadrze, a „ramiona w górę, więc między
  miejscami zerowymi" stoi wyłącznie w opisie pod krokiem, czyli w miejscu, którego uczeń
  domyślnie nie rozwija. To jest krok wart punktu CKE.

Projekt zastępuje jedno i drugie w całości.

## Treść i wynik

Rozwiąż nierówność \(x(x - 6) \le 7\). Zapisz obliczenia. Zadanie otwarte, 2 punkty.

Policzone od zera: \(x^{2}-6x-7 \le 0\), \(\Delta = 36 + 28 = 64\), \(\sqrt{\Delta} = 8\),
\(x_{1} = -1\), \(x_{2} = 7\), ramiona w górę, więc \(x \in \langle -1,\ 7\rangle\).
**Zgodne z kluczem CKE** (s. 9 do 10 `odpowiedzi.pdf`), który idzie tą samą drogą i też
szkicuje wykres.

## Kryteria CKE i gdzie są pokryte

| Kryterium | Punkty | Gdzie |
|---|---|---|
| nierówność w postaci \(x^{2}-6x-7 \le 0\) | 0, etap konieczny | linijka 4 |
| pierwiastki trójmianu \(x_{1} = -1\), \(x_{2} = 7\) | 1 | linijka 18 |
| zbiór rozwiązań \(\langle -1,\ 7\rangle\) | 1 | linijka 21 |

## Metoda i dwie rzeczy, które ją zmieniają wobec starej wersji

**1. Dwa tory na miejsca zerowe.** \(x_{1}\) i \(x_{2}\) to dokładnie ta para niezależnych
rachunków, którą zad. 7 liczy obok siebie, a zad. 8 liczy dla dwóch mianowników.
W rozwiązaniu opisowym idą obok siebie (`rozw-2kol rozw-dwatory`), w filmie **po kolei**:
najpierw cały \(x_{1}\), potem \(x_{2}\), a wynik pierwszego czeka w kadrze.

**2. Parabola wraca do filmu.** Ostatnie trzy kroki to szkic: parabola ramionami w górę
przez \(-1\) i \(7\), potem zielony fragment pod osią, potem odcinek na osi i zapis
przedziału. Powód: to jest krok, za który CKE daje punkt, a dotąd niósł go wyłącznie
zwinięty opis. Widżet `widgetNierownoscKwadratowa` pokazuje to samo interaktywnie i to nie
jest dublowanie: widżet uczeń otwiera sam, film ma być zrozumiały bez niczego obok.

## Ogniwa wypisane jawnie

To, co ekspert liczy w głowie, a co tu dostaje własną linijkę i własny krok:

- \(x \cdot x - x \cdot 6\), czyli skąd \(x^{2} - 6x\),
- \(a = 1\), \(b = -6\), \(c = -7\) odczytane osobno, zanim cokolwiek wejdzie do wzoru,
- \(36 + 28\) przed \(64\), bo tu ginie znak: \(-4 \cdot 1 \cdot (-7)\) daje **plus** 28,
- \(-(-6)\) przed \(6\), bo podwójny minus we wzorze na pierwiastki to drugie takie miejsce,
- \(\dfrac{-2}{2}\) i \(\dfrac{14}{2}\) przed wynikami.

## Linijki

Dwadzieścia jeden linijek rachunku, potem zdanie zamykające na całą szerokość
(nie jest krokiem filmu). Linijek rachunku jest dokładnie tyle, ile kroków filmu.

| # | Linijka | Uwaga |
|---|---|---|
| 1 | \(x(x - 6) \le 7\) | zapis z treści |
| 2 | \(x \cdot x - x \cdot 6 \le 7\) | ogniwo: co mnoży co |
| 3 | \(x^{2} - 6x \le 7\) z dopiskiem \(\big/ - 7\) | |
| 4 | \(x^{2} - 6x - 7 \le 0\) | etap konieczny CKE |
| 5 | **Współczynniki:** \(a = 1\), \(b = -6\), \(c = -7\) | podpisane słowem, jak założenie w zad. 8 |
| 6 | \(\Delta = (-6)^{2} - 4 \cdot 1 \cdot (-7)\) | wzór z tablicy |
| 7 | \(\Delta = 36 + 28\) | ogniwo: tu powstaje plus |
| 8 | \(\Delta = 64\) | |
| 9 | \(\sqrt{\Delta} = 8\) | |
| 10 | \(x_{1,2} = \dfrac{-(-6) \pm 8}{2 \cdot 1}\) | wzór z tablicy, podstawienie |
| 11 | \(x_{1,2} = \dfrac{6 \pm 8}{2}\) | ogniwo: podwójny minus |
| 12 | \(x_{1} = \dfrac{6 - 8}{2}\) | lewy tor |
| 13 | \(x_{1} = \dfrac{-2}{2}\) | ogniwo |
| 14 | \(x_{1} = -1\) | lewy tor, koniec |
| 15 | \(x_{2} = \dfrac{6 + 8}{2}\) | prawy tor |
| 16 | \(x_{2} = \dfrac{14}{2}\) | ogniwo |
| 17 | \(x_{2} = 7\) | prawy tor, koniec |
| 18 | **Miejsca zerowe:** \(\boldsymbol{x_{1} = -1}\), \(\boldsymbol{x_{2} = 7}\) | punkt CKE |
| 19 | \(a = 1 > 0\), czyli ramiona paraboli idą w górę | w filmie: szkic paraboli |
| 20 | Pod osią parabola leży między \(-1\) a \(7\) | w filmie: zielony fragment i odcinek na osi |
| 21 | \(\boldsymbol{x \in \langle -1,\ 7\rangle}\) | punkt CKE |
| 22 | Rozwiązaniem nierówności są wszystkie liczby od \(-1\) do \(7\), razem z końcami. | cała szerokość, nie jest krokiem filmu |

**Odstępstwo, świadome:** linijki 19 i 20 są zdaniami, nie wyrażeniami. Wniosek o ramionach
paraboli nie da się zapisać samym rachunkiem, a jest wart punktu, więc dostaje własne
linijki zamiast tonąć w komentarzu. Reszta rozwiązania trzyma zasadę „jedna linijka,
jedno wyrażenie".

### Układ

Jedna kolumna (`rozwiazanie-kroki`), bo wzory z tablicy stosuje się w środku, nie na starcie.
Wewnątrz niej dwa tory (`rozw-2kol rozw-dwatory rozw-srodek`) na linijki 12 do 17, tak jak
zad. 8 wstawia dwa tory w środek rozwiązania jednokolumnowego. Szersza przerwa
(`rozw-odstep`) w dwóch miejscach: przed linijką 5 (kończy się przekształcanie nierówności,
zaczyna liczenie pierwiastków) i przed linijką 19 (kończy się rachunek, zaczyna odczyt).

Sprawdzenia pod kreską **nie ma**: w nierówności podstawienie jednej liczby niczego nie
dowodzi, a sprawdzanie całego przedziału to osobne zadanie.

### Komentarze między linijkami

Siedem na dwadzieścia jeden, tylko tam, gdzie sam zapis nie tłumaczy przejścia:

- **pod 1:** Chcemy mieć po prawej stronie zero. Najpierw opuszczamy nawias.
- **pod 4:** Po prawej stoi zero, więc szukamy miejsc zerowych. Współczynniki odczytujemy
  z lewej strony, razem ze znakami.
- **pod 5:** Przy \(x^{2}\) nie stoi żadna liczba, czyli stoi tam \(1\). Minus przed \(6x\)
  i przed \(7\) należy do współczynnika.
- **pod 6:** \(-4 \cdot 1 \cdot (-7)\) to iloczyn dwóch liczb ujemnych, więc wychodzi plus:
  \(-4 \cdot (-7) = 28\).
- **pod 10:** \(-b\) znaczy „liczba przeciwna do \(b\)". Skoro \(b = -6\), to \(-b = 6\).
- **pod 11:** Znak \(\pm\) mówi, że wyniki są dwa. Liczymy każdy osobno.
- **pod 19:** Parabola przecina oś w \(-1\) i \(7\), a ramiona ma w górę, więc pod osią
  leży dokładnie między nimi.


## Film, dwadzieścia jeden kroków

Każdy krok wygląda tak samo: czysty czarny zapis, zapala się to, co się zmienia, animacja,
znów wszystko czarne. Kolor tylko na tym, co się w tym kroku zmienia.

| # | Co się rusza | Zielone |
|---|---|---|
| 1 | zapis nierówności pojawia się od zera | nic |
| 2 | \(x\) sprzed nawiasu rozdwaja się i wchodzi przed każdy składnik z nawiasu; nawias znika | dwa nowe \(x\) i kropki mnożenia |
| 3 | \(x \cdot x\) zamienia się w \(x^{2}\), \(x \cdot 6\) w \(6x\) | wykładnik \(2\), który się pojawia |
| 4 | \(7\) leci łukiem nad znakiem \(\le\) i po drodze zmienia się w \(-7\); po prawej zostaje \(0\) | znak minus przy siódemce i zero |
| 5 | pod nierównością wysuwa się linijka współczynników, każdy zjeżdża ze swojego miejsca w nierówności | trzy minusy, bo o nie chodzi |
| 6 | liczby ze współczynników wsuwają się w miejsca \(b\), \(a\), \(c\) w zapisanym wzorze | wstawiane liczby |
| 7 | \((-6)^{2}\) zamienia się w \(36\), \(-4 \cdot 1 \cdot (-7)\) w \(+28\) | plus przed \(28\) |
| 8 | \(36 + 28\) zamienia się w \(64\) | nic |
| 9 | nad \(64\) pojawia się znak pierwiastka i całość zamienia się w \(8\) | \(8\) |
| 10 | liczby wsuwają się w miejsca we wzorze na pierwiastki | wstawiane liczby |
| 11 | \(-(-6)\) zamienia się w \(6\), \(2 \cdot 1\) w \(2\) | \(6\), które powstaje z dwóch minusów |
| 12 | zapis rozdziela się: zostaje sam \(x_{1}\) z minusem, \(\pm\) zamienia się w \(-\) | znak minus |
| 13 | \(6 - 8\) zamienia się w \(-2\) | \(-2\) |
| 14 | \(\dfrac{-2}{2}\) zamienia się w \(-1\) | nic |
| 15 | \(x_{1} = -1\) odjeżdża na górę kadru i tam zostaje; wjeżdża \(x_{2} = \dfrac{6+8}{2}\) | nic, to krok przenoszący |
| 16 | \(6 + 8\) zamienia się w \(14\) | \(14\) |
| 17 | \(\dfrac{14}{2}\) zamienia się w \(7\) | nic |
| 18 | oba wyniki zjeżdżają w jedną linijkę podpisaną „Miejsca zerowe" | nic |
| 19 | pod spodem rysuje się oś \(x\) z \(-1\) i \(7\), a przez te punkty przechodzi parabola ramionami w górę | nic |
| 20 | fragment paraboli poniżej osi zapala się, a pod nim na osi zapala się odcinek od \(-1\) do \(7\) z pełnymi kropkami na końcach | fragment paraboli i odcinek |
| 21 | odcinek zamienia się w zapis \(x \in \langle -1,\ 7\rangle\) | nawiasy kątowe zostają czarne, wynik bez koloru |

**Rysunek w krokach 19 do 21** ma być szkicem, nie dokładnym wykresem: oś \(x\), dwa
podpisane punkty, gładka parabola. Bez siatki, bez osi \(y\), bez skali. Chodzi o kształt
i o to, gdzie leży pod osią.

**Krok 15 nie ma koloru**, bo nic się w nim nie przelicza, tylko przesuwa. To ta sama
zasada, co w zad. 7 przy odstawianiu wyniku na górę kadru.

## Opisy pod filmem, po jednym na krok

Wzór w ramce tylko tam, gdzie stoi w tablicy (delta i pierwiastki, s. 8).

1. Zapisujemy nierówność z zadania.
2. Opuszczamy nawias: \(x\) mnoży każdy składnik osobno.
3. Wykonujemy oba mnożenia: \(x \cdot x = x^{2}\) oraz \(x \cdot 6 = 6x\).
4. Siódemka przechodzi na drugą stronę i zmienia znak.<br>Po prawej zostaje zero i dopiero teraz da się szukać miejsc zerowych.
5. Odczytujemy współczynniki.<br>Przy \(x^{2}\) nie stoi żadna liczba, czyli stoi tam \(1\). Minusy należą do współczynników.
6. Wyróżnik liczymy ze wzoru:\[\Delta = b^{2} - 4ac\]Liczby ujemne wstawiamy w nawiasach.
7. \((-6)^{2} = 36\), a \(-4 \cdot 1 \cdot (-7) = 28\).<br>Dwie liczby ujemne w iloczynie dają plus, więc dodajemy.
8. \(36 + 28 = 64\).
9. \(\sqrt{64} = 8\).
10. Miejsca zerowe liczymy ze wzoru:\[x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}\]
11. \(-b\) to liczba przeciwna do \(b\), a \(b = -6\), więc \(-b = 6\).
12. Znak \(\pm\) daje dwa wyniki. Liczymy najpierw ten z minusem.
13. \(6 - 8 = -2\).
14. \(\dfrac{-2}{2} = -1\).
15. Pierwszy wynik odstawiamy na górę. Teraz ten sam rachunek z plusem.
16. \(6 + 8 = 14\).
17. \(\dfrac{14}{2} = 7\).
18. Mamy oba miejsca zerowe. Za samo to klucz CKE daje punkt.
19. Współczynnik przy \(x^{2}\) jest dodatni, więc ramiona paraboli idą w górę.<br>Parabola przecina oś w miejscach zerowych.
20. Szukamy \(x\), dla których wartość jest mniejsza lub równa zeru, czyli miejsc, gdzie parabola leży pod osią. To fragment między miejscami zerowymi.
21. Nierówność jest nieostra, więc same miejsca zerowe też pasują: w nich lewa strona równa się zeru. Dlatego końce należą do przedziału.

## Rozbrojone typowe błędy, dwa

1. **Zgubiony znak w delcie.** \(c = -7\) jest odczytane osobną linijką (5), podstawione
   w nawiasie (6) i rozpisane osobnym krokiem (7). Nigdzie nie ma ostrzeżenia, jest za to
   trzykrotne pokazanie tego samego minusa.
2. **Zły kierunek przedziału.** Krok 20 pokazuje wprost fragment pod osią, a nie wynik
   podany słowem. Uczeń widzi, że to ten między pierwiastkami, bo ramiona idą w górę.

## Koszt i co wyciąć, gdyby było za długo

Dwadzieścia jeden kroków, o dwa więcej niż zad. 8, czyli nowy rekord w arkuszu. Gdyby
Henrich uznał, że kropek jest za dużo, pierwsze do scalenia są kroki 2 i 3 (opuszczanie
nawiasu), potem 13 i 16 (dzielenia). Nie ruszać kroków 5 do 7 ani 19 do 21: tam siedzą
oba punkty i oba typowe błędy.

## Podpowiedź

Pole `hint` zostaje bez zmian.

---

# Zadanie 10

## Stan wyjściowy

Zadanie ma rozwiązanie opisowe z doklejonym nagłówkiem „DAWNE POKAŻ WIĘCEJ" i powtórzoną
pod nim starą treścią (jedna z trzech takich pozostałości w arkuszu, wymieniona w `TODO.md`).
Filmu nie ma. Widżet `widgetFunkcjaPrzedzialami` jest i zostaje.

Projekt zastępuje rozwiązanie opisowe jedną całością i dokłada film.

## Treść i wynik

Funkcja dana trzema wzorami, wykres w arkuszu (`media/zad10/zad10rys.png`): poziomy odcinek
na wysokości \(3\) od \(x = -4\) (kółko otwarte) do \(x = -2\), potem odcinek malejący do
\((2,\ -1)\), potem rosnący do \((4,\ 1)\) (kropka pełna). Zadanie zamknięte z lukami,
4 punkty, po jednym za każdą lukę.

Policzone od zera ze wzorów, nie z rysunku:

| luka | odpowiedź | skąd |
|---|---|---|
| 1. dziedzina | \((-4,\ 4\rangle\) | suma trzech przedziałów ze wzoru |
| 2. zbiór wartości | \(\langle -1,\ 3\rangle\) | \(\{3\} \cup \langle -1,\ 3) \cup (-1,\ 1\rangle\) |
| 3. wartości ujemne | \((1,\ 3)\) | \(-x+1 < 0\) daje \((1,\ 2\rangle\), \(x-3 < 0\) daje \((2,\ 3)\) |
| 4. wartość największa | \((-4,\ -2\rangle\) | \(3\) tylko na poziomym odcinku |

**Zgodne z kluczem CKE** (s. 11 `odpowiedzi.pdf`), co do nawiasu.

## Dlaczego to zadanie w ogóle dostaje film

Nie ma tu rachunku do rozpisania, jest odczyt. Cztery pytania to cztery różne sposoby
patrzenia na ten sam obraz: raz rzutujemy wykres na oś \(x\), raz na oś \(y\), raz szukamy
tego, co pod osią, raz tego, co najwyżej. **To jest ruch, który dokładnie odpowiada temu,
co uczeń ma zrobić w głowie**, a więc dokładnie ten przypadek, w którym animacja daje coś
ponad statyczny rysunek.

Widżet pokazuje to interaktywnie i zostaje. Film ma być zrozumiały bez niego.

## Wspólna scena

Wykres rysuje się **raz, w kroku 1, i stoi do końca filmu**. Odwzorowuje rysunek z arkusza:
te same osie i ta sama skala, wykres w fiolecie (`--accent-purple`, jak w arkuszach CKE),
podpis \(y = f(x)\) przy krzywej, kółko otwarte w \((-4,\ 3)\), kropka pełna w \((4,\ 1)\).
Osie i siatka szare, żeby nie konkurowały z wykresem.

Nad wykresem stoi **etykieta bieżącej części** („1. Dziedzina", „2. Zbiór wartości",
„3. Wartości ujemne", „4. Największa wartość"). Zmienia się tylko na styku części, czyli
cztery razy w całym filmie. Wynik zamkniętej części odjeżdża pod wykres i tam zostaje,
więc na końcu widać wszystkie cztery odpowiedzi naraz.

**Kolor:** zielony wyłącznie na tym, co w danym kroku pokazujemy, i tylko w jednym miejscu
naraz. Wykres pozostaje fioletowy przez cały film.

## Linijki i kroki, część po części

Szesnaście linijek, szesnaście kroków. Układ jednokolumnowy, cztery części rozdzielone
szerszą przerwą (`rozw-odstep`), każda z wytłuszczonym nagłówkiem. Kolumny wzorów nie ma:
w tablicy nie stoi nic, z czego się tu korzysta.

### Część 1: dziedzina

| # | Linijka | Film |
|---|---|---|
| 1 | Dziedzina to wszystkie \(x\), nad którymi wykres coś ma. | wykres pojawia się od zera; pod nim, na osi \(x\), zapala się cień całego wykresu, od \(-4\) do \(4\) |
| 2 | Kółko otwarte, więc \(-4\) nie należy: \((-4\) | kółko w \((-4,\ 3)\) zapala się i zjeżdża pionowo na oś, gdzie zostaje jako pusta kropka; obok pojawia się zapis \((-4\) |
| 3 | Kropka pełna, więc \(4\) należy: \(4\rangle\) | to samo z kropką w \((4,\ 1)\), pełną; zapis \(4\rangle\) |
| 4 | \(\boldsymbol{(-4,\ 4\rangle}\) | oba kawałki zapisu zjeżdżają ku sobie i łączą się w jeden przedział |

Komentarz pod linijką 2: Kółko z pustym środkiem znaczy, że tego punktu na wykresie nie ma.
Zamalowana kropka znaczy, że jest.

### Część 2: zbiór wartości

| # | Linijka | Film |
|---|---|---|
| 5 | Zbiór wartości to wszystkie wysokości, na których wykres coś ma. Patrzymy na oś \(y\). | etykieta zmienia się na „2. Zbiór wartości"; cień wykresu zapala się tym razem na osi \(y\), od \(-1\) do \(3\) |
| 6 | Najniżej wykres schodzi w punkcie \((2,\ -1)\): \(\langle -1\) | wierzchołek zapala się i jedzie poziomo na oś \(y\), gdzie zostaje jako pełna kropka; zapis \(\langle -1\) |
| 7 | Najwyżej wykres jest na wysokości \(3\): \(3\rangle\) | poziomy odcinek zapala się i jedzie na oś \(y\), pełna kropka; zapis \(3\rangle\) |
| 8 | \(\boldsymbol{\langle -1,\ 3\rangle}\) | oba kawałki łączą się w przedział |

Komentarz pod linijką 7: Kółko otwarte jest tylko na samym lewym końcu, w \(x = -4\).
Reszta odcinka leży na wysokości \(3\) i należy do wykresu, więc wartość \(3\) jest osiągana.

### Część 3: wartości ujemne

| # | Linijka | Film |
|---|---|---|
| 9 | Wartości ujemne to \(y < 0\), czyli fragmenty wykresu pod osią \(x\). | etykieta „3. Wartości ujemne"; oś \(x\) zapala się na chwilę, żeby było wiadomo, co jest granicą |
| 10 | Pod osią wykres jest między \(x = 1\) a \(x = 3\). | fragment wykresu poniżej osi zapala się w całości, jednym ciągiem, i zjeżdża cieniem na oś \(x\) |
| 11 | W \(x = 1\) wykres dotyka osi, czyli \(f(1) = 0\), a zero nie jest ujemne: \((1\) | punkt \((1,\ 0)\) zapala się jako pusta kropka; zapis \((1\) |
| 12 | Tak samo w \(x = 3\): \(3)\) | to samo w \((3,\ 0)\); zapis \(3)\) |
| 13 | \(\boldsymbol{(1,\ 3)}\) | kawałki łączą się w przedział |

Komentarz pod linijką 10: Wykres schodzi pod oś, dochodzi do najniższego punktu i wraca,
nigdzie się nie urywając, więc to jeden przedział, a nie dwa.

Ten komentarz i to, że fragment zapala się jednym ciągiem, są jedynym miejscem, w którym
rozbrajamy dzielenie odpowiedzi na \((1,\ 2\rangle\) i \((2,\ 3)\). Bez ostrzeżeń.

### Część 4: największa wartość

| # | Linijka | Film |
|---|---|---|
| 14 | Największa wartość to \(3\), odczytana w punkcie 2. | etykieta „4. Największa wartość"; na wysokości \(3\) zapala się pozioma linia przez cały kadr |
| 15 | Na tej wysokości leży poziomy odcinek, od \(x = -4\) (kółko otwarte) do \(x = -2\). | poziomy odcinek wykresu zapala się i zjeżdża cieniem na oś \(x\); na końcach cienia pusta kropka i pełna kropka |
| 16 | \(\boldsymbol{(-4,\ -2\rangle}\) | cień zamienia się w zapis przedziału |

Komentarz pod linijką 15: W \(x = -2\) wykres tylko się załamuje, nie urywa, więc ten punkt
należy i nawias jest kątowy.

**Odstępstwo, świadome:** w części 4 oba końce idą jednym krokiem, a nie dwoma jak
w częściach 1 i 3. Powód: symbole kółka i kropki są już wyjaśnione w krokach 2 i 3,
więc to powtórka, nie nowa treść. Rozbijanie na dwa kroki dokładałoby kropkę bez treści.

### Zdanie zamykające

Wiersz na całą szerokość, nie jest krokiem filmu:

> W polach wpisujemy: \((-4,\ 4]\), \([-1,\ 3]\), \((1,\ 3)\), \((-4,\ -2]\). Nawias
> kwadratowy z polecenia znaczy to samo co kątowy: koniec należy do przedziału.

To domyka pętlę z poleceniem: zadanie każe wpisać przedziały w zapisie z nawiasem
kwadratowym, a rozwiązanie prowadzone jest w kątowym.

## Opisy pod filmem, po jednym na krok

Bez wzoru w ramce: w tablicy nie ma tu czego pokazać.

1. Dziedzina to wszystkie \(x\), nad którymi wykres w ogóle istnieje.<br>Rzutujemy więc cały wykres na oś \(x\).
2. Kółko z pustym środkiem znaczy, że tego punktu na wykresie nie ma.<br>Dlatego przy \(-4\) stoi nawias okrągły.
3. Zamalowana kropka znaczy, że punkt należy do wykresu.<br>Przy \(4\) stoi więc nawias kątowy.
4. Składamy oba końce w jeden przedział.
5. Teraz patrzymy na wysokości, czyli rzutujemy wykres na oś \(y\).
6. Najniżej wykres schodzi w punkcie \((2,\ -1)\). Ten punkt należy do wykresu, więc \(-1\) jest wartością funkcji.
7. Najwyżej wykres jest na wysokości \(3\).<br>Kółko otwarte stoi tylko na samym lewym końcu, więc reszta poziomego odcinka należy i wartość \(3\) jest osiągana.
8. Składamy oba końce w jeden przedział.
9. Wartość ujemna to wartość mniejsza od zera, czyli miejsce, w którym wykres leży pod osią \(x\).
10. Pod osią wykres idzie jednym ciągiem: schodzi, dochodzi do najniższego punktu i wraca.
11. W \(x = 1\) wykres dotyka osi, czyli wartość wynosi tam zero. Zero nie jest ujemne, więc \(1\) nie należy.
12. W \(x = 3\) jest tak samo.
13. Składamy końce w jeden przedział.
14. Największą wartością jest \(3\), już ją odczytaliśmy.<br>Teraz szukamy \(x\), dla których wykres jest na tej wysokości.
15. Na wysokości \(3\) leży cały poziomy odcinek.<br>W \(x = -2\) wykres tylko się załamuje, nie urywa, więc ten punkt należy.
16. Cztery odpowiedzi gotowe.

## Rozbrojone typowe błędy, dwa

1. **Nawias okrągły zamiast kątowego.** Kroki 2 i 3 pokazują oba symbole obok siebie na
   jednym rysunku, zanim padnie pierwsza odpowiedź, i wracają w krokach 11, 12 i 15.
2. **Dziedzina pomylona ze zbiorem wartości.** Kroki 1 i 5 to ten sam ruch w dwie różne
   strony: raz cień na oś \(x\), raz na oś \(y\). Różnicę widać z samego obrazu.

## Czego nie ustalono

- Nie wiadomo, czy szesnaście kropek kroków przy filmie z wykresem czyta się na telefonie
  tak samo jak przy filmie z rachunkiem: kadr jest tu gęstszy, bo wykres zajmuje jego
  większość, a wyniki zamkniętych części zostają pod nim. Do obejrzenia po renderze.
- Nie wiadomo, czy zamknięte wyniki czterech części zmieszczą się pod wykresem w kadrze
  16:9 bez zmniejszania wykresu. Jeżeli nie, wynik części znika przy zmianie etykiety,
  a zbiorczy widok czterech odpowiedzi wypada.
- `formulasPage` zostaje na 23 bez weryfikacji, czy to najlepsza strona dla tego zadania.
