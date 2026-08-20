# manimations/

Skrypty Manim generujące wideo do `solutionStepByStep` w `exercises.json` (finalne pliki lądują w `matura/<sheet-id>/media/zadN/`).

## Środowisko

Render robi się **w devkontenerze** i tylko tam (Manim Community v0.18.1). Opis renderowania na Windowsie Henricha odpadł 2026-08-20, bo Henrich już na nim nie pracuje; wersje tamtej maszyny zostały w historii repo i w porównaniu niżej.

### Devkontener — Debian (dodane 2026-08-11)

Manim, ffmpeg i minimalny TeX Live siedzą w obrazie kontenera (blok w `.devcontainer/Dockerfile` z `ARG MANIM_VERSION`), więc render odpala się w kontenerze bez żadnego przygotowania: `manim solutionZadN.py <NazwaScenyKlasy>`.

- LaTeX to TeX Live w minimalnym zestawie z dokumentacji Manima (~1–1,5 GB), a nie `texlive-full` — pokrywa to, czego używają istniejące sceny. Gdyby render zgłosił brakujący plik `.sty`, dopisuje się konkretny pakiet w Dockerfile.
- Instalacja nie wymaga wyjątku w firewallu (`pypi.org` jest poza allowlistą): obraz buduje się, zanim host nałoży firewall, a po starcie kontenera Manim nic już nie pobiera.
- Przypięty jest **tylko sam Manim**. Zależności pod spodem instalują się w najnowszych wersjach (sprawdzone 2026-08-11: `ManimPango 0.6.1`, `numpy 2.4.6`, `Pillow 12.3.0`, ffmpeg **5.1.9** z Debiana 12). Dawny host Henricha miał inne (`0.6.0` / `2.2.1` / `11.0.0`, ffmpeg 7.1) i mimo to dawał ten sam obraz - patrz porównanie niżej.
- **Nie podawaj flagi jakości** (`-ql`/`-qh` itd.). Flaga jakości nadpisuje `pixel_width`/`pixel_height` z `manim.cfg`, a wraz z rozdzielczością zmieniają się **proporcje kadru**: `-qh` daje 1920×1080 (16:9) zamiast 840×360 (21:9), czyli inne rozmieszczenie wzorów w kadrze niż w plikach już wgranych na stronę. Samo `manim plik.py Scena` czyta `manim.cfg` i trafia w 840×360 @ 60 fps.

#### Porównanie host ↔ kontener (zrobione 2026-08-11) — ✅ zgodne

Ten sam skrypt (`solutionZad2.py`, `ScenaZadania2`, czyli krok 6) wyrenderowany w kontenerze i zestawiony z hostowym `matura/2024-grudzien/media/zad2/zad2rozw_step6.mp4`:

- **Parametry pliku identyczne**: 840×360, 60 fps, 120 klatek, 2,000 s, h264 High, yuv420p.
- **SSIM średnio 0,999856**, najgorsza klatka 0,999543 (klatka 95, w środku animacji przekształcenia).
- W powiększeniu 4× glify mają **tę samą geometrię i te same pozycje** — różnice siedzą wyłącznie na krawędziach antyaliasingu.
- Skąd bierze się ta resztkowa różnica — test izolujący koder (render `--format=png`, czyli bez kompresji, jako trzeci punkt odniesienia; klatka 95):

  | Porównanie | SSIM |
  |---|---|
  | bezstratny render kontenera ↔ własny MP4 kontenera (sam koder) | 0,999601 |
  | bezstratny render kontenera ↔ MP4 z hosta | 0,999480 |
  | MP4 kontener ↔ MP4 host | 0,999581 |

  Czyli **sama kompresja H.264 wprowadza różnicę tego samego rzędu co cała różnica host↔kontener** i wystarcza do jej wyjaśnienia. Obawa o metryki fontu (MiKTeX vs TeX Live) **się nie potwierdziła**.
- **Nie ustalono**, jaka część różnicy przypada na koder, a jaka na sam render — wymagałoby to bezstratnych klatek z hosta, a referencja istnieje wyłącznie jako H.264. Znane różnice po stronie kodera: ffmpeg 5.1.9 vs 7.1 i waga pliku 20 kB vs 27 kB.

Wniosek: kontener nadaje się także do **finalnych** renderów, nie tylko do podglądu.

