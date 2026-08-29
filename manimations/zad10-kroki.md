# Zadanie 10, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

Scena: `solutionZad10.py`. Projekt dydaktyczny:
[../issues/projekt-zad9-zad10-2024-grudzien.md](../issues/projekt-zad9-zad10-2024-grudzien.md).

Pierwszy film w tym arkuszu, który **nie rozpisuje rachunku, tylko czyta rysunek**.
Pięć kroków: jeden na sam rysunek i po jednym na każde z czterech zdań do uzupełnienia.

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
- **prawa połowa**: nagłówek bieżącej części (zmienia się cztery razy) i lista
  odpowiedzi, która rośnie do czterech pozycji i zostaje w kadrze do końca.

Wykres, osie, siatka i lista wyników to **scenografia**: stoją przez cały film i nigdy
nie gasną. Każdy krok dokłada tylko to, co w nim zielone.

## Kroki

| # | Co się dzieje | Zielone |
|---|---|---|
| 1 | powstaje układ współrzędnych, wykres i jego dwa końce | nic, nic się jeszcze nie odczytuje |
| 2 | **zdanie 1, dziedzina**: rzut obu końców na oś \(x\), każdy ze swoją kropką, pas między nimi, pas zamienia się w \((-4,\ 4\rangle\) na liście | rzuty, końce, pas |
| 3 | **zdanie 2, zbiór wartości**: najniższy punkt i poziomy odcinek rzutują się na oś \(y\), pas zamienia się w \(\langle -1,\ 3\rangle\) | punkt, odcinek, rzuty, pas |
| 4 | **zdanie 3, wartości ujemne**: zapala się fragment pod osią, na osi pas z pustymi kółkami, pas zamienia się w \((1,\ 3)\) | fragment, pas, puste kółka |
| 5 | **zdanie 4, największa wartość**: poziom \(y = 3\), poziomy odcinek, rzut na oś, pas zamienia się w \((-4,\ -2\rangle\), **nagłówek części znika** | poziom, odcinek, rzuty, pas |

Każdy z czterech kroków środkowych i ostatni idą tym samym schematem: **podświetlenie na
wykresie, rzut kreskowany na oś, zielony pas z właściwymi końcami, pas zamienia się
w gotowy przedział na liście**. To jest wprost zasada z `manimations/README.md`, punkt 42:
w filmie, który czyta rysunek, jednostką kroku jest **jedna myśl**, a nie jeden symbol,
a jedna myśl to tu jedno zdanie do uzupełnienia.

Na ostatniej klatce w kadrze stoją **wszystkie cztery odpowiedzi naraz**, obok wykresu.

### Co się zmieniło w wersji trzeciej (2026-08-29)

Dziewięć kroków zeszło do pięciu, a przedział przestał powstawać dwuetapowo.

Wersja druga składała przedział ze **skrawków** (`"(-4"`, `",\ "`, `"4\rangle"`)
ustawionych obok siebie przez `arrange()`, na wysokości pod nagłówkiem części, i dopiero
stamtąd odsyłała go na listę. Henrich: „zapisy przedziałów, które pojawiają się pod
nagłówkami, źle się renderują". Renderowały się źle z powodu, który był w samym pomyśle:
trzy osobne `MathTex`-y nie stoją na wspólnej linii bazowej i mają przypadkowy odstęp,
więc nawias, przecinek i liczba rozjeżdżają się tak, jak nie rozjechałyby się w jednym
wzorze. Etap pośredni wypadł w całości: **zielony pas zamienia się od razu w gotowy
przedział**, złożony jednym `MathTex`-em, i ląduje wprost na liście.

Wzorcem ruchu jest dawny krok 9 (Henrich: „animacje w ostatnim kroku wyglądają świetnie,
możesz stosować podobne do reszty kroków"). Ten sam schemat idzie teraz przez wszystkie
cztery części.

## Dlaczego to zadanie w ogóle dostało film

Cztery pytania to cztery różne sposoby patrzenia na ten sam obraz: raz rzutujemy wykres
na oś \(x\), raz na oś \(y\), raz szukamy tego, co pod osią, raz tego, co najwyżej.
Ruch odpowiada dokładnie temu, co uczeń ma zrobić w głowie. Widżet
`widgetFunkcjaPrzedzialami` pokazuje to interaktywnie i zostaje; film ma być zrozumiały
bez niego.

## Co zmierzono po renderze (2026-08-29, wersja trzecia)

- `tools/styk-klatek.sh`: cztery styki, od 0,99910 do 0,99997, **bez zastrzeżeń**.
- `tools/klatki.sh stany`: obejrzane wszystkie pięć kroków, początek i koniec każdego.
  Pierwsza klatka kroku zgadza się z ostatnią klatką poprzedniego, lista odpowiedzi rośnie
  po jednej pozycji na krok, na końcu nagłówek znika i zostaje wykres z czterema wynikami.
- `tools/klatki.sh film … 2`: krok 2 obejrzany klatka po klatce. Rzuty kreskowane, zjazd
  kropek na oś, pas, przejście pasa w zapis. Bez zieleni na pierwszej i ostatniej klatce.
- `tools/zielen-krokow.py`: pierwsza i ostatnia klatka każdego kroku czyste, ale kroki 2, 3
  i 4 dostają uwagę „zieleń gaśnie ratami, ogon 5 klatek". **To fałszywy alarm i został
  obejrzany**, a nie zignorowany: zieleń nie gaśnie tu osobnym `set_color`, tylko sama
  przechodzi w czerń w środku `ReplacementTransform` (zielony pas zamienia się w czarny
  zapis przedziału), więc ostatnie klatki morfu mają jeszcze pojedyncze zielonawe piksele
  na krawędziach glifów. Krzywa kroku 2 kończy się `996 54 4 4 3 3 0`, czyli realnie jedna
  słabo zielona klatka i cztery po trzy do czterech pikseli. Heurystyka liczy wszystko
  poniżej jednej dziesiątej szczytu, więc łapie ten ogon; oko go nie widzi.
