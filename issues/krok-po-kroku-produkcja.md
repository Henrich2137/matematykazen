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

## Rewersy — czego nie widać na pierwszy rzut oka

**Zrobione 2026-08-11** dla wszystkich trzech zadań z krokami (zad. 1, 2 i 3 —
razem 23 kroki i 23 rewersy). Odtwarza to jedną komendą `tools/rewersy.sh`:

```
tools/rewersy.sh matura/2024-grudzien/media/zad2/krok-po-kroku
```

Pod spodem to nadal jedna linijka ffmpeg — rewersu **nie renderuje Manim**,
powstaje z gotowego pliku, więc nie może się z nim rozjechać:

```
ffmpeg -i stepN.mp4 -vf "reverse,tpad=stop_mode=clone:stop_duration=0.25" -an stepNreverse.mp4
```

Trzy rzeczy, które przy tym wybuchną, jeśli się o nich nie pomyśli:

1. **Przytrzymanie stanu końcowego wyląduje na POCZĄTKU rewersu.** Odwrócenie
   zamienia końce miejscami, więc 0,25 s bezruchu z końca kroku staje się
   0,25 s bezruchu na starcie cofki, a rewers kończy się dokładnie w tej klatce,
   której przeglądarka nie zdąży namalować (patrz pułapka 1 wyżej). Efekt byłby
   ten sam co w v18: po cofnięciu na ekranie zostaje niepełny obraz.
   **Rozwiązane przez `tpad`**, nie przez przerabianie scen: filtr klonuje
   ostatnią klatkę rewersu przez 0,25 s, więc przytrzymanie jest po obu stronach
   bez dotykania Manima. Działa też dla zad. 1 i 3, które przytrzymania na końcu
   nie mają w ogóle (to stary format sprzed poprawki).
2. **Rewers kroku 1 kończy się pustym kadrem**, bo krok 1 rysuje działanie od
   zera. Cofnięcie z pierwszej kropki prowadziłoby do stanu „nic nie ma" —
   dlatego w odtwarzaczu z kropki 0 nie da się cofnąć (decyzja Henricha).
3. **`-an` jest istotne** — pliki nie mają ścieżki dźwiękowej, a bez tej flagi
   ffmpeg potrafi dołożyć pustą i niepotrzebnie zwiększyć wagę.

Nazewnictwo (potwierdzone przez Henricha 2026-08-11): `stepN.mp4` +
`stepNreverse.mp4`, w katalogu `krok-po-kroku/`. Odtwarzacz **nie czyta nazwy
rewersu z danych** — dokłada `reverse` przed rozszerzeniem nazwy z pola `src`,
więc `exercises.json` wymienia tylko plik w przód.

Zmierzone po wygenerowaniu (23 kroki): rewers ma dokładnie tyle klatek co
oryginał plus 0,25 s (15 przy 60 fps, 30 przy 120), a SSIM końca kroku wobec
startu rewersu i startu kroku wobec końca rewersu wynosi ≥ 0,9994 — przy szumie
samej kompresji rzędu 0,9996.

## Pasek postępu między kropkami

Henrich chce przenieść dzisiejszy pasek spod filmu **w odstęp między kropką
bieżącą a następną**. Technicznie to ten sam mechanizm co dziś (pętla
`requestAnimationFrame` w `showStep`, świadomie bez przejścia CSS — wcześniejsza
wersja na `timeupdate` + `transition` sprawiała, że pasek jechał gumowato), tylko
z innym celem rysowania: wypełnia się odcinek łączący dwie kropki, a nie belka
pod filmem.

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
- **Miej wzorzec spoza przeglądarki.** Odczyt pikseli mówi, CO widać, ale nie
  mówi, czy to właściwa klatka. Wyciągnij tę samą klatkę z pliku
  (`ffmpeg -vf "select=eq(n\,K)"`) i porównaj liczbę ciemnych pikseli oraz ich
  prostokąt. Tak wyszło 2026-08-11, że kliknięcie ostatniej kropki pokazuje
  PIERWSZĄ klatkę ostatniego kroku: odtwarzacz raportował 3354 ciemne piksele
  w prostokącie (466, 310, 813, 409), a plik miał w ostatniej klatce 1557
  w (594, 309, 685, 410). Bez wzorca „coś się wyświetla" wyglądałoby poprawnie.

## Pułapka podglądu: `python3 -m http.server` nie umie przewijać wideo

`SimpleHTTPRequestHandler` **nie obsługuje żądań zakresowych** (`Range`), a bez
nich przeglądarka nie ma jak skoczyć w środek filmu: `video.seekable` zostaje
puste (`seekable.end(0) === 0`), każde ustawienie `currentTime` cicho wraca do
zera, a film daje się tylko odtworzyć od początku.

To wygląda dokładnie jak błąd w kodzie odtwarzacza i kosztowało 2026-08-11
sporo czasu na szukanie nieistniejącej usterki. Do pracy nad czymkolwiek, co
przewija film (kropki, rewersy od bieżącej klatki), użyj serwera z obsługą
Range, np.:

```
npx http-server -p 8000 -a 127.0.0.1
```

Sprawdzenie: `curl -s -o /dev/null -w "%{http_code}" -r 0-100 <url-filmu>`
ma zwrócić **206**, nie 200. GitHub Pages Range obsługuje, więc produkcji to
nie dotyczy — tylko lokalnego podglądu.

## Odtwarzanie z prędkością 4× gubi klatki

Zmierzone w Chromium: plik 720p120 przy 4× gubi 218 klatek z 720 (dekoder musi
przerobić 480 kl./s) i kończy w 0,59 s zamiast 0,50. Przy 60 fps tego nie ma.
Przy 1× i 0,25× — czas co do setnej sekundy, 6 zgubionych klatek.

Uznane za akceptowalne, bo 4× to tryb „przewiń", nie „oglądaj". Pomiar robiony
w kontenerze, na procesorze desktopowym — **telefon i Safari nie były
sprawdzone**.

## Struktura plików (wdrożona 2026-08-11)

```
matura/<arkusz>/media/zadN/krok-po-kroku/
├── step1.mp4
├── step1reverse.mp4
└── ...
```

Poprzednio płasko, jako `media/zadN/zadNrozw_stepM.mp4`. Podfolder jest
konieczny, bo rewersy podwajają liczbę plików i mieszały się z rysunkami.
`manimations/` **zostaje na wierzchu repo** — decyzja Henricha: produkcja ma być
oddzielona od statycznej strony, żeby przyszła gałąź hostingowa nie ciągnęła
za sobą źródeł animacji.
