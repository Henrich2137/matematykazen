# Produkcja filmów „krok po kroku" — pułapki i konwencje

Opis działania, nie problem do naprawy. Rzeczy, które kosztowały czas przy
pierwszym przejściu (2026-08-11) i których nie widać z samego kodu.
Projekt docelowy: `docs/superpowers/specs/2026-08-11-rozwiazania-krok-po-kroku-design.md`.

## Parametry renderu

`manimations/manim.cfg`: **1280×720, 120 fps, tło białe.** 1280 pokrywa telefon
przy DPR 3 (potrzeba 900 px) i desktop przy DPR 2 (840 px). 120 fps to zapas pod
spowolnienie w odtwarzaczu — spowolnienie nie dorysowuje klatek, więc materiał
60 fps przy 0,25× wygląda jak 15 fps.

**Nie podawaj flagi jakości** (`-ql`/`-qh`). Nadpisuje `pixel_width`/`pixel_height`
z `manim.cfg` i zmienia proporcje kadru — porównanie z istniejącymi plikami
przestaje być prawomocne, choć wygląda na wykonane.

Waga: krok 1–2 s waży 17–67 kB. Przejście z 840×360/60 na 1280×720/120 dało
około 2×, nie 10×.

## Trzy pułapki, każda wykryta dopiero pomiarem

### 1. Krok musi kończyć się `self.wait(0.25)`

Przeglądarka po zakończeniu odtwarzania zostawia na ekranie klatkę sprzed
samego końca pliku. Przy 120 fps klatka trwa 8 ms, więc gubi się ich więcej niż
kiedyś. Efekt: ostatni dorysowany element nie zostaje w spoczynku — a to
właśnie ten obraz uczeń ogląda najdłużej.

Zmierzone na kroku 1: plik miał treść do x=925, przeglądarka pokazywała do
x=792 (brakowało wykładnika `⁻⁵`). Po dodaniu przytrzymania oba obszary
identyczne.

### 2. Z końca kroku trzeba wyciąć sprzątanie sceny

`self.remove(...)` i `self.clear()` na końcu kroku przygotowują scenę pod
następny. Zostawione, wykonują się **w trakcie** przytrzymania z punktu 1 i uczeń
ogląda pusty kadr. Tak wyglądał krok 2 w v18: ostatnia klatka miała dokładnie
**zero** ciemnych pikseli.

Generator ucina więc z końca każdego kroku wszystkie linie zaczynające się od
`self.remove(` lub `self.clear()`.

### 3. Kroki nie są samowystarczalne

Krok 2 przekształca wyłącznie `kroki[0][0..2]`, więc domykający nawias
z wykładnikiem (`kroki[0][3]`) nie trafia na scenę — w oryginalnej procedurze
narysował go wcześniej krok 1. Wymaga jawnego `self.add(kroki[0])` na wejściu.
Pozostałe pięć kroków punkt wyjścia dodaje sobie samo.

Wykryte po SSIM: krok 2 wypadał 0,9929 wobec ~0,999+ w pozostałych, czyli
o rząd wielkości powyżej szumu kodera. Po poprawce 0,999614.

**Wniosek na przyszłość:** projektując cięcie na sekcje trzeba pilnować stanu
przenoszonego między krokami, nie tylko granic czasowych.

## Jak dziś powstaje sześć plików z jednej sceny

`solutionZad2.py` ma kroki 1–5 w bloku `"""`, aktywny krok 6 — historycznie
przełączano je komentarzem i renderowano raz na krok. Przy przerabianiu zadania 2
zastąpił to generator w scratchpadzie: bierze preambułę (linie 1–67, definicje
i skalowanie) i dokleja kod jednego kroku.

Zakresy linii po zmianach z 2026-08-11:

| krok | linie | uwagi |
|---|---|---|
| 1 | 73 | |
| 2 | 80–88 | + `self.add(kroki[0])` na wejściu, ostatnia linia ucinana |
| 3 | 95–103 | |
| 4 | 111–119 | bez końcowego `clear/add/wait` — to przygotowanie pod krok 5 |
| 5 | 127–128 | |
| 6 | 134–136 | |

**To jest rozwiązanie tymczasowe i kruche** — zakresy linii rozjadą się przy
pierwszej edycji sceny. Zastąpi je skrypt z paczki B (`tools/manim-kroki.sh`),
który ma też generować rewersy przez `ffmpeg -vf reverse` (rewersu nie renderuje
Manim — powstaje z gotowego pliku, więc nie może się z nim rozjechać).

## Jak weryfikować, żeby nie dać się oszukać

- **Zrzut ekranu z Playwrighta potrafi kłamać przy wideo.** Ten sam zakończony
  film raz pokazywał się poprawnie, raz bez wykładnika, raz jako pusty kadr —
  to kwestia momentu malowania obrazu, nie zawartości pliku.
- **Wiarygodny jest odczyt pikseli**: `drawImage(video)` na `<canvas>` plus
  `getImageData`, i liczenie ciemnych pikseli oraz ich prostokąta obejmującego.
  Idzie przez JavaScript, z pominięciem kompozytora obrazu.
- **Do porównania dwóch wersji filmu**: `ffmpeg -lavfi ssim`. Poziom szumu samej
  kompresji to około 0,9996 — dopiero wyraźnie niżej oznacza różnicę w treści.
  Sam SSIM nie mówi GDZIE jest różnica, więc do tego dochodzi obejrzenie
  najgorszej klatki w powiększeniu.
- **Zanim porównasz cokolwiek**, sprawdź `ffprobe`, czy oba pliki mają te same
  wymiary i liczbę klatek. Inaczej „porównanie" przejdzie na niewłaściwym
  materiale.

## Odtwarzanie z prędkością 4× gubi klatki

Zmierzone w Chromium: plik 720p120 przy 4× gubi 218 klatek z 720 (dekoder musi
przerobić 480 kl./s) i kończy w 0,59 s zamiast 0,50. Przy 60 fps tego nie ma.
Przy 1× i 0,25× — czas co do setnej sekundy, 6 zgubionych klatek.

Uznane za akceptowalne, bo 4× to tryb „przewiń", nie „oglądaj". Pomiar robiony
w kontenerze, na procesorze desktopowym — **telefon i Safari nie były
sprawdzone**.

## Docelowa struktura plików (paczka A, jeszcze nie wdrożona)

```
matura/<arkusz>/media/zadN/krok-po-kroku/
├── krok1.mp4
├── krok1-rewers.mp4
└── ...
```

Dziś pliki wciąż leżą płasko jako `media/zadN/zadNrozw_stepM.mp4`.
`manimations/` **zostaje na wierzchu repo** — decyzja Henricha: produkcja ma być
oddzielona od statycznej strony, żeby przyszła gałąź hostingowa nie ciągnęła
za sobą źródeł animacji.
