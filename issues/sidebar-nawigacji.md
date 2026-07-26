# Sidebar nawigacji zamiast okienka „⋯"

Status: do zrobienia. Spec ustalony z Henrichem 2026-07-26 (Sesja 2).
Robione RAZEM z [likwidacja-top-bara.md](likwidacja-top-bara.md) — to jedna zmiana layoutu podzielona
na dwa pliki tematycznie. Sesja lokalna (nie cloud): wymaga iteracji wizualnej.

## Czego dotyczy

Dziś wszystkie rzadsze akcje siedzą w `#bar-menu` — okienku wypadającym spod przycisku `⋯`
przy prawej krawędzi paska (`template.html` ~161–182, `style/sheet.css` 133–162, obsługa
`app/bootstrap.js` 8–18). Menu ma dziś 13 przycisków w przypadkowej kolejności, bez grup i bez ikon.

Zastępujemy je wysuwanym panelem bocznym po LEWEJ, otwieranym strzałką tuż obok logo.

## Zachowanie (ustalone, nie zmieniać bez pytania)

- **Otwieranie/zamykanie**: jeden przycisk-strzałka po prawej od `#logo`. Ten sam przycisk zamyka
  (strzałka obraca się ◀ ↔ ▶). Dodatkowo `Esc` zamyka.
- **Arkusz się NIE rusza** — panel to nakładka, żadnego `transform`/zwężania kolumny zadań.
- **Bez przyciemnienia tła na desktopie.** Panel jest wąski i mieści się w lewym marginesie,
  więc nic nie zasłania — nie ma czego przygaszać.
- **Poniżej progu** (patrz niżej) panel nachodzi na kartę zadania. Wtedy — i tylko wtedy —
  dochodzi lekkie przyciemnienie treści (`rgba(0,0,0,.25)`, bez blura) oraz zamykanie
  kliknięciem w arkusz. Powyżej progu klik w arkusz NIE zamyka panelu.
- **Warstwy**: panel musi być nad panelami PDF. Dzisiejsze `z-index`: karty/treść 1–4,
  `.wskaznik-otwarte` 8, `#tablica-wzorow-panel`/`#zasady-oceniania-panel` 9, `#top-bar` 10,
  `#bar-menu` 11, `#egzamin-podsumowanie` 20, toast zgłoszeń 22 (`style/sheet.css:1241`).
  Sidebar → **`z-index: 12`**, przyciemnienie → 11. Podsumowanie egzaminu i toast zostają nad nim.
- **Stan otwarcia nie jest zapamiętywany** między odświeżeniami — domyślnie zamknięty.
  (Świadomie: panel jest do sporadycznych akcji, nie do stałego trzymania.)

### Próg „panel zasłania treść"

Karta zadania ma `width: 650px + padding 50px` = **750 px** (`style/sheet.css:261`).
Przy panelu 260 px + 16 px odstępu margines wystarcza od `(750/2 + 276) × 2` ≈ **1300 px**.

- `min-width: 1300px` → panel w marginesie, bez przyciemnienia, klik w arkusz nie zamyka.
- `max-width: 1299px` → panel nad treścią, lekkie przyciemnienie, klik w arkusz zamyka.
- `max-width: 560px` → panel pełnoekranowy (te same reguły co wyżej; szerokość `100%`,
  bo 260 px na 360-px ekranie i tak zasłania wszystko, a pełna szerokość daje czytelne pozycje).

Progi wpisać do `style/responsive.css` (ładowany OSTATNI — kolejność kaskady, patrz CLAUDE.md).

## Kolejność i nazwy pozycji

```
  Grudzień 2024                    ← nagłówek panelu, NIE przycisk (tytuł arkusza z meta.sheetTitle)
  ─────────────────────────────
  📐  Otwórz tablicę wzorów
  📋  Otwórz zasady oceniania
  ▶   Rozpocznij egzamin            ← w trakcie egzaminu: „Zakończ egzamin"
        Zegar               na wierzchu ●○
        Wskaźniki samooceny   wszystkie ●○○
  ✓   Sprawdź wszystkie odpowiedzi
  👁   Pokaż wszystkie rozwiązania
  ↺   Zresetuj arkusz
  ─────────────────────────────    ← cienka kreska 1 px, BEZ nagłówka sekcji
  ◐   Motyw                     auto ●○○
  #   Punktacja             wszystko ●○○
  ⚡  Poprawność odpowiedzi natychmiast ●○
  ⚠  Zgłoś błąd pod zadaniem     wł. ●○
```

- Sub-opcje zegara i wskaźników są **zawsze widoczne**, wcięte, mniejszym fontem — nie zwijają się.
- **Nie dodawać do panelu wskaźnika ani przełącznika trybu** ćwiczenia/egzamin — świadoma decyzja
  (2026-07-26): przełącznik żyje pod tytułem arkusza, patrz „Przełącznik trybu"
  w [likwidacja-top-bara.md](likwidacja-top-bara.md). W panelu jest tylko akcja
  „Rozpocznij / Zakończ egzamin", żeby nie było dwóch wejść do tego samego stanu.
