# Projekt: zadania 15 i 16, arkusz 2024-grudzień

Dokument projektowy (co ma zobaczyć uczeń), nie instrukcja techniczna. Powstał 2026-08-28,
po zad. 13 i 14. Zapis do repozytorium rządzi się osobnymi plikami: `SOLUTION_TEXT_RULES.md`,
`manimations/README.md`, `COLORS.md`.

Oba zadania są zamknięte, po 1 pkt, oba z działu „ciągi" i oba mają `formulasPage: 9`.

## Stan wyjściowy

Oba mają dziś jednoakapitowe `solutionText` napisane przed zasadami z sierpnia (cały rachunek
zbity w jedno zdanie, w zad. 15 na dodatek z półpauzą) i **żadnego filmu**. Projekt zastępuje
teksty w całości i dokłada dwie sceny. Widżet zad. 15 (`widgetCiagArytmetyczny`, suwak \(m\)
i słupki trzech wyrazów) zostaje bez zmian.

## Wyniki policzone od zera i porównane z kluczem

| zadanie | mój rachunek | klucz CKE | zgodne |
|---|---|---|---|
| 15 | \(4 + 2m = \dfrac{5m + m}{2}\), stąd \(4 + 2m = 3m\) i \(m = 4\) | D | tak |
| 16 | \(q = \dfrac{1}{9} : \dfrac{1}{6} = \dfrac{2}{3}\), \(a_4 = \dfrac{2}{27}\), \(a_5 = \dfrac{4}{81}\) | C | tak |

