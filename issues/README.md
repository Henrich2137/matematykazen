# issues/

Szczegółowe opisy pojedynczych problemów: konkretne pliki, linie, mechanizm awarii, dlaczego to się dzieje. TODO.md ma tylko krótkie hasło + link tutaj; ten katalog ma całą logikę potrzebną do naprawy bez odtwarzania kontekstu od zera.

Zasady:
- Jeden plik = jeden problem. Nazwa pliku: krótki opisowy slug po polsku, kebab-case.
- Nowy problem znaleziony podczas pracy → nowy plik tutaj + jedna linijka w TODO.md z odnośnikiem `(issues/nazwa.md)`.
- Naprawione → przenieś notatkę do `done/` (patrz `done/README.md`) i usuń plik stąd.
- Nie czytaj tego katalogu z automatu przy każdej sesji — otwieraj konkretny plik, gdy TODO.md do niego linkuje.

## Aktywne

- [dwie-karty-tryb-egzaminu.md](dwie-karty-tryb-egzaminu.md) — dwie karty tego samego arkusza blokują "zakończ egzamin"
- [dark-mode-wskazniki-scroll.md](dark-mode-wskazniki-scroll.md) — kropki wskaźników "gumkują" przy scrollowaniu
- [dokumentacja-exam-mode-luka.md](dokumentacja-exam-mode-luka.md) — ARCHITECTURE.md nie opisuje połowy trybu egzaminu
- [numer-zadania-podnumer.md](numer-zadania-podnumer.md) — regex numeru zadania gubi podnumery (12.1 vs 12.2)
- [motyw-rozjezdza-sie-miedzy-kartami.md](motyw-rozjezdza-sie-miedzy-kartami.md) — dark/light mode niespójny między kartami przeglądarki
- [ocenianie-cichy-blad-zapisu.md](ocenianie-cichy-blad-zapisu.md) — `ustawFazeOceniania()` cicho połyka błędy zapisu do localStorage
- [wskazniki-reload-faza-oceniania.md](wskazniki-reload-faza-oceniania.md) — wskaźniki „oceń się" znikają po odświeżeniu strony po egzaminie
- [zadania-nie-renderuja-sie-mobile.md](zadania-nie-renderuja-sie-mobile.md) — zadania nie renderują się na telefonie (Pixel 7a/GrapheneOS, Firefox i Brave)

## Opisy konstrukcji (nie problemy)

- [playwright-podglad.md](playwright-podglad.md) — Playwright + Chromium w kontenerze: skąd się bierze przeglądarka i jak podbić wersję

## Archiwum (kod usunięty, ale trzymany na wypadek powrotu)

- [archiwum-hover-podglad.md](archiwum-hover-podglad.md) — usunięty hover-podgląd „wartość → następna" w panelu ustawień

## Plany

- [plan-ui-paczki-2026-08.md](plan-ui-paczki-2026-08.md) — otwarte punkty UI z TODO.md podzielone na 4 sekwencyjne paczki + decyzje Henricha; wsad dla sesji autonomicznych
