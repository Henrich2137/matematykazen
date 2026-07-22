# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Detailed architecture and exercise data schema live in [ARCHITECTURE.md](ARCHITECTURE.md); the full CSS/layout reference lives in [ARCHITECTURE_CSS.md](ARCHITECTURE_CSS.md).** Read them before touching the rendering logic in template.html, the schema in a sheet's exercises.json, or style.css — and keep them in sync when you change what they describe. Don't duplicate their content here.

## Product context

MatematykaZen is an interactive platform for learning math for the Polish "matura podstawowa" exam, inspired by Brilliant.org. Current phase: demo/MVP. Content = official CKE exam sheets: closed-form exercises get hints/explanations (sometimes interactive widgets); open-form exercises use an off-platform-solve + self-grade flow (`selfScore`). UI philosophy: minimalist, no ads. Business model: freemium (CKE base free, proprietary content paid). This repo is one instance of the exam-sheet page pattern; sibling folders (e.g. `matematykazen11`) hold other sheets with the same structure.

## What this is

A static Polish-language practice site for CKE "matura podstawowa" exam sheets. No backend, no build system, no package manager.

**Migration in progress since 2026-07-10 (see TODO.md for status):** moving from one hardcoded exam-sheet page to multiple sheets sharing a single renderer. Target structure:

- [index.html](index.html) — landing page, pure static HTML (`.landing-*` styles), links to each sheet.
- `template.html` (root; replaces the old `matematykazen.html`) — the shared exam-sheet renderer, now the **single** page that renders *any* sheet: hidden exercise `<template>` + at the bottom a run of `<script src>` tags (`widgets/_helpers.js`, the nine `widgets/*.js` widget files, `widgets/_registry.js`, then `script.js`) that render exercises from a sheet's data file and wire up all interactivity. Which sheet is chosen by the `?arkusz=<id>` URL param (`<id>` = folder name under `matura/`); the per-sheet `matura/<id>/index.html` copies were removed.
- `matura/<sheet-id>/` (e.g. `matura/2024-grudzien/`, `matura/2026-maj/`) — one folder per exam sheet: its `exercises.json`, its `media/zadN/` assets (PNG images + Manim-produced MP4 solution videos; keep filenames **lowercase**) and its own exam/answer-key PDFs. All asset paths in `exercises.json` are **sheet-relative** and joined to the folder by `mediaPath()` in script.js.
- [script.js](script.js) — app logic: exercise rendering (`loadExercises`), answers/hints, step-by-step solutions, exam mode, formula-sheet PDF panels, bootstrap (`startSheet()`). Reads the `?arkusz=<id>` URL param into `SHEET_ID` to pick the sheet (`matura/<id>/exercises.json`), key its localStorage and resolve its media/PDF paths (`mediaPath`).
- [widgets/](widgets/) — the interactive answer widgets, one file per widget (e.g. `widgets/osLiczbowa.js` → `widgetOsLiczbowa`), plus `widgets/_helpers.js` (shared `wg*` helpers, loaded first) and `widgets/_registry.js` (the `WIDZETY` name→function registry, loaded last of the three groups). In the repo **root-level directory** (one shared copy for all sheets). **All loaded before `script.js`** because `loadExercises` reads `WIDZETY` (classic scripts sharing the global scope, so load order matters).
- `exercises.json` (one per sheet, under `matura/<sheet-id>/`) — pure data: an object `{ meta, exercises }` (`meta` = per-sheet title/description/marking-key PDF; `exercises` = the array of exercise objects), `fetch`ed at startup by `startSheet()`. Interactive widgets are referenced by name (`"solutionWidget": "widgetX"` → the `WIDZETY` registry in `widgets/_registry.js`). All math in it is written in **KaTeX** (`\( ... \)` / `\[ ... \]`; schema + conventions documented in ARCHITECTURE.md — JSON has no comments).
- [style.css](style.css) — all styling (exam sheet + landing), shared by all sheets.

Plus `vendor/katex/` — KaTeX vendored for fully offline math rendering (don't edit those files; to bump the version replace them from the npm tarball) — and `wybrane_wzory_matematyczne.pdf` (shared formula sheet shown in a floating panel; stays in the root). Each wired sheet's exam + answer-key PDFs now live in its own `matura/<id>/` folder; other not-yet-wired sheets and text extracts sit in `inne arkusze PDF/` — do not delete. The 2024-grudzień answers in `matura/2024-grudzien/exercises.json` were verified against the CKE key (2026-07-05).

## Task tracking

**The active TODO file is [TODO.md](TODO.md) — open items only.** The user (Henrich) checks it most often and curates priority himself (`WYSOKI`/`NISKI`/`NAJNIŻSZY PRIORYTET` sections) — don't edit those directly. Any new bug, idea, or task you want him to see goes under the **"DO REALZACJI Dopisane przez SONNETA LUB OPUSA"** section at the bottom, appended under your own model's subsection (`SONNET DOPISAŁ:` / `OPUS DOPISAŁ:`), in Polish. **Always check `TODO.md` before starting work and keep it in sync.**

**Done items do not stay in TODO.md.** When an item is completed, move it (marked `[DONE]`/`[ZROBIONE]` with the date and a short note on how it was solved) into the **current** file under [DONE/](DONE/) — see [DONE/README.md](DONE/README.md) for which file is current and the split rule (one file per merged partia, not per calendar period) — and delete it from TODO.md, so TODO.md stays short and cheap to load. **Do not read files under DONE/ by default** — open one only when you genuinely need project history: a broader view of the project, debugging a harder problem, or checking whether/how something was already solved before. Start from `DONE/README.md`'s tagged index rather than opening files blind. (Older names `todo1DONE.md`/`todo2.md`/`todo3.md`/`todo.md`/`todoDONE.md`/`TODODONE.md`/root `DONE.md` no longer exist — their content was merged/renamed/split into TODO.md and `DONE/`.)

## Running / previewing

No build or test tooling. **Serve the directory with a static file server** (e.g. `npx serve`, `python -m http.server`) — since the exercises.json migration the exam page loads its data with `fetch`, which does not work over `file://` (the page then shows a message explaining exactly this; index.html alone still opens fine from a file). No linter/test suite — verify changes by opening the page and clicking through the exercise(s) you touched.

## Content notes

- All user-facing content and code comments are Polish; keep new content in Polish, direct exam-prep tone.
- Known media defect: last frame of `matura/2024-grudzien/media/zad2/zad2rozw_step6.mp4` shows 5⁻⁴ instead of 5⁴ — needs an external Manim re-render; the step caption already carries the correction.


## User notes

- Ostrzegaj mnie przed włączeniem ciężkiego zadania np subagent-heavy sessions, które ostatnio wciągnęły mi 60% session limit dosyć szybko gdy robiłem code-review ultra