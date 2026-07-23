# Dwie karty tego samego arkusza blokują "zakończ egzamin"

**Status:** NIE naprawione (zgłoszone 2026-07-22, Sonnet) — wymaga większej przebudowy niż drobna poprawka.

## Mechanizm awarii

1. Użytkownik otwiera ten sam arkusz w dwóch kartach (A i B), obie w trybie egzaminu.
2. Karta A kończy egzamin: usuwa klucz `KLUCZ_EGZAMINU` z localStorage.
3. Karta B nic o tym nie wie — zostaje na zawsze w `body.tryb-egzaminu`.
4. Kliknięcie "zakończ egzamin" w karcie B wywołuje `finishExam()` w script.js, która na starcie robi `if (!stan) return;` — `stan` jest `null` (bo klucz już usunięty przez kartę A), więc funkcja wychodzi natychmiast.
5. Efekt: zegar w karcie B stoi, rozwiązania/punkty są ukryte, przycisk "zakończ egzamin" nic nie robi i nie pokazuje żadnego komunikatu błędu. Jedyny ratunek to ręczne odświeżenie strony.

## Dlaczego to się dzieje

Stan trybu egzaminu trzymany jest tylko w localStorage; karty nie nasłuchują zmian tego stanu między sobą, więc karta B renderuje UI na podstawie własnej pamięci (`body.tryb-egzaminu` ustawione przy starcie), a nie aktualnego localStorage.

## Możliwe kierunki naprawy

- Nasłuch zdarzenia `storage` w script.js — gdy `KLUCZ_EGZAMINU` zniknie/zmieni się w innej karcie, karta B powinna zareagować (np. sama zakończyć/zresetować widok, albo pokazać komunikat "egzamin zakończony w innej karcie").
- Alternatywnie: inna architektura synchronizacji stanu między kartami (np. `BroadcastChannel`).
- `finishExam()` powinna przynajmniej dać użytkownikowi jakiś feedback zamiast cichego `return`, niezależnie od wybranego rozwiązania.

## Powiązane, już naprawione

Dwie mniejsze poprawki z tej samej okolicy zostały już zrobione — patrz `DONE/03-biezace.md`:
- nieudany start egzaminu kasujący postęp,
- "resetuj punktację" niekasujące trwającego egzaminu.

## Pliki

- `script.js` — `finishExam()`
