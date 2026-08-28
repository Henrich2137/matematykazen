# Projekt: zadanie 17 (17.1 i 17.2), arkusz 2024-grudzień

Dokument projektowy (co ma zobaczyć uczeń), nie instrukcja techniczna. Powstał 2026-08-28,
po zad. 15 i 16. Zapis do repozytorium rządzi się osobnymi plikami: `SOLUTION_TEXT_RULES.md`,
`manimations/README.md`, `COLORS.md`.

Oba podpunkty są zamknięte, po 1 pkt, oba z trygonometrii i oba mają `formulasPage: 11`.
Nagłówek „Zadanie 17." (`maxScore: 0`) niesie wspólny rysunek i zostaje bez zmian.

## Stan wyjściowy

Oba mają dziś jednozdaniowe `solutionText` napisane przed zasadami z sierpnia (cały rachunek
zbity w jedno zdanie, w obu z półpauzą przed literą odpowiedzi) i **żadnego filmu**. Projekt
zastępuje teksty w całości i dokłada dwie sceny. Widżetu tu nie ma i nie projektuję go:
nie ma czym ruszać, bo trójkąt jest jeden, o ustalonych bokach.

## Rysunek z arkusza

`media/zad17/zad17.png`: \(C\) u góry z lewej, \(A\) pod nim (kąt prosty), \(B\) daleko
z prawej, \(D\) na odcinku \(AB\) blisko \(A\). Podpisane \(|AC| = \sqrt{15}\) przy pionowym
boku, \(8\) przy \(BC\), \(6\) przy odcinku \(DB\).

Kąt prosty jest przy \(A\), więc **przeciwprostokątną trójkąta \(ABC\) jest \(BC\)**,
a \(AB\) i \(AC\) to przyprostokątne. To jest jedyna trudna rzecz w 17.1 i połowa trudności
w 17.2, bo w tablicy wzorów kąt prosty stoi przy \(C\), czyli przy innej literze.

## Wyniki policzone od zera i porównane z kluczem

| zadanie | mój rachunek | klucz CKE | zgodne |
|---|---|---|---|
| 17.1 | \(\sin(\angle ABC) = \dfrac{|AC|}{|BC|} = \dfrac{\sqrt{15}}{8}\) | D | tak |
| 17.2 | \(|AB| = \sqrt{64 - 15} = 7\), \(|AD| = 1\), \(\operatorname{tg}(\angle ADC) = \dfrac{\sqrt{15}}{1} = \sqrt{15}\) | A | tak |

