# widgets/ — interaktywne widżety rozwiązań

Indeks katalogu. **Zanim zaprojektujesz nowy widżet, przeczytaj
[PROJEKTOWANIE.md](PROJEKTOWANIE.md)**: zasady dydaktyczne i spójności
wypracowane z Henrichem w pilotażu 2026-maj. Jeden widżet = jeden plik = jedna funkcja `widget*`, podpięta do
zadania przez pole `solutionWidget` w `exercises.json` (wartością jest **nazwa**
funkcji jako string — JSON nie przechowuje funkcji).

Pełny opis mechaniki renderowania jest w [ARCHITECTURE.md](../ARCHITECTURE.md)
(sekcja „Rendering model", pole `solutionWidget`), style w
[style/sheet.css](../style/sheet.css). Ten plik jest tylko spisem treści —
żeby nie trzeba było otwierać dziewięciu plików, by sprawdzić, co już istnieje.

## Kolejność ładowania (ma znaczenie)

To są klasyczne skrypty we wspólnym zakresie globalnym, nie moduły. `template.html`
ładuje je w tej kolejności i **nie wolno jej zmieniać**:

1. `_helpers.js` — wspólne pomocniki `wg*`, muszą istnieć przed widżetami
2. pliki `widgets/*.js` — definiują funkcje `widget*`
3. `_registry.js` — mapa nazwa → funkcja; wymaga, by wszystkie były już zdefiniowane
4. dopiero potem `app/*.js` (`app/render.js` czyta `WIDZETY`)

**Nowy widżet = nowy plik w `widgets/` + wpis w `_registry.js` + tag `<script>`
w `template.html`.** Pominięcie któregokolwiek z tych trzech kroków daje ciche
„brak widżetu", bez błędu w konsoli.

## Co już istnieje

Numery zadań to numery **CKE z arkusza**, nie pozycje w tablicy `exercises`
— patrz ostrzeżenie na końcu pliku. Pierwsza tabela: arkusz 2024-grudzień.

| Plik | Funkcja | Zad. | Temat | Sterowanie |
|---|---|---|---|---|
| `osLiczbowa.js` | `widgetOsLiczbowa` | 1 | równanie z wartością bezwzględną \|x+a\|=b na osi liczbowej | dwa pola liczbowe (a, b) + przeciąganie punktu + reset |
| `procentSkladany.js` | `widgetProcentSkladany` | 5 | procent składany, kapitał po 0/1/2 latach vs linia celu | suwak oprocentowania |
| `nierownoscKwadratowa.js` | `widgetNierownoscKwadratowa` | 9 | nierówność kwadratowa: parabola i przedział rozwiązań | przeciąganie punktu po osi x |
| `funkcjaPrzedzialami.js` | `widgetFunkcjaPrzedzialami` | 10 | funkcja określona przedziałami, podświetlanie aktywnego wzoru | suwak po dziedzinie |
| `parabola.js` | `widgetParabola` | 12.1 | monotoniczność paraboli, gałąź rosnąca/malejąca | przeciąganie punktu po wykresie |
| `ciagArytmetyczny.js` | `widgetCiagArytmetyczny` | 15 | ciąg arytmetyczny — równość różnic kolejnych wyrazów | suwak parametru m |
| `koloTrygonometryczne.js` | `widgetKoloTrygonometryczne` | 18 | koło jednostkowe, sinus i cosinus kąta rozwartego | przeciąganie punktu po okręgu |
| `katWpisany.js` | `widgetKatWpisany` | 20 | kąt wpisany i środkowy oparte na tym samym łuku | przeciąganie punktu C po okręgu |
| `prostopadloscian.js` | `widgetProstopadloscian` | 30 | prostopadłościan o stałej sumie krawędzi, maksimum pola | suwak x = AB |

Arkusz **2026-maj** (pilotaż Fable, 2026-08-15):

| Plik | Funkcja | Zad. | Temat | Sterowanie |
|---|---|---|---|---|
| `odsetkiSkladane.js` | `widgetOdsetkiSkladane` | 2 | odsetki z procentu składanego, słupki kapitału | suwak oprocentowania |
| `rownanieIloczynowe.js` | `widgetRownanieIloczynowe` | 8 | równanie iloczynowe, zerowanie nawiasów na osi | klik w oś + przeciąganie punktu |
| `nierownoscTrojmianu.js` | `widgetNierownoscTrojmianu` | 10 | nierówność 3x²−2x−8 ≥ 0, parabola i przedziały | klik w oś + przeciąganie punktu |
| `bilety.js` | `widgetBilety` | 11 | bilety do teatru, rachunek w kolumnach | suwak liczby biletów |
| `funkcjaLamana.js` | `widgetLamana121` | 12.1 | równanie f(x)=c i największa wartość na przedziale | zakładki + przeciąganie prostych |
| `funkcjaLamana.js` | `widgetLamana122` | 12.2 | zbiór wartości i argumenty z f(x)>c | zakładki + suwak + przeciąganie |
| `funkcjaLiniowa.js` | `widgetLiniowaWspolczynniki` | 13.1 | znaki współczynników a i b prostej | dwa suwaki + przeciąganie punktu na osi y |
| `funkcjaLiniowa.js` | `widgetLiniowaTangens` | 13.2 | tangens kąta nachylenia, trójkąt jak w tablicach | suwak a |

(`funkcjaLamana.js` i `funkcjaLiniowa.js` to świadome wyjątki od zasady „jeden
plik = jeden widżet": para widżetów jednego zadania dzieli rysowanie tej samej
figury, więc mieszka razem.)

Wszystkie są **tematyczne, nie uniwersalne** — każdy ma wpisane na
sztywno liczby ze swojego zadania. Nie da się „podpiąć istniejącego widżetu"
do nowego zadania bez przepisania go; nowy temat to nowy plik.

Wszystkie rysują na `<canvas>` (szerokość 520 px, wysokość 130–310 px zależnie
od widżetu) i mają ten sam układ: tytuł → płótno → (opcjonalnie) sterowanie →
odczyt pod spodem.

## Pomocniki z `_helpers.js`

Widżet dostaje kontener (`.solution-interactive-container`) i buduje w nim
własny DOM. **Bez sztywnych `id`** — wszystko szukane wewnątrz kontenera, bo ten
sam widżet może wystąpić w kilku miejscach naraz.

**Budowanie DOM**
- `wgElement(tag, klasa, html)` — element z klasą i treścią
- `wgCanvas(container, width, height)` — płótno gotowe pod HiDPI

**Interakcja**
- `wgPointerPos(canvas, event)` — pozycja wskaźnika w układzie płótna
- `wgDraggable(canvas, hitTest, onDrag)` — przeciąganie punktu (mysz i dotyk)
- `wgPrzyciagnij(wartosc, cele, prog)` — delikatne przyklejanie do wartości
  z zadania, żeby dało się w nią trafić palcem

**Wzory i liczby**
- `wgMath(tex)` — KaTeX do stringa, z pamięcią podręczną. **Używaj tego, nie
  `renderMathInElement`** — auto-render przy przeciąganiu zabija płynność
- `wgTexLiczba(v, maxFrac, minFrac)` — liczba po polsku w zapisie TeX
  (przecinek jako `{,}`, spacje tysięcy jako `\,`)
- `wgUstawHTML(el, html)` — podmiana treści tylko gdy naprawdę się zmieniła

**Widoki i układ współrzędnych** (dodane 2026-08-15)
- `wgZakladki(container, etykiety, onZmiana)` — pasek zakładek przełączających
  widoki jednego widżetu (np. dwa zdania zad. 12.1); zwraca stan `{ aktywna }`
- `wgUklad({X0, X1, Y0, Y1, szer, wys, margines})` — mapowanie wartość↔piksel
  (`px/py/vx/vy`) dla płótna z marginesami
- `wgRysujUklad(ctx, uklad, opcje)` — siatka, osie ze strzałkami, podziałka
  i liczby (z odstępem pod kropki na osi)
- `wgWysokoscKwadratowa(o)` — wysokość płótna, przy której kratka układu
  jest kwadratowa (podaj to samo `o` co do `wgUklad`)

**Rysowanie**
- `wgStrzalka(ctx, x1, y1, x2, y2)` — strzałka na płótnie
- `wgZarejestrujRysowanie(canvas, rysuj)` — **obowiązkowe w każdym widżecie**;
  bez tego widżet nie przemaluje się po zmianie motywu i zostanie w kolorach
  poprzedniego
- `wgHex(kolor)`, `wgOdswiezKolory()`, `wgPrzemaluj()` — obsługa motywu

**Kolory**
Nie wpisuj kolorów na sztywno. Bierz je z `WG_KOLORY` — to lustro zmiennych CSS
(`--canvas-bg`, `--wg-osie`, `--wg-siatka`, `--wg-tekst`, `--wg-linia`,
`--accent-purple`, `--wg-punkt`, `--wg-zolty`, `--accent-green`, `--wg-slupek`,
`--correct` i kilka innych), odświeżane przy każdej zmianie motywu. Wartości
w pliku to tylko awaryjny zapas, gdyby CSS się nie wczytał.

## Klasy CSS

Zdefiniowane w [style/sheet.css](../style/sheet.css):
`.widget`, `.widget-title`, `.widget-canvas`, `.widget-controls`,
`.widget-readout`, `.widget-formula-list`, `.wg-formula`,
`.wg-ok` / `.wg-zle` / `.wg-neutral` (stan odczytu), `.wg-reset`,
`.wg-a` / `.wg-b` (pola liczbowe wpisane w środek wzoru).

## ⚠️ Pułapka: numer zadania ≠ pozycja w tablicy

W `exercises.json` **nie ma pola z numerem zadania** — numer siedzi wyłącznie
w treści pola `question` („Zadanie 15."). A tablica `exercises` ma więcej
pozycji niż arkusz ma zadań, bo zadania wieloczęściowe mają osobny wpis-rodzic
i osobne wpisy na części:

- arkusz 2024-grudzień: **30 zadań CKE**, ale **35 pozycji** w tablicy
- zadanie 12 zajmuje 4 pozycje (12., 12.1, 12.2, 12.3)
- zadanie 17 zajmuje 3 pozycje (17., 17.1, 17.2)

Od pozycji 11 numeracja rozjeżdża się na dobre: `exercises[24]` to **zadanie 20**,
a `exercises[34]` to **zadanie 30**. Liczenie zadań po indeksie tablicy daje więc
ciche trafienie w cudze zadanie. Numer czytaj z pola `question`.
