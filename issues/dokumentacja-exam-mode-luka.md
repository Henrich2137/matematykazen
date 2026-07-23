# ARCHITECTURE.md nie opisuje połowy trybu egzaminu

**Status:** NIE naprawione.

## Problem

Sekcja "Exam mode" w `ARCHITECTURE.md` (~linia 80) opisuje kończenie egzaminu wyłącznie przez `#egzamin-koniec` i wymienia tylko dwa klucze localStorage. W kodzie jest więcej:

- brakuje `#egzamin-koniec-bar`,
- brakuje `#egzamin-start-stopka`,
- brakuje trzeciego klucza localStorage `KLUCZ_OCENIANIA`,
- brakuje całej fazy "oceń się" ze wskaźnikami (`.wskaznik-otwarte` i towarzyszący mechanizm).

Lista ID w komentarzu "referenced by the inline JS, so keep the IDs stable" (`ARCHITECTURE.md` ~linia 97) nie zawiera `#egzamin-koniec-bar` ani `#theme-toggle` — ryzyko, że ktoś restylujący pasek skasuje te elementy jako rzekomo niepodpięte.

## Dark mode — dla kontrastu

Dark mode jest udokumentowany wzorowo w tym samym pliku — to punkt odniesienia co do poziomu szczegółowości, jaki powinna mieć sekcja "Exam mode".

## Kierunek naprawy

- Uzupełnić sekcję "Exam mode" w `ARCHITECTURE.md` o: `#egzamin-koniec-bar`, `#egzamin-start-stopka`, `KLUCZ_OCENIANIA`, fazę "oceń się".
- Dodać brakujące ID (`#egzamin-koniec-bar`, `#theme-toggle`) do listy "stable IDs referenced by inline JS".

## Pliki

- `ARCHITECTURE.md` (~linia 80 sekcja "Exam mode", ~linia 97 lista stabilnych ID)