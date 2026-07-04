# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Product context

MatematykaZen is an interactive platform for learning math for the Polish "matura podstawowa" exam (basic-level high school finals), with extended-level content planned eventually — inspired by Brilliant.org. Current phase: demo/MVP for validating the idea.

- **Content**: official CKE exam sheets (arkusze maturalne). Closed-form (multiple choice) exercises get a hint and an explanation, sometimes interactive (in the Brilliant.org style). Open-form exercises use a simplified flow: the student solves it themselves off-platform, then self-grades correctness in the UI (see `selfScore` in the exercise schema below).
- **UI philosophy**: minimalist, no ads, no distractions.
- **Business model**: freemium — the CKE exercise base is free; proprietary exercises/features are the paid tier (subscription vs. one-time purchase is still undecided).

This repo (`matematykazengithubrepo`) is one instance of the exam-sheet page pattern; sibling/predecessor folders (e.g. `matematykazen11`, ...) hold other exam sheets following the same structure.

## What this is

A static, single-page Polish-language practice site for one specific exam sheet ("Egzamin maturalny z matematyki podstawowej grudzień 2024, próbna CKE"). No backend, no build system, no package manager. Three files drive everything:

- [matematykazen.html](matematykazen.html) — the page skeleton around which all logic revolves: renders exercises from the data file, and handles all UI (answer buttons, hints, step-by-step solutions, the CKE formula sheet shown as an embedded PDF). Contains the hidden exercise `<template>` div and an inline `<script>` at the bottom that renders exercises and wires up all interactivity.
- [exercises.js](exercises.js) — pure data: a single `exercises` array of plain objects (content, answers, correct answer, hint, solution text, optional step-by-step solution, scoring, link to a formula-sheet page), loaded via `<script src="exercises.js">` before the inline script runs. **Target format is `exercises.json`** — the plan is to migrate this data file to JSON; until then it stays a `.js` file exposing a global array.
- [style.css](style.css) — all page styling: minimalist, single centered column.

Plus per-exercise asset folders `zad1/`, `zad2/`, `zad3/`, ... (Polish "zadanie" = "task/exercise") containing PNG images and MP4 step-by-step solution videos, and `wybrane_wzory_matematyczne.pdf`, a formula-sheet PDF shown in a floating panel.

Step-by-step solution videos are produced externally with **Manim** (the Python math-animation library), then exported as short `.mp4` files and dropped into the relevant `zadN/` folder — they aren't generated or editable from within this repo, only referenced and played back (see `solutionStepByStep` below).

## Task tracking

The active TODO list lives in `todo.md` (bugs + design/later suggestions from smoke-testing). Check it before starting work and keep it in sync. Phase-specific files (e.g. the former `todoFaza1.md`) are deleted once their work is done — recreate one only if you need to hand off a phase to a fresh session.

## Running / previewing

There is no build or test tooling. Open [matematykazen.html](matematykazen.html) directly in a browser, or serve the directory with any static file server (e.g. `npx serve` or `python -m http.server`) if `file://` restrictions cause the embedded PDF `<object>` not to load.

There's no linter or test suite — verify changes by opening the page and clicking through the exercise(s) you touched (answer buttons, hint/solution toggles, step navigation, formula-sheet button).

## Architecture

### Rendering model

`loadExercises()` (defined inline at the bottom of [matematykazen.html](matematykazen.html)) runs once on page load. For each entry in the `exercises` array it clones the hidden `#exercise-template` node, fills in the fields, and appends the clone to `#exercises-wrapper`. All per-exercise behavior (answer click handling, hint/solution toggling, step-by-step nav, scoring) is wired up inside this same function at render time — there are no persistent component classes.

### Exercise data schema (`exercises.js`)

**Styling rule for `exercises.js`:** only put inline HTML/CSS (e.g. a `style="…"` on an `<img>`) into an exercise's data when it is genuinely specific to that one exercise — e.g. Zad 2's inline number image opting out of the block/centred `.question img` rule with `display:inline-block; vertical-align:middle`. Anything that should apply to *all* exercises (answer-button alignment, generic figure sizing, colours, spacing, …) belongs in [style.css](style.css), never copy-pasted per entry. If you catch yourself adding the same inline style to several exercises, move it to a CSS rule instead.

