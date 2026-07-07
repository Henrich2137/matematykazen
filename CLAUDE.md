# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Detailed architecture, exercise data schema and the full CSS/layout reference live in [ARCHITECTURE.md](ARCHITECTURE.md).** Read it before touching the rendering logic in matematykazen.html, the schema in exercises.json, or style.css — and keep it in sync when you change what it describes. Don't duplicate its content here.

## Product context

MatematykaZen is an interactive platform for learning math for the Polish "matura podstawowa" exam, inspired by Brilliant.org. Current phase: demo/MVP. Content = official CKE exam sheets: closed-form exercises get hints/explanations (sometimes interactive widgets); open-form exercises use an off-platform-solve + self-grade flow (`selfScore`). UI philosophy: minimalist, no ads. Business model: freemium (CKE base free, proprietary content paid). This repo is one instance of the exam-sheet page pattern; sibling folders (e.g. `matematykazen11`) hold other sheets with the same structure.

## What this is

A static Polish-language practice site for one exam sheet ("Egzamin maturalny z matematyki podstawowej grudzień 2024, próbna CKE"). No backend, no build system, no package manager. These files drive everything:

- [index.html](index.html) — landing page, pure static HTML (`.landing-*` styles).
- [matematykazen.html](matematykazen.html) — the exam-sheet page: hidden exercise `<template>` + at the bottom two `<script src>` tags (`solutionsInteractive.js` then `script.js`) that render exercises from the data file and wire up all interactivity.
- [script.js](script.js) — app logic: exercise rendering (`loadExercises`), answers/hints, step-by-step solutions, exam mode, formula-sheet PDF panels, bootstrap (`startSheet()`).
- [solutionsInteractive.js](solutionsInteractive.js) — the interactive answer widgets (`wg*` helpers + `widget*` functions) and the `WIDZETY` name→function registry. **Loaded before `script.js`** because `loadExercises` reads `WIDZETY` (both are classic scripts sharing the global scope, so load order matters).
- [exercises.json](exercises.json) — pure data: an array of exercise objects, `fetch`ed at startup by `startSheet()`. Interactive widgets are referenced by name (`"solutionInteractive": "widgetX"` → the `WIDZETY` registry in solutionsInteractive.js). All math in it is written in **KaTeX** (`\( ... \)` / `\[ ... \]`; schema + conventions documented in ARCHITECTURE.md — JSON has no comments).
- [style.css](style.css) — all styling (exam sheet + landing).

Plus `vendor/katex/` — KaTeX vendored for fully offline math rendering (don't edit those files; to bump the version replace them from the npm tarball).

Plus per-exercise asset folders `zad1/`, `zad2/`, … (PNG images + Manim-produced MP4 solution videos; keep filenames **lowercase**) and `wybrane_wzory_matematyczne.pdf` (formula sheet shown in a floating panel). The official exam + answer key PDFs and their text extracts live in `arkusze PDF/` — do not delete; all 30 answers in exercises.json were verified against the CKE key (2026-07-05).

## Task tracking

**The active TODO file is [TODO.md](TODO.md) — open items only.** The user (Henrich) checks it most often, so any new bug, idea, or verification result you want him to see goes there (append under the "NOWE PUNKTY TODO ZAPISYWANE PRZEZ CLAUDE" section, in Polish). **Always check `TODO.md` before starting work and keep it in sync.**

**Done items do not stay in TODO.md.** When an item is completed, move it to [TODODONE.md](TODODONE.md) (marked `[DONE]`/`[ZROBIONE]` with the date and a short note on how it was solved) and delete it from TODO.md, so TODO.md stays short and cheap to load. **Do not read TODODONE.md by default** — open it only when you genuinely need project history: a broader view of the project, debugging a harder problem, or checking whether/how something was already solved before. (Older names `todo1DONE.md`/`todo2.md`/`todo3.md`/`todo.md`/`todoDONE.md` no longer exist — their content was merged/renamed into these two files.)

## Running / previewing

No build or test tooling. **Serve the directory with a static file server** (e.g. `npx serve`, `python -m http.server`) — since the exercises.json migration the exam page loads its data with `fetch`, which does not work over `file://` (the page then shows a message explaining exactly this; index.html alone still opens fine from a file). No linter/test suite — verify changes by opening the page and clicking through the exercise(s) you touched.

## Content notes

- All user-facing content and code comments are Polish; keep new content in Polish, direct exam-prep tone.
- [matematykazen.html](matematykazen.html) has a commented-out `<meta http-equiv="refresh" content="5">` dev-reload snippet flagged `DELETE THIS BEFERE PUBLISHING` — leave it commented out; don't ship it enabled.
- Known media defect: last frame of `zad2/zad2rozw_step6.mp4` shows 5⁻⁴ instead of 5⁴ — needs an external Manim re-render; the step caption already carries the correction.
