# Landing page używa niewłaściwych zmiennych CSS (kontrast WCAG)

**Status:** NIE naprawione.

## Problem

Dwie zmienne CSS na stronie głównej (`index.html` / `style/landing.css`) są użyte niezgodnie z ich przeznaczeniem — pożyczają tokeny zaprojektowane dla paneli PDF, przez co landing page jest przypadkowo sprzężony ze stylem krzyżyka paneli.

1. **`.landing-footer`** (`style/landing.css:90`) bierze kolor tekstu z `--border-close` — tokena ramki krzyżyka zamykającego panele PDF. Jego ciemna wartość to `#666` na tle `#1b1b1b`, czyli kontrast **3.0:1** — poniżej progu WCAG AA **4.5:1** dla tekstu 13px. Powinien iść przez `--text-faint-*`.

2. **`.landing-card`** (`style/landing.css:63`) bierze ramkę z `--bg-hover` — tokena tła stanu hover. Powinna iść przez jeden z tokenów `--border*`.

## Skutek uboczny

Ktoś przestrajający wygląd krzyżyka paneli PDF (`--border-close`) lub hover (`--bg-hover`) po cichu zmieni też wygląd strony głównej — a testowany przy takiej zmianie będzie panel, nie landing, więc regresja na landing page przejdzie niezauważona.

## Kierunek naprawy

- `.landing-footer` → kolor tekstu przez `--text-faint-*` (sprawdzić dokładną nazwę tokenu w `style/base.css`).
- `.landing-card` → ramka przez odpowiedni `--border*` token.

## Pliki

- `style/landing.css:90` (`.landing-footer`)
- `style/landing.css:63` (`.landing-card`)
- `style/base.css` (definicje zmiennych `--text-faint-*`, `--border*`)
