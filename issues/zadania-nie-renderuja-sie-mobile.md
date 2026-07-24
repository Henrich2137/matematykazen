# Zadania nie renderują się na telefonie (arkusz 2024-grudzień)

**Status:** NIE zdiagnozowane. Repro od Henricha 2026-07-24, do zbadania przez Opusa.

## Repro

- Urządzenie: **Pixel 7a, GrapheneOS**.
- Powtarza się na **dwóch różnych przeglądarkach** na tym urządzeniu: **Firefox** i **Brave** — więc raczej nie quirk pojedynczej przeglądarki, prędzej coś wspólnego dla obu (silnik renderowania mobile Chrome-pochodny w obu, albo coś na poziomie systemu/sieci GrapheneOS).
- Objaw: pasek górny, menu i tytuł arkusza renderują się normalnie (`#bar-*`, `#exercises-sheet-title`) — **tylko lista zadań jest pusta**, jakby `loadExercises()` (app/render.js) nie odpaliło się albo padło w trakcie.
- Henrich nie ma na razie zrzutu ekranu ani logu konsoli z tego urządzenia.

## Hipotezy do sprawdzenia (nieprzetestowane)

- `fetch()` po `exercises.json` w `startSheet()` (app/state.js) może się nie udawać na mobile z innego powodu niż desktop — sprawdzić czy to nie np. Content-Security-Policy, ścieżka względna łamana przez `?arkusz=` routing, albo jakiś mobile-specific network quirk.
- Możliwy JS error w trakcie `loadExercises()` blokujący resztę renderowania (np. któryś widżet/typ zadania rzuca wyjątkiem na mobile Chrome-pochodnym silniku, którego desktop Chrome/Firefox nie łapie).
- GrapheneOS domyślnie ma bardziej restrykcyjne ustawienia sieciowe/prywatności (np. blokowanie niektórych zapytań, storage partitioning) — sprawdzić, czy któryś z mechanizmów `localStorage`/`fetch` używanych w `state.js`/`render.js` może być tam blokowany po cichu.
- Desktop-emulacja (Playwright z mobile viewport + user agent) może NIE odtworzyć błędu, jeśli przyczyna jest specyficzna dla silnika/OS-u telefonu, a nie samego rozmiaru ekranu — jeśli emulacja nie repro, to sygnał że problem jest głębszy niż CSS/viewport.

## Sugerowany kierunek diagnozy

1. Spróbować odtworzyć przez zdalne debugowanie (`chrome://inspect` z telefonu podłączonego USB, albo `about:debugging` w Firefoksie) — złapać faktyczny błąd w konsoli. To najszybsza droga do konkretnej przyczyny; bez tego reszta to zgadywanie.
2. Jeśli zdalne debugowanie niedostępne: dodać tymczasowe, bardzo widoczne logowanie błędów (np. `window.onerror` wypisujący komunikat na stronie) żeby Henrich mógł przesłać treść błędu bez podłączania kabla.
3. Sprawdzić czy `fetch('matura/2024-grudzien/exercises.json')` w ogóle dochodzi (network tab / prosty test w konsoli telefonu).

## Pliki

- `app/state.js` — `startSheet()`, `mediaPath()`, `fetch` danych arkusza.
- `app/render.js` — `loadExercises()`.
