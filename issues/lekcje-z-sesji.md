# Lekcje z sesji

Wnioski, które warto przenieść na następne zadania: **czego dana sesja nauczyła
o sposobie pracy**. To nie jest ani „co zrobiono" (od tego jest `done/`), ani
„jak coś działa" (od tego są pozostałe pliki w tym katalogu i README-y).

Wyjątek od zasady „jeden plik w `issues/` = jeden problem" — ten plik nie opisuje
awarii i nigdy się nie „zamyka", tylko rośnie. Najnowsze wpisy na górze.

Wpisy zawierają wyłącznie rzeczy sprawdzone. Tam, gdzie czegoś nie udało się
rozstrzygnąć, jest to napisane wprost — „nie ustalono" jest tu pełnoprawnym
wynikiem i nie wolno go podmieniać na prawdopodobne wyjaśnienie.

---

## 2026-08-11 — Manim w kontenerze: co spec twierdził, a czego nie sprawdził

Sesja: brainstorming → spec → instalacja z hosta → weryfikacja renderu w kontenerze.
Środowisko wyszło dobrze. Ale dwa twierdzenia w spec-u okazały się przy zderzeniu
z rzeczywistością fałszywe, a jedno moje wyjaśnienie w trakcie weryfikacji —
przedwczesne. Wszystkie trzy przypadki mają tę samą postać: **coś prawdopodobnego
zostało zapisane jak coś ustalonego.**

### 1. Fałszywa przesłanka pod dwiema warstwami projektu

**Co ustalono:** w `solutionZad2.py` kroki 1–5 są zakomentowane jednym blokiem
`"""` (linie 54–126), aktywny jest tylko krok 6. Wyrenderowany z tego pliku klip
ma 2,000 s i 120 klatek — dokładnie tyle co `zad2rozw_step6.mp4` na stronie.
Żadne cięcie gotowego wideo nie było więc potrzebne.

**Czego NIE ustalono:** czy tak powstawały kroki w pozostałych zadaniach.
Sprawdzone tylko tyle, że `solutionZad3.py` **nie ma ani jednego bloku `"""`**,
więc uogólnienie „tak robiono zawsze" jest nieprawdziwe. `solutionZad1.py`
i `solutionZad4.py` takie bloki mają, ale nie sprawdzano, czy pełnią tę samą rolę.

**Lekcja.** Największa część spec-a (warstwy 2 i 3: sekcje `self.next_section()`
plus skrypt `tools/manim-kroki.sh`) rozwiązywała problem „jak pociąć długą scenę
na kroki". Dla zadania 2 ten problem nie istnieje. Sygnał leżał na wierzchu:
`manimations/README.md` mówił wprost „**domysł, niepotwierdzone**". Koszt
sprawdzenia to przeczytanie 140 linii jednego pliku.

> Cudze „nie wiem, jak to działa" w dokumentacji to zadanie do wykonania, nie
> kontekst do przyjęcia. Zanim zaprojektujesz mechanizm, przeczytaj plik, który
> ten mechanizm ma zastąpić.

### 2. Flaga wpisana do spec-a z pamięci była błędna

**Co ustalono:** `manim -qh` renderuje 1920×1080, a `manim` bez flagi jakości —
840×360, zgodnie z `pixel_width`/`pixel_height` w `manim.cfg`. Zmierzone `ffprobe`
na obu wynikach. Pliki na stronie mają 840×360, czyli **inne proporcje kadru**
(21:9 vs 16:9), a więc inne rozmieszczenie wzorów.

**Lekcja.** Komenda weryfikacyjna w spec-u brzmiała `manim -qh solutionZad2.py
ScenaZadania2`. Gdyby porównanie zrobić tak, jak kazał spec, zestawiałoby materiał
o różnych proporcjach — i wyglądałoby to na poprawnie wykonany krok. Błąd przeszedł
przez brainstorming, self-review spec-a, przegląd Henricha i model hostowy, bo
wszystkie te etapy czytały ten sam tekst. Wykrył go dopiero `ffprobe` na wyniku.

