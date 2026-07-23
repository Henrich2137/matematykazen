# Obrazki CKE i wideo z Manima świecą na biało w dark mode

**Status:** NIE naprawione.

## Problem

Migracja dark mode świadomie przypięła `--canvas-bg: #fff` dla płócien widgetów (to jest celowe — widgety matematyczne muszą mieć białe tło). Ale nikt nie dodał żadnej reguły tła/filtra dla:

- `.question img` (`style/sheet.css:293`),
- obrazków kroków rozwiązania,
- elementów `<video>`.

Wszystkie PNG pod `matura/**/` są nieprzezroczyste białe, więc w dark mode renderują się jako jaskrawe białe prostokąty na karcie o tle `#1b1b1b`.

## Kierunek naprawy

- CSS: dodać np. lekkie przyciemnienie/`filter` (typu `filter: brightness(.85) contrast(1.1)` lub podobne) na `.question img`, obrazkach kroków i `<video>` w trybie dark — punkt startowy, wymaga wizualnej kalibracji.
- Alternatywa (większy nakład): re-render PNG/MP4 z ciemnym tłem u źródła — nierealne dla CKE PNG (oficjalne materiały), ale możliwe dla własnych wideo z Manima (patrz TODO.md → "DLA HENRICHA" → przerenderowanie w Manimie).

## Pliki

- `style/sheet.css:293` (`.question img`)
- pliki `matura/**/media/**/*.png`, `*.mp4`
