# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Detailed architecture and exercise data schema live in [ARCHITECTURE.md](ARCHITECTURE.md); the full CSS/layout reference lives in [ARCHITECTURE_CSS.md](ARCHITECTURE_CSS.md).** Read them before touching the rendering logic in template.html, the schema in a sheet's exercises.json, or the CSS in style/ — and keep them in sync when you change what they describe. Don't duplicate their content here.

## Product context

MatematykaZen is an interactive platform for learning math for the Polish "matura podstawowa" exam, inspired by Brilliant.org. Current phase: demo/MVP. Content = official CKE exam sheets: closed-form exercises get hints/explanations (sometimes interactive widgets); open-form exercises use an off-platform-solve + self-grade flow (`selfScore`). UI philosophy: minimalist, no ads. Business model: freemium (CKE base free, proprietary content paid). This repo is one instance of the exam-sheet page pattern; sibling folders (e.g. `matematykazen11`) hold other sheets with the same structure.

## OVERVIEW.md

[OVERVIEW.md](OVERVIEW.md) — a standalone, Polish-language project summary (opis projektu, arkusze, funkcje, model biznesowy) maintained by Claude web (projekt „Matematyka Zen" na claude.ai) for use outside this repo, starting with an "Ostatnia aktualizacja" timestamp line. **ZASADA: aktualizuj datę i treść tego pliku po każdej większej zmianie, która może wpłynąć na jego treść** (nowy arkusz, nowa funkcja, zmiana modelu biznesowego itp.) — nie czekaj, aż użytkownik o to poprosi.

## What this is

A static Polish-language practice site for CKE "matura podstawowa" exam sheets. No backend, no build system, no package manager.

**Migration in progress since 2026-07-10 (see TODO.md for status):** moving from one hardcoded exam-sheet page to multiple sheets sharing a single renderer. Target structure:

- [index.html](index.html) — landing page, pure static HTML (`.landing-*` styles), links to each sheet.
- `template.html` (root; replaces the old `matematykazen.html`) — the shared exam-sheet renderer, now the **single** page that renders *any* sheet: hidden exercise `<template>` + at the bottom a run of `<script src>` tags (`widgets/_helpers.js`, the nine `widgets/*.js` widget files, `widgets/_registry.js`, then the ten `app/*.js` files) that render exercises from a sheet's data file and wire up all interactivity. Which sheet is chosen by the `?arkusz=<id>` URL param (`<id>` = folder name under `matura/`); the per-sheet `matura/<id>/index.html` copies were removed.
- `matura/<sheet-id>/` (e.g. `matura/2024-grudzien/`, `matura/2026-maj/`) — one folder per exam sheet: its `exercises.json`, its `media/zadN/` assets (PNG images + Manim-produced MP4 solution videos; keep filenames **lowercase**) and its four source PDFs/extracts under fixed names (`arkusz.pdf`/`.txt`, `odpowiedzi.pdf`/`.txt` — same in every sheet, so paths are predictable from the id alone). All asset paths in `exercises.json` are **sheet-relative** and joined to the folder by `mediaPath()` in `app/state.js`. **[matura/README.md](matura/README.md) is the source of truth** for which sheets exist and what the exam actually is (poziom podstawowy, Formuła 2023, próbna vs właściwa, CKE symbol, wired or not) — read it there, don't duplicate the list here.
- [app/](app/) — app logic, split (2026-07-23) into classic (non-module) scripts sharing one global scope — **load order matters**, `template.html` lists them in the required order: `state.js` (globals, `mediaPath`/`renderMath`, `SHEET_ID`) → `theme.js` (jasny/ciemny/auto) → `exam.js` (tryb egzaminu, timer) → `indicators.js` (wskaźniki „oceń się") → `panels.js` (PDF-panele tablicy wzorów/zasad oceniania) → `answers.js` (`normalizeAnswer`/`markCorrectAnswer`) → `steps.js` (rozwiązania krok po kroku, double-buffer wideo — shared mutable state like `currentStep`/`stepSwapToken` passed via a `ctx` object, not closures) → `report.js` (zgłaszanie błędów: dyskretny link pod zadaniem + formularz rozwijany **w karcie zadania** — jeden wspólny węzeł przenoszony przez `insertBefore` — obowiązkowy opis (3–2000 znaków, limit pilnowany i w `maxlength`, i w JS), pigułki kategorii, → Formspree AJAX ręcznym `fetch`em (świadomie bez SDK z CDN — offline-first), toggle w menu, honeypot + throttling; `dodajLinkZgloszenia` wołane z render.js, więc ładowane przed nim) → `render.js` (`loadExercises` — renderowanie wszystkich typów zadań) → `bootstrap.js` (panel boczny `#sidebar` — następca menu „⋯", usuniętego 2026-07-27 — `startSheet()`, **loaded last**). Reads the `?arkusz=<id>` URL param into `SHEET_ID` to pick the sheet (`matura/<id>/exercises.json`), key its localStorage and resolve its media/PDF paths (`mediaPath`).
- [widgets/](widgets/) — the interactive answer widgets, one file per widget (e.g. `widgets/osLiczbowa.js` → `widgetOsLiczbowa`), plus `widgets/_helpers.js` (shared `wg*` helpers, loaded first) and `widgets/_registry.js` (the `WIDZETY` name→function registry, loaded last of the three groups). In the repo **root-level directory** (one shared copy for all sheets). **All loaded before `app/*.js`** because `loadExercises` (in `app/render.js`) reads `WIDZETY` (classic scripts sharing the global scope, so load order matters).
- `exercises.json` (one per sheet, under `matura/<sheet-id>/`) — pure data: an object `{ meta, exercises }` (`meta` = per-sheet title/description/marking-key PDF; `exercises` = the array of exercise objects), `fetch`ed at startup by `startSheet()`. Interactive widgets are referenced by name (`"solutionWidget": "widgetX"` → the `WIDZETY` registry in `widgets/_registry.js`). All math in it is written in **KaTeX** (`\( ... \)` / `\[ ... \]`; schema + conventions documented in ARCHITECTURE.md — JSON has no comments).
- [style/](style/) — all styling (exam sheet + landing), shared by all sheets, split into `base.css` (variables/theme/reset), `sheet.css` (exam-sheet chrome), `landing.css` (index.html), `exam.css` (exam mode + open-exercise indicators) and `responsive.css` (breakpoints, must load last — cascade order matters). template.html loads all five; index.html only `base.css` + `landing.css`.

Plus `vendor/katex/` — KaTeX vendored for fully offline math rendering (don't edit those files; to bump the version replace them from the npm tarball) — and `tablica-wzorow.pdf` (shared formula sheet shown in a floating panel; stays in the root).

- **`tablica-wzorow-transkrypt/`** — transcript of that PDF (created 2026-07-28), **for models, not served to users**: one Markdown file per CKE section (`01-…` … `16-…`) plus `README.md`. Read it instead of the PDF whenever you need a formula — filling in `formulasPage`, checking a solution, writing hints. Start from `README.md`: its "Skorowidz" maps exercise wording ("nierówność wykładnicza", "pole trapezu") to a formula ID and page, so you load one 300–800-token section rather than the whole sheet. Formulas use the **same KaTeX delimiters as `exercises.json`** (`\( … \)` / `\[ … \]`), so they paste straight into exercises — just remember JSON needs `\\`. Each formula carries its PDF page (printed = physical, no offset) and a coarse position (`góra`/`środek`/`dół`). `README.md` has a **„Czego tu NIE MA"** section listing what the transcript does *not* carry (drawings/graphs → PDF pages 8, 11, 12, 15–28; section 17's trig value table → s. 34; front/back matter) — read it before concluding the formula sheet lacks something. Figures are rendered as **legends of symbols**, not descriptions of the drawing, and each affected section header says so with the PDF page to open. Verified 2026-07-28: every „•" bullet on pages 4–34 was listed from the PDF and matched one-to-one against transcript IDs (this caught one omission — `[8.10]` compound interest, since restored), all 795 formulas render in the vendored KaTeX, and every numerically checkable identity passes (26k random-value assertions).

## Task tracking

**The active TODO file is [TODO.md](TODO.md) — open items only.** The user (Henrich) checks it most often and curates priority himself (`WYSOKI`/`NISKI`/`NAJNIŻSZY PRIORYTET` sections) — don't edit those directly. Any new bug, idea, or task you want him to see goes under the **"DO REALZACJI Dopisane przez SONNETA LUB OPUSA"** section at the bottom, appended under your own model's subsection (`SONNET DOPISAŁ:` / `OPUS DOPISAŁ:`), in Polish. **Always check `TODO.md` before starting work and keep it in sync.**

**Done items do not stay in TODO.md.** When an item is completed, move it (marked `[DONE]`/`[ZROBIONE]` with the date and a short note on how it was solved) into the **current** file under [done/](done/) — see [done/README.md](done/README.md) for which file is current and the split rule (one file per merged partia, not per calendar period) — and delete it from TODO.md, so TODO.md stays short and cheap to load. **Do not read files under done/ by default** — open one only when you genuinely need project history: a broader view of the project, debugging a harder problem, or checking whether/how something was already solved before. Start from `done/README.md`'s tagged index rather than opening files blind. (Older names `todo1DONE.md`/`todo2.md`/`todo3.md`/`todo.md`/`todoDONE.md`/`TODODONE.md`/root `DONE.md` no longer exist — their content was merged/renamed/split into TODO.md and `done/`.)

## Git / gitdoc

**STATUS AS OF 2026-08-01: gitdoc is currently DISABLED for this repo — verify before trusting anything below.** `gitdoc.enabled` defaults to `false` and is not set anywhere: it's absent from both `.vscode/settings.json` (emptied by commit `3a985b5`, "usunięcie settingsów z repo i przeniesienie do user settings") and the global user settings.json (`C:\Users\<user>\AppData\Roaming\Code\User\settings.json`) — the "move to user settings" never actually happened, the key was just deleted. **`git status` / `git log` timing should NOT be assumed to include gitdoc auto-commits right now.**

Important mechanical fact (source: `out/config.js` in the installed extension), which explains why this happened and constrains any fix: **`gitdoc.enabled` can only ever be set at `ConfigurationTarget.Workspace`** — the extension's own setter hard-codes it:
```js
set enabled(value) {
    config().update(ENABLED_KEY, value, vscode.ConfigurationTarget.Workspace);
}
```
The Enable/Disable command (and thus the GitDoc UI toggle) always writes to **this repo's `.vscode/settings.json`**, never to global user settings — so putting `gitdoc.enabled: true` in the global file doesn't compose the way the rest of gitdoc's settings do; if you want gitdoc back on, set it back in `.vscode/settings.json` (or re-toggle via the UI), not in the global user settings.json. Global user settings.json is still the right place for the *other* `gitdoc.*` keys (delay/push/pull behavior) if you ever want to override them, since only `enabled` has this workspace-only restriction.

**When gitdoc IS enabled**, the behavior described below applies — but as of this writing every one of these values (`autoPush: "onCommit"`, `autoPull: "onPush"`, `pullOnOpen: true`, `commitOnClose: true`, `pushMode: "forcePush"`, `autoCommitDelay: 30000`) is just the **extension's built-in default** — none of them are explicitly set in any settings.json found on this machine. Don't assume a settings file documents them; they come from the extension itself (`out/config.js`).

If/when re-enabled, expect:
- gitdoc auto-commits on every save (timestamp-only messages, no prefix) and **immediately pushes each one to `origin`** (`autoPush: "onCommit"` default) — this bypasses the "confirm before push" rule for those commits specifically, because they're not something the assistant initiated.
- `git log` on this repo would routinely show a run of bare-timestamp commits between two "real" (prefixed, authored) commits — these are gitdoc, not the assistant, even during an assistant session (e.g. Henrich editing TODO.md in the editor mid-session).
- Before squashing a range of commits for the assistant's own work, check `git show --stat` on each one — don't assume every commit in the range is the assistant's; a gitdoc auto-commit from Henrich's own edits can land in the middle of the range (happened 2026-07-26, see `done/03-2026-07-27.md`).
- Because autoPush is immediate, treat any commit as **already on `origin`** unless proven otherwise — there is no local-only staging window to rely on.

Verified against the installed extension (`vsls-contrib.gitdoc-0.2.3`, VS Code 1.130.0) on 2026-07-26 (mechanics) and 2026-08-01 (enabled-state + config-target check), in case the commit cadence is ever tuned:
- **`gitdoc.autoCommitDelay` (default 30000 ms) is a debounce, not an interval** (`out/watcher.js`: `debounce(() => commit(repo), autoCommitDelay)`, timer reset on every repo-state change). Raising it to e.g. 20 min means "commit 20 min after the *last* edit", not "commit every 20 min" — during continuous editing nothing is committed at all until you pause (or close VS Code, which `commitOnClose` catches).
- The debounced function is cached per repository object in a `commitMap` that is never cleared, so **a changed `autoCommitDelay` only takes effect after `Developer: Reload Window`**, not on settings save.
- There is **no "commit every N saves"** option — the only knobs are `autoCommitDelay`, `filePattern` (which files trigger a commit), `excludeBranches`, and fully manual mode (`gitdoc.enabled: false` + the `GitDoc: Commit` command).
- `gitdoc.pushMode` defaults to **`"forcePush"`** — worth knowing before diagnosing any odd `origin` history.

## Running / previewing

No build or test tooling. **Serve the directory with a static file server** (e.g. `npx serve`, `python -m http.server`) — since the exercises.json migration the exam page loads its data with `fetch`, which does not work over `file://` (the page then shows a message explaining exactly this; index.html alone still opens fine from a file). No linter/test suite — verify changes by opening the page and clicking through the exercise(s) you touched.

## Content notes

- All user-facing content and code comments are Polish; keep new content in Polish, direct exam-prep tone.
- Known media defect: last frame of `matura/2024-grudzien/media/zad2/zad2rozw_step6.mp4` shows 5⁻⁴ instead of 5⁴ — needs an external Manim re-render; the step caption already carries the correction.


## User notes

- Ostrzegaj mnie przed włączeniem ciężkiego zadania np subagent-heavy sessions, które ostatnio wciągnęły mi 60% session limit dosyć szybko gdy robiłem code-review ultra

## Cloud sessions / routines

- Pushuj do najnowszej gałęzi z najnowszymi zmianami — nawet jeśli to jest `master` — zamiast tworzyć nową gałąź. Można to pominąć tylko jeśli użytkownik wyraźnie zażyczy sobie inaczej w prompcie.
- Każdego commita rozpoczynaj prefiksem z nazwą modelu i poziomem wysiłku, który go wykonał, np. `Sonnet High Cloud: ...` lub `Opus Medium Cloud: ...`.
- Nie zaglądaj do brancha `backup-przed-squash-gitdoc` (lokalnie ani `origin/`) — to tylko archiwalny backup sprzed squasha autozapisów gitdoc. Wyjątek: gdy chcesz sprawdzić bardzo szczegółową historię automatycznych commitów generowanych przez gitdoca.