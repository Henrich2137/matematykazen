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
- [dark-mode-inwersja-przegladarki.md](dark-mode-inwersja-przegladarki.md) — odwracanie kolorów grafik/wideo w dark mode działa inaczej w Chrome/Brave (jaśniejszy prostokąt) i w ogóle nie działa w Samsung Internet
- [dokumentacja-exam-mode-luka.md](dokumentacja-exam-mode-luka.md) — ARCHITECTURE.md nie opisuje połowy trybu egzaminu
- [numer-zadania-podnumer.md](numer-zadania-podnumer.md) — regex numeru zadania gubi podnumery (12.1 vs 12.2)
- [motyw-rozjezdza-sie-miedzy-kartami.md](motyw-rozjezdza-sie-miedzy-kartami.md) — dark/light mode niespójny między kartami przeglądarki
- [ocenianie-cichy-blad-zapisu.md](ocenianie-cichy-blad-zapisu.md) — `ustawFazeOceniania()` cicho połyka błędy zapisu do localStorage
- [wskazniki-reload-faza-oceniania.md](wskazniki-reload-faza-oceniania.md) — wskaźniki „oceń się" znikają po odświeżeniu strony po egzaminie
- [zadania-nie-renderuja-sie-mobile.md](zadania-nie-renderuja-sie-mobile.md) — zadania nie renderują się na telefonie (Pixel 7a/GrapheneOS, Firefox i Brave)
- [krok-po-kroku-v20-testy.md](krok-po-kroku-v20-testy.md) — checklista testów Henricha dla odtwarzacza v20 (zad. 1/2/3) i kadru 16:9 zad. 2 (v19); część potwierdzona, część otwarta
- [testowanie-archiwum.md](testowanie-archiwum.md) — pełna sekcja TESTOWANIE HENRICH z TODO.md sprzed skrócenia (v33-v62); gotowy scenariusz przejścia arkuszy zadanie po zadaniu
- [chrome-devtools-mcp-cache-eacces.md](chrome-devtools-mcp-cache-eacces.md) — plugin chrome-devtools-mcp nie działa: `EACCES` przy zapisie do `~/.cache` (root:root), naprawa wymaga Rebuild Container

## Nie problemy, tylko opisy działania

Wyjątek od zasady „jeden plik = jeden problem": rzeczy, które nie są zepsute,
ale mają na tyle nieoczywistą konstrukcję, że bez notatki nikt jej nie odtworzy.
Siedzą tutaj, a nie w CLAUDE.md, bo do codziennej pracy nad stroną nie są potrzebne —
CLAUDE.md ma z każdej z nich tylko kilka linijek i odnośnik tutaj.

- [rozwiazanie-krok-po-kroku-odtwarzacz.md](rozwiazanie-krok-po-kroku-odtwarzacz.md) — odtwarzacz kroków w przeglądarce: serwer bez obsługi przewijania wideo, gubienie klatek przy 4×, jak weryfikować, żeby zrzut ekranu nie skłamał (produkcja samych filmów: manimations/README.md)
- [playwright-podglad.md](playwright-podglad.md) — Playwright + Chromium w kontenerze (przeglądarka z bindu hosta, przypięta wersja i jak ją podbić) + pułapki pisania skryptów pod tę stronę
- [flatpak-osierocone-dane.md](flatpak-osierocone-dane.md) — dane po odinstalowanych flatpakach zostają w `~/.var/app` (przepis: jak znaleźć, jak sprawdzić przed kasowaniem, których ustawień nie przenosić)
- [git-i-gitdoc.md](git-i-gitdoc.md) — gitdoc (wyłączony) + natywny auto-fetch/auto-pull: dlaczego gitdoc da się włączyć tylko per-workspace, co by robił po włączeniu, `forcePush`, debounce `autoCommitDelay`, `task.allowAutomaticTasks`
- [licencja-i-cla.md](licencja-i-cla.md) — PolyForm Noncommercial + CLA: co jest w którym pliku meta i dwa placeholdery (pseudonim, URL Required Notice) zmieniane parami
- [licencja-premium.md](licencja-premium.md) — rozdział licencyjny: `widgets/` na licencji zastrzeżonej (premium), reszta na PolyForm; gdzie biegnie granica, dlaczego bez daty i hasha, i czego w `widgets/` kłaść nie wolno
- [claude-code-pluginy.md](claude-code-pluginy.md) — plugin superpowers: scope project, przypięty SHA, pułapka przy szukaniu w cache'u marketplace'u, pusty `vendor/superpowers/`

## Archiwum (kod usunięty, ale trzymany na wypadek powrotu)

- [archiwum-hover-podglad.md](archiwum-hover-podglad.md) — usunięty hover-podgląd „wartość → następna" w panelu ustawień

## Plany

- [plan-ui-paczki-2026-08.md](plan-ui-paczki-2026-08.md) — otwarte punkty UI z TODO.md podzielone na 4 sekwencyjne paczki + decyzje Henricha; wsad dla sesji autonomicznych
