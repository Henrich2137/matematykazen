# Zadania nie renderują się na telefonie (arkusz 2024-grudzień)

**Status:** ZDIAGNOZOWANE 2026-07-24 — patrz „Przyczyna" na dole. Fix: `.nojekyll` w rootcie.

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

##HENRICH DOPISUJE:
Gdy włączyłem na firefoxie na Pixelu 7a zadania się wczytały ale bez przycisku "rozwiązanie" oraz bez "podpowiedź". Na dole wyświetlił się taki komunikat:
"

⚠ Wystąpił błąd strony (pokaż ten tekst autorowi):

• Nie wczytano skryptu: https://henrich2137.github.io/matematykazen/widgets/_helpers.js
• Nie wczytano skryptu: https://henrich2137.github.io/matematykazen/widgets/_registry.js
• [render zadania (index 0)] WIDZETY is not defined
  loadExercises/<@https://henrich2137.github.io/matematykazen/app/render.js:659:28
  loadExercises@https://henrich2137.github.io/matematykazen/app/render.js:91:15
  startSheet@https://henrich2137.github.io/matematykazen/app/bootstrap.js:207:9
• [render zadania (index 4)] WIDZETY is not defined
  loadExercises/<@https://henrich2137.github.io/matematykazen/app/render.js:659:28
  loadExercises@https://henrich2137.github.io/matematykazen/app/render.js:91:15
  startSheet@https://henrich2137.github.io/matematykazen/app/bootstrap.js:207:9
• [render zadania (index 8)] WIDZETY is not defined
  loadExercises/<@https://henrich2137.github.io/matematykazen/app/render.js:659:28
  loadExercises@https://henrich2137.github.io/matematykazen/app/render.js:91:15
  startSheet@https://henrich2137.github.io/matematykazen/app/bootstrap.js:207:9
• [render zadania (index 9)] WIDZETY is not defined
  loadExercises/<@https://henrich2137.github.io/matematykazen/app/render.js:659:28
  loadExercises@https://henrich2137.github.io/matematykazen/app/render.js:91:15
  startSheet@https://henrich2137.github.io/matematykazen/app/bootstrap.js:207:9
• [render zadania (index 12)] WIDZETY is not defined
  loadExercises/<@https://henrich2137.github.io/matematykazen/app/render.js:659:28
  loadExercises@https://henrich2137.github.io/matematykazen/app/render.js:91:15
  startSheet@https://henrich2137.github.io/matematykazen/app/bootstrap.js:207:9
• [render zadania (index 17)] WIDZETY is not defined
  loadExercises/<@https://henrich2137.github.io/matematykazen/app/render.js:659:28
  loadExercises@https://henrich2137.github.io/matematykazen/app/render.js:91:15
  startSheet@https://henrich2137.github.io/matematykazen/app/bootstrap.js:207:9
• [render zadania (index 22)] WIDZETY is not defined
  loadExercises/<@https://henrich2137.github.io/matematykazen/app/render.js:659:28
  loadExercises@https://henrich2137.github.io/matematykazen/app/render.js:91:15
  startSheet@https://henrich2137.github.io/matematykazen/app/bootstrap.js:207:9

  "
## PRZYCZYNA (potwierdzona 2026-07-24)

To **nie był problem telefonu ani mobilnej przeglądarki**. GitHub Pages domyślnie
przepuszcza repo przez Jekylla, a Jekyll **pomija pliki i katalogi zaczynające się
od `_`**. Efekt: `widgets/_helpers.js` i `widgets/_registry.js` nigdy nie trafiły
na opublikowaną stronę.

Sprawdzone przez `curl` na żywo:

| URL | HTTP |
|---|---|
| `https://henrich2137.github.io/matematykazen/widgets/_helpers.js` | 404 |
| `https://henrich2137.github.io/matematykazen/widgets/_registry.js` | 404 |
| `https://henrich2137.github.io/matematykazen/widgets/osLiczbowa.js` | 200 |

Brak `_registry.js` → `WIDZETY is not defined` → każde zadanie z widżetem
degraduje się (od commita 33c1740 do placeholdera zamiast wywalać całą listę),
stąd „zadania bez przycisku rozwiązanie/podpowiedź". Lokalnie
(`python -m http.server`) wszystko działa, bo tam nie ma Jekylla — dlatego
objaw wyglądał na mobile-only.

**Fix:** pusty plik `.nojekyll` w rootcie repo (wyłącza przetwarzanie Jekyllem,
Pages serwuje pliki 1:1). Alternatywa (nieużyta): zmiana nazw na
`helpers.js`/`registry.js` — `.nojekyll` chroni też przyszłe pliki z `_`.
