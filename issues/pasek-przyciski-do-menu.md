# Przyciski "pokaż tablice wzorów" i "pokaż zasady oceniania" — zawsze do menu ⋯

**Status:** NIE zrobione.

## Ustalenia

- Oba przyciski (`#toggle-tablica`, `#toggle-zasady`) mają zniknąć z górnego paska (`#bar-right` / `#bar-left` w `template.html:51-73`) i przenieść się do `#bar-menu` (`template.html:81-90`), obok istniejących pozycji menu.
- **Zawsze schowane, niezależnie od urządzenia** — nie robimy osobnego zachowania desktop/telefon, nie ma warunku na szerokość ekranu ani `pointer: coarse`. Prościej niż rozważane warianty (breakpoint / dotyk) — świadoma decyzja, żeby nie komplikować.
- To zastępuje osobny punkt "przyciski niemieszczące się na pasku trafiają do menu" (był w TODO) — uznany za zbędny, bo po tej zmianie na pasku i tak nie ma już nic, co mogłoby się nie zmieścić.

## Mechanizm

- Przenieść `<button id="toggle-tablica">` i `<button id="toggle-zasady">` z `#bar-left`/`#bar-right` do `#bar-menu` w `template.html`.
- `app/panels.js` odwołuje się do nich przez `getElementById` (linie 6-7, 32-33) — samo przeniesienie w DOM nie wymaga zmian w JS, dopóki ID zostają te same.
- Sprawdzić CSS w `style/sheet.css` / `style/responsive.css` — czy selektory stylujące te przyciski są przypięte do `#bar-left`/`#bar-right` (wtedy trzeba dorobić styl pod `#bar-menu`, spójny z resztą pozycji menu, np. `#natychmiastowa-toggle`).

## Pliki

- `template.html:51-73` (pasek), `template.html:81-90` (`#bar-menu`)
- `app/panels.js:1-40` (logika pokaż/schowaj, etykiety przycisków)
- `style/sheet.css`, `style/responsive.css` (style paska vs style menu)