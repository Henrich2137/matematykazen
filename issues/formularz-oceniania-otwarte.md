# Formularz wspomagający samoocenę zadań otwartych

**Status:** NIE zrobione. Spec doprecyzowany z Henrichem 2026-07-24, do zrobienia przez Opusa.

## Cel

Dziś zadania otwarte (`selfScore: true`) mają tylko miejsce na notatki + przyciski „0 pkt"…„max pkt" do ręcznej samooceny po porównaniu z rozwiązaniem. Ma dojść:

1. **Nowe pole „ostateczna odpowiedź"** — uczeń wpisuje końcowy wynik (np. `x=5`), strona go normalizuje i automatycznie sprawdza (ta sama logika co `normalizeAnswer`/`markCorrectAnswer` dla zadań zamkniętych, `app/answers.js`). **To pole ma być widoczne W TRAKCIE egzaminu** — w przeciwieństwie do checklisty niżej i do rozwiązań, które w trybie egzaminu zostają ukryte do końca (`body.tryb-egzaminu` w style/exam.css). To jedyny automatyczny sygnał poprawności, jaki zadania otwarte dostają.
2. **Mini-formularz checklista** (dopiero po odblokowaniu rozwiązania, jak reszta selfScore-UI) w formie: „Czy w Twoich obliczeniach znajduje się: **x**?", „…**y**?", „…**z**?" — gdzie x/y/z to poszczególne elementy oficjalnego klucza zasad oceniania CKE, za które przyznawane są punkty (np. „długość boku BC = 5cm"). To checklista pomocnicza, **NIE sumuje punktów automatycznie** — uczeń nadal sam wybiera ostateczną liczbę punktów przyciskami „0 pkt"…„max pkt" jak dziś; formularz ma mu tylko ułatwić decyzję.
3. **Zastrzeżenie prawne** ("gwiazdka") — **raz, ogólnie** (stopka / regulamin serwisu), nie przy każdym zadaniu: strona nie jest egzaminatorem, każdy przypadek trzeba sprawdzić indywidualnie.

## Zakres pierwszego podejścia

Henrich: zrób **prototyp na 1-2 zadaniach otwartych** jako dowód koncepcji (pełny mechanizm UI + ręcznie wpisana checklista dla tych 1-2 zadań), do jego akceptacji — reszta zadań dostanie checklisty później, sukcesywnie dopisywane do `exercises.json`.

## Otwarte pytania do rozstrzygnięcia przy implementacji (Opus)

- Schemat danych w `exercises.json`: nowe pole per selfScore-zadanie, np. `"kryteriaOceny": ["...", "...", "..."]` (lista stringów) + osobne pole na poprawną „ostateczną odpowiedź" do normalizacji (analogicznie do istniejącego `correctAnswer`/`correctAnswerIndex` wzorca w innych typach zadań — sprawdź ARCHITECTURE.md, sekcja schematu).
- UI checklisty: prawdopodobnie zestaw checkboxów pod notatkami, nad przyciskami punktacji; nie musi wpływać na `earnedScore` bezpośrednio.
- Które 1-2 zadania na prototyp: dowolne, ale wybierz coś z jasnym, rozbitym na punkty kluczem oceniania w PDF-ie `matura/<id>/*odpowiedzi.pdf`, żeby checklista miała sens.

## Powiązane

- Wzorzec normalizacji/sprawdzania: `app/answers.js` (`normalizeAnswer`, `markCorrectAnswer`).
- Wzorzec obecnego UI zadań otwartych: `app/render.js` + `selfScore` w schemacie (ARCHITECTURE.md).