**Zmiany w `.devcontainer/Dockerfile` robi się z hosta, nie z kontenera** — `.devcontainer/` jest w kontenerze zamontowany read-only (patrz `.devcontainer/README.md`). Po edycji trzeba przebudować obraz: Dev Containers → „Rebuild Container".

## Workflow

0. **Każdy krok musi kończyć się `self.wait(0.25)`** — inaczej ostatni element animacji nie zostaje na ekranie. Przeglądarka po zakończeniu odtwarzania zatrzymuje obraz kilka klatek przed końcem pliku (przy 120 fps klatka trwa 8 ms, więc gubi się ich więcej niż kiedyś). Wykryte 2026-08-11 na kroku 1 zadania 2: w pliku ostatnia klatka miała wykładnik `⁻⁵` (obszar do x=925), a przeglądarka pokazywała w spoczynku obraz bez niego (do x=792). Po dodaniu przytrzymania oba obszary są identyczne. To nie jest kosmetyka — właśnie ta klatka zostaje na ekranie, gdy uczeń patrzy na krok.
1. Render sceny: `manim --save_sections solutionZadN.py <NazwaScenyKlasy>` (bez flagi jakości, patrz wyżej) — wynik ląduje w `media/videos/solutionZadN/720p120/`, a **każdy krok osobnym plikiem** w podkatalogu `sections/`, w kolejności `<Scena>_0000_krok1.mp4`, `_0001_krok2.mp4`, …
2. Cięcie jest **zrobione samym renderem** (2026-08-12) — granice kroków wyznacza `self.next_section("krokN")` w scenie. Wcześniej automatu nie było: kroki przełączało się komentarzem `"""` i renderowało po jednym, przez co w repo leżały skrypty z zakomentowaną większością treści, a `solutionZad2.py` w tej postaci **nie odtwarzał** wgranych plików (brakowało w nim m.in. przytrzymań `self.wait(0.25)`). Wszystkie cztery sceny są już przepisane na sekcje.

**To załatwiło problem stanu przenoszonego między krokami.** Odtworzenie zadania 2 krok po kroku (2026-08-11) pokazało, że **krok 2 nie renderuje się poprawnie w izolacji**: przekształca tylko `kroki[0][0..2]`, więc domykający nawias z wykładnikiem (`kroki[0][3]`) w ogóle nie trafia na scenę — w oryginalnej procedurze był tam już narysowany przez krok 1. Przy renderze przez sekcje ten problem znika z definicji: scena jedzie w całości, a sekcja to tylko miejsce cięcia gotowego materiału, więc każdy krok zaczyna się dokładnie tam, gdzie skończył poprzedni. Sprawdzone: sześć kroków zadania 2 wyrenderowanych przez `--save_sections` wychodzi **identycznych co do piksela** (SSIM 1,000000) z plikami wgranymi wcześniej na stronę.

**Dwie zasady, których trzeba pilnować w scenie:**

- `self.wait(0.25)` na końcu KAŻDEJ sekcji (punkt 0 wyżej) i **zawsze przed** `self.clear()`/`self.remove()`. Przytrzymanie po wyczyszczeniu sceny trzyma białą planszę — i to ona zostaje uczniowi na ekranie. Złapane porównaniem SSIM z wgranym plikiem (krok 2 zad. 2 wypadał 0,9967 zamiast 1,0).
- Wspólne skalowanie kroków pod kadr 16:9: jeden współczynnik liczony z najszerszego kroku (`MARGINES = 0.85`), a nie dopasowanie każdego kroku osobno — inaczej litery zmieniają rozmiar w trakcie przekształcenia i `Transform` robi z tego zoom. Wzorzec jest w każdej z czterech scen.
3. Skopiować pocięte pliki do `matura/<sheet-id>/media/zadN/solution-step-by-step/` pod nazwami `stepM.mp4` (nazwy lowercase, patrz CLAUDE.md). Zmiana z 2026-08-11: wcześniej leżały płasko jako `zadNrozw_stepM.mp4`.
4. Wygenerować rewersy: `tools/rewersy.sh matura/<sheet-id>/media/zadN/solution-step-by-step`. Robi to ffmpeg z gotowych plików, nie Manim — przycisk ◄ w odtwarzaczu odtwarza `stepMreverse.mp4`. Pułapki (m.in. konieczne przytrzymanie na końcu rewersu) opisuje [issues/krok-po-kroku-produkcja.md](../issues/krok-po-kroku-produkcja.md).

