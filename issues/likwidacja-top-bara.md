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
- `#bar-center` (`#exercises-mode-subtitle`, „tryb ćwiczenia") **znika bez zamiennika** —
  tytuł arkusza jest już w nagłówku sidebara i nad pierwszym zadaniem (`#sheet-title-heading`).
  Sprawdzić `updateModeSubtitle()` w `app/exam.js` — albo usunąć, albo zostawić element ukryty.
- `#menu-button` (`⋯`) znika — zastępuje go strzałka przy logo (patrz drugi issue).

## Warstwy

Klaster i logo: **`z-index: 10`** — tyle co dziś `#top-bar`, czyli nad panelami PDF (9),
bez zmiany dzisiejszej hierarchii. Sidebar dostaje 12, przyciemnienie 11,
podsumowanie egzaminu 20, toast 22.

Uwaga: `#zasady-oceniania-panel` jest przypięty do **lewej** krawędzi (`left: 30px`,
`top: 100px`, `style/sheet.css:171+`) — czyli dokładnie tam, gdzie wychodzi sidebar.
Sidebar (z-index 12) ma go przykrywać, ale warto sprawdzić, czy uchwyt przesuwania panelu
nie zostaje pod spodem w połowie widoczny.

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
- [ ] ARCHITECTURE_CSS.md zaktualizowany.
