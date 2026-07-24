# Tablica wzorów ma się automatycznie wyłączać po zakończeniu egzaminu

**Status:** NIE zrobione.

## Problem

Panel tablicy wzorów (`#tablica-wzorow-panel`, pokazywany/chowany przez `showFormulasPanel()`/`hideFormulasPanel()` w `app/panels.js:9-16`) nie jest automatycznie zamykany, gdy egzamin się kończy — jeśli był otwarty w trakcie egzaminu, zostaje otwarty także w fazie "oceń się".

## Mechanizm

- W `finishExam()` (`app/exam.js:120-...`), przy przełączaniu trybu (`document.body.classList.remove("tryb-egzaminu")`, `exam.js:125`), dodać wywołanie `hideFormulasPanel()` jeśli panel jest aktualnie otwarty (`tablicaPanel.style.display === "block"`). `hideFormulasPanel` jest globalną funkcją zdefiniowaną w `panels.js` — mimo że wg CLAUDE.md `exam.js` ładuje się PRZED `panels.js`, to nie problem: `finishExam()` wykonuje się dopiero po kliknięciu użytkownika, czyli długo po tym, jak wszystkie skrypty już się załadowały i zdefiniowały swoje funkcje.

## Pliki

- `app/exam.js` (`finishExam`)
- `app/panels.js:9-16` (`hideFormulasPanel`)