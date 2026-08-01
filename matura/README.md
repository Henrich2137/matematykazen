# matura/

Arkusze egzaminacyjne CKE — jeden katalog na arkusz. Nazwa katalogu (`<id>`) jest
jednocześnie wartością parametru URL `?arkusz=<id>`, którym `template.html` wybiera,
co wyrenderować.

## Co to za egzamin

Wszystkie arkusze tutaj to **matura z matematyki na poziomie podstawowym, Formuła 2023**,
wydane przez **CKE** (Centralną Komisję Egzaminacyjną). Czas trwania: 180 minut, 50 punktów
do zdobycia (potwierdzone w nagłówkach obu arkuszy: „LICZBA PUNKTÓW DO UZYSKANIA: 50").
To egzamin obowiązkowy dla każdego maturzysty — próg zdania to 30%.

Dwa rodzaje arkuszy trafiają do tego katalogu:
- **matura właściwa** — arkusz z rzeczywistej sesji egzaminacyjnej (maj / czerwiec / sierpień),
- **matura próbna** (CKE nazywa je „test diagnostyczny") — arkusz udostępniany przez CKE
  zwykle w grudniu, żeby uczniowie i szkoły sprawdzili poziom przygotowania. Ma tę samą
  strukturę i tę samą formułę co właściwa, nie liczy się do wyniku matury.

„Formuła 2023" to obowiązujący od 2023 r. wariant egzaminu (nowa podstawa programowa) —
arkusze w starej Formule 2015 mają inną strukturę i **nie pasują** do tego katalogu bez
osobnego przemyślenia schematu danych.

## Arkusze

| `<id>` | Sesja | Rodzaj | Symbol arkusza | Status |
|---|---|---|---|---|
| `2024-grudzien` | 6 grudnia 2024 | próbna (test diagnostyczny) | MMAP-P0-100-2412 | wpięty — 30 zadań, odpowiedzi zweryfikowane z kluczem CKE (2026-07-05) |
| `2025-maj` | maj 2025 | matura właściwa | — | **niewpięty** — same PDF-y, brak `exercises.json` |
| `2026-maj` | 5 maja 2026 | matura właściwa | MMAP-P0-100-2605 | wpięty — 33 zadania; część grafik jeszcze do wycięcia z PDF-a |

## Zawartość katalogu arkusza

Cztery stałe nazwy plików źródłowych — **takie same w każdym arkuszu**, żeby ścieżkę dało się
złożyć z samego `<id>`, bez listowania katalogu:

| plik | co to |
|---|---|
| `arkusz.pdf` | oficjalny arkusz egzaminacyjny CKE |
| `arkusz.txt` | jego ekstrakt tekstowy (`pdftotext -layout`) — do czytania przez model |
| `odpowiedzi.pdf` | oficjalne zasady oceniania / klucz odpowiedzi CKE; to jego pokazuje panel „zasady oceniania" (`meta.zasadyPdf`) |
| `odpowiedzi.txt` | ekstrakt tekstowy klucza |

Plus dane platformy:

| plik / katalog | co to |
|---|---|
| `exercises.json` | treść zadań, podpowiedzi i rozwiązania — schemat opisany w [ARCHITECTURE.md](../ARCHITECTURE.md) |
| `media/zadN/` | grafiki (PNG) i animacje rozwiązań z Manima (MP4), jeden katalog na numer zadania |

Arkusz bez `exercises.json` jest „niewpięty" — leży tu jako materiał źródłowy, ale
`?arkusz=<id>` go nie wyrenderuje i nie ma go na stronie głównej.

Pliki `.txt` bywają niekompletne (dla `2025-maj` ich w ogóle nie ma) — to ekstrakty robione
w miarę potrzeby, nie wymóg. Ścieżki w `exercises.json` są **względne do katalogu arkusza**
i sklejane z nim przez `mediaPath()` w [app/state.js](../app/state.js) — nie wpisuj
`matura/<id>/` do danych.
