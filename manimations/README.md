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

Manim, ffmpeg i minimalny TeX Live siedzą w obrazie kontenera (blok w `.devcontainer/Dockerfile` z `ARG MANIM_VERSION`), więc render odpala się w kontenerze bez żadnego przygotowania: `manim -qh solutionZadN.py <NazwaScenyKlasy>`.

- LaTeX to TeX Live w minimalnym zestawie z dokumentacji Manima (~1–1,5 GB), a nie `texlive-full` — pokrywa to, czego używają istniejące sceny. Gdyby render zgłosił brakujący plik `.sty`, dopisuje się konkretny pakiet w Dockerfile.
- Instalacja nie wymaga wyjątku w firewallu (`pypi.org` jest poza allowlistą): obraz buduje się, zanim host nałoży firewall, a po starcie kontenera Manim nic już nie pobiera.
- **Rozjazd wizualny host ↔ kontener jest możliwy** — inny silnik LaTeX (MiKTeX vs TeX Live) i inne fonty systemowe mogą dać minimalnie inne metryki liter i grubości kresek. Dopóki porównanie klatek nie zostanie zrobione, kontener traktujemy jako środowisko **podglądu**, a finalne rendery robimy na hoście.

**Zmiany w `.devcontainer/Dockerfile` robi się z hosta, nie z kontenera** — `.devcontainer/` jest w kontenerze zamontowany read-only (patrz `.devcontainer/README.md`). Po edycji trzeba przebudować obraz: Dev Containers → „Rebuild Container".

## Workflow

1. Render sceny: `manim -qh solutionZadN.py <NazwaScenyKlasy>` — wynik ląduje w `media/videos/solutionZadN/<rozdzielczość>/`.
2. Cięcie całej sceny na kroki (`_step1.mp4`, `_step2.mp4`, …) — **nie ma jeszcze zautomatyzowanego mechanizmu**. Istniejące pliki `_stepN.mp4` powstały historycznie, ręcznie. Docelowe rozwiązanie (sekcje `self.next_section()` w scenach + skrypt `tools/manim-kroki.sh`) jest zaprojektowane i czeka na osobną paczkę — patrz [docs/superpowers/specs/2026-08-11-manim-w-kontenerze-design.md](../docs/superpowers/specs/2026-08-11-manim-w-kontenerze-design.md), warstwy 2 i 3.
3. Skopiować pocięte pliki do `matura/<sheet-id>/media/zadN/` pod nazwami `zadNrozw_stepM.mp4` (nazwy lowercase, patrz CLAUDE.md).

`media/` w tym folderze to cache Manim (Tex/svg, obrazy, wideo pośrednie) — odtwarzalny z plików `.py`, dlatego jest w `.gitignore` w katalogu głównym repo.