Each element of `exercises` is an object with this shape (see the header comment in [exercises.js](exercises.js) for a note on a planned but not-yet-implemented `type`/`number`/`numberSection` schema for multi-part exercises — the current entries don't use it and instead just make multi-part exercises separate array entries, e.g. "Zadanie 12.1", "Zadanie 12.2", "Zadanie 17.1", "Zadanie 17.2"):

- `question` — HTML string, rendered into `.question`. Often embeds `<img>` tags pointing into the exercise's `zadN/` folder.
- `answers` — array of HTML strings for multiple-choice buttons. Empty array (`[]`) means an open-ended/self-graded exercise (no buttons rendered).
- `correctAnswerIndex` — 0-based index into `answers` of the correct option (`0` = A, `1` = B, …). `-1` or a missing field marks an open-ended/unfilled exercise: clicking an answer just toggles a single `?` feedback marker instead of grading. Replaces the old string-matching `correctAnswer` field — grading is now `i === correctAnswerIndex` in the render loop, so the answer's HTML no longer has to match anything verbatim. `loadExercises` `console.warn`s if the index is out of range.
- `maxScore` — the exercise's point value. A correct click sets that exercise's `exercise.earnedScore = maxScore`; a wrong click resets it to `0`. `totalScore` is then recomputed as the sum of every `earnedScore` (`updateTotalScore()`), so scoring is idempotent and self-correcting — no `isScoreGiven` flag or manual add/subtract.
- `selfScore` — currently unused by the render logic (no self-scoring UI implemented yet); present in the data for future use.
- `hint` — HTML shown/hidden by the "Podpowiedź" button.
- `formulasPage` — page number into `wybrane_wzory_matematyczne.pdf`, or `null` to hide the "Pokaż potrzebne wzory" button. Clicking it calls `otworzTabliceNaStronie(page)`, which replaces the PDF `<object>` inside `#tablica-wzorow-panel` entirely (changing just `data` doesn't reliably reload PDF viewers) and then shows the panel via `pokazTablice()`. Show/hide is centralised in `pokazTablice()`/`schowajTablice()` (they toggle the panel's `display` and keep the `#toggle-tablica` label in sync); the bar button and the in-panel close button (`#tablica-close`, the ✕ in its bottom-right corner) both go through them.
- `solutionText` / `solutionTextMore` — HTML for the solution panel; `solutionTextMore` is behind an extra "Pokaż więcej" toggle and its container auto-hides when empty.
- `solutionStepByStep` — either `null` or an array of `{ type: "video"|"image"|"text", src, text }` steps rendered one at a time with prev/next navigation inside the solution panel. `renderStep()` returns a plain HTML string (video steps are wrapped in a `.step-video` div holding the `<video>`, a small `.video-overlay-icon` pause marker (two black vertical bars drawn with `::before`/`::after`, horizontally centred at the bottom of the film) and a thin grey `.video-progress`/`.video-progress-bar` (the bar has a short `width` transition so it slides rather than jumps between `timeupdate` events); the caption goes in a `.step-comment` div); `showStep()` then works on the real, already-inserted `<video>`: it sets `defaultPlaybackRate`/`playbackRate` (currently `1`), and wires click-to-toggle play/pause, a `.paused` class on `.step-video` (which reveals the ▶ icon whenever the video is paused or ended), and a `timeupdate` handler that fills the progress bar. Doing all this on the attached element is deliberate — JS properties/listeners can't be set on the throwaway string `renderStep` returns. Reaching the last step calls `markCorrectAnswer()`, which reveals the correct answer button (guarded against a missing button) — i.e. finishing the walkthrough is how open-style exercises "give away" the answer. The "Rozwiązanie" button itself is hidden in `loadExercises` when an exercise has no solution content at all (no text/steps/interactive/more).
- `solutionInteractive` — either `null` or a `function(container)` invoked at render time to inject custom interactive widgets (e.g. the `<canvas id="numberLine">` number-line drawn by `drawNumberLine1()` in the inline script — the only such helper actually defined). Note: Zadanie 5's data still calls a `rysujWykresEksponencjalny()` graph helper that no longer exists in the inline script (a dangling reference from an unfinished exponential-graph widget), so Zadanie 5 currently displays a placeholder note about this ("coś nie wyszło").

### Asset folder convention

Each exercise that needs images or video gets its own `zadN/` folder (matching the exercise number, not array index) referenced by relative path from the HTML's location, e.g. `zad6/zad6.png`, `zad6/zad6odp1.png` (odpowiedź = answer option image), `zad1/zad1rozw_step1.mp4` (rozwiązanie = solution). Many exercises defined in `exercises.js` (roughly 12 onward) are still stubs — `correctAnswerIndex: -1`, generic hints, no `solutionStepByStep`/`solutionInteractive`, and some reference `zadN/` folders or images (e.g. `zad23/zad23.png`) that don't exist on disk yet. When filling these in, follow the pattern of the completed early exercises (1–3, 6) rather than inventing a new structure.

### Scoring / UI chrome

`maxTotalScore` (top of [exercises.js](exercises.js)) must be kept in sync with the sum of all `maxScore` values — it's used to render the running total in `#total-score`. The `#score-switch-button` in the top bar cycles through three display modes (all per-exercise scores / total only / nothing) by toggling `.exercise-score` element visibility, purely client-side, no persistence.

## CSS & layout reference

> **Keep this section in sync.** Whenever you change [style.css](style.css) (or the DOM structure it targets), update this section in the same edit so it always describes the current layout. Treat it as the source of truth for "how is this laid out and why" before touching styles.

[style.css](style.css) is a single flat stylesheet (no preprocessor, no CSS variables yet). Fonts come from a Google Fonts `@import` at the top (`STIX Two Math` for math, `Lora` fallback). The page is one centred column on a white background; `body` is `text-align: center` and most block widths are fixed at **650px** (`#bar-container` conceptually and `.exercise-container`). Section banners in the file use `/* ===== NAZWA ===== */` comment headers, in Polish — follow that convention.

### Top bar (`#top-bar`)

Restructured to a **flexbox three-zone layout** (previously each element used `position: absolute`/`fixed` with hard-coded negative offsets like `right: -330px`, which overlapped whenever the title, score width, or window size changed — do **not** reintroduce that pattern).

- `#top-bar` — `position: fixed`, full width, bottom border + subtle shadow, `z-index: 10`. This is the only element in the bar that is positioned/fixed.
- `#bar-container` — full-width **CSS grid** row (`display: grid; grid-template-columns: 1fr auto 1fr; align-items: center`, padded `12px 30px`, no `max-width` — it spans the viewport like the original design so the title can be centred on the whole screen). Holds exactly three zone divs, one per grid column:
  - `#bar-left` (left column, left-aligned) → `#logo` ("Matematyka Zen").
  - `#bar-right` (right column, right-aligned, `flex-wrap: nowrap`) → groups `#total-score`, `#score-switch-button`, `#toggle-tablica` on one line, in that order. The side zones never wrap vertically — do not put `flex-wrap: wrap` back here.
  - `#bar-center` (middle `auto` column, `justify-self: center`) → `#exercises-sheet-title`. Because the two flanking columns are equal `1fr` tracks, it lands at the **true page centre** regardless of how wide the logo or the right group are (a plain flexed centre column drifts off-centre when the side zones differ in width) — without being taken out of flow, so it can never visually overlap the logo or the controls the way the old `position: absolute` version could on narrow windows. `min-width: 0` + `overflow: hidden` + `text-overflow: ellipsis` (with `white-space: nowrap` kept) is what lets the middle column shrink and truncate the title with an ellipsis if the side zones leave too little room for it, instead of overflowing into them or wrapping onto a second line — wrapping was rejected because it would grow `#top-bar`'s height. `pointer-events: none` is a leftover safety net in case any overlap ever happens anyway.
- To add another control to the bar, drop it into the appropriate zone div — no offsets to recompute. The IDs (`#logo`, `#total-score`, `#score-switch-button`, `#toggle-tablica`, `#tablica-wzorow-panel`, `#tablica-wzorow`, `#tablica-close`) are referenced by the inline JS, so keep the IDs stable when restyling; the `#bar-left/center/right` wrappers are layout-only and JS-free.
- `#tablica-wzorow-panel` — the floating formula-sheet panel: `position: fixed`, top-right, `display: none` until the JS toggles it to `block`. `z-index: 9` (just under the bar). It's a container around the PDF `<object id="tablica-wzorow">` (which fills it at `width/height: 100%`, borderless) plus `#tablica-close` — the ✕ close button absolutely positioned in the panel's top-right corner. The panel owns the border/shadow/size; the `<object>` is what `otworzTabliceNaStronie` swaps out, so keeping the chrome on the wrapper means a page change never loses the border or the close button.

### Exercise cards & solution panel

- `.exercise-container` — the per-exercise card (650px, left-aligned text, `font-size: 18px`), cloned from the hidden `#exercise-template`. `position: relative` so `.exercise-score` (the per-exercise points badge) can sit at its top-right; the badge colour tier is one of `.low-/.mid-/.high-exercise-score`. Figure images in the question (`.question img`) are forced to `display: block; margin: 15px auto` so they sit centred on their own line instead of floating mid-sentence and shifted right; a genuinely inline image (e.g. Zad 2's number inside "Liczba … jest równa") must opt out with an inline `display:inline-block; vertical-align:middle` in its own `style`.
- `.button-container button` — multiple-choice answer buttons (~22% wide, inline-block). `vertical-align: middle` on the button (and on any `img` inside it, e.g. Zad 6's answer images) keeps the option letter (A., B., …) centred on the vertical axis rather than sitting at the bottom next to a taller image or a wrapped neighbour — do **not** switch these to flex, which would break inline `<sup>`/`<sub>` in answers like `5<sup>4</sup>`. State classes toggled by JS: `.correct` (green border) / `.incorrect` (red border).
- `.light-button` / `.light-button-container` — the borderless text actions ("Podpowiedź / Rozwiązanie / Pokaż potrzebne wzory", step arrows, "Pokaż więcej").
- `.hint-container` / `.solution-container` — both `display: none` by default, revealed by JS. Inside the solution panel, the sub-blocks `.solution-text-container`, `.solution-step-by-step-container`, `.solution-interactive-container` each use `:empty { display: none }` so they self-hide when the exercise has no such content. Step media sizing lives in `.solution-step-by-step-container video/img`; each step's caption is wrapped by `renderStep()` in a `.step-comment` div with a ~2-line `min-height`, and `.steps-content` has `min-height: 250px`, so the step-by-step panel keeps a roughly constant height (the nav doesn't jump) until a caption runs past ~2 lines. The blocks are separated by `border-bottom` dividers; `loadExercises` strips the divider off the **last visible** block (computed from `hasText`/`hasSteps`/`hasInteractive`/`hasMore`) so a text-only solution has no dangling separator underneath. The revealed "Pokaż więcej" content (`.solution-text-more`) is padded `0 40px` so it isn't glued to the left edge. The `#toggle-tablica` button has `min-width: 200px` so it doesn't resize when its label toggles between "▼ Pokaż tablice wzorów" and "▲ Schowaj tablice wzorów".

### Known layout gotchas

- Spacing below the fixed bar is currently done with literal `<br><br><br><br>` in the HTML rather than a `padding-top`/`margin-top` on the content — crude, and coupled to the bar's height. If you change the bar height noticeably, adjust that spacer (ideally replace it with real spacing on `#exercises-wrapper`).
- Widths are hard-coded `650px` in several places; there are no responsive/media-query breakpoints yet, so the layout is desktop-first. Narrow viewports are not handled beyond the top bar's `flex-wrap`.

## Content notes

- All user-facing content and code comments in the existing files are Polish; keep new exercise content in Polish and consistent with the existing tone (direct, exam-prep style).
- [matematykazen.html](matematykazen.html) has a commented-out `<meta http-equiv="refresh" content="5">` dev-reload snippet flagged `DELETE THIS BEFERE PUBLISHING` — leave it commented out unless actively doing rapid local iteration, and don't ship it enabled.