- Nagłówek panelu bierze tytuł z `applySheetMeta()` (`app/bootstrap.js:122`), tego samego pola co
  `#sheet-title-heading`.

## Mapowanie na istniejące ID (nie zmieniać ID!)

Cała logika w `app/*.js` woła `getElementById` — **przenosimy przyciski, zostawiamy ID**,
inaczej sypie się `theme.js`, `exam.js`, `indicators.js`, `panels.js`, `report.js`, `bootstrap.js`.

| Pozycja w sidebarze | ID | Gdzie obsługa |
|---|---|---|
| Otwórz tablicę wzorów | `#toggle-tablica` | `app/panels.js` |
| Otwórz zasady oceniania | `#toggle-zasady` | `app/panels.js` |
| Rozpocznij egzamin | `#egzamin-start` | `app/exam.js` |
| Zakończ egzamin | `#egzamin-koniec-menu` | `app/exam.js` |
| Zegar | `#zegar-toggle` | `app/exam.js` |
| Wskaźniki samooceny | `#wskazniki-tryb-toggle` | `app/indicators.js` |
| Sprawdź wszystkie odpowiedzi | `#sprawdz-wszystkie` | `app/bootstrap.js:113` |
| Pokaż wszystkie rozwiązania | `#show-all-solutions` | `app/bootstrap.js:235` |
| Zresetuj arkusz | `#reset-scores` | `app/bootstrap.js:22` |
| Motyw | `#theme-toggle` | `app/theme.js` |
| Punktacja | `#score-switch-button` | `app/bootstrap.js:39` |
| Poprawność odpowiedzi | `#natychmiastowa-toggle` | `app/bootstrap.js:85` |
| Zgłoś błąd pod zadaniem | `#zglos-blad-toggle` | `app/report.js` |

Uwaga na `style/exam.css:17–40`: reguły trafiają w te przyciski selektorem `#bar-menu #egzamin-start`
(podwójne ID celowo, dla specyficzności nad `#bar-menu button`). Po zmianie kontenera na
`#sidebar` trzeba te selektory przepisać — inaczej „rozpocznij egzamin" straci wyszarzenie
przed wczytaniem arkusza i przełączanie start/koniec przestanie działać.

### Zmiany etykiet (tylko tekst, logika bez zmian)

- `resetuj punktację` → **`Zresetuj arkusz`**. Zakres działania BEZ ZMIAN (kasuje `KLUCZ_POSTEPU`,
  `KLUCZ_OCENIANIA`, `KLUCZ_EGZAMINU` + reload). Tekst `confirm()` w `app/bootstrap.js:23`
  dopasować do nowej nazwy.
- `widok punktów: …` → **`Punktacja: wł. / tylko suma / wył.`** — uwaga, `bootstrap.js:42–57`
  porównuje `innerHTML` przycisku ze stringiem, żeby wiedzieć, w którym stanie jest.
  Przy zmianie tekstu **trzeba przepisać ten cykl na `data-stan`** (i tak jest kruchy, a z ikoną
  w środku przycisku `innerHTML` przestanie się zgadzać całkowicie).
- `pokazuj poprawność od razu: tak/nie` → `Pokaż poprawność odpowiedzi: natychmiast / po kliknięciu „sprawdź"`
  (`bootstrap.js:90–92`).
- `pokaż wszystkie rozwiązania` → `Pokaż wszystkie rozwiązania` / `Schowaj wszystkie rozwiązania`
  (`bootstrap.js:244` ustawia `textContent` — z ikoną trzeba pisać do wewnętrznego `<span>`,
  nie do całego przycisku).
- `wskaźniki „oceń się"` → `Wskaźniki samooceny zad. otwartych` (`app/indicators.js`).

## Dwa typy pozycji (ustalone 2026-07-26)

Panel ma ~260 px, minus padding i ikona zostaje **~200 px na tekst** (≈30 znaków przy 13 px) —
dlatego segmented control z trzema podpisami odpada, a etykiety ustawień są SKRÓCONE
(„Poprawność odpowiedzi", nie „Pokaż poprawność odpowiedzi: natychmiast / po kliknięciu…").

### Akcja — czasownik, klikalny przycisk

`[ikona] Otwórz tablicę wzorów` — pełna szerokość, hover z tłem `--bg-muted`, tekst w `--text`.

### Ustawienie — rzeczownik + aktualny stan, cykl

```html
<button id="theme-toggle" class="sidebar-ustawienie"
        data-stan="auto" data-stany="jasny,ciemny,auto">
  <svg …/><span class="etykieta">Motyw</span>
  <span class="wartosc">auto</span><span class="kropki" aria-hidden="true"></span>
</button>
```

