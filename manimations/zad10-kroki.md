# Zadanie 10, kroki rozwiązania

> **Uwaga: czekają poprawki** (Henrich, 2026-08-28, wpisane w `TODO.md`, sekcja
> DO ZROBIENIA). Zapis budowany pod nagłówkiem części ma wyglądać tak samo jak pozycje
> listy odpowiedzi. Krok 9 (warunek \(y < 0\) ze strzałką) wypada. Kroki 2 i 3 łączą się
> w jeden, tak samo 11, 12 i 13, i analogicznie pozostałe pary odczytujące te same symbole.
> Zasady spisane: `manimations/README.md`, punkty 42 do 44, oraz punkt 2c w skillu
> `projektowanie-rozwiazan`.

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

Scena: `solutionZad10.py`. Projekt dydaktyczny:
[../issues/projekt-zad9-zad10-2024-grudzien.md](../issues/projekt-zad9-zad10-2024-grudzien.md).

Pierwszy film w tym arkuszu, który **nie rozpisuje rachunku, tylko czyta rysunek**.
Szesnaście kroków, jeden do jednego z szesnastoma linijkami rozwiązania opisowego.

## Treść

Funkcja \(f\) dana trzema wzorami, wykres w arkuszu. Cztery luki do uzupełnienia,
po jednym punkcie każda. Odpowiedzi, zgodne z kluczem CKE:

| luka | odpowiedź |
|---|---|
| dziedzina | \((-4,\ 4\rangle\) |
| zbiór wartości | \(\langle -1,\ 3\rangle\) |
| wartości ujemne | \((1,\ 3)\) |
| argumenty największej wartości | \((-4,\ -2\rangle\) |

## Układ kadru

Inny niż w pozostałych scenach, bo nie ma tu rachunku do rozpisania:

- **lewa połowa**: układ współrzędnych z wykresem, odwzorowany z rysunku w arkuszu
  (ten sam fiolet, ten sam podpis \(y = f(x)\), kółko otwarte w \((-4,\ 3)\), kropka
  pełna w \((4,\ 1)\)). Zakres osi \(y\) jest węższy niż w arkuszu (\(-2\) do \(4\)
  zamiast \(-5\) do \(5\)), bo kadr 16:9 jest niski, a wykres i tak żyje między
  \(-1\) a \(3\). Jednostki na obu osiach są równe, więc kształt jest ten sam;
- **prawa połowa**: etykieta bieżącej części (zmienia się cztery razy), zapis
  budowany z dwóch końców przedziału i lista zamkniętych odpowiedzi, która rośnie
  do czterech pozycji i zostaje w kadrze do końca.

Wykres, osie, siatka i lista wyników to **scenografia**: stoją przez cały film i nigdy
nie gasną. Każdy krok dokłada tylko to, co w nim zielone.

## Kroki

| # | Co się dzieje | Zielone |
|---|---|---|
| 1 | wykres powstaje od zera, rzut całego wykresu na oś \(x\) | pas dziedziny na osi |
| 2 | kółko otwarte zjeżdża na oś, zapis \((-4\) | kółko i zapis |
| 3 | kropka pełna zjeżdża na oś, zapis \(4\rangle\) | kropka i zapis |
| 4 | oba końce składają się w \((-4,\ 4\rangle\) i idą na listę | nic |
| 5 | ten sam wykres, ale rzut na oś \(y\) | pas wartości na osi |
| 6 | najniższy punkt \((2,\ -1)\) jedzie na oś \(y\), zapis \(\langle -1\) | kropka i zapis |
| 7 | poziomy odcinek jedzie na oś \(y\), zapis \(3\rangle\) | odcinek, kropka i zapis |
| 8 | składamy \(\langle -1,\ 3\rangle\), idzie na listę | nic |
| 9 | warunek \(y < 0\) przy osi \(y\), ze strzałką w dół | warunek i strzałka |
| 10 | fragment wykresu pod osią zapala się jednym ciągiem i rzutuje na oś | fragment i pas |
| 11 | \((1,\ 0)\) jako pusta kropka, zapis \((1\) | kropka i zapis |
| 12 | to samo w \((3,\ 0)\), zapis \(3)\) | kropka i zapis |
| 13 | składamy \((1,\ 3)\), idzie na listę | nic |
| 14 | poziom \(y = 3\) przez cały wykres | linia i podpis |
| 15 | poziomy odcinek rzutuje się na oś, pusta kropka w \(-4\), pełna w \(-2\) | odcinek, pas i końce |
| 16 | pas zamienia się w \((-4,\ -2\rangle\) i idzie na listę | nic |

Na ostatniej klatce w kadrze stoją **wszystkie cztery odpowiedzi naraz**, obok wykresu.

## Dlaczego to zadanie w ogóle dostało film

Cztery pytania to cztery różne sposoby patrzenia na ten sam obraz: raz rzutujemy wykres
na oś \(x\), raz na oś \(y\), raz szukamy tego, co pod osią, raz tego, co najwyżej.
Ruch odpowiada dokładnie temu, co uczeń ma zrobić w głowie. Widżet
`widgetFunkcjaPrzedzialami` pokazuje to interaktywnie i zostaje; film ma być zrozumiały
bez niego.

## Co zmierzono po renderze (2026-08-28)

- `tools/zielen-krokow.py`: każdy krok zaczyna i kończy się bez zieleni, bez zastrzeżeń.
- `tools/test-krokow.js --zadania=9`: dwa ziarna, bez zastrzeżeń.
- `tools/styk-klatek.sh`: trzynaście z piętnastu styków powyżej progu 0,999
  (od 0,99920 do 0,99993). **Dwa styki są poniżej**: 1→2 daje 0,99885, a 2→3 daje 0,99878.
- Te dwa styki sprawdzone osobno, bo skrypt świeci na nich czerwono:
  - mapa różnic pokazuje słabe obrysy **wszystkich** krawędzi kadru (siatka, wykres, tekst),
    a nie jeden element obecny w jednej klatce, czyli nie ma tam różnicy treści;
  - klatki 0 do 5 pliku `step2.mp4` są między sobą nieruchome i wszystkie odbiegają od
    końca `step1.mp4` tak samo, więc nie chodzi o animację, która „dogania";
  - największa różnica pojedynczego piksela to 159 na 765 możliwych, przy 1194 pikselach
    z 921600 różniących się o więcej niż 30.
- **Czego nie ustalono:** dlaczego akurat te dwa styki, skoro kroki 2 i 3 kończą się tak
  samo jak krok 4, którego styk wypada 0,99993. Wydłużenie postoju na końcu kroku,
  rozjaśnienie siatki i wprowadzanie kopii z zerową przezroczystością (żeby nie dokładać
  drugiej krawędzi na tę samą) niczego tu nie zmieniły. Scena ma dużo cienkich linii,
  więc podejrzenie pada na kompresję, ale to jest przypuszczenie, nie pomiar.
