# manimations/

Skrypty Manim generujące wideo do `solutionStepByStep` w `exercises.json` (finalne pliki lądują w `matura/<sheet-id>/media/zadN/`).

## Środowisko (sprawdzone na maszynie Henricha, 2026-08-11)

- Python: 3.12.8
- Manim: Community v0.18.1 (`pip install manim==0.18.1`)
- ffmpeg: 7.1 (gyan.dev full build)
- LaTeX: MiKTeX 25.4 (do renderowania wzorów przez Manim)

Zależności Pythona (z `pip freeze`): `manim==0.18.1`, `ManimPango==0.6.0`, `numpy==2.2.1`, `pillow==11.0.0`, `scipy==1.14.1`.

## Workflow

1. Render sceny: `manim -qh solutionZadN.py <NazwaScenyKlasy>` — wynik ląduje w `media/videos/solutionZadN/<rozdzielczość>/`.
2. Cięcie całej sceny na kroki (`_step1.mp4`, `_step2.mp4`, …) — **domysł, niepotwierdzone**: prawdopodobnie jakaś komenda (ffmpeg?), ale nie sprawdzone. **TODO: dopisać dokładną komendę.** (Sonnet 5, 2026-08-11)
3. Skopiować pocięte pliki do `matura/<sheet-id>/media/zadN/` pod nazwami `zadNrozw_stepM.mp4` (nazwy lowercase, patrz CLAUDE.md).

`media/` w tym folderze to cache Manim (Tex/svg, obrazy, wideo pośrednie) — odtwarzalny z plików `.py`, nie musi być commitowany.