Zasady oceniania w obu są jednozdaniowe („1 pkt, odpowiedź poprawna"), więc nie ma etapów
do pokrycia: rozwiązanie ma po prostu dowieźć literę.

---

# Zadanie 15

## Metoda

Warunek na ciąg arytmetyczny brany wprost z tablicy, wzór \([8.3]\) ze strony 9:
\(a_n = \dfrac{a_{n-1} + a_{n+1}}{2}\), czyli **środkowy wyraz jest średnią sąsiadów**.
Drugie możliwe podejście, przez stałą różnicę \((4+2m) - 5m = m - (4+2m)\), odpada:
daje dwa nawiasy z minusem przed nimi, czyli dokładnie tę operację, na której uczniowie
najczęściej gubią znak, a w tablicy i tak go nie ma.

Wzór ze średnią wchodzi jednak dopiero **po** przykładzie na liczbach (zasady tekstowe,
punkt „najpierw liczba, potem litera"): w ciągu \(2,\ 5,\ 8\) widać gołym okiem, że
\(\dfrac{2 + 8}{2} = 5\).

## Pułapka, pod którą zadanie jest napisane

Uczeń, który myli ciąg arytmetyczny z geometrycznym, szuka tu stałego ilorazu, a nie stałej
różnicy. Drugi wariant tej samej pomyłki: przekonanie, że ciąg arytmetyczny musi rosnąć.
Rozbrajają to dwa ostatnie kroki, czyli sprawdzenie: po podstawieniu \(m = 4\) ciąg wychodzi
\(20,\ 12,\ 4\), a więc **malejący**, i to właśnie w nim obie różnice są równe \(-8\).
Nie ma ostrzeżenia „uczniowie często mylą", jest policzony przykład.

## Ogniwa wypisane jawnie

- \(m\) to inaczej \(1m\), więc \(5m + 1m = 6m\), a nie \(5m\) z doklejoną literą,
- \(6m : 2 = 3m\), bo dzieli się sama szóstka,
- \(3m - 2m = 1m = m\), znowu przez jedynkę, której w zapisie nie widać.

## Linijki (dziesięć, jeden do jednego z krokami filmu)

| # | linijka |
|---|---|
| 1 | \((5m,\ 4 + 2m,\ m)\) z podpisami \(a_1,\ a_2,\ a_3\) |
| 2 | \(a_2 = \dfrac{a_1 + a_3}{2}\), po przykładzie \(\dfrac{2 + 8}{2} = 5\) |
| 3 | \(4 + 2m = \dfrac{5m + m}{2}\) |
| 4 | \(4 + 2m = \dfrac{6m}{2}\) |
| 5 | \(4 + 2m = 3m\) |
| 6 | \(4 = 3m - 2m\) |
| 7 | \(4 = m\) |
| 8 | \(\boldsymbol{m = 4}\) |
| 9 | sprawdzenie: \(20,\ 12,\ 4\) |
| 10 | \(12 - 20 = -8\) oraz \(4 - 12 = -8\) |
| , | Odpowiedź **D**. | zdanie zamykające, nie jest krokiem |

Układ: jedna kolumna z komentarzami. Wzór z tablicy jest jeden i stosuje się go na starcie,
więc stoi nad rachunkiem, nie w drugiej kolumnie. Linijki 9 i 10 idą pod kreską, w bloku
sprawdzenia: punkt CKE zapada na linijce 8.

## Kroki filmu

Kadr: pas z ciągiem na górze (zostaje do końca filmu, bo z niego przylatują wyrażenia
i do niego wracają liczby), rachunek na środku, werdykt na dole od kroku 8.

1. **Nazwanie wyrazów.** Wjeżdża ciąg \((5m,\ 4 + 2m,\ m)\), nad wyrazami pojawiają się
   podpisy \(a_1,\ a_2,\ a_3\). Bez koloru: nic się nie liczy.
2. **Skąd wzór.** Ciąg odjeżdża do pasa na górze. Na środku staje przykład \(2,\ 5,\ 8\),
   pod nim mniejszym pismem \(\dfrac{2 + 8}{2} = 5\); zielone są obie piątki, żeby było
   widać, że środkowy wyraz i średnia skrajnych to ta sama liczba. Przykład znika, a na jego
   miejsce wjeżdża wzór \(a_2 = \dfrac{a_1 + a_3}{2}\).
3. **Podstawienie.** Każda litera zamienia się w wyrażenie, które **przylatuje z pasa**:
   \(a_2\) w \(4 + 2m\), \(a_1\) w \(5m\), \(a_3\) w \(m\). Zielone są przylatujące
   wyrażenia, bo one są nowe.
4. **Licznik.** Przy samotnym \(m\) w liczniku pojawia się zielona jedynka (\(1m\)),
   dopiero potem \(5m + 1m\) zwija się w \(6m\).
5. **Dzielenie przez dwa.** \(\dfrac{6m}{2}\) zamienia się w \(3m\): szóstka i dwójka
   gasną w miejscu, w którym powstaje trójka.
6. **Przeniesienie.** Po prawej stronie linijki staje szary dopisek \(\big/ - 2m\),
   a \(2m\) leci łukiem nad znakiem równości i po drugiej stronie ląduje z minusem.
7. **Redukcja.** \(3m - 2m\) zwija się w zielone \(1m\), potem jedynka znika i zostaje \(m\).
8. **Wynik.** Obie strony zamieniają się miejscami, więc w kadrze stoi \(m = 4\).
   Na dole pojawia się napis „Odpowiedź D", czarny, i zostaje do końca. Bez koloru:
   nic się nie przelicza.
9. **Sprawdzenie, część pierwsza.** Czwórka z wyniku leci do pasa i wyrażenia zamieniają się
   w liczby: \(20,\ 12,\ 4\). Zielone są trzy nowe liczby.
10. **Sprawdzenie, część druga.** Z pasa zjeżdżają liczby do dwóch rachunków:
    \(12 - 20 = -8\) i \(4 - 12 = -8\). Zielone są oba wyniki. Widać, że różnica jest stała
    i że jest ujemna, czyli ciąg maleje.

Opis pod filmem niesie w kroku 2 wzór \([8.3]\) w ramce (jest w tablicy). W pozostałych
krokach ramki nie ma.

---

# Zadanie 16

## Metoda

Piąty wyraz liczony **po kolei**, wyraz po wyrazie: najpierw iloraz \(q\), potem \(a_4\),
potem \(a_5\). Krótsza droga \(a_5 = a_3 \cdot q^{2}\) jest dla tego ucznia gorsza: żeby ją
zrozumieć, trzeba już wiedzieć, skąd bierze się wykładnik \(2\), a to jest dokładnie ta
wiedza, której tu brakuje. Mnożenie przez \(q\) dwa razy pokazuje samą definicję ciągu
geometrycznego w działaniu.

Wzoru \([8.4]\) z tablicy tu nie używam i to jest świadome: \(a_n = a_1 \cdot q^{n-1}\)
wymaga \(a_1\), którego zadanie nie podaje, więc trzeba by go najpierw wyliczyć wstecz.
Definicji ilorazu tablica nie podaje wcale, więc idzie ona zwykłym zdaniem, bez ramki.

## Pułapka, pod którą zadanie jest napisane

Dystraktor **B** to \(\dfrac{2}{27}\), czyli **czwarty** wyraz. Kto pomnoży przez \(q\) tylko
raz, trafia dokładnie w podaną odpowiedź i nie ma jak się zorientować. Dlatego każdy wynik
pośredni jest w filmie podpisany swoją nazwą i odkładany do pasa na górze: w kadrze widać
\(a_4 = \dfrac{2}{27}\), a pytanie dotyczy \(a_5\). Drugi dystraktor, **A** \(\left(\dfrac{1}{15}\right)\),
to ciąg potraktowany jak arytmetyczny.

Drugie miejsce, w którym się tu przewraca: dzielenie ułamka przez ułamek. Dostaje trzy osobne
kroki, żeby było widać, że kreska ułamka to dzielenie, a dzielenie zamienia się na mnożenie
przez odwrotność.

## Ogniwa wypisane jawnie

- \(\dfrac{a_3}{a_2}\) to zapis dzielenia, więc \(\dfrac{1}{9} : \dfrac{1}{6}\) dostaje własną linijkę,
- odwrotność \(\dfrac{1}{6}\) zapisana jako \(\dfrac{6}{1}\), z zamianą licznika z mianownikiem
  na oczach ucznia, a nie od razu jako \(6\),
- mnożenie ułamków pisane najpierw jako \(\dfrac{1 \cdot 6}{9 \cdot 1}\), dopiero potem policzone,
- skracanie \(\dfrac{6}{9}\) przez \(3\) w osobnym kroku.

## Linijki (szesnaście, jeden do jednego z krokami filmu)

| # | linijka |
|---|---|
| 1 | \(a_2 = \dfrac{1}{6}\) oraz \(a_3 = \dfrac{1}{9}\) |
| 2 | \(q = \dfrac{a_3}{a_2}\) |
| 3 | \(q = \dfrac{\frac{1}{9}}{\frac{1}{6}}\) |
| 4 | \(q = \dfrac{1}{9} : \dfrac{1}{6}\) |
| 5 | \(q = \dfrac{1}{9} \cdot \dfrac{6}{1}\) |
| 6 | \(q = \dfrac{1 \cdot 6}{9 \cdot 1}\) |
| 7 | \(q = \dfrac{6}{9}\) |
| 8 | \(\boldsymbol{q = \dfrac{2}{3}}\) |
| 9 | \(a_4 = a_3 \cdot q\) |
| 10 | \(a_4 = \dfrac{1}{9} \cdot \dfrac{2}{3}\) |
| 11 | \(a_4 = \dfrac{1 \cdot 2}{9 \cdot 3}\) |
| 12 | \(\boldsymbol{a_4 = \dfrac{2}{27}}\) |
| 13 | \(a_5 = a_4 \cdot q\) |
| 14 | \(a_5 = \dfrac{2}{27} \cdot \dfrac{2}{3}\) |
| 15 | \(a_5 = \dfrac{2 \cdot 2}{27 \cdot 3}\) |
| 16 | \(\boldsymbol{a_5 = \dfrac{4}{81}}\) |
| , | Odpowiedź **C**. | zdanie zamykające, nie jest krokiem |

Układ: jedna kolumna z komentarzami. Wzoru z tablicy nie ma ani jednego, więc nad rachunkiem
nic nie stoi.

## Kroki filmu

Kadr: pas danych i wyników na górze, rachunek na środku, werdykt na dole. Pas rośnie w miarę
liczenia: najpierw dwa dane wyrazy, po kroku 8 dochodzi \(q\), po kroku 12 dochodzi \(a_4\).
Dzięki temu w ostatniej klatce widać obok siebie \(a_4\) i \(a_5\), czyli to, co odróżnia
poprawną odpowiedź od dystraktora B.

1. **Dane.** Wjeżdżają \(a_2 = \dfrac{1}{6}\) i \(a_3 = \dfrac{1}{9}\), a obok nich znak
   zapytania przy \(a_5\). Bez koloru.
2. **Skąd iloraz.** Dane odjeżdżają do pasa. Między \(a_2\) a \(a_3\) rysuje się strzałka
   z podpisem \(\cdot\,q\): każdy następny wyraz to poprzedni razy \(q\). Strzałka znika,
   a zostaje linijka \(q = \dfrac{a_3}{a_2}\).
3. **Podstawienie.** \(a_3\) i \(a_2\) zamieniają się w ułamki, które przylatują z pasa.
   Zielone są oba ułamki.
4. **Kreska to dzielenie.** Duża kreska ułamka zamienia się w zielony dwukropek, a licznik
   i mianownik zjeżdżają obok siebie w jedną linijkę.
5. **Odwrotność.** Dwukropek zamienia się w kropkę mnożenia, a w drugim ułamku szóstka
   i jedynka **zamieniają się miejscami**, każda po swoim łuku. Zielone są obie.
6. **Mnożenie ułamków.** Nad kreską staje \(1 \cdot 6\), pod kreską \(9 \cdot 1\).
7. **Rachunek.** \(1 \cdot 6\) zwija się w \(6\), \(9 \cdot 1\) w \(9\).
8. **Skracanie.** Nad kreską \(6\) zamienia się w \(2\), pod kreską \(9\) w \(3\), a obok
   przez chwilę stoi mniejszym pismem \(6 : 3\) i \(9 : 3\). Wynik \(q = \dfrac{2}{3}\)
   odjeżdża do pasa.
9. **Czwarty wyraz.** Na środku staje \(a_4 = a_3 \cdot q\). Bez koloru: to zapis planu.
10. **Podstawienie.** \(a_3\) i \(q\) zamieniają się w ułamki przylatujące z pasa.
11. **Mnożenie ułamków.** Nad kreską \(1 \cdot 2\), pod kreską \(9 \cdot 3\).
12. **Rachunek.** Wychodzi \(\dfrac{2}{27}\) i odjeżdża do pasa jako \(a_4\).
13. **Piąty wyraz.** Na środku staje \(a_5 = a_4 \cdot q\), znowu bez koloru.
14. **Podstawienie.** \(a_4\) i \(q\) przylatują z pasa.
15. **Mnożenie ułamków.** Nad kreską \(2 \cdot 2\), pod kreską \(27 \cdot 3\).
16. **Wynik.** Wychodzi \(\dfrac{4}{81}\), a na dole pojawia się „Odpowiedź C".

Kroki 6, 7 oraz 11 i 15 celowo powtarzają ten sam rachunek na trzy sposoby: uczeń ma zobaczyć,
że mnożenie ułamków wygląda za każdym razem tak samo, niezależnie od tego, jak brzydkie są liczby.

---

## Czego nie ustalono

- **Nie sprawdzano**, czy uczniowie faktycznie wybierają w zad. 16 dystraktor B częściej niż
  pozostałe. Sprawozdanie CKE do tego arkusza nie podaje rozkładu odpowiedzi na dystraktory,
  a arkusz jest testem diagnostycznym. Projekt zakłada, że pułapka jest realna, bo wynika
  wprost z budowy zadania (\(\dfrac{2}{27}\) to dokładnie \(a_4\)), a nie z pomiaru.
