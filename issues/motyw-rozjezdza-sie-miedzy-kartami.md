# Dark/light mode niespójny między kartami przeglądarki

**Status:** NIE naprawione. Niski priorytet.

## Problem

`readTheme()` czyta motyw z localStorage zamiast stanu, który dana karta faktycznie renderuje, a nikt nie nasłuchuje zdarzenia `storage`. Efekt: dwie karty tego samego arkusza potrafią pokazywać różny motyw i różne etykiety przycisku przełącznika motywu jednocześnie — zmiana motywu w karcie A nie propaguje się do karty B aż do ręcznego odświeżenia.

To ten sam rodzaj problemu co [dwie-karty-tryb-egzaminu.md](dwie-karty-tryb-egzaminu.md) — brak synchronizacji stanu między kartami przez `storage`/`BroadcastChannel`.

## Kierunek naprawy (zdecydowane 2026-07-24, przydzielone Sonnetowi)

Zakres celowo zawężony do samego motywu (bez ogólnego cross-tab helpera, żeby nie dotykać trybu egzaminu): w `app/theme.js` dodać `window.addEventListener("storage", e => { if (e.key === KLUCZ_MOTYWU) applyTheme(readTheme()); })`, żeby karta zaktualizowała klasę na `<html>` (`theme-light`/`theme-dark`) i etykietę `#theme-toggle`, gdy motyw zmieni się w innej karcie.

## Pliki

- `app/theme.js` — `readTheme()`, `applyTheme()`, `KLUCZ_MOTYWU` (= `"matematykazen-motyw"`), `#theme-toggle`