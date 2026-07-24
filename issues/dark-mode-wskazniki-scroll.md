# Kropki wskaźników "gumkują" przy scrollowaniu

**Status:** NIE naprawione.

## Mechanizm

- `.wskaznik-otwarte` ma `transition: top 0.12s ease` (`style/exam.css:213`).
- `repozycjonujWskazniki()` (`app/indicators.js:143`) przepisuje właściwość `top` w każdej klatce `requestAnimationFrame` podczas scrollowania (planowane przez `zaplanujRepozycje()`, `app/indicators.js:132`).
- Efekt: tranzycja restartuje się co klatkę i nigdy nie kończy — kropki wloką się za zadaniami i drgają jeszcze ~120ms po zatrzymaniu scrolla.

## Dlaczego to źle

Animacja `transition` ma sens tylko przy skokowej repozycji (np. po ocenieniu zadania, gdy kropka nagle zmienia miejsce), nie przy ciągłej repozycji w rAF-pętli podczas scrolla.

## Kierunek naprawy (zdecydowane 2026-07-24, przydzielone Sonnetowi)

Dodawać/usuwać w `app/indicators.js` klasę (np. `.bez-tranzycji` na `.wskaznik-otwarte`, ustawiającą `transition: none` w `style/exam.css:213`) na czas aktywnego scrolla, przywracać po ~150ms ciszy od ostatniego eventu scroll (debounce timerem — celowo NIE `scrollend`, dla szerszej zgodności przeglądarek). Animacja `transition: top` zostaje tylko dla skokowej repozycji po ocenieniu zadania.

## Pliki

- `style/exam.css:213` (`.wskaznik-otwarte`, `transition: top 0.12s ease`)
- `app/indicators.js` — `repozycjonujWskazniki()`, `zaplanujRepozycje()`