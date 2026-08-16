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

**Barwa jest ta sama w obu motywach.** Niebieskie zostaje niebieskie, zielone
zielone, i to wszędzie: w CSS, w widżecie, na rysunku i w filmie. Ciemny motyw
zmienia tylko **odcień**, żeby kolor był czytelny na ciemnym tle. Nie ma już
żadnej roli, która w jednym motywie jest jedną barwą, a w drugim inną (do
2026-08-16 wyjątkiem było podstawianie pod `x`, patrz niżej).

Dwie kolumny z hexami są więc dokładnymi wartościami tej samej barwy, a nie
dwiema różnymi decyzjami. Wpisując nowy token, podaj obie.

| Rola | Zmienna CSS | `WG_KOLORY` | barwa | jasny | ciemny |
|---|---|---|---|---|---|
| **podstawianie pod `x`** (przeciągany punkt, `x` i liczba na jego miejscu) | `--wg-niewiadoma` | `niewiadoma` | błękit | `#0077b6` | `#46aadf` |
| **wybór ucznia** (zaznaczona odpowiedź ABCD, focus) | `--accent-blue-strong` | `info` | niebieski | `#4a90d9` | `#6ab0ff` |
| **poprawne** | `--correct` | `ok` | zielony | `#0AB32F` | `#3ccf5a` |
| **niepoprawne** | `--incorrect` | `zle` | czerwony | `#d9534f` | `#e07b76` |
| **wykres funkcji** (jak w arkuszach CKE) | `--accent-purple` | `wykres` | fiolet | `#7a3fa8` | `#a97fd0` |
| punkt / uchwyt | `--wg-punkt` | `punkt` | pomarańcz | `#e8871e` | `#f0a04b` |
| drugi parametr | `--wg-zolty` | `zolty` | żółty | `#c99700` | `#e0b64a` |
| oznaczenie miejsca (nie „dobrze") | `--accent-green` | `zielony` | zielony | `#2e7d32` | `#4a9d54` |
| tło płótna (= tło strony) | `--canvas-bg` | `plotno` | tło | `#fff` | `#141414` |
| osie | `--wg-osie` | `osie` | szary | `#666` | `#a6a6a6` |
| siatka | `--wg-siatka` | `siatka` | szary | `#eee` | `#2f2f2f` |
| liczby, podpisy | `--wg-tekst` | `tekst` | szary | `#333` | `#dcdcdc` |
| linia pomocnicza | `--wg-linia` | `linia` | szary | `#999` | `#7d7d7d` |
| przerywana, słabsza | `--wg-linia-slaba` | `liniaSlaba` | szary | `#bbb` | `#555` |
| wyróżniony odcinek | `--wg-linia-mocna` | `liniaMocna` | szary | `#444` | `#c4c4c4` |

Wypełnienia półprzezroczyste: `--wg-obszar-ok`, `--wg-obszar-info`,
`--wg-obszar-wykres`, `--wg-slupek-ok`.

**Zielony i czerwony znaczą wyłącznie poprawność.** Chcesz coś wyróżnić bez
oceniania — weź niebieski albo pomarańczowy.

**Punkt podstawiania nie zmienia się na zielony/czerwony.** O poprawności mówi
✓/✗ obok, nie barwa samego elementu (zad. 9, v36).

**Ciemny wariant podstawiania nie jest wybrany, tylko wyliczony.** `#46aadf` to
dokładnie to, co filtr ciemnego motywu robi z błękitem `#0077b6` z filmu, więc
widżet i film pokazują tę samą barwę. Zmieniasz jedno, przelicz drugie:
`python3 tools/odwroc-kolor.py '#0077b6'`.

Jasny wariant to `#0077b6`, nie `#72d9fe`: ten drugi ma na białym tle kontrast
1,6:1, czyli jest nieczytelny.

> Do 2026-08-16 stał tu pomarańcz `#eb9614`. Nie było to widzimisię: stary filtr
> (samo `invert(92%)`) zamieniał błękit z filmu na pomarańcz, a widżet się do tego
> dopasowywał. Po dołożeniu `hue-rotate(180deg)` film zostaje niebieski, więc
> pomarańcz stracił powód istnienia i wrócił błękit.

## We wzorach (KaTeX)

`\textcolor` wymaga hexa, więc przez `wgHex`, nie z palca:

```js
const nieb = tex => `\\textcolor{${wgHex(WG_KOLORY.info)}}{${tex}}`;
```

## Obrazki i filmy odwracają się w ciemnym motywie

Grafiki PNG i filmy z Manima to jeden plik na oba motywy: ciemny nakłada
`invert(92%) hue-rotate(180deg)`. **Koloru ciemnego nie wybierasz, on się
wylicza.**

Filtr odwraca **samą jasność**, barwę zostawia. Ciemnoniebieski robi się
jasnoniebieski (`#003366` → `#a1ccf7`), a nie pomarańczowy. Biel z pliku ląduje
dokładnie na `#141414`, czyli w tle ciemnej strony, więc grafiki nie mają ramki.
(Do 2026-08-16 stało tu samo `invert(92%)`, przez co zielony wychodził różowy,
a niebieski pomarańczowy.)

**Jedyne ograniczenie: jaskrawe barwy się nie mieszczą.** Czysty żółty
`#ffcc00` jest tak jasny, że po ściemnieniu nie ma już czym być żółty, i wychodzi
brązowy `#714600`. Skrypt to sygnalizuje. W scenach Manima bierz odcienie
przytłumione, nie czyste.

```
python3 tools/odwroc-kolor.py '#0077b6'            # co z tego wyjdzie
python3 tools/odwroc-kolor.py '#0077b6' '#46aadf'  # czy to para
python3 tools/odwroc-kolor.py --szukaj '#46aadf'   # czego użyć, żeby wyszło to
```

**Ta sama barwa w widżecie i w filmie to nie przypadek, tylko rachunek.** Widżet
rysuje na płótnie, więc nic go nie odwraca, a film przechodzi przez filtr. Żeby
uczeń widział jedną barwę „podstawiam pod x", ciemny wariant tokenu jest
policzony tym skryptem z wartości użytej w scenie Manima. Zmieniasz kolor
w scenie, przelicz token.

## ⚠️ Otwarte

**Odwracanie w Firefoksie na Bazzite (zgłoszone 2026-08-16).** Ta sama strona,
ten sam motyw: Chrome pokazuje kolory poprawnie, Firefox na tej samej maszynie
zachowuje się tak, jakby obrotu odcienia w ogóle nie było. Na Windowsie i na
telefonie (Pixel 7a, Chrome i Firefox) wszystko gra. Podejrzani po kolei: stary
arkusz stylów w pamięci przeglądarki, rysowanie na procesorze zamiast karty
graficznej, profil koloru ekranu. Szersze rozpoznanie problemów między
przeglądarkami: [issues/dark-mode-inwersja-przegladarki.md](issues/dark-mode-inwersja-przegladarki.md).
(Samsung Browser świadomie odpuszczony: sam przemalowuje strony na ciemno.)

Notatki Henricha miały inne kody niż kod (poprawny `#3f7d4a` vs `#0AB32F`,
niepoprawny `#8a4a4a` vs `#d9534f`, wykres `#7030a0` vs `#7a3fa8`). Do
rozstrzygnięcia, czy to korekta palety (= przemalowanie strony), czy zapis
z pamięci. Uwaga: liczby z tej notatki były robione pod stary filtr i po zmianie
się nie zgadzają. Dziś `#7030a0` daje `#d49efc` (jasny fiolet), a nie `#8dc164`.