- **Kolor**: żadnego akcentu. Etykieta `--text-faint-2`, wartość `--text` + `font-weight: 600`.
  Świadoma decyzja: `--accent-blue-strong` (#4a90d9) znaczy już „Twój wybór w zadaniu"
  (ABCD, widżety), a zielony/czerwony to poprawność — kolor w menu konkurowałby ze znaczeniem
  z treści. Dodatkowo kontrast działa w obu motywach bez dobierania nowych zmiennych.
- **Kropki stanu** (`●○○`) po prawej: ile stanów ma przełącznik i który jest aktywny.
  Generowane z `data-stany`, nie wpisywane ręcznie. `aria-hidden` — dla czytnika ekranu
  wystarczy tekst wartości (dodać `aria-live="polite"` na `.wartosc`).
  To ONE rozwiązują cykl na telefonie: bez nich tapnięcie jest klikaniem w ciemno.
- **Hover-podgląd tylko na desktopie**: pod `@media (hover: hover)` po najechaniu wartość
  pokazuje `auto → jasny`. Na dotyku ta reguła w ogóle się nie stosuje.
- **Kolejność stanów — jedna zasada dla wszystkich**: lewo = stan domyślny (najbogatszy),
  kolejne kliknięcia idą w prawo, ostatni = wyłączone. Kropka wędruje zawsze w prawo i zawija
  na początek. Dzięki temu pierwsza kropka zawsze znaczy „tak jak było na starcie".
  Konwencja przełącznika ON/OFF (lewo = off) tu NIE obowiązuje — to cykl, nie suwak.

  | Ustawienie | `data-stany` |
  |---|---|
  | Motyw | `auto,jasny,ciemny` (tak jak dziś `MOTYWY` w `app/theme.js:10`) |
  | Punktacja | `wszystko,tylko suma,wył.` |
  | Poprawność odpowiedzi | `natychmiast,po „sprawdź"` |
  | Zgłoś błąd pod zadaniem | `wł.,wył.` |
  | Zegar | `na wierzchu,wył.` |
  | Wskaźniki samooceny | `wszystkie,wypełnione,wył.` |

  Motyw jest wyjątkiem od „więcej → mniej" (nie jest skalą) — rządzi nim samo „domyślny pierwszy".
  TODO.md ma w tym miejscu zapisane „jasny/ciemny/auto"; obowiązuje kolejność z kodu.
- Ten sam wzorzec dla sub-opcji egzaminu (Zegar — 2 stany, Wskaźniki — 3), tylko mniejszy
  font i wcięcie. Nie robić z nich osobnego typu kontrolki.
- **Separacja akcji od ustawień**: cienka kreska 1 px (`--separator`), bez nagłówka sekcji
  i bez pustej przerwy.

**Wzorzec dla wszystkich toggle'ów z ikoną**: JS pisze do `.wartosc` (i przestawia `data-stan`),
NIGDY do `textContent` całego przycisku — inaczej pierwszy zapis skasuje ikonę, etykietę i kropki.
Dotyczy to `bootstrap.js:42–57` (dziś porównuje `innerHTML` ze stringiem), `bootstrap.js:90`,
`bootstrap.js:244`, `theme.js`, `exam.js` (zegar), `indicators.js`, `report.js`.
`data-stan` jest jedynym źródłem prawdy o pozycji w cyklu.

## Ikony

Inline SVG w `template.html` (kreskowe, `stroke: currentColor`, `stroke-width: 1.5`, viewBox 24×24,
render 20×20) — zero plików, działa offline, dziedziczy kolor motywu. Henrich nic nie przygotowuje.
Emoji w szkicu wyżej to tylko oznaczenia — w kodzie mają być SVG.

## Kryteria akceptacji

- [ ] Żadne ID przycisku się nie zmieniło; wszystkie 13 funkcji działa jak przed zmianą.
- [ ] Panel otwiera się i zamyka tą samą strzałką; `Esc` zamyka.
- [ ] ≥1300 px: panel nie dotyka karty zadania, brak przyciemnienia, klik w zadanie nie zamyka.
- [ ] <1300 px: przyciemnienie + klik w arkusz zamyka.
- [ ] Panel rysuje się NAD otwartą tablicą wzorów i zasadami oceniania.
- [ ] Arkusz nie drgnie ani o piksel przy otwieraniu (sprawdzić pozycję pierwszej karty).
- [ ] Tryb egzaminu: pozycja przełącza się na „Zakończ egzamin", wyszarzenia z `exam.css` działają.
- [ ] Motyw ciemny: panel, ikony i separator mają kontrast (nie białe tło).
- [ ] Każde ustawienie pokazuje wartość i kropki stanu; kropki zgadzają się z `data-stany`.
- [ ] Po pełnym cyklu (klik × liczba stanów) etykieta, ikona i kropki są nienaruszone.
- [ ] Na telefonie (brak hovera) wartość i kropki nadal informują o stanie.
- [ ] Test na 360 px i 1920 px (Playwright + `python -m http.server`).
