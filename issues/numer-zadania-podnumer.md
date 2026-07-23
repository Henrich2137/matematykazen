# Regex numeru zadania gubi podnumery (12.1 vs 12.2)

**Status:** NIE naprawione. Niski priorytet — dziś nieszkodliwe.

## Problem

Numer zadania wyciągany jest regexem `/Zadanie\s*(\d+)/i` (`script.js:891`), który łapie tylko część przed kropką. Gdyby kiedyś zadanie 12.1 i 12.2 były oba otwarte (selfScore), dostałyby dwie identyczne kropki wskaźnika "12" z identycznym tooltipem — nie do odróżnienia.

## Dlaczego dziś nieszkodliwe

W obu obecnie wgranych arkuszach żadne zadanie otwarte (selfScore) nie ma podnumeru — kolizja nie występuje.

## Kierunek naprawy

Docelowo lepsze byłoby jawne pole `numer` w `exercises.json` zamiast wyciągania go regexem z tekstu zadania. Przydałoby się też w `console.warn` w `script.js:695` i `script.js:1004`, które nadal drukują mylące `index + 1` zamiast prawdziwego numeru zadania.

## Pliki

- `script.js:891` (regex `/Zadanie\s*(\d+)/i`)
- `script.js:695`, `script.js:1004` (`console.warn` z `index + 1`)
- `matura/<sheet-id>/exercises.json` (miejsce na docelowe pole `numer`)