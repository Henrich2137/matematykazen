# manimations/

Skrypty Manim generujące wideo do `solutionStepByStep` w `exercises.json` (finalne pliki lądują w `matura/<sheet-id>/media/zadN/`).

## Środowisko

Są dwa, celowo z **tą samą wersją Manima (Community v0.18.1)** — chodzi o to, żeby ten sam skrypt dawał ten sam obraz niezależnie od tego, gdzie go wyrenderowano.

### Host — Windows Henricha (sprawdzone 2026-08-11)

- Python: 3.12.8
- Manim: Community v0.18.1 (`pip install manim==0.18.1`)
- ffmpeg: 7.1 (gyan.dev full build)
- LaTeX: MiKTeX 25.4 (do renderowania wzorów przez Manim)

Zależności Pythona (z `pip freeze`): `manim==0.18.1`, `ManimPango==0.6.0`, `numpy==2.2.1`, `pillow==11.0.0`, `scipy==1.14.1`.

### Devkontener — Debian (dodane 2026-08-11)

Manim, ffmpeg i minimalny TeX Live siedzą w obrazie kontenera (blok w `.devcontainer/Dockerfile` z `ARG MANIM_VERSION`), więc render odpala się w kontenerze bez żadnego przygotowania: `manim solutionZadN.py <NazwaScenyKlasy>`.

- LaTeX to TeX Live w minimalnym zestawie z dokumentacji Manima (~1–1,5 GB), a nie `texlive-full` — pokrywa to, czego używają istniejące sceny. Gdyby render zgłosił brakujący plik `.sty`, dopisuje się konkretny pakiet w Dockerfile.
- Instalacja nie wymaga wyjątku w firewallu (`pypi.org` jest poza allowlistą): obraz buduje się, zanim host nałoży firewall, a po starcie kontenera Manim nic już nie pobiera.
- Przypięty jest **tylko sam Manim**. Zależności pod spodem instalują się w najnowszych wersjach i różnią się od hosta (sprawdzone 2026-08-11: kontener dostaje `ManimPango 0.6.1`, `numpy 2.4.6`, `Pillow 12.3.0`, host ma `0.6.0` / `2.2.1` / `11.0.0`). Różni się też ffmpeg: **5.1.9** w kontenerze (tyle daje Debian 12) vs **7.1** na hoście.
- **Nie podawaj flagi jakości** (`-ql`/`-qh` itd.). Flaga jakości nadpisuje `pixel_width`/`pixel_height` z `manim.cfg`, a wraz z rozdzielczością zmieniają się **proporcje kadru**: `-qh` daje 1920×1080 (16:9) zamiast 840×360 (21:9), czyli inne rozmieszczenie wzorów w kadrze niż w plikach już wgranych na stronę. Samo `manim plik.py Scena` czyta `manim.cfg` i trafia w 840×360 @ 60 fps.

#### Porównanie host ↔ kontener (zrobione 2026-08-11) — ✅ zgodne

Ten sam skrypt (`solutionZad2.py`, `ScenaZadania2`, czyli krok 6) wyrenderowany w kontenerze i zestawiony z hostowym `matura/2024-grudzien/media/zad2/zad2rozw_step6.mp4`:

- **Parametry pliku identyczne**: 840×360, 60 fps, 120 klatek, 2,000 s, h264 High, yuv420p.
- **SSIM średnio 0,999856**, najgorsza klatka 0,999543 (klatka 95, w środku animacji przekształcenia).
- W powiększeniu 4× glify mają **tę samą geometrię i te same pozycje** — różnice siedzą wyłącznie na krawędziach antyaliasingu.
- Winowajcą resztkowej różnicy jest najpewniej **ffmpeg, nie render**: pliki ważą 20 kB (kontener) vs 27 kB (host), czyli koder dobrał inny bitrate. Obawa o metryki fontu (MiKTeX vs TeX Live) **się nie potwierdziła**.

Wniosek: kontener nadaje się także do **finalnych** renderów, nie tylko do podglądu. Gdyby kiedyś jednak zależało na bit-w-bit zgodności z wcześniejszymi plikami, jedyna znana różnica do wyrównania to wersja ffmpeg.

**Zmiany w `.devcontainer/Dockerfile` robi się z hosta, nie z kontenera** — `.devcontainer/` jest w kontenerze zamontowany read-only (patrz `.devcontainer/README.md`). Po edycji trzeba przebudować obraz: Dev Containers → „Rebuild Container".

## Workflow

1. Render sceny: `manim solutionZadN.py <NazwaScenyKlasy>` (bez flagi jakości, patrz wyżej) — wynik ląduje w `media/videos/solutionZadN/360p60/`.
2. Cięcie całej sceny na kroki (`_step1.mp4`, `_step2.mp4`, …) — **nie ma jeszcze zautomatyzowanego mechanizmu**. Ustalone 2026-08-11 przez odczytanie `solutionZad2.py`: dotychczasowe pliki `_stepN.mp4` powstawały tak, że wszystkie kroki poza jednym były **zakomentowane blokiem `"""`**, a scena renderowana raz na krok. Dlatego skrypty w tym folderze leżą w repo z zakomentowaną większością treści — to nie jest porzucony kod, tylko ostatni stan tej ręcznej procedury (`solutionZad2.py` stoi na kroku 6). Docelowe rozwiązanie (sekcje `self.next_section()` w scenach + skrypt `tools/manim-kroki.sh`) jest zaprojektowane i czeka na osobną paczkę — patrz [docs/superpowers/specs/2026-08-11-manim-w-kontenerze-design.md](../docs/superpowers/specs/2026-08-11-manim-w-kontenerze-design.md), warstwy 2 i 3.
3. Skopiować pocięte pliki do `matura/<sheet-id>/media/zadN/` pod nazwami `zadNrozw_stepM.mp4` (nazwy lowercase, patrz CLAUDE.md).

`media/` w tym folderze to cache Manim (Tex/svg, obrazy, wideo pośrednie) — odtwarzalny z plików `.py`, dlatego wyklucza go `manimations/.gitignore`.
