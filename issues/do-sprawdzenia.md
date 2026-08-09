# Do sprawdzenia na żywo przez Henricha

Rzeczy z planu UI (`issues/plan-ui-paczki-2026-08.md`), których nie dało się potwierdzić
zrzutem Playwrighta — każda sesja dopisuje tu 1–3 pozycje po swojej paczce.

## Paczka 1 — Drobnica (Sonnet 5 High, 2026-08-09)

- **Odstęp między wierszami przycisków (Podpowiedź/Rozwiązanie/Zgłoś błąd/Pokaż wzory) na
  realnym telefonie.** Zwiększony `row-gap` z 10px na 20px w `style/responsive.css` — na
  zrzucie 390px szerokości wygląda dobrze, ale „w sam raz vs. za dużo" to kwestia dotyku/wzroku
  na prawdziwym ekranie, nie piksela na screenshotcie.

- **Pigułka punktacji przy zadaniu (`.exercise-score`, „0 / 1 pkt") na bardzo wąskich
  telefonach** (iPhone SE / starsze Androidy, ~360px) — przysunięta o 40px bliżej treści
  (`right: -120px` → `-80px`), sprawdzona na 1280px i 390px. Na węższych ekranach badge
  przechodzi na inne pozycjonowanie (`style/responsive.css`), więc warto zerknąć, czy nie
  nachodzi na treść zadania.

- **Stopka arkusza i landing na prawdziwym telefonie**: nowa linijka „© 2026 Henrich2137 ·
  Licencja" — sprawdzić, czy link faktycznie otwiera się wygodnie (obszar dotyku, nie tylko
  wygląd) i czy nie wygląda na zbyt blady/niekontrastowy w słońcu na ekranie telefonu.
