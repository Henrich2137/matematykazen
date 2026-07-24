# issues/

Szczegółowe opisy pojedynczych problemów: konkretne pliki, linie, mechanizm awarii, dlaczego to się dzieje. TODO.md ma tylko krótkie hasło + link tutaj; ten katalog ma całą logikę potrzebną do naprawy bez odtwarzania kontekstu od zera.

Zasady:
- Jeden plik = jeden problem. Nazwa pliku: krótki opisowy slug po polsku, kebab-case.
- Nowy problem znaleziony podczas pracy → nowy plik tutaj + jedna linijka w TODO.md z odnośnikiem `(issues/nazwa.md)`.
- Naprawione → przenieś notatkę do `DONE/` (patrz `DONE/README.md`) i usuń plik stąd.
- Nie czytaj tego katalogu z automatu przy każdej sesji — otwieraj konkretny plik, gdy TODO.md do niego linkuje.

## Aktywne

- [dwie-karty-tryb-egzaminu.md](dwie-karty-tryb-egzaminu.md) — dwie karty tego samego arkusza blokują "zakończ egzamin"
- [dark-mode-obrazki-wideo.md](dark-mode-obrazki-wideo.md) — obrazki CKE i wideo z Manima świecą na biało w dark mode
- [dark-mode-css-zmienne-landing.md](dark-mode-css-zmienne-landing.md) — landing page używa niewłaściwych zmiennych CSS (kontrast WCAG)
- [dark-mode-wskazniki-scroll.md](dark-mode-wskazniki-scroll.md) — kropki wskaźników "gumkują" przy scrollowaniu
- [dokumentacja-exam-mode-luka.md](dokumentacja-exam-mode-luka.md) — ARCHITECTURE.md nie opisuje połowy trybu egzaminu
- [numer-zadania-podnumer.md](numer-zadania-podnumer.md) — regex numeru zadania gubi podnumery (12.1 vs 12.2)
- [motyw-rozjezdza-sie-miedzy-kartami.md](motyw-rozjezdza-sie-miedzy-kartami.md) — dark/light mode niespójny między kartami przeglądarki
- [ocenianie-cichy-blad-zapisu.md](ocenianie-cichy-blad-zapisu.md) — `ustawFazeOceniania()` cicho połyka błędy zapisu do localStorage
- [wskazniki-reload-faza-oceniania.md](wskazniki-reload-faza-oceniania.md) — wskaźniki „oceń się" znikają po odświeżeniu strony po egzaminie
- [egzamin-zegar-toggle.md](egzamin-zegar-toggle.md) — toggle widoczności zegara w trybie egzaminu
- [egzamin-tablica-auto-zamkniecie.md](egzamin-tablica-auto-zamkniecie.md) — tablica wzorów ma się wyłączać automatycznie po zakończeniu egzaminu