Zasady oceniania w obu są jednozdaniowe („1 pkt, odpowiedź poprawna"), więc nie ma etapów
do pokrycia: rozwiązanie ma po prostu dowieźć literę.

---

# Zadanie 17.1

## Metoda

Definicja sinusa kąta ostrego wprost z tablicy, wzór \([9.1]\) ze strony 11:
\(\sin\alpha = \dfrac{a}{c}\), gdzie \(a\) leży naprzeciw kąta, a \(c\) jest
przeciwprostokątną. Innej drogi tu nie ma i nie ma czego liczyć: całe zadanie polega na
tym, żeby dopasować dwa boki do dwóch miejsc we wzorze.

Dlatego rozwiązanie **nie zaczyna się od wzoru**, tylko od dwóch osobnych linijek, w których
każdy z tych boków zostaje nazwany. Wzór wchodzi dopiero jako trzecia linijka, kiedy jest
już co do niego wstawić.

## Pułapka, pod którą zadanie jest napisane

Dystraktor **B** to \(\dfrac{7}{8}\), czyli \(\dfrac{|AB|}{|BC|}\), a więc **cosinus** tego
samego kąta: bok przyległy zamiast boku naprzeciw. Kto weźmie „ten drugi" bok, trafia
w gotową odpowiedź i nie ma jak się zorientować, bo \(7\) da się w tym trójkącie policzyć.

Rozbraja to podział na dwa pierwsze kroki. W kroku 1 zapala się \(BC\) i pada słowo
„przeciwprostokątna", w kroku 2 zapala się \(AC\) i pada „naprzeciw kąta \(ABC\)". Dwa różne
boki, dwa różne kroki, dwa różne uzasadnienia. Nie ma ostrzeżenia „uczniowie często mylą",
jest dwa razy pokazany palcem inny bok.

Drugi wybrany błąd z listy to **brak kontroli wyniku**. Sinus kąta ostrego nie może wyjść
większy od \(1\), bo przeciwprostokątna jest najdłuższym bokiem. Ostatni krok to sprawdza
na liczbach, nie zdaniem „sprawdź, czy wynik ma sens".

## Ogniwa wypisane jawnie

- naprzeciw kąta prostego zawsze leży przeciwprostokątna, więc kąt prosty przy \(A\) wskazuje
  bok \(BC\), a nie ten, który jest narysowany najdłużej,
- \(\sqrt{15} < \sqrt{16} = 4\), więc licznik jest mniejszy od \(4\), a mianownik ma \(8\).

## Linijki (sześć, jeden do jednego z krokami filmu)

| # | linijka |
|---|---|
| 1 | \(|BC| = 8\) |
| 2 | \(|AC| = \sqrt{15}\) |
| 3 | \(\sin\alpha = \dfrac{a}{c}\) |
| 4 | \(\sin(\angle ABC) = \dfrac{|AC|}{|BC|}\) |
| 5 | \(\boldsymbol{\sin(\angle ABC) = \dfrac{\sqrt{15}}{8}}\) |
| 6 | sprawdzenie: \(\dfrac{\sqrt{15}}{8} < 1\) |
| , | Odpowiedź **D**. | zdanie zamykające, nie jest krokiem |

Układ: jedna kolumna z komentarzami. Wzór z tablicy jest jeden, więc stoi w rachunku jako
własna linijka, a nie w drugiej kolumnie. Linijka 6 idzie pod kreską, w bloku sprawdzenia:
punkt CKE zapada na linijce 5.

## Kroki filmu

Kadr: rysunek trójkąta po lewej stronie, w tych samych oznaczeniach co w arkuszu, przez cały
film. Rachunek po prawej. Podpisy boków na rysunku tym samym pismem co rachunek, bo na
telefonie rysunek zejdzie do ułamka szerokości ekranu.

1. **Przeciwprostokątna.** Kwadracik kąta prostego przy \(A\) mruga, a od niego przez trójkąt
   przejeżdża wzrok na przeciwległy bok: **zapala się na zielono odcinek \(BC\)** razem
   z podpisem \(8\). Po prawej staje \(|BC| = 8\). Zieleń schodzi na koniec kroku.
2. **Bok naprzeciw kąta.** Przy \(B\) rysuje się łuk kąta. **Zapala się na zielono odcinek
   \(AC\)** z podpisem \(\sqrt{15}\), czyli bok, który ten łuk „widzi" po drugiej stronie.
   Po prawej dochodzi \(|AC| = \sqrt{15}\).
3. **Wzór.** Rysunek zostaje bez koloru. Po prawej wjeżdża \(\sin\alpha = \dfrac{a}{c}\),
   a przy nim, mniejszym pismem, dwa podpisy: \(a\) naprzeciw kąta, \(c\) przeciwprostokątna.
   Podpisy znikają przed końcem kroku, wzór zostaje.
4. **Nazwy boków w miejsce liter.** \(a\) zamienia się w \(|AC|\), \(c\) w \(|BC|\), każda
   litera w miejscu, w którym stała. Jednocześnie na rysunku zapalają się oba boki naraz,
   po jednym na literę.
5. **Liczby w miejsce nazw.** \(|AC|\) zamienia się w \(\sqrt{15}\), \(|BC|\) w \(8\).
   Liczby **przylatują z rysunku**, każda ze swojego boku. Na dole pojawia się napis
   „Odpowiedź D", czarny, i zostaje do końca.
6. **Sprawdzenie sensu.** Pod wynikiem, mniejszym pismem, staje \(\sqrt{15} < \sqrt{16} = 4\),
   potem \(4 < 8\), a na końcu zostaje \(\dfrac{\sqrt{15}}{8} < 1\). Rysunek podświetla przy
   tym \(BC\) jako najdłuższy bok trójkąta.

Opis pod filmem niesie w kroku 3 wzór \([9.1]\) w ramce (jest w tablicy). W pozostałych
krokach ramki nie ma.

---

# Zadanie 17.2

## Metoda

Tangens z tablicy, wzór \([9.1]\) ze strony 11: \(\operatorname{tg}\alpha = \dfrac{a}{b}\),
czyli bok naprzeciw kąta przez bok przyległy. Brakującą przyprostokątną \(AD\) liczę przez
\(|AB|\), a \(|AB|\) z twierdzenia Pitagorasa, wzór \([10.1]\) ze strony 15.

Kolejność jest odwrotna do rachunkowej i to jest decyzja, nie przypadek: **najpierw wzór
tangensa, potem odkrycie, że \(|AD|\) nie jest dane, i dopiero potem Pitagoras**. Uczeń ma
wiedzieć, po co liczy \(|AB|\), zanim zacznie je liczyć. Ta sama kolejność co w zad. 16,
gdzie najpierw pada plan, a potem rachunek.

Drogi przez podobieństwo trójkątów albo przez funkcje kąta \(ABC\) odpadają: obie wymagają
narzędzia cięższego niż zadanie, a Pitagoras i definicja tangensa stoją w tablicy.

## Pułapka, pod którą zadanie jest napisane

Dystraktor **D** to \(\dfrac{\sqrt{15}}{8}\), czyli **odpowiedź z podpunktu 17.1**. Kto
przepisze poprzedni wynik albo policzy funkcję kąta przy \(B\) zamiast przy \(D\), trafia
w gotową odpowiedź. Sedno tego podpunktu jest właśnie takie: kąt jest inny i trójkąt
jest inny, mimo że rysunek ten sam.

Rozbraja to krok 1: na rysunku **zapala się mały trójkąt \(ACD\)**, a reszta, czyli
odcinek \(DB\), zostaje szara. Uczeń widzi, że pracujemy w innej figurze, zanim padnie
jakikolwiek wzór. Ta sama różnica wraca w kroku 12, kiedy przy \(AD\) staje \(1\), a przy
\(AB\) stoi już \(7\): dwa różne odcinki, dwie różne liczby, obie w kadrze naraz.

Drugi wybrany błąd z listy to **pierwiastek i potęga**: \((\sqrt{15})^{2}\). Dostaje własny
komentarz i własny moment w kroku 8, bo podniesienie do kwadratu i pierwiastek znoszą się
tylko wtedy, gdy uczeń wie, że to robią.

## Ogniwa wypisane jawnie

- \(|AD| = |AB| - |DB|\), bo \(D\) leży **na** odcinku \(AB\), a \(|DB| = 6\),
- \((\sqrt{15})^{2} = 15\), bo pierwiastek pyta „co podniesione do kwadratu daje \(15\)",
  a kwadrat to od razu odwraca,
- \(|AB| = 7\), bo \(7 \cdot 7 = 49\), a długość boku nie bywa ujemna,
- dzielenie przez \(1\) niczego nie zmienia, więc \(\dfrac{\sqrt{15}}{1} = \sqrt{15}\).

## Linijki (piętnaście, jeden do jednego z krokami filmu)

| # | linijka |
|---|---|
| 1 | \(|AC| = \sqrt{15}\) oraz \(|DB| = 6\) |
| 2 | \(\operatorname{tg}\alpha = \dfrac{a}{b}\) |
| 3 | \(\operatorname{tg}(\angle ADC) = \dfrac{|AC|}{|AD|}\) |
| 4 | \(|AD| = |AB| - 6\) |
| 5 | \(a^{2} + b^{2} = c^{2}\) |
| 6 | \(|AB|^{2} + |AC|^{2} = |BC|^{2}\) |
| 7 | \(|AB|^{2} + (\sqrt{15})^{2} = 8^{2}\) |
| 8 | \(|AB|^{2} + 15 = 64\) |
| 9 | \(|AB|^{2} = 64 - 15\) |
| 10 | \(|AB|^{2} = 49\) |
| 11 | \(\boldsymbol{|AB| = 7}\) |
| 12 | \(|AD| = 7 - 6\) |
| 13 | \(\boldsymbol{|AD| = 1}\) |
| 14 | \(\operatorname{tg}(\angle ADC) = \dfrac{\sqrt{15}}{1}\) |
| 15 | \(\boldsymbol{\operatorname{tg}(\angle ADC) = \sqrt{15}}\) |
| , | Odpowiedź **A**. | zdanie zamykające, nie jest krokiem |

Układ: jedna kolumna z komentarzami. Wzory z tablicy są dwa, ale wchodzą w odległych
miejscach rachunku (linijka 2 i linijka 5), więc każdy stoi jako własna linijka, a nie
w drugiej kolumnie. Osobny odstęp oddziela trzy części: plan (1 do 4), Pitagoras (5 do 13)
i powrót do tangensa (14 do 15).

## Kroki filmu

Kadr: ten sam rysunek co w 17.1, po lewej, przez cały film. Rachunek po prawej. Liczby
policzone po drodze **dopisują się na rysunku przy swoim odcinku**, nie do tabelki z boku:
po kroku 11 przy \(AB\) staje \(7\), po kroku 13 przy \(AD\) staje \(1\).

1. **Który trójkąt.** Przy \(D\) rysuje się łuk kąta \(ADC\). **Zapala się trójkąt \(ACD\)**,
   czyli boki \(AC\), \(CD\) i \(AD\), a odcinek \(DB\) zostaje szary. Po prawej staje
   \(|AC| = \sqrt{15}\) oraz \(|DB| = 6\).
2. **Wzór.** Po prawej wjeżdża \(\operatorname{tg}\alpha = \dfrac{a}{b}\), a przy nim
   mniejszym pismem: \(a\) naprzeciw kąta, \(b\) przy kącie. Podpisy znikają, wzór zostaje.
3. **Nazwy boków.** \(a\) zamienia się w \(|AC|\), \(b\) w \(|AD|\). Na rysunku zapala się
   przy tym \(AC\) (znane) i osobno \(AD\), przy którym staje **znak zapytania**.
   Znak zapytania zostaje na rysunku aż do kroku 13.
4. **Skąd wziąć \(AD\).** Na rysunku zapala się cały odcinek \(AB\), a potem od jego prawego
   końca odcina się kawałek \(DB\) z podpisem \(6\). Po prawej staje \(|AD| = |AB| - 6\).
   Widać, że \(AD\) jest tym, co z \(AB\) zostaje.
5. **Pitagoras.** Rysunek wraca do dużego trójkąta \(ABC\), kwadracik kąta prostego przy
   \(A\) mruga. Po prawej wjeżdża \(a^{2} + b^{2} = c^{2}\), a przy nim mniejszym pismem
   podpis, że \(c\) to przeciwprostokątna, czyli bok naprzeciw kąta prostego.
6. **Nazwy boków.** \(a\) zamienia się w \(|AB|\), \(b\) w \(|AC|\), \(c\) w \(|BC|\).
   Każda nazwa zapala się jednocześnie ze swoim bokiem na rysunku.
7. **Liczby w miejsce nazw.** \(|AC|\) zamienia się w \(\sqrt{15}\), \(|BC|\) w \(8\).
   Liczby przylatują z rysunku. \(|AB|\) zostaje nazwą, bo jest niewiadomą.
8. **Kwadraty.** \((\sqrt{15})^{2}\) zamienia się w \(15\): najpierw znika daszek pierwiastka,
   potem dwójka wykładnika, a pod spodem, mniejszym pismem, przez chwilę stoi
   \(\sqrt{15} \cdot \sqrt{15} = 15\). Równocześnie \(8^{2}\) zwija się w \(64\).
9. **Przeniesienie.** Po prawej stronie linijki staje szary dopisek \(\big/ - 15\),
   a \(15\) leci łukiem nad znakiem równości i po drugiej stronie ląduje z minusem.
10. **Odejmowanie.** \(64 - 15\) zwija się w \(49\).
11. **Pierwiastkowanie.** Dwójka wykładnika przy \(|AB|\) gaśnie, a po prawej \(49\) zamienia
    się w \(7\); pod spodem, mniejszym pismem, przez chwilę stoi \(7 \cdot 7 = 49\).
    Siódemka **odlatuje na rysunek** i zostaje przy odcinku \(AB\).
12. **Odejmowanie odcinków.** Linijka \(|AD| = |AB| - 6\) wraca na środek, a \(|AB|\)
    zamienia się w \(7\), które przylatuje z rysunku.
13. **Długość \(AD\).** \(7 - 6\) zwija się w \(1\). Jedynka odlatuje na rysunek i zastępuje
    znak zapytania przy \(AD\). Na rysunku stoją teraz obok siebie \(7\) przy \(AB\)
    i \(1\) przy \(AD\).
14. **Powrót do tangensa.** Linijka \(\operatorname{tg}(\angle ADC) = \dfrac{|AC|}{|AD|}\)
    wraca na środek, \(|AC|\) zamienia się w \(\sqrt{15}\), \(|AD|\) w \(1\), obie liczby
    przylatują z rysunku.
15. **Wynik.** Jedynka w mianowniku gaśnie razem z kreską ułamka i zostaje \(\sqrt{15}\).
    Na dole pojawia się napis „Odpowiedź A".

Opis pod filmem niesie w kroku 2 wzór \([9.1]\), a w kroku 5 wzór \([10.1]\), oba w ramce
(oba są w tablicy). W pozostałych krokach ramki nie ma.

---

## Czego nie ustalono

- **Nie sprawdzano**, czy uczniowie faktycznie wybierają w 17.2 dystraktor D częściej niż
  pozostałe. Sprawozdanie CKE do tego arkusza nie podaje rozkładu odpowiedzi na dystraktory,
  a arkusz jest testem diagnostycznym. Projekt zakłada, że pułapka jest realna, bo wynika
  wprost z budowy zadania (\(\dfrac{\sqrt{15}}{8}\) to dokładnie odpowiedź z 17.1), a nie
  z pomiaru.
- **Nie ustalono, skąd bierze się dystraktor C w 17.1** (\(\dfrac{\sqrt{15}}{4}\)). Dla B
  (\(\dfrac{7}{8}\), cosinus) i A (\(\dfrac{1}{2}\), wartość z tabelki dla \(30^\circ\))
  droga jest widoczna, dla C nie, więc projekt jej nie rozbraja i nie zgaduje.
- **Nie zmierzono czytelności rysunku na telefonie.** Oba filmy trzymają rysunek w kadrze
  przez cały czas, a rysunek jest szeroki (około \(1{,}8:1\)). Ryzyko jest to samo, co
  zgłoszone przy zad. 10, 11 i 12 (wpisy `TESTOWANIE HENRICH` v96 i v97), i sprawdza się
  je dopiero na wyrenderowanym filmie, nie na etapie projektu.
## Co zmieniło się przy realizacji (2026-08-28)

Filmy są zrobione: `manimations/solutionZad17_1.py` (6 kroków) i `solutionZad17_2.py`
(15 kroków). Trzy rzeczy wyszły przy renderze inaczej, niż zakładał projekt:

- **Podpis odcinka \(AD\) nie mieści się pod podstawą.** \(AD\) ma jedną siódmą długości
  podstawy, więc liczba wpisana pod nim zlewa się z literą \(D\) i z szóstką. Zamiast tego
  są **dwie klamry na różnych głębokościach**: krótka pod \(AD\) (najpierw znak zapytania,
  od kroku 13 jedynka) i długa pod \(AB\) (siódemka od kroku 11). Klamra mówi jednoznacznie,
  którego odcinka dotyczy liczba, a ostatnia klatka pokazuje obie naraz, czyli dokładnie to,
  o co w tym podpunkcie chodzi.
- **W 17.1 liczby wlatują do wzoru z pasa odczytu, nie wprost z rysunku** (krok 5). Pas trzyma
  obie potrzebne wartości, więc wracają stamtąd, gdzie je odczytaliśmy (`manimations/README.md`,
  punkt 38). W 17.2 źródłem jest sam rysunek, bo ósemka nigdy nie trafia do pasa.
- **Małe podpisy liter przy wzorach odpadły.** Projekt przewidywał legendę („\(a\) naprzeciw
  kąta, \(c\) przeciwprostokątna") mniejszym pismem w kroku ze wzorem. To jest opisywanie
  tego, co i tak widać w następnym kroku, więc kroki ze wzorem są dziś czyste i bez koloru.
  Legenda została w opisie pod filmem.

Rachunki pomocnicze, które zostały: \(\sqrt{15} < \sqrt{16} = 4\) w kroku 6 filmu 17.1
oraz \(\sqrt{15} \cdot \sqrt{15} = 15\) (krok 8) i \(7 \cdot 7 = 49\) (krok 11)
w filmie 17.2. Wszystkie stoją mniejszym pismem i znikają przed końcem swojego kroku.

Sprawdzone po renderze: styki klatek od 0,9997 w górę w obu scenach, zieleń schodzi do zera
w każdym kroku, `tools/test-krokow.js` na obu kartach bez zastrzeżeń.
