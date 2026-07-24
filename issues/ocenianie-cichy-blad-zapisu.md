# `ustawFazeOceniania()` cicho połyka błędy zapisu do localStorage

**Status:** NIE naprawione. Niski priorytet.

## Problem

`ustawFazeOceniania()` (`app/indicators.js:21-26`) połyka błędy zapisu do localStorage bez żadnego komunikatu. Gdy localStorage jest zablokowany (np. tryb prywatny przeglądarki, wyczerpany limit), kliknięcie "ukryj wskaźniki" nie utrwala się — wskaźniki (kropki) wracają po każdym odświeżeniu strony, a użytkownik nie dostaje żadnej informacji, dlaczego jego wybór "nie trzyma się".

## Kierunek naprawy (zdecydowane 2026-07-24, przydzielone Sonnetowi)

W gałęzi `catch` wywołać istniejący toast z app/report.js: `pokazZglosToast("nie udało się zapisać ustawienia", true)` (funkcje globalne — classic scripts współdzielą scope; report.js ładuje się po indicators.js, ale w momencie kliknięcia wszystko już załadowane).

## Pliki

- `app/indicators.js:21-26` (`ustawFazeOceniania()`)
- `app/report.js` (`pokazZglosToast()`, do wywołania)