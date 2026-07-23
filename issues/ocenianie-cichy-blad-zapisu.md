# `ustawFazeOceniania()` cicho połyka błędy zapisu do localStorage

**Status:** NIE naprawione. Niski priorytet.

## Problem

`ustawFazeOceniania()` (`script.js:280-285`) połyka błędy zapisu do localStorage bez żadnego komunikatu. Gdy localStorage jest zablokowany (np. tryb prywatny przeglądarki, wyczerpany limit), kliknięcie "ukryj wskaźniki" nie utrwala się — wskaźniki (kropki) wracają po każdym odświeżeniu strony, a użytkownik nie dostaje żadnej informacji, dlaczego jego wybór "nie trzyma się".

## Kierunek naprawy

- Przy złapanym błędzie zapisu pokazać użytkownikowi krótki komunikat (np. "nie udało się zapisać ustawienia") zamiast cichego catch.

## Pliki

- `script.js:280-285` (`ustawFazeOceniania()`)