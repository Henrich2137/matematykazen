# Przekazanie pracy: pilotaż Fable na 2026-maj (stan po v47, 2026-08-15)

Notatka sztafetowa: Fable kończył sesję z małym zapasem limitu, ten plik pozwala
dokończyć robotę innemu modelowi bez czytania całej rozmowy. Punkt wejścia dla
świeżej sesji: [fable-brief-2026-maj.md](fable-brief-2026-maj.md) (zasady tam
opisane nadal obowiązują), potem ten plik.

## Co jest zrobione (wszystko zacommitowane i wypchnięte)

Zadania arkusza 2026-maj z kompletem podpowiedź + rozwiązanie opisowe + widżet:

- zad. 2 (v41-v44, `widgets/odsetkiSkladane.js`), zad. 8 (v42-v44,
  `widgets/rownanieIloczynowe.js`), zad. 10 (v44, `widgets/nierownoscTrojmianu.js`),
  zad. 11 (v45, `widgets/bilety.js`), zad. 12.1/12.2 (v46, `widgets/funkcjaLamana.js`,
  dwa widżety z zakładkami), zad. 13.1/13.2 (v47, `widgets/funkcjaLiniowa.js`).
- Rysunki z arkusza wycięte do `matura/2026-maj/media/zad12/zad12rys.png`
  i `.../zad13/zad13rys.png` (metoda niżej).
- Wpisy TESTOWANIE HENRICH w TODO.md są aktualne dla v43-v47 (część pewnie
  nieprzeklikana). Szczegóły każdej wersji: done/04-biezace.md.

## Następne zadanie: zad. 14 (CZEKA NA POTWIERDZENIE HENRICHA, nie zaczynać samemu)

Opis Henricha z czatu (2026-08-15): "2 parabole oznaczone innymi kolorami.
Suwakiem zmieniamy domyślnie ustawioną 1 i tym samym przesuwamy parabolę
lewo/prawo. Warto zostawić działanie suwaka normalnie, aby uczeń widział, że
matma działa tutaj na odwrót, niż by się spodziewał." (chodzi o przesunięcie
wykresu: g(x) = f(x - c), plus na suwaku przesuwa w prawo... sprawdzić treść
zad. 14 w exercises.json przed projektowaniem; zadanie ma wpis pod indeksem 17).

## Konwencje wypracowane w tej sesji (obowiązują dalej)

**Pełny przewodnik projektowania widżetów (dydaktyka, spójność, checklist):
[widgets/PROJEKTOWANIE.md](../widgets/PROJEKTOWANIE.md)** - czytać PRZED
wymyślaniem nowego widżetu, punkty niżej to skrót techniczny.

- **Wielorazowe klocki w `widgets/_helpers.js`** (opisane też w widgets/README.md):
  `wgZakladki` (karty w widżecie), `wgUklad` + `wgRysujUklad` (układ współrzędnych),
  `wgWysokoscKwadratowa` (wysokość płótna dająca KWADRATOWĄ kratkę - Henrich tego
  wymaga na każdym wykresie w układzie współrzędnych). Nowe widżety budować na nich.
- Para widżetów jednego zadania może mieszkać w jednym pliku (precedens:
  funkcjaLamana.js, funkcjaLiniowa.js).
- Suwak dostaje kolor tego, czym rusza: `slider.style.accentColor =
  wgHex(WG_KOLORY.niewiadoma)` ustawiane w draw() (przemalowuje się z motywem).
  Drugi parametr = `WG_KOLORY.zolty`. Etykieta suwaka: `.wg-suwak-etykieta`.
- Odczyt pod widżetem: linijki rozdzielane `<br>`, wartości przez `wgTexLiczba`,
  kolory przez `\textcolor` + `wgHex`; ✓/✗ (`.wg-ok`/`.wg-zle`) zapala się, gdy
  suwak trafi w wartości z zadania. Element ruszany NIE zielenieje (COLORS.md).
- Rozwiązania opisowe: wzór na starcie przez `\[ \]`, potem
  `<div class="rozwiazanie-kroki">` z krótkimi linijkami; `solutionTextMore`
  zostaje pustym stringiem. Zakaz pauz/półpauz wszędzie.
- Nowy widżet = plik + wpis w `widgets/_registry.js` + tag `<script>`
  w template.html + wiersz w tabeli widgets/README.md.
- Po każdej paczce: podbić wersję w template.html (#wersja) i index.html
  (.landing-wersja) naraz, wpis do TODO.md (TESTOWANIE HENRICH) i do
  done/04-biezace.md, jeden commit, push.

## Wycinanie rysunków z PDF-ów w tym kontenerze

Nie ma pdftoppm/gs/mutool, PyPI za firewallem, headless Chromium nie renderuje
PDF. Działa Ghostscript wołany przez ctypes z biblioteki
`/usr/lib/x86_64-linux-gnu/libgs.so.10` (zależność dvisvgm). Wzór wywołania:

```python
import ctypes
gs = ctypes.CDLL("/usr/lib/x86_64-linux-gnu/libgs.so.10")
inst = ctypes.c_void_p(); gs.gsapi_new_instance(ctypes.byref(inst), None)
args = [b"gs", b"-dNOPAUSE", b"-dBATCH", b"-dSAFER", b"-sDEVICE=png16m",
        b"-r220", b"-dFirstPage=N", b"-dLastPage=N",
        b"-sOutputFile=strona.png", b"sciezka/do/pliku.pdf"]
arr = (ctypes.c_char_p * len(args))(*args)
gs.gsapi_init_with_args(inst, len(args), arr)
gs.gsapi_exit(inst); gs.gsapi_delete_instance(inst)
```

Potem kadr przez PIL: zgrubny crop + autotrym bieli (ImageChops.difference
z białym tłem, getbbox, margines 12 px). Nazwy plików małymi literami.

## Testowanie (skrót z briefu, sprawdzone w praktyce)

Serwer: `node tools/serwer.js 8001`. Playwright z
`NODE_PATH=/usr/local/share/npm-global/lib/node_modules`, selektor
`.exercise-container:not(#exercise-template)`, `scrollIntoViewIfNeeded()` przed
klikaniem w canvas, na koniec `page.locator('.katex-error').count()` ma być 0.
Zrzuty obu motywów przez `page.emulateMedia({ colorScheme: 'dark' })`.
