# Dark/light mode niespójny między kartami przeglądarki

**Status:** NIE naprawione. Niski priorytet.

## Problem

`readTheme()` czyta motyw z localStorage zamiast stanu, który dana karta faktycznie renderuje, a nikt nie nasłuchuje zdarzenia `storage`. Efekt: dwie karty tego samego arkusza potrafią pokazywać różny motyw i różne etykiety przycisku przełącznika motywu jednocześnie.

To ten sam rodzaj problemu co [dwie-karty-tryb-egzaminu.md](dwie-karty-tryb-egzaminu.md) — brak synchronizacji stanu między kartami przez `storage`/`BroadcastChannel`. Jeśli robisz ogólne rozwiązanie tego problemu, rozważ załatwienie obu na raz.

## Kierunek naprawy

- Nasłuch `storage` na klucz motywu, żeby karta zaktualizowała UI (klasę na `body`, etykietę `#theme-toggle`) gdy motyw zmieni się w innej karcie.

## Pliki

- `script.js` — `readTheme()`, `#theme-toggle`