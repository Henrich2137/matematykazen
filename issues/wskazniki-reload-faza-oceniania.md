# Wskaźniki „oceń się" nie przeżywają odświeżenia strony po egzaminie

**Objaw.** Kończysz próbny egzamin → przy nieocenionych zadaniach otwartych pojawiają się żółte wskaźniki (faza „oceń się") → F5/reload → wskaźniki znikają i faza zostaje wygaszona (żeby wróciły, trzeba zrobić egzamin od nowa).

**Mechanizm.** Przy ładowaniu strony `applyTrybWskaznikow()` ([app/indicators.js](../app/indicators.js)) woła `pokazWskaznikiOtwarte()` ZANIM `loadExercises` wypełni globalną tablicę `zadaniaOtwarte`. Lista nieocenionych jest więc pusta → `pokazWskaznikiOtwarte()` trafia w gałąź `if (!oczekujace.length) { ustawFazeOceniania(false); return; }` i gasi fazę, zanim `startSheet()` ([app/bootstrap.js](../app/bootstrap.js), gałąź `else if (czyFazaOceniania()) pokazWskaznikiOtwarte()`) zdąży ją prawidłowo odtworzyć po renderze.

**Skąd się wziął.** Bug PRE-ISTNIEJĄCY, ujawniony przy podziale script.js → app/*.js (2026-07-23). W starym, jednoplikowym script.js ten sam scenariusz w ogóle CRASHOWAŁ stronę: `const zadaniaOtwarte` był deklarowany PONIŻEJ wywołania na load (linia ~637 vs wywołanie ~321) → `ReferenceError: Cannot access 'zadaniaOtwarte' before initialization` (TDZ) → skrypt zatrzymywał się, zadania się nie renderowały. Po podziale `zadaniaOtwarte` jest w `app/state.js` (ładowany pierwszy), więc nie ma crasha — ale funkcja „przetrwania odświeżenia" (opisana w komentarzach jako zamierzona) nadal nie działa. Refaktor świadomie tego nie ruszał („bez zmiany zachowania").

**Możliwa naprawa.** Nie gasić fazy przy load, gdy arkusz nie jest jeszcze wyrenderowany — np. w `pokazWskaznikiOtwarte()` czyścić fazę tylko gdy `document.body.classList.contains("arkusz-wczytany")`. Wtedy load-time wywołanie nic nie psuje, a `startSheet()` po renderze odtworzy wskaźniki poprawnie.
