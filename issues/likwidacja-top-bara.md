# Likwidacja `#top-bar` — pływające logo i klaster prawego górnego rogu

Status: do zrobienia. Spec ustalony z Henrichem 2026-07-26 (Sesja 2).
Robione RAZEM z [sidebar-nawigacji.md](sidebar-nawigacji.md).

## Czego dotyczy

`#top-bar` (`template.html` ~128–158, `style/sheet.css` 1–130) to `position: fixed` pasek na całą
szerokość z siatką `1fr auto 1fr`: logo | podtytuł trybu | zegar + suma + „zakończ egzamin" + `⋯`.
Znika w całości. To, co dziś w nim siedzi, zostaje pływającymi elementami bez wspólnego tła.

Przy okazji naprawia to zastany defekt: **`#top-bar` daje 13 px poziomego scrolla przy 360 px**
(pasek mierzy 373 px) — cała strona daje się przesuwać w bok. Wpis Sonneta z TODO.md,
osobnego issue nie ma; po tej zmianie znika razem z paskiem.

## Docelowy układ

```
 ┌──────────────────────────────────────────────────┐
 │ Matematyka Zen v0.05  ◀              12/46 pkt   │   ← ćwiczenia
 │                                                  │
 │              ┌────────────────┐                  │
 │              │   zadanie 1    │                  │
```

```
 │ Matematyka Zen v0.05  ◀   41:20 12/46 pkt ✕Zakończ│  ← egzamin
```

- **Lewy górny róg**: `#logo` + strzałka sidebara, `position: fixed`, bez tła i bez ramki paska.
- **Prawy górny róg**: `position: fixed`, `display: flex; gap`, elementy jako osobne „pigułki"
  (własne tło `var(--bg)`, ramka, `border-radius`) — nie jeden wspólny kontener wizualny.
  - poza egzaminem: **tylko `#total-score`**,
  - w egzaminie: `#egzamin-timer` + `#total-score` + `#egzamin-koniec-bar` obok siebie.
