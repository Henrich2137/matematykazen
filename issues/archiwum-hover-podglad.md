# Archiwum: hover-podgląd „wartość → następna" w panelu ustawień

**Status:** usunięte 2026-08-10 na życzenie Henricha (v14 wprowadziła hover, ale
w praniu chowanie aktualnej wartości pod najechaniem myszą odejmowało
intuicyjności — nie było widać, na czym się aktualnie stoi, dopóki się nie
najechało). Zastąpione: `.wartosc` widoczne cały czas, hover nic już tam nie
zmienia. Nie kasować tego pliku bez potrzeby — to jedyna ścieżka powrotna do
kodu, gdyby ktoś chciał hover przywrócić.

Dotyczyło przycisków `.sidebar-ustawienie` (Zegar, Wskaźniki, Motyw,
Punktacja, Poprawność, Zgłoś błąd) — patrz spec
`docs/superpowers/specs/2026-08-09-paczka-ui-drobiazgi-design.md`, punkt 1.

## Usunięty kod

### `app/state.js` — `ustawWartosc()`

```js
const podglad = btn.querySelector(".wartosc-podglad");
if (podglad) {
    const nast = nastepnyStan(btn);
    podglad.textContent = nast ? `${wartosc} → ${nast}` : wartosc;
}
```

### `template.html` — po każdym `<span class="wartosc">...</span>` w
`.sidebar-ustawienie` (6 wystąpień: `#zegar-toggle`, `#wskazniki-tryb-toggle`,
`#theme-toggle`, `#score-switch-button`, `#natychmiastowa-toggle`,
`#zglos-blad-toggle`)

```html
<span class="wartosc-podglad" aria-hidden="true"></span>
```

### `style/sheet.css`

```css
.sidebar-ustawienie .wartosc,
.sidebar-ustawienie .wartosc-podglad {
    font-size: 12px;
    white-space: nowrap;
    color: var(--text);
    font-weight: 400;
}
.sidebar-ustawienie .wartosc-podglad {
    display: none;
    font-size: 12px;
    font-weight: 400;
    color: var(--text-faint);
}
/* Podgląd „auto → jasny" po najechaniu — TYLKO na wskaźnikach z hoverem.
   Na dotyku ta reguła w ogóle się nie stosuje, dlatego o stanie informują
   przede wszystkim wartość i kropki. */
@media (hover: hover) {
    .sidebar-ustawienie:hover:not(:disabled) .wartosc {
        display: none;
    }
    .sidebar-ustawienie:hover:not(:disabled) .wartosc-podglad {
        display: inline;
    }
}
```

oraz w bloku sub-opcji:

```css
.sidebar-ustawienie.sidebar-sub .wartosc,
.sidebar-ustawienie.sidebar-sub .wartosc-podglad {
    font-size: 11px;
}
```

## Jak przywrócić

1. Wklej z powrotem powyższy CSS i HTML.
2. W `app/state.js` w `ustawWartosc()` przywróć blok `podglad` (funkcja
   `nastepnyStan()` nigdzie nie została usunięta — jest dalej używana przez
   sam cykl kliknięć w kilku plikach `app/*.js`, więc jest gotowa do użycia).
