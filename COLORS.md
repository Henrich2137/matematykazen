# COLORS.md — co kolor znaczy i której zmiennej użyć

**Nigdy nie wpisuj koloru wprost.** W widżecie bierz z `WG_KOLORY`, w CSS ze
zmiennej — inaczej nie przełączy się razem z motywem. Gdzie tokeny są
zdefiniowane: [ARCHITECTURE_CSS.md](ARCHITECTURE_CSS.md).

## Domyślnie NIE koloruj

Kolor jest wyjątkiem, nie ustawieniem startowym. Pytanie przed pokolorowaniem:
**czy uczeń ma w tej chwili na to patrzeć?** Jeśli nie — zostaw czarne.
Kolor bierze się z czynności ucznia, nie z tego, że coś jest ważne.

Cztery pokolorowane rzeczy naraz nie wyróżniają już niczego — i psują też
zielony/czerwony, które naprawdę coś niosą.

> Przykład: w zad. 8 (2026-maj) uczeń przeciąga `x`, więc `x` jest niebieskie.
> Parametr `m` zostaje czarny — uczeń go nie rusza.

W animacjach tak samo: kolor podąża za tym, co się dzieje, i schodzi po kroku.

## Role

| Rola | Zmienna CSS | `WG_KOLORY` | jasny | ciemny |
|---|---|---|---|---|
| **wybór ucznia** (odpowiedź, przeciągany punkt, podstawiana liczba) | `--accent-blue-strong` | `info` | `#4a90d9` | `#6ab0ff` |
| **poprawne** | `--correct` | `ok` | `#0AB32F` | `#3ccf5a` |
| **niepoprawne** | `--incorrect` | `zle` | `#d9534f` | `#e07b76` |
| **wykres funkcji** (jak w arkuszach CKE) | `--accent-purple` | `wykres` | `#7a3fa8` | `#a97fd0` |
| punkt / uchwyt | `--wg-punkt` | `punkt` | `#e8871e` | `#f0a04b` |
| drugi parametr | `--wg-zolty` | `zolty` | `#c99700` | `#e0b64a` |
| oznaczenie miejsca (nie „dobrze") | `--accent-green` | `zielony` | `#2e7d32` | `#4a9d54` |
| tło płótna (= tło strony) | `--canvas-bg` | `plotno` | `#fff` | `#141414` |
| osie | `--wg-osie` | `osie` | `#666` | `#a6a6a6` |
| siatka | `--wg-siatka` | `siatka` | `#eee` | `#2f2f2f` |
| liczby, podpisy | `--wg-tekst` | `tekst` | `#333` | `#dcdcdc` |
| linia pomocnicza | `--wg-linia` | `linia` | `#999` | `#7d7d7d` |
| przerywana, słabsza | `--wg-linia-slaba` | `liniaSlaba` | `#bbb` | `#555` |
| wyróżniony odcinek | `--wg-linia-mocna` | `liniaMocna` | `#444` | `#c4c4c4` |

Wypełnienia półprzezroczyste: `--wg-obszar-ok`, `--wg-obszar-info`,
`--wg-obszar-wykres`, `--wg-slupek-ok`.

**Zielony i czerwony znaczą wyłącznie poprawność.** Chcesz coś wyróżnić bez
oceniania — weź niebieski albo pomarańczowy.

**Niebieski punkt nie zmienia się na zielony/czerwony.** O poprawności mówi ✓/✗
obok, nie barwa samego elementu (zad. 9, v35).

## We wzorach (KaTeX)

`\textcolor` wymaga hexa, więc przez `wgHex`, nie z palca:

```js
const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.info)}}{${tex}}`;
```

## Obrazki i filmy odwracają się w ciemnym motywie

Grafiki PNG i filmy z Manima to jeden plik na oba motywy — ciemny nakłada
`invert(92%)`, bez korekty odcienia. **Koloru ciemnego nie wybierasz, on się
wylicza.** Zielony w filmie wyjdzie różowy.

```
python3 tools/odwroc-kolor.py '#7030a0'            # co z tego wyjdzie
python3 tools/odwroc-kolor.py '#7030a0' '#8dc164'  # czy to para
python3 tools/odwroc-kolor.py --szukaj '#eb9614'   # czego użyć, żeby wyszło to
```

## ⚠️ Otwarte

Notatki Henricha miały inne kody niż kod (poprawny `#3f7d4a` vs `#0AB32F`,
niepoprawny `#8a4a4a` vs `#d9534f`, wykres `#7030a0` vs `#7a3fa8`). Do
rozstrzygnięcia, czy to korekta palety (= przemalowanie strony), czy zapis
z pamięci. Z liczenia: para wykresów `#7030a0` → `#8dc164` jest idealna, ale
`#72d9fe` → `#eb9614` nie jest parą (żeby wyszedł ten pomarańcz, w pliku musi
być `#0065ff`).
