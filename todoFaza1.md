# Faza 1 — pozostałe porządki w silniku (dla następnej sesji)

Ten plik to lista zadań do wykonania w **nowej sesji czatu**, żeby nie ciągnąć kontekstu poprzedniej.
Zakres: tylko silnik + zadania 1–6 (nie uzupełniamy treści stubów 7–30 i nie ruszamy designu).

## Zanim zaczniesz
1. Przeczytaj `CLAUDE.md` (opisuje architekturę, schemat danych i layout — jest aktualny).
2. Pliki, których dotyczy Faza 1: **`matematykazen12.html`** (cały silnik jest w inline `<script>` na dole) oraz pomocniczo `exercises.js` (dane).
3. Nie ma builda ani testów. Po każdej zmierze weryfikuj tak:
   - Składnia inline-skryptu (Git Bash):
     `awk '/<script>/{f=1;next} /<\/script>/{f=0} f' matematykazen12.html > /tmp/mz.js && node --check /tmp/mz.js`
   - Klik-test w prawdziwej przeglądarce (Chrome/Firefox, **nie** VS Code Integrated Browser — tam filmy się nie renderują, to znany problem środowiska): zad. 1 (odpowiedzi, podpowiedź, rozwiązanie krok-po-kroku, wzory), zad. 6 (dobra odpowiedź na zielono).

## Co jest już ZROBIONE (nie powtarzaj)
- Bug playbacku filmów: `renderStep()` zwraca czysty string, a `showStep()` ustawia `defaultPlaybackRate` i `playbackRate = 0.1` na realnym `<video>`.
- Ocena odpowiedzi przeniesiona na `correctAnswerIndex` (liczba) — zamiast porównywania stringów HTML. Wszystkie zadania w `exercises.js` już zmigrowane (`-1` = otwarte/niewypełnione).
- Bug „punkt nie cofał się po złej odpowiedzi": usunięty flag `isScoreGiven`; każde zadanie ma `earnedScore`, a `updateTotalScore()` przelicza sumę od zera.
- `markCorrectAnswer()` zabezpieczony przed brakiem przycisku (`if (button)`).
- `CLAUDE.md` zaktualizowany pod powyższe.

---

## ZADANIA DO ZROBIENIA

### 1. Usuń martwy kod (dwie nieużywane funkcje rysujące)
- W `matematykazen12.html` usuń całe definicje funkcji:
  - `drawExponentialGraph(...)` — jest **znakowym duplikatem** `drawNumberLine1` (rysuje oś liczbową, nie wykres) i nigdzie nie jest wołana.
  - `rysujWykresEksponencjalny(...)` — niedokończona (główna pętla rysująca jest zakomentowana), brak wywołań. Zad. 5 ma teraz `solutionInteractive: null`, więc nikt jej nie używa.
- **Zostaw** `drawNumberLine1` — używa jej zad. 1 (`solutionInteractive` + `oninput`).
- Po usunięciu potwierdź brak odwołań:
  `grep -rn "drawExponentialGraph\|rysujWykresEksponencjalny" matematykazen12.html exercises.js` → powinno być puste.

### 2. Scal potrójny listener `.solution-button` w jeden
- Obecnie `exerciseClone.querySelector(".solution-button").addEventListener("click", ...)` jest wywoływane **trzy razy** (główny toggle pokaż/schowaj rozwiązanie + osobno w gałęzi „są kroki" + w gałęzi „brak kroków"). Działa, ale jest mylące i kruche.
- Docelowo: **jeden** handler klliknięcia „Rozwiązanie", który:
  - chowa `hintContainer`,
  - toggluje widoczność `solutionContainer`,
  - jeśli zadanie ma kroki (`solutionStepByStep`) → pokazuje `solutionStepByStepContainer` i woła `showStep(currentStep)`, w przeciwnym razie ją chowa.
- Uwaga na zakresy: `currentStep`, `showStep`, `steps` są dziś zdefiniowane wewnątrz bloku `if (... exercise.solutionStepByStep ...)`. Trzeba to przeorganizować, np. policzyć wcześniej `const hasSteps = Array.isArray(exercise.solutionStepByStep)` i wynieść `currentStep`/`showStep` na poziom widoczny dla handlera. Zachowaj obecne zachowanie (kroki pojawiają się dopiero po kliknięciu „Rozwiązanie", ostatni krok woła `markCorrectAnswer`).

### 3. Zadeklaruj „wyciekające" zmienne globalne
- `totalScore = 0;` (na górze skryptu) → `let totalScore = 0;`. Sprawdź, że `updateTotalScore()` w `loadExercises` dalej ją widzi (przy `let` na poziomie skryptu — tak).
- `formulasButton = exerciseClone.querySelector(".formulas-button")` → dodaj `const`.
- `var elements = document.getElementsByClassName('exercise-score')` (2 wystąpienia w handlerze `#score-switch-button`) → `const elements`.
- Cel: żadnych niejawnych globali. Po zmianie `node --check` + klik-test paska punktów (przełącznik „widok punktów").

### 4. Przenieś `<script>` przed `</body>`
- Inline-skrypt zaczyna się obecnie **po** `</body></html>` (niepoprawny HTML). Przenieś cały blok `<script>...</script>` tak, aby stał tuż **przed** `</body>`.
- To zmiana czysto porządkowa (przeglądarki i tak go wykonują), ale należy do Fazy 1. Po przeniesieniu `node --check` na wyekstrahowanym skrypcie i szybki klik-test, że strona nadal działa.

### 5. (Do weryfikacji — prawdopodobnie już OK) Duplikat `id="numberLine"`
- Kiedyś canvas `#numberLine` tworzyły zad. 1 i zad. 5 → zduplikowane `id` w DOM. Zad. 5 ma teraz `solutionInteractive: null`, więc drugi canvas się nie renderuje.
- Zadanie: tylko potwierdź, że żadne inne zadanie nie tworzy drugiego `#numberLine`. Jeśli w przyszłości wróci widżet w innym zadaniu — użyj **klasy** (`.numberLine`) zamiast `id`, bo `id` musi być unikalny. Możesz to odhaczyć jako zrobione po weryfikacji.

---

## Poza zakresem Fazy 1 (NIE rób tutaj — osobne fazy)
- **Faza 2:** `maxTotalScore` jest na sztywno `7`, a realna suma `maxScore` to ~49. Docelowo liczyć z danych: `const maxTotalScore = exercises.reduce((s,e)=>s+(e.maxScore||0),0)`. Zrobić dopiero po ustaleniu poprawnych `maxScore`.
- **Faza 3:** migracja `exercises.js` → `exercises.json` (wymaga wyniesienia funkcji `solutionInteractive` do rejestru widżetów i wygenerowania numerów zadań w JS zamiast wklejania w treść).
- Wszystkie punkty „design/wygląd" i „na potem" są w `todo.md`.