- `#bar-center` znika, ale wskaźnik trybu **nie** — przenosi się i zmienia w przełącznik
  (patrz „Przełącznik trybu" niżej).
- `#menu-button` (`⋯`) znika — zastępuje go strzałka przy logo (patrz drugi issue).

## Warstwy

Klaster i logo: **`z-index: 10`** — tyle co dziś `#top-bar`, czyli nad panelami PDF (9),
bez zmiany dzisiejszej hierarchii. Sidebar dostaje 12, przyciemnienie 11,
podsumowanie egzaminu 20, toast 22.

Uwaga: `#zasady-oceniania-panel` jest przypięty do **lewej** krawędzi (`left: 30px`,
`top: 100px`, `style/sheet.css:171+`) — czyli dokładnie tam, gdzie wychodzi sidebar.
Sidebar (z-index 12) ma go przykrywać, ale warto sprawdzić, czy uchwyt przesuwania panelu
nie zostaje pod spodem w połowie widoczny.

## Przełącznik trybu (ćwiczenia / egzamin)

Ustalone 2026-07-26. Dzisiejszy `#exercises-mode-subtitle` to bierny napis w środku paska
(`app/exam.js:83` — `updateModeSubtitle()` przepisuje go z klasy `body.tryb-egzaminu`).
Zamiast znikać razem z paskiem, staje się **segmented control pod tytułem arkusza**:

```
              Matura grudzień 2024          ← #sheet-title-heading (template.html:325)
           ┌────────────┬─────────┐
           │ ćwiczenia  │ egzamin │         ← nowy #tryb-przelacznik
           └────────────┴─────────┘
             ▲ aktywny
```

- Miejsce: `#exercises-wrapper`, zaraz po `<h1 id="sheet-title-heading">`. Element statyczny
  w `template.html` — `loadExercises()` dokleja zadania NA KONIEC wrappera, więc nagłówek
  i przełącznik zostają pierwszymi dziećmi (ten sam mechanizm co dziś dla `<h1>`).
- **Świadomie nie jest `position: fixed`** — scrolluje się z treścią. Za „zawsze widoczny"
  stan egzaminu odpowiada zegar w prawym klastrze; przełącznik jest punktem wejścia, nie HUD-em.
- Kliknięcie nieaktywnej połówki = te same funkcje co przyciski w panelu:
  `startExamPrompt()` / `finishExamPrompt()` (`app/exam.js:117` i `:139`). Oba mają `confirm()`,
  więc przełącznik nie zadziała natychmiast — to celowe, egzamin nie może wystartować przypadkiem.
  Po anulowaniu dialogu przełącznik musi wrócić do stanu poprzedniego (nie zostawiać
  „egzamin" podświetlonego).
- Stan czytany z `body.tryb-egzaminu` — `updateModeSubtitle()` zostaje, tylko przestawia
  klasę `.aktywny` na połówkach zamiast pisać `textContent`. Nazwę funkcji można zostawić
  albo zmienić na `updateModeSwitch()` — wołana jest w `enableExamMode()` i `finishExam()`.
- To realizuje wpis z sekcji „do przekminienia": *tryb egzaminu nie powinien być tak schowany
  w opcjach* — po zmianie ten wpis można usunąć z TODO.md.
- W panelu bocznym **nie** ma osobnego wskaźnika trybu — tylko pozycja
  „Rozpocznij / Zakończ egzamin" (patrz [sidebar-nawigacji.md](sidebar-nawigacji.md)).
- Uwaga na `setExamMenuDisabled()` (`app/exam.js:99`): lista `OPCJE_MENU_EGZAMIN` blokuje
  m.in. `egzamin-start`. Przełącznik jest osobnym elementem — jego połówka „ćwiczenia"
  w trakcie egzaminu **nie** ma być zablokowana (to jedyne wyjście z egzaminu obok
  `#egzamin-koniec`), więc nie dopisywać go do tej listy.

## Odstęp na górze

`#exercises-wrapper { padding-top: 100px }` (`style/base.css:226`) istnieje wyłącznie po to,
by treść nie chowała się pod paskiem. Bez paska można go mocno zmniejszyć — ale nie do zera:
pływające pigułki nadal zajmują górę ekranu. Wartości do przejrzenia razem:
`base.css:228` (100px), `responsive.css:52` (80px @720), `responsive.css:135` (110px @560).

## Do sprawdzenia po zmianie

- `responsive.css:120–147` — cała sekcja `@media (max-width: 560px)` przebudowuje `#bar-container`
  na jedną kolumnę i chowa `#egzamin-koniec-bar` poniżej ~430 px, bo wypychał `⋯` poza ekran.
  Po likwidacji paska to nieaktualne; przy pływających pigułkach trzeba na nowo zmierzyć,
  czy klaster mieści się na 360 px (jeśli nie — zegar i „zakończ" mogą zejść do drugiego rzędu,
  a nie znikać: pełnowymiarowy „zakończ egzamin" jest w stopce arkusza jako `#egzamin-koniec`).
- `style/exam.css:151` (`body.tryb-egzaminu #total-score`) — reguły pokazywania/chowania
  timera i sumy w trybie egzaminu.
- ARCHITECTURE_CSS.md ma sekcję „Top bar" opisującą siatkę `1fr auto 1fr` — **do przepisania**
  (komentarz na górze `sheet.css:14` wprost o tym przypomina).

## Kryteria akceptacji

- [ ] `#top-bar` nie istnieje w DOM; strona nie scrolluje się poziomo przy 360 px
      (zmierzyć `document.documentElement.scrollWidth` vs `clientWidth`).
- [ ] Poza egzaminem w prawym górnym rogu jest wyłącznie suma punktów.
- [ ] W trybie egzaminu zegar, suma i „zakończ egzamin" stoją obok siebie i mieszczą się na 360 px.
- [ ] Pigułki i logo są czytelne nad treścią zadania przy scrollowaniu (mają własne tło).
- [ ] Klaster nadal jest nad panelami PDF (tak jak dziś pasek), a sidebar nad wszystkim.
- [ ] Widok punktów „tylko suma"/„nic" nadal chowa właściwe elementy.
- [ ] Przełącznik trybu pod tytułem: pokazuje właściwy stan po odświeżeniu w trakcie egzaminu,
      startuje i kończy egzamin, a anulowanie `confirm()` nie zostawia go w złym stanie.
- [ ] ARCHITECTURE_CSS.md zaktualizowany.
