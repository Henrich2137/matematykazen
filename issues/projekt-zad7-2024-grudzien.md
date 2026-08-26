# Projekt lepszych rozwiązań: zadanie 7, arkusz 2024-grudzień

Dokument projektowy, nie kod. Opisuje, co uczeń ma zobaczyć i zrozumieć.
Wpisanie do repozytorium to osobny krok: `SOLUTION_TEXT_RULES.md` i `manimations/README.md`.

Data: 2026-08-26. **Wdrożone tego samego dnia** (v84 Beta): podpowiedź, `solutionText`
i czternastokrokowy film są już w repozytorium.

## Zadanie i klucz

Para liczb \(x=-1\) i \(y=6\) jest rozwiązaniem układu
\[\begin{cases} ax + 3y = 20 \\ x + by = 5 \end{cases}\]
Pytanie: ile wynosi \(a \cdot b\). Odpowiedzi: A. \(-2\), B. \(-0{,}5\), C. \(0{,}5\), D. \(2\).

Policzone od zera: \(a\cdot(-1) + 3\cdot 6 = 20\), więc \(-a + 18 = 20\), \(-a = 2\), \(a = -2\).
Dalej \((-1) + b\cdot 6 = 5\), więc \(6b = 6\), \(b = 1\). Stąd \(a\cdot b = -2\).
**Zgadza się z kluczem CKE: odpowiedź A** (`odpowiedzi.pdf`, s. 6; zasady oceniania to samo
1 pkt za poprawną odpowiedź, żadnych kryteriów cząstkowych).

## Co jest dziś nie tak

| miejsce | co jest teraz | dlaczego to wada |
|---|---|---|
| podpowiedź | „Podstaw podane wartości x i y do obu równań, oblicz a i b, a następnie ich iloczyn" | to jest cały plan rozwiązania, a nie rusztowanie. Po jej przeczytaniu pierwszy rachunek przepisuje się bez myślenia, czyli podpowiedź przekracza próg z SKILL.md |
| oba tory | lewy tor rozbija mnożenie na osobny krok, prawy robi podstawienie i przestawienie \(b\cdot 6\) na \(6b\) w jednym | uczeń widzi dwa różne tempa dla dwóch bliźniaczych rachunków. Krok 8 filmu robi dwie rzeczy naraz, wbrew regule „jeden krok = jedno przekształcenie" |
| lewy tor | \(a\cdot(-1) + 3\cdot 6 = 20\) przechodzi od razu w \(-a + 18 = 20\) | w jednym ruchu dzieje się reguła znaku i zwykły rachunek. Reguła znaku to dokładnie ta pułapka, na której powstaje dystraktor D |
| opisy kroków | krok 1 mówi „Zapisujemy układ z zadania" | opisuje słowami to, co widać w kadrze |

