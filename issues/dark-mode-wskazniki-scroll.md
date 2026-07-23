# Kropki wskaźników "gumkują" przy scrollowaniu

**Status:** NIE naprawione.

## Mechanizm

- `.wskaznik-otwarte` ma `transition: top 0.12s ease` (`style/exam.css:164`).
- `repozycjonujWskazniki()` przepisuje właściwość `top` w każdej klatce `requestAnimationFrame` podczas scrollowania.
- Efekt: tranzycja restartuje się co klatkę i nigdy nie kończy — kropki wloką się za zadaniami i drgają jeszcze ~120ms po zatrzymaniu scrolla.

## Dlaczego to źle

Animacja `transition` ma sens tylko przy skokowej repozycji (np. po ocenieniu zadania, gdy kropka nagle zmienia miejsce), nie przy ciągłej repozycji w rAF-pętli podczas scrolla.

## Kierunek naprawy

- Wyłączyć/pominąć `transition` na `top` podczas aktywnego scrollowania (np. dodać/usunąć klasę modyfikującą `transition: none` w trakcie scrolla, przywrócić po jego zakończeniu) i zostawić animację tylko dla skokowej repozycji po ocenieniu.

## Pliki

- `style/exam.css:164` (`.wskaznik-otwarte`, `transition: top 0.12s ease`)
- `script.js` — `repozycjonujWskazniki()`