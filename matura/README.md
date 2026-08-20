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
| `2026-maj` | 5 maja 2026 | matura właściwa | MMAP-P0-100-2605 | wpięty — 33 zadania, wszystkie rysunki wstawione, odpowiedzi zamknięte zgodne z kluczem CKE (2026-08-20); podpowiedzi i rozwiązania powstają zadanie po zadaniu |

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

## Robisz nowy ekstrakt `.txt`? Wyrównaj go do lewej (2026-08-15)

**Zdejmij wspólny lewy margines, ZANIM zapiszesz plik.** To część tworzenia ekstraktu,
nie sprzątanie „kiedyś".

`pdftotext -layout` zachowuje układ kolumn ze strony, a arkusze CKE mają treść w wąskiej
kolumnie po prawej — więc **każda linia zaczyna się od ~50 spacji**, które nic nie znaczą
i za które płaci każdy model przy każdym czytaniu. W czterech istniejących plikach było to
**44% objętości**: 360 kB → 202 kB po wyrównaniu.

Narzędzie: **[tools/wyrownaj-transkrypt.py](../tools/wyrownaj-transkrypt.py)**

```
python3 tools/wyrownaj-transkrypt.py matura/<id>/arkusz.txt     # nadpisuje w miejscu
python3 tools/wyrownaj-transkrypt.py --sucho <plik>             # tylko pokaż wynik
```

Trzy rzeczy, które ono robi dobrze — powtórz je, gdyby ktoś pisał to od nowa:

- **Zdejmuje wspólny margines, nie kasuje wcięć.** Wcięcia względne niosą strukturę
  (podpunkty pod „2 pkt –", wypunktowania, wyrównanie „ALBO") i muszą zostać.
- **Margines liczy z najczęstszego wcięcia, nie z minimum.** W plikach są linie spoza
  głównej kolumny — watermark „arkusze.pl" wdrukowany pionowo z boku strony i nagłówek
  bieżący siedzą na pozycji 0, więc minimum zaniżyłoby margines do zera, czyli do braku
  jakiejkolwiek zmiany.
- **Działa na bajtach, nie na tekście.** Ekstrakty bywają w różnych kodowaniach
  (`2024-grudzien` jest w **cp1250**, `2026-maj` w **UTF-8**). Wcięcia to spacje ASCII,
  więc operacja bajtowa daje ten sam wynik bez ryzyka rozsypania polskich znaków przy
  zapisie. Nie zakładaj UTF-8 przy czytaniu tych plików.

Po przetworzeniu skrypt sam sprawdza, że plik po usunięciu wszystkich białych znaków jest
bajt w bajt taki sam jak przed — czyli że treść jest nietknięta. Kopii nie robi, historię
trzyma git.

**Nie przepisuj takiego pliku modelem.** To źródło prawdy o poprawności matematycznej,
a przepisywanie dwóch tysięcy linii wzorów CKE może cicho przekręcić znak albo indeks.
Czyszczenie ma być skryptem z automatyczną weryfikacją.

### Czego skrypt NIE usuwa

Watermarku „Więcej arkuszy znajdziesz na stronie: arkusze.pl", stopek („Strona X z 42")
ani nagłówków bieżących — to osobna decyzja i osobna zmiana. Powody:

- **stopka** niesie orientację w arkuszu i przydaje się przy odsyłaniu do strony PDF-a;
- **watermark** w arkuszu `2024-grudzien` bywa **sklejony z treścią w jednej linii**
  (`"…arkusze.pl  Zasady oceniania"`), więc kasowanie całych linii gubiłoby treść;
- największa bezużyteczna pozycja po marginesie to **tabele „Wymaganie ogólne /
  szczegółowe"** (20% pliku, 327 linii w `2026-maj/odpowiedzi.txt`) — mapują zadanie na
  numer w podstawie programowej, co przy pisaniu podpowiedzi i rozwiązań nie jest do
  niczego potrzebne. Nikt ich jeszcze nie wycinał.

Zmierzone udziały w `2026-maj/odpowiedzi.txt` przed wyrównaniem: margines 59,6%,
sekcje „Uwagi:" 43,9% (**zostawić — to materiał na `gradingCriteria`**), tabele
„Wymagania" 20,2%, kursywa unicode 𝑛/𝑘 2,8%, stopki 2,7%, nagłówek bieżący 1,7%,
strona tytułowa 1,7%, watermark 1,3%. Pozycje się nakładają, nie sumuj ich.
