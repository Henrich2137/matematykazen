# Regex numeru zadania gubi podnumery (12.1 vs 12.2)

**Status:** NIE naprawione. Niski priorytet — dziś nieszkodliwe.

## Problem

Numer zadania wyciągany jest regexem `/Zadanie\s*(\d+)/i` (`app/render.js:440`), który łapie tylko część przed kropką. Gdyby kiedyś zadanie 12.1 i 12.2 były oba otwarte (selfScore), dostałyby dwie identyczne kropki wskaźnika "12" z identycznym tooltipem — nie do odróżnienia.

## Dlaczego dziś nieszkodliwe

Zweryfikowane 2026-07-24: w obu obecnie wgranych arkuszach istnieją podnumerowane zadania (np. `matura/2026-maj/exercises.json` — "Zadanie 12.1"/"12.2", "13.1"/"13.2" itd.), ale wszystkie mają `"type": "fillIn"`, nie `"selfScore"` — nie wchodzą do rejestru `zadaniaOtwarte` (app/render.js), więc kolizja faktycznie nie występuje. To nie są błędne dane, tylko luka w regexie na wypadek gdyby kiedyś podnumerowane zadanie było typu selfScore.

## Kierunek naprawy (zdecydowane 2026-07-24, przydzielone Sonnetowi)

Szybka łatka regexu: zmienić na `/Zadanie\s*([\d.]+)/i`, żeby łapał pełny numer z podnumerem (np. "12.1"), bez zmian w exercises.json. Sprawdzić przy okazji, czy nic innego nie zakłada, że `numer` jest liczbą całkowitą (sortowanie/porównania w app/indicators.js, app/report.js). Przydałoby się też poprawić `console.warn` w `app/render.js:141` i `app/render.js:554`, które nadal drukują mylące `index + 1` zamiast prawdziwego numeru zadania.

## Pliki

- `app/render.js:440` (regex `/Zadanie\s*(\d+)/i`)
- `app/render.js:141`, `app/render.js:554` (`console.warn` z `index + 1`)
- `matura/<sheet-id>/exercises.json` (dane potwierdzone poprawne — bez zmian)