`media/` w tym folderze to cache Manim (Tex/svg, obrazy, wideo pośrednie) — odtwarzalny z plików `.py`, dlatego wyklucza go `manimations/.gitignore`.

5. Obejrzeć wynik na stronie **wyłącznie przez `node tools/serwer.js 8000`**. `python3 -m http.server` **nie nadaje się do pracy nad wideo**: nie obsługuje żądań zakresowych (`Range`), a bez nich przeglądarka nie potrafi przewinąć filmu — `video.seekable` zostaje pusty, a każde ustawienie `currentTime` cicho wraca do zera. Wygląda to jak błąd w kodzie odtwarzacza i raz już nim nie było (2026-08-11, sporo straconego czasu). Sprawdzian: `curl -s -o /dev/null -w "%{http_code}\n" -r 0-100 <url filmu>` ma zwrócić **206**, nie 200.

## Jak ma wyglądać animacja (zasady Henricha, 2026-08-12)

Wszystkie trzy wyszły z jego przeglądu zadań 3, 5 i 6 (v27). Łamie je automatyczne
`TransformMatchingShapes` bez nadzoru — Manim paruje wtedy kształty po podobieństwie, więc
szóstka z `60\,000` potrafi polecieć do licznika ułamka zamiast do mianownika, a nawias
`(1+p)^2` zamiast przesunąć się, znika i pojawia się na nowo. **Sprawdzaj każdy krok okiem
na gotowym pliku, a nie po samym „wyrenderowało się bez błędu".**

1. **Ciągłość między krokami.** Ostatnia klatka kroku N musi wyglądać dokładnie tak jak
   pierwsza klatka kroku N+1 — bo w odtwarzaczu to jest jedno i to samo miejsce, uczeń
   zatrzymuje się na nim i dopiero potem puszcza dalej. Wszelkie podświetlenia zdejmuj
   **przed** końcowym `self.wait(0.25)`, nie po nim. Jeśli coś ma zostać podświetlone przez
   kilka kroków (np. założenie \(x\ne 1\)), to musi być podświetlone w obu filmach.
   Sprawdzalne maszynowo: ostatnia klatka `stepN.mp4` kontra pierwsza klatka `stepN+1.mp4`.
2. **Ruch ma odpowiadać rachunkowi.** Element, który w rachunku wędruje w konkretne miejsce,
   ma tam dolecieć — a nie zniknąć i pojawić się gdzie indziej. Przy dłuższych wyrażeniach
   nie licz na automatyczne parowanie: wskazuj pary indeksami glifów (wzorzec z `solutionZad4.py`).
3. **Kolor to wskazówka, nie ozdoba.** Kolorem (czyli czymkolwiek poza czernią/bielą)
   oznaczasz **tylko to, na co uczeń ma spojrzeć**: składnik przenoszony na drugą stronę,
   czynnik, który się skraca. Znak, który się pojawia albo znika, może być czerwony.
   Nie koloruje się całego wyrażenia „bo się w nim coś zmieniło".

## Jak pisać opisy kroków (ROW 3, pole `text` w exercises.json)

Też zasady Henricha (2026-08-12). Priorytetem jest to, żeby uczeń zrozumiał, a nie żeby
zapis był formalnie poprawny.

- **Nie opisuj słowami tego, co widać na filmie.** „Zaczynamy od równania z wartością
  bezwzględną: \(|x+4|=7\)" nie mówi nic ponad obraz. Wystarczy „Zapisujemy \(|x+4|=7\)".
- **Tłumacz to, co naprawdę wymaga tłumaczenia, ale po ludzku.** Nie „wyrażenie pod modułem
  przyjmuje wartości przeciwne", tylko pokazane na liczbach, czym ta wartość bezwzględna
  właściwie jest. Żargonu tyle, ile uczeń musi znać na maturze, reszta zwykłymi słowami.
- **Krótkie linijki, wzór w osobnym wierszu.** Pole `text` trafia do DOM przez `innerHTML`,
  więc `<br>` i `\[ … \]` działają. Zbity akapit czyta się gorzej niż cztery linijki.
- **Żadnych myślników ani podkreśleń poza wzorami.** `-`, `—`, `_` mylą się z minusem,
  zwłaszcza w zdaniu, w którym obok stoi liczba ujemna. Zamiast myślnika: przecinek, kropka
  albo nowa linijka.