> Flagi i komendy, których nie uruchomiłeś, nie są jeszcze wiedzą. Do kroku
> weryfikacyjnego dopisuj też, **po czym poznać, że porównanie jest prawomocne**
> (tu: zgodne wymiary i liczba klatek) — inaczej krok potrafi „przejść" na
> niewłaściwym materiale.

### 3. Przedwczesne wskazanie przyczyny — złapane pomiarem

**Co ustalono.** Render w kontenerze zgadza się z hostowym: identyczne parametry
pliku (840×360, 60 fps, 120 klatek, 2,000 s, h264 High, yuv420p), SSIM średnio
0,999856 przez 120 klatek (najgorsza 0,999543), a w powiększeniu 4× ta sama
geometria glifów. Do porównania na najgorszej klatce:

| Porównanie | SSIM |
|---|---|
| bezstratny render kontenera ↔ własny MP4 kontenera (sam koder) | 0,999601 |
| bezstratny render kontenera ↔ MP4 z hosta | 0,999480 |
| MP4 kontener ↔ MP4 host | 0,999581 |

Wniosek, który z tego **wynika**: sama kompresja H.264 wprowadza różnicę tego
samego rzędu co cała zaobserwowana różnica host↔kontener, więc do jej wyjaśnienia
wystarcza. Obawa wpisana do spec-a — że MiKTeX i TeX Live dadzą inne metryki
fontu — nie znalazła potwierdzenia.

**Czego NIE ustalono:** jaka część różnicy przypada na koder, a jaka na render.
Rozstrzygnięcie wymagałoby bezstratnych klatek z hosta, których nie ma —
referencja istnieje wyłącznie jako H.264. Wiadomo tylko, że wersje ffmpega się
różnią (5.1.9 w kontenerze, 7.1 na hoście) i że pliki ważą 20 kB vs 27 kB.

**Lekcja.** Do weryfikacji szedłem z podejrzanym wskazanym z góry (rozjechane
wersje `ManimPango`/`numpy`/`Pillow`) i po pierwszych pomiarach zapisałem
w README i w `done/`, że winowajcą jest ffmpeg. Było to prawdopodobne, ale
niesprawdzone — a różnica między „prawdopodobne" a „zmierzone" jest dokładnie tym,
co odróżnia notatkę użyteczną za pół roku od takiej, która wprowadzi w błąd.
Test izolujący koder (render `--format=png`, czyli bez kompresji, jako trzeci punkt
odniesienia) kosztował jedną komendę.

> Hipotezę o przyczynie potwierdza się pomiarem, który mógłby ją obalić. Przy
> różnicach wizualnych potrzebne są dwa rodzaje dowodu naraz: metryka ilościowa
> (bo oko nie odróżni 0,9998 od 1,0) i oglądnięcie najgorszego przypadku
> (bo metryka nie mówi, **gdzie** jest różnica).

### 4. Co zadziałało i warto powtarzać

- **Sprawdzenie ograniczeń środowiska przed spisaniem planu.** Jedno
  `touch .devcontainer/.probe` ujawniło read-only mount i od razu ustawiło podział
  pracy host/kontener. Gdyby wyszło to w trakcie realizacji, plan trafiłby w ślepy
  zaułek w połowie.
- **Kryterium akceptacji wskazujące konkretny plik referencyjny**, a nie „sprawdź,
  czy wygląda tak samo". Dzięki temu weryfikacja dała wynik, a nie wrażenie.
- **Podział na paczki: najpierw środowisko, potem testy, dopiero potem nadbudowa.**
  Decyzja Henricha wbrew propozycji zrobienia wszystkich czterech warstw naraz.
  Okazała się trafna z powodu, którego wtedy nikt nie znał — warstwy 2 i 3 stały
  na przesłance z punktu 1. W jednej paczce powstałby działający mechanizm
  rozwiązujący nieistniejący problem.
