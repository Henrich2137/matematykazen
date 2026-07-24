# Toggle "widoczność zegara: włączony/wyłączony" w menu ⋯

**Status:** NIE zrobione.

## Ustalenia

- Nowy przycisk w `#bar-menu` (`template.html:81-90`), wzorowany na istniejącym `#natychmiastowa-toggle` (`app/bootstrap.js:70-91`): klik przełącza etykietę i zapisuje stan.
- **Zapis globalny w localStorage** (bez sufiksu `SHEET_ID`, tak jak `KLUCZ_NATYCHM_POPRAWNOSC` w `app/state.js`) — ustawienie ma przetrwać odświeżenie i dotyczyć wszystkich arkuszy, spójnie z resztą toggle'i w menu.
- Toggle steruje samą **widocznością** `#egzamin-timer` (`template.html:68`, wypełniany w `app/exam.js`) — licznik ma dalej tykać i kończyć egzamin po czasie w tle, tylko span ma być `display: none`.

## Mechanizm

- Dodać klucz np. `KLUCZ_ZEGAR_WIDOCZNY` w `app/state.js` obok `KLUCZ_NATYCHM_POPRAWNOSC`.
- Dodać `<button id="zegar-toggle">` w `#bar-menu`.
- W `app/exam.js` (obok `tickExam` / miejsca, gdzie `egzaminTimerSpan` jest aktualizowany, `exam.js:16,34`): funkcja `odswiezWidocznoscZegara()` ustawiająca `egzaminTimerSpan.style.display` i etykietę przycisku, wołana raz na starcie i po kliknięciu — analogicznie do `odswiezTrybPoprawnosci()` w `app/bootstrap.js:75-91`.

## Pliki

- `app/state.js` (nowy klucz localStorage)
- `app/exam.js:16,34` (`egzaminTimerSpan`, `tickExam`)
- `template.html:68,81-90` (span zegara, menu)