Czego **nie** trzeba ruszać: liczba linijek rozwiązania opisowego zgadza się dziś z liczbą
kroków filmu (12 do 12, plus wiersz „Odpowiedź A." przez całą szerokość). Układ dwóch torów
też zostaje: to jest świadomy wzorzec Henricha z 2026-08-21 i pasuje do rachunku.

## Dwie pułapki, które rozbrajamy

Wybrane z `references/typowe-bledy.md`, po jednej na artefakt, wplecione w te kroki,
w których grożą.

- **Znak przy mnożeniu przez \(-1\)** (grupa „Znaki, nawiasy, ułamki"). Uczeń, który zapisze
  \(-a = 2\) i odczyta stąd \(a = 2\), trafia prosto w odpowiedź D. Rozbrajamy osobnym krokiem
  filmu, w którym minus powstaje na oczach ucznia, i drugim, w którym minus przechodzi na wynik.
- **Odpowiedź na inne pytanie** (grupa „Czytanie treści zadania"). Uczeń liczy \(a = -2\),
  widzi \(-2\) wśród odpowiedzi i kończy, nie licząc iloczynu. Tym razem trafia dobrze
  przypadkiem, ale nawyk zostaje na zadania, w których to kosztuje punkt. Rozbrajamy
  przedostatnim krokiem, który wraca do polecenia.

## Podpowiedź

> Zapis „para \(x=-1\), \(y=6\) jest rozwiązaniem układu" znaczy, że po wstawieniu tych
> dwóch liczb **oba** równania mają się zgadzać.
> Popatrz, co po takim wstawieniu zostaje niewiadomą.

Dlaczego tak: podpowiedź odsyła do słowa z treści („jest rozwiązaniem"), a nie podaje planu.
Uczeń dalej musi sam zauważyć, że rolami zamieniły się litery: znane są \(x\) i \(y\),
szukane \(a\) i \(b\). To jest jedyna trudność tego zadania, więc to ona ma zostać dla ucznia.

## Rozwiązanie opisowe

Układ **dwa tory** bez zmian (`rozw-2kol rozw-dwatory rozw-srodek`). Kolumny wzorów nie ma,
bo w tablicy wzorów nie ma tu czego położyć, więc **w tym rozwiązaniu nie ma zieleni**:
zielony chodzi w parze ze wzorem obok, a wzoru obok nie będzie. Nie dokładaj koloru.

Wiersz wspólny na górze (przez obie kolumny):

1. \(\begin{cases} ax + 3y = 20 \\ x + by = 5 \end{cases}\)

Dalej dwa tory obok siebie:

| lewy tor, szukamy \(a\) | prawy tor, szukamy \(b\) |
|---|---|
| 2. \(ax + 3y = 20\) | 8. \(x + by = 5\) |
| 3. \(a \cdot (-1) + 3 \cdot 6 = 20\) | 9. \((-1) + b \cdot 6 = 5\) |
| 4. \(-a + 3 \cdot 6 = 20\) | 10. \(-1 + 6b = 5\) |
| 5. \(-a + 18 = 20\) | 11. \(6b = 6\) |
| 6. \(-a = 2\) | 12. \(b = 1\) |
| 7. \(a = -2\) | (komórka pusta, na KOŃCU kolumny) |

Wiersze wspólne na dole (przez obie kolumny):

13. \(a \cdot b = (-2) \cdot 1\)
14. \(\boldsymbol{a \cdot b = -2}\)
15. Odpowiedź **A**.

Razem **14 linijek rachunku**, czyli 14 kroków filmu, plus wiersz z odpowiedzią.
To o dwie linijki więcej niż dziś: doszła linijka 4 (sama reguła znaku) i linijka 10
(samo uporządkowanie zapisu w prawym torze). Prawy tor jest teraz o jedną linijkę krótszy
od lewego, więc pusta komórka idzie na sam dół tej kolumny, nie w jej środek.

## Film krok po kroku

Czternaście kroków, każdy w schemacie: wszystko czarne, zapala się zielone to, co się zmienia,
animacja, znów wszystko czarne. Kroki, które tylko coś wybierają albo przesuwają, są bez koloru.

### Etap pierwszy, wyznaczamy \(a\)

**Krok 1.** Przed: pusty kadr. Ruch: wjeżdża cały układ w klamrze. Po: układ na środku.
Koloru brak, nic się nie przelicza.
Opis: „Znane są \(x\) i \(y\). Szukamy \(a\) oraz \(b\)."

**Krok 2.** Przed: układ w klamrze. Ruch: pierwsze równanie wysuwa się z klamry i zjeżdża
na środek kadru, reszta znika. Po: samo \(ax + 3y = 20\). Koloru brak, to tylko wybór.
Opis: „Bierzemy pierwsze równanie. Drugim zajmiemy się osobno, za chwilę."

**Krok 3.** Przed: \(ax + 3y = 20\). Zapalają się na zielono litery \(x\) i \(y\), bo one
za chwilę znikną, ustępując miejsca liczbom. Ruch: \(-1\) **wsuwa się dokładnie w miejsce**
litery \(x\), a \(6\) w miejsce litery \(y\); nawiasy przy \(-1\) pojawiają się, ale nawiasów
nie kolorujemy. Po: \(a \cdot (-1) + 3 \cdot 6 = 20\).
Opis: „Skoro ta para jest rozwiązaniem, to po wstawieniu liczb równanie musi się zgadzać."

**Krok 4.** To jest nowy krok i on niesie pułapkę znaku. Przed: \(a \cdot (-1) + 3 \cdot 6 = 20\).
Zapalają się na zielono kropka mnożenia, jedynka i jej minus, czyli to, co zaraz zmieni rolę.
Ruch: kropka i nawiasy znikają, a minus **przesuwa się przed literę** \(a\) i tam zostaje,
czyli zamienia się w znak całego wyrazu, zamiast zniknąć i pojawić się gdzie indziej.
Litera \(a\) zostaje czarna, bo dalej jest tą samą literą. Po: \(-a + 3 \cdot 6 = 20\).
Opis: „Mnożenie przez \(-1\) nie zmienia litery, zmienia tylko jej znak.
Na liczbach widać to od razu: \(7 \cdot (-1)\) to \(-7\)."

**Krok 5.** Przed: \(-a + 3 \cdot 6 = 20\). Zielone: \(3\), kropka i \(6\), bo znikają.
Ruch: trzy czynniki schodzą się w jedną liczbę \(18\). Po: \(-a + 18 = 20\). Bez opisu,
widać wszystko.

**Krok 6.** Przed: \(-a + 18 = 20\). Zielone: \(18\) razem ze swoim plusem.
Ruch: osiemnastka **przelatuje przez znak równości** i po drodze zmienia znak, a po prawej
stronie zlewa się z dwudziestką w \(2\). Po: \(-a = 2\).
Opis: „Osiemnastka zmienia znak, bo przechodzi na drugą stronę:\[20 - 18 = 2\]"

**Krok 7.** Przed: \(-a = 2\). Zielone: minus przed \(a\) oraz dwójka po prawej, bo obie
te rzeczy zmienią wartość. Ruch: minus sprzed \(a\) **przelatuje na prawą stronę** i staje
przed dwójką. Po: \(a = -2\).
Opis: „Chcemy samo \(a\), więc obie strony mnożymy przez \(-1\). Minus wędruje na wynik."

### Etap drugi, wyznaczamy \(b\)

**Krok 8.** Przed: \(a = -2\) na środku. Ruch: napis \(a = -2\) odjeżdża pod górną krawędź
kadru i tam zostaje do końca filmu, a na jego miejsce wjeżdża \(x + by = 5\).
Koloru brak, nic się nie przelicza. Bez opisu.

**Krok 9.** Bliźniak kroku 3. Przed: \(x + by = 5\). Zielone: litery \(x\) i \(y\).
Ruch: \(-1\) wsuwa się w miejsce \(x\), \(6\) w miejsce \(y\). Po: \((-1) + b \cdot 6 = 5\).
Bez opisu, uczeń widział ten sam ruch sześć kroków wcześniej.

**Krok 10.** Nowy krok, bliźniak kroku 4, tylko tu chodzi o porządek zapisu, nie o znak.
Przed: \((-1) + b \cdot 6 = 5\). Zielone: kropka mnożenia oraz szóstka, bo szóstka zmienia
miejsce i rolę. Ruch: nawiasy przy \(-1\) znikają, a szóstka **przesuwa się przed literę**
\(b\); litera \(b\) zostaje czarna. Po: \(-1 + 6b = 5\).
Opis: „Liczbę przy niewiadomej zapisujemy z przodu, więc zamiast \(b \cdot 6\) piszemy \(6b\)."

**Krok 11.** Przed: \(-1 + 6b = 5\). Zielone: \(-1\). Ruch: minus jedynka przelatuje przez
znak równości, zmienia znak i zlewa się z piątką w \(6\). Po: \(6b = 6\).
Opis: „Znów zmiana znaku przy przejściu na drugą stronę:\[5 + 1 = 6\]"

**Krok 12.** Przed: \(6b = 6\). Zielone: obie szóstki, bo obie znikają.
Ruch: szóstka sprzed \(b\) i szóstka po prawej znikają jednocześnie, dzieląc obie strony.
Po: \(b = 1\). Bez opisu.

### Etap trzeci, wracamy do polecenia

**Krok 13.** To jest krok, który rozbraja odpowiadanie na inne pytanie.
Przed: \(b = 1\) na środku, \(a = -2\) pod górną krawędzią. Ruch: napis \(a = -2\) zjeżdża
z góry, oba wyniki spotykają się i **wsuwają w miejsca liter** w świeżo zapisanym \(a \cdot b\).
Zielone: litery \(a\) i \(b\), bo ustępują liczbom. Po: \(a \cdot b = (-2) \cdot 1\).
Opis: „Pytanie dotyczy iloczynu \(a \cdot b\), a nie samego \(a\) ani samego \(b\)."

**Krok 14.** Przed: \(a \cdot b = (-2) \cdot 1\). Zielone: kropka, nawiasy pomijamy,
oraz jedynka, bo znika. Ruch: jedynka i kropka znikają, a \(-2\) zostaje jako wynik.
Po: \(a \cdot b = -2\).
Opis: „Mnożenie przez \(1\) niczego nie zmienia. Odpowiedź **A**."

## Widżet

**Nie projektuję i nie polecam.** To jest czyste przekształcanie równań: nie ma tu wielkości,
którą uczeń mógłby poruszyć, ani zależności, którą miałby zaobserwować. Pole `solutionWidget`
zostaje puste.

## Czego nie ustalono

- **Czy 14 kroków nie jest już za dużo jak na zadanie za 1 punkt.** To ocena Henricha, nie moja.
  Jeśli ma być krócej, pierwszy do sklejenia jest krok 5 z krokiem 4, ale wtedy wraca
  pułapka znaku w jednym ruchu z rachunkiem, czyli tracimy główny zysk tej poprawki.
- ~~Jak w Manimie zrobić „minus przesuwa się przed literę"~~. **Ustalone przy renderze:**
  same pary glifów wystarczyły, ale ruch po linii prostej wyglądał w połowie jak
  przekreślenie litery, bo znak przelatywał przez nią na wylot. Rozwiązaniem jest
  `path_arc`, czyli łuk zamiast prostej: w kroku 4 minus obchodzi literę \(a\),
  a w kroku 10 szóstka i litera \(b\) mijają się łukiem, zamiast przelatywać jedna
  przez drugą. Sprawdzone na klatce ze środka obu kroków.
- **Łamanie linijek na telefonie.** W wąskiej kolumnie długie linijki łamią się w środku
  wzoru („\(a \cdot (-1) + 3 \cdot\)" i niżej „\(6 = 20\)"). Tak było i przed tą zmianą,
  ale teraz łamią się dwie linijki zamiast jednej. Nie ruszałem tego, bo to zmiana w CSS,
  nie w treści; wpis jest w TODO.md.
- **Czy podpowiedź w nowej wersji nie jest za słaba.** Sprawdzalne tylko na uczniu.
