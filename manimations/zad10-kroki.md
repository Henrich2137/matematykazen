# Zadanie 10, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

Scena: `solutionZad10.py`. Projekt dydaktyczny:
[../issues/projekt-zad9-zad10-2024-grudzien.md](../issues/projekt-zad9-zad10-2024-grudzien.md).

Pierwszy film w tym arkuszu, który **nie rozpisuje rachunku, tylko czyta rysunek**.
Dziewięć kroków, jeden do jednego z dziewięcioma linijkami rozwiązania opisowego.

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
| 2 | oba końce naraz: kółko otwarte i kropka pełna zjeżdżają na oś, powstają dwa kawałki zapisu | końce i zapisy |
| 3 | kawałki składają się w \((-4,\ 4\rangle\) i idą na listę | nic |
| 4 | ten sam wykres, ale rzut na oś \(y\) | pas wartości na osi |
| 5 | najniższy punkt i poziomy odcinek jadą na oś \(y\), przedział powstaje i idzie na listę | punkt, odcinek i zapisy |
| 6 | fragment wykresu pod osią zapala się jednym ciągiem i rzutuje na oś \(x\) | fragment i pas |
| 7 | oba końce wyłączone (w nich wartość jest zerem), przedział idzie na listę | puste kropki i zapisy |
| 8 | poziom \(y = 3\) przez cały wykres | linia i podpis |
| 9 | poziomy odcinek rzutuje się na oś, przedział idzie na listę, **etykieta części znika** | odcinek, pas i końce |

Podział jest nierówny celowo: **pierwsza część idzie wolniej** (trzy kroki), bo tam pierwszy
raz tłumaczy się kółko i kropkę. Każda następna ma dwa kroki, bo powtarza znany już odczyt.
To jest wprost zasada z `manimations/README.md`, punkt 42: w filmie, który czyta rysunek,
jednostką kroku jest jedna myśl, a nie jeden symbol.

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
- `tools/styk-klatek.sh`: osiem styków, od 0,99929 do 0,99993, **bez zastrzeżeń**. Dwa styki,
  które w pierwszej wersji wypadały poniżej progu, zniknęły razem z krokami, których dotyczyły;
  przy okazji poprawiła je też zmiana, dzięki której kopia znacznika startuje niewidoczna,
  zamiast dokładać drugą krawędź na oryginał już w pierwszej klatce kroku.
