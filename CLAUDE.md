# CLAUDE.md

Napisz na początku sesji: "Wczytałem CLAUDE.md"

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Detailed architecture and exercise data schema live in [ARCHITECTURE.md](ARCHITECTURE.md); the full CSS/layout reference lives in [ARCHITECTURE_CSS.md](ARCHITECTURE_CSS.md).** Read them before touching the rendering logic in template.html, the schema in a sheet's exercises.json, or the CSS in style/ — and keep them in sync when you change what they describe. Don't duplicate their content here. **[COLORS.md](COLORS.md) — what each colour *means* and which token to use** (blue = the student's choice, green/red = correctness only, default is *no* colour); read it before colouring anything in a widget, an exercise or a Manim scene.

**Writing a solution? Read the rules first, they are short.**

- **`solutionText` (rozwiązanie zwykłe) → [SOLUTION_TEXT_RULES.md](SOLUTION_TEXT_RULES.md).** One expression per line; green marks what changes. Three layouts to pick from (one column, two columns, two parallel tracks) — the file says which fits what, and only formulas that are actually in `tablica-wzorow.pdf` may sit beside a line.
- **Manim scene (rozwiązanie krok po kroku) → „Zasady krok po kroku" in [manimations/README.md](manimations/README.md).** One step = one transformation; every step goes black → green → animation → black.
- **They must stay in step: one line of the written solution = one step of the film.** Change one, change the other.

## Bezpieczeństwo poza devcontainerem

**Sprawdź na starcie sesji, czy działasz na hoście (poza devcontainerem), czy w devcontainerze.** Jeśli na hoście — obowiązują zasady z [HOSTRULES.md](HOSTRULES.md) jako **twarde ograniczenia, nie sugestie**: stosuj się do nich automatycznie, przy każdym działaniu, bez czekania na przypomnienie i niezależnie od tego, czy bieżące zadanie o nich wspomina. Nie omijaj ich dla wygody ani żeby "po prostu skończyć zadanie" — jeśli zadanie wymaga czegoś, co HOSTRULES.md zabrania, zatrzymaj się i zapytaj, zamiast szukać obejścia. W razie wątpliwości, czy jesteś na hoście czy w kontenerze, załóż, że na hoście, i działaj wg HOSTRULES.md.

## Product context

Matematyka Zen is an interactive platform for learning math for the Polish "matura podstawowa" exam, inspired by Brilliant.org. Current phase: demo/MVP. Content = official CKE exam sheets: closed-form exercises get hints/explanations (sometimes interactive widgets); open-form exercises use an off-platform-solve + self-grade flow (`selfScore`). UI philosophy: minimalist, no ads. Business model: freemium (CKE base free, proprietary content paid). This repo is one instance of the exam-sheet page pattern; sibling folders (e.g. `matematykazen11`) hold other sheets with the same structure.

## OVERVIEW.md

[OVERVIEW.md](OVERVIEW.md) — a standalone, Polish-language project summary (opis projektu, arkusze, funkcje, model biznesowy) maintained by Claude web (projekt „Matematyka Zen" na claude.ai) for use outside this repo, starting with an "Ostatnia weryfikacja" timestamp line. **ZASADA: aktualizuj datę i treść tego pliku po każdej większej zmianie, która może wpłynąć na jego treść** (nowy arkusz, nowa funkcja, zmiana modelu biznesowego itp.) — nie czekaj, aż użytkownik o to poprosi.

**Its reader is Claude web, not Claude Code.** It is the bird's-eye view for business and product planning by someone who has *not* opened the repo: what exists, what the site does, where it is heading. So keep it **short and skimmable**, and keep technical detail out — how something works, how it is counted, how it is run belongs in this file and in the docs next to the code. When in doubt, cut from OVERVIEW.md and write the detail here instead.

### Statystyki arkuszy w OVERVIEW.md

The "Arkusze maturalne" section carries hard numbers per sheet. **Never count them by hand** — [tools/statystyki.py](tools/statystyki.py) computes them straight from `exercises.json`, and its docstring is the source of truth for what each line means:

```
python3 tools/statystyki.py            # wszystkie arkusze
python3 tools/statystyki.py 2026-maj   # jeden arkusz
python3 tools/statystyki.py --braki    # + numery zadań, w których czegoś brakuje
```

Counting rules (implemented in the script, repeated here so you know what you are looking at):
- **Zadanie** = one *scoring* entry in `exercises.json`. A bundle header („Zadanie 12." above 12.1 and 12.2) has `maxScore: 0` and does **not** count, so 12 + 12.1 + 12.2 = three entries but two exercises.
- **Podpowiedź / rozwiązanie opisowe / rozwiązanie wideo / widżet** = the matching field (`hint` / `solutionText` / `solutionStepByStep` / `solutionWidget`) is non-empty.
- **Widżety** are reported as a count of distinct widgets in the sheet, never as a fraction of exercises — not every exercise can or should get one.
- **Odpowiedzi zweryfikowane z kluczem CKE** = the closed-form answers were compared against `matura/<id>/odpowiedzi.pdf`.

**Run the script and rewrite the numbers (and the date at the top) whenever you finish a batch of work on a sheet** — new hints, solutions, videos or widgets. It is one command, so that section has no excuse to drift.

Beyond that, treat OVERVIEW.md as something **you** keep current, not something Henrich has to ask for: if a session touches the sheets or the feature set at all, run the script before you finish and check that the prose around the numbers still matches reality.

## Licensing / contributions

The repo is **PolyForm Noncommercial 1.0.0** (`LICENSE.md` — official text verbatim, don't reword it) plus a **CLA** in `CONTRIBUTING.md`; CKE exercises/keys are **not** covered by the license. Two deliberate placeholders (owner pseudonym `Henrich2137`, `Required Notice:` URL on GitHub Pages) must be changed in pairs — details, file-by-file, in [issues/licencja-i-cla.md](issues/licencja-i-cla.md). Read it before touching any of those files.

**`widgets/` is the one exception and it is proprietary** (since 2026-08-20): all rights reserved, own licence in `widgets/LICENSE.md`, SPDX header in every file. It holds the premium interactive solutions. Two rules follow, and they bind you as much as they bind a human contributor:

- **Put nothing in `widgets/` except the `widget*.js` files themselves.** Anything the free site needs in order to run belongs in `app/`, `style/` or `tools/`. Whatever sits in `widgets/` vanishes from the free build the day that directory goes behind the paywall, so dropping a shared helper in there silently breaks the free site. This is why `app/widget-helpers.js` and `app/widget-registry.js` live where they do; do not move them back.
- **Every new file in `widgets/` needs the four-line SPDX header** the existing ones carry. Without it a copied file looks unowned.

The reasoning, the file-by-file map and what is deliberately *not* covered: [issues/licencja-premium.md](issues/licencja-premium.md).

## What this is

A static Polish-language practice site for CKE "matura podstawowa" exam sheets. No backend, no build system, no package manager.

Structure (since the 2026-07-10 migration from one hardcoded page to many sheets sharing a single renderer):

- [index.html](index.html) — landing page, pure static HTML (`.landing-*` styles), links to each sheet.
- `template.html` (root) — the shared exam-sheet renderer, the **single** page that renders *any* sheet: hidden exercise `<template>` + at the bottom a run of `<script src>` tags (`app/widget-helpers.js`, the 20 `widgets/*.js` widget files, `app/widget-registry.js`, then the ten `app/*.js` files) that render exercises from a sheet's data file and wire up all interactivity. Which sheet is chosen by the `?arkusz=<id>` URL param (`<id>` = folder name under `matura/`); the per-sheet `matura/<id>/index.html` copies were removed.
- `matura/<sheet-id>/` (e.g. `matura/2024-grudzien/`, `matura/2026-maj/`) — one folder per exam sheet: its `exercises.json`, its `media/zadN/` assets (PNG images + Manim-produced MP4 solution videos; keep filenames **lowercase**) and its four source PDFs/extracts under fixed names (`arkusz.pdf`/`.txt`, `odpowiedzi.pdf`/`.txt` — same in every sheet, so paths are predictable from the id alone). All asset paths in `exercises.json` are **sheet-relative** and joined to the folder by `mediaPath()` in `app/state.js`. **[matura/README.md](matura/README.md) is the source of truth** for which sheets exist and what the exam actually is (poziom podstawowy, Formuła 2023, próbna vs właściwa, CKE symbol, wired or not) — read it there, don't duplicate the list here. The `.txt` extracts are **not all UTF-8** (`2024-grudzien` is cp1250) and are kept left-aligned; if you ever make a new one, `matura/README.md` has the rule and `tools/wyrownaj-transkrypt.py` does it.
- [app/](app/) — app logic, split (2026-07-23) into classic (non-module) scripts sharing one global scope — **load order matters**, `template.html` lists them in the required order: `state.js` (globals, `mediaPath`/`renderMath`, `SHEET_ID`) → `theme.js` (jasny/ciemny/auto) → `exam.js` (tryb egzaminu, timer) → `indicators.js` (wskaźniki „oceń się") → `panels.js` (PDF-panele tablicy wzorów/zasad oceniania) → `answers.js` (`normalizeAnswer`/`markCorrectAnswer`) → `steps.js` (rozwiązania krok po kroku, double-buffer wideo — shared mutable state like `currentStep`/`stepSwapToken` passed via a `ctx` object, not closures) → `report.js` (zgłaszanie błędów: dyskretny link pod zadaniem + formularz rozwijany **w karcie zadania** — jeden wspólny węzeł przenoszony przez `insertBefore` — obowiązkowy opis (3–2000 znaków, limit pilnowany i w `maxlength`, i w JS), pigułki kategorii, → Formspree AJAX ręcznym `fetch`em (świadomie bez SDK z CDN — offline-first), toggle w menu, honeypot + throttling; `dodajLinkZgloszenia` wołane z render.js, więc ładowane przed nim) → `render.js` (`loadExercises` — renderowanie wszystkich typów zadań) → `bootstrap.js` (panel boczny `#sidebar` — następca menu „⋯", usuniętego 2026-07-27 — `startSheet()`, **loaded last**). Reads the `?arkusz=<id>` URL param into `SHEET_ID` to pick the sheet (`matura/<id>/exercises.json`), key its localStorage and resolve its media/PDF paths (`mediaPath`).
- [widgets/](widgets/) — the interactive answer widgets, one file per widget (e.g. `widgets/osLiczbowa.js` → `widgetOsLiczbowa`). In the repo **root-level directory** (one shared copy for all sheets), loaded before the `app/*.js` files because `loadExercises` (in `app/render.js`) reads `WIDZETY` (classic scripts sharing the global scope, so load order matters). **This directory is proprietary, not PolyForm** — see the licensing section below before you put anything in it. The shared plumbing deliberately lives *outside* it: `app/widget-helpers.js` (shared `wg*` helpers, loaded first of all) and `app/widget-registry.js` (the `WIDZETY` name→function registry, loaded right after the widget files); both were called `widgets/_helpers.js` / `widgets/_registry.js` until 2026-08-20.
- `exercises.json` (one per sheet, under `matura/<sheet-id>/`) — pure data: an object `{ meta, exercises }` (`meta` = per-sheet title/description/marking-key PDF; `exercises` = the array of exercise objects), `fetch`ed at startup by `startSheet()`. Interactive widgets are referenced by name (`"solutionWidget": "widgetX"` → the `WIDZETY` registry in `app/widget-registry.js`). All math in it is written in **KaTeX** (`\( ... \)` / `\[ ... \]`; schema + conventions documented in ARCHITECTURE.md — JSON has no comments).
- [style/](style/) — all styling (exam sheet + landing), shared by all sheets, split into `base.css` (variables/theme/reset), `sheet.css` (exam-sheet chrome), `landing.css` (index.html), `exam.css` (exam mode + open-exercise indicators) and `responsive.css` (breakpoints, must load last — cascade order matters). template.html loads all five; index.html only `base.css` + `landing.css`.

Plus `vendor/katex/` — KaTeX vendored for fully offline math rendering (don't edit those files; to bump the version replace them from the npm tarball) — `vendor/fonts/` — Lora + STIX Two Math vendored the same way (2026-08-09), replacing a `@import` from `fonts.googleapis.com` in `style/base.css`; the header comment in `vendor/fonts/fonts.css` explains the `unicode-range` requirement and which weights are (and aren't) carried, so read it before adding a font-family or weight anywhere in `style/` — and `tablica-wzorow.pdf` (shared formula sheet shown in a floating panel; stays in the root).

- **`tablica-wzorow-transkrypt/`** — transcript of that PDF (created 2026-07-28), **for models, not served to users**: one Markdown file per CKE section (`01-…` … `16-…`) plus `README.md`. Read it instead of the PDF whenever you need a formula — filling in `formulasPage`, checking a solution, writing hints. Start from `README.md`: its "Skorowidz" maps exercise wording ("nierówność wykładnicza", "pole trapezu") to a formula ID and page, so you load one 300–800-token section rather than the whole sheet. Formulas use the **same KaTeX delimiters as `exercises.json`** (`\( … \)` / `\[ … \]`), so they paste straight into exercises — just remember JSON needs `\\`. Each formula carries its PDF page (printed = physical, no offset) and a coarse position (`góra`/`środek`/`dół`). `README.md` has a **„Czego tu NIE MA"** section listing what the transcript does *not* carry (drawings/graphs → PDF pages 8, 11, 12, 15–28; section 17's trig value table → s. 34; front/back matter) — read it before concluding the formula sheet lacks something. Figures are rendered as **legends of symbols**, not descriptions of the drawing, and each affected section header says so with the PDF page to open. Verified 2026-07-28: every „•" bullet on pages 4–34 was listed from the PDF and matched one-to-one against transcript IDs (this caught one omission — `[8.10]` compound interest, since restored), all 795 formulas render in the vendored KaTeX, and every numerically checkable identity passes (26k random-value assertions).

## Task tracking

**The active TODO file is [TODO.md](TODO.md) — open items only.** The user (Henrich) checks it most often and curates priority himself (`WYSOKI`/`NISKI`/`NAJNIŻSZY PRIORYTET` sections) — don't edit those directly. Any new bug, idea, or task you want him to see goes under the **"DO REALZACJI Dopisane przez SONNETA LUB OPUSA"** section at the bottom, appended under your own model's subsection (`SONNET DOPISAŁ:` / `OPUS DOPISAŁ:`), in Polish. **Always check `TODO.md` before starting work and keep it in sync.**

**Done items do not stay in TODO.md.** When an item is completed, move it (marked `[DONE]`/`[ZROBIONE]` with the date and a short note on how it was solved) into the **current** file under [done/](done/) — see [done/README.md](done/README.md) for which file is current and the split rule (one file per merged partia, not per calendar period) — and delete it from TODO.md, so TODO.md stays short and cheap to load. **Do not read files under done/ by default** — open one only when you genuinely need project history: a broader view of the project, debugging a harder problem, or checking whether/how something was already solved before. Start from `done/README.md`'s tagged index rather than opening files blind. (Older names `todo1DONE.md`/`todo2.md`/`todo3.md`/`todo.md`/`todoDONE.md`/`TODODONE.md`/root `DONE.md` no longer exist — their content was merged/renamed/split into TODO.md and `done/`.)

## Git

### Gałęzie (układ z 2026-08-22)

Repozytorium ma dwie gałęzie robocze. Dawny `master` nazywa się dziś `main`.

| gałąź | gdzie ląduje | do czego służy |
|---|---|---|
| `dev` | GitHub Pages (`henrich2137.github.io/matematykazen/`) | codzienna praca: tu idą commity i pushe, tu Henrich testuje |
| `main` | Cloudflare, czyli `matematykazen.pl` | wersja oficjalna, zwykle kilka commitów za `dev` |

- **„Push" bez dopowiedzenia zawsze znaczy push na `dev`.** Nowej gałęzi nie zakładasz, chyba że Henrich wyraźnie o to poprosi. Wypuszczenie zmiany na `main`, czyli pod domenę, robisz **tylko wtedy, gdy Henrich powie to wprost**: „ma być widoczne publicznie", „wypuść dla użytkowników", „na produkcję", „na domenę" i podobnie. Sam z siebie nie awansujesz niczego na `main`, nawet jeśli praca wygląda na skończoną, i w razie wątpliwości pytasz.
- **Na `main` nic nie commitujesz wprost.** Wchodzi tam wyłącznie to, co jest już na `dev`, i tylko przez awans:
  ```
  git checkout main && git merge --ff-only dev && git push && git checkout dev
  ```
  Lokalna gałąź `main` ma `--ff-only` ustawione na stałe (`branch.main.mergeOptions`), więc git odmówi, gdyby scalanie miało zrobić commit scalający. Odmowa oznacza, że `main` ma coś, czego nie ma `dev`: zatrzymaj się i zapytaj, niczego nie forsuj.
- **Stara nazwa już nie istnieje.** `origin/master` zniknął; `origin/master-old` to archiwum sprzed lipca 2026 i tam nie zaglądasz.

- **Na starcie sesji sprawdź, czy klon nie jest do tyłu — jeśli jest, zrób `pull` ZANIM zaczniesz pracę.** Odkąd zadanie startowe robi już tylko `fetch` (2026-08-15), nic nie scala samo, więc `dev` bywa kilkadziesiąt commitów w plecy, a Ty edytujesz nieaktualne pliki. To jest **Twoje zadanie, nie Henricha** — on nie ma tego pamiętać.
  - `git fetch && git rev-list --left-right --count HEAD...@{u}` → wynik `0<TAB>0` znaczy „jesteś na bieżąco". Pierwsza liczba = commity lokalne, druga = commity czekające na origin. (`@{u}` to gałąź śledzona, czyli `origin/dev`, gdy siedzisz na `dev`.)
  - Druga liczba > 0 i brak własnych zmian → `git pull --ff-only`. Na hoście przechodzi zawsze.
  - **W kontenerze** pull może paść na read-only `.devcontainer/`/`.vscode/` (patrz punkt niżej). Jeśli padnie — nie kombinuj i nie kasuj niczego, tylko powiedz Henrichowi, żeby zrobił pull z hosta.
  - Masz na to **stałą zgodę** — `fetch`/`pull --ff-only` w tym repo to nie jest „polecenie sieciowe do uzgodnienia" z HOSTRULES.md. Pierwsza liczba > 0 (lokalne commity) albo brudne drzewo robocze → **zatrzymaj się i zapytaj**, nic nie nadpisuj.
- **gitdoc is DISABLED** (verified 2026-08-01) — no auto-commits, no auto-push. Every commit in the log is a human's or the assistant's.
- **Auto-fetch is on, auto-pull is not** (`git.autofetch` + a `git fetch --prune` task on folder open). Fetch never touches the working tree, so local `dev` can be many commits behind at session start — check, and **merge only by hand**. The folderOpen task used to run `git pull --ff-only`; it was replaced 2026-08-15 because inside the devcontainer it kept aborting half-way on the read-only `.devcontainer/`/`.vscode/` mounts, leaving the files updated but HEAD stale (looks like dozens of phantom local changes). Symptom and safe repair in [issues/git-i-gitdoc.md](issues/git-i-gitdoc.md) — don't switch it back to `pull`.
- **`.vscode/` and `.devcontainer/` are mounted read-only in the devcontainer** — edit them from the host; a `checkout`/`pull` touching them from inside the container half-fails (see `.devcontainer/README.md`).
- Mechanics of all three (why gitdoc can only be enabled per-workspace, what would happen if it were re-enabled, `forcePush`, the `autoCommitDelay` debounce, the `task.allowAutomaticTasks` requirement): [issues/git-i-gitdoc.md](issues/git-i-gitdoc.md).

## Oddawanie pracy do testów (added 2026-08-09)

Zasady od Henricha, po pierwszej paczce, w której każda z nich została złamana. Dotyczą momentu, w którym kończysz porcję pracy i mówisz „sprawdź".

- **Rzeczy do sprawdzenia przez Henricha piszesz w DWÓCH miejscach: w oknie czatu i w `TODO.md` w sekcji `TESTOWANIE HENRICH:`.** Nie zakładaj na to osobnego pliku w `issues/` — Henrich tam nie zagląda, a `TODO.md` czyta najczęściej. (Plik `issues/do-sprawdzenia.md` istniał krótko 2026-08-09 i został z tego powodu usunięty.) Wpis ma mówić, co kliknąć i czego szukać — nie streszczać zmiany. Zasady formatowania tych wpisów są w TODO.md, sekcja „ZASADY DLA CLAUDE-A".
  - **Próg wejścia jest wysoki (zaostrzony 2026-08-20).** Wpis wchodzi tam tylko wtedy, gdy przechodzi **oba** sita: (1) nie da się tego sprawdzić w sesji, skryptami z `tools/` ani Playwrightem, (2) Henrich **nie natrafi na to przypadkiem**, korzystając ze strony normalnie. Ciemny motyw, skrajne położenia suwaków, blokady przeciągania, słabe łącze, telefon: tak. „Czy widżet się rysuje", „czy odczyt pokazuje wynik": nie, bo to widać przy pierwszym kliknięciu. Sekcja ma mieścić się na ekranie (około dwudziestu punktów); dokładając nowy wpis, wyrzuć albo zarchiwizuj któryś stary. Pełne scenariusze do przejścia kiedyś idą do [issues/testowanie-archiwum.md](issues/testowanie-archiwum.md), nie do TODO.md.
- **Zanim oddasz cokolwiek do testów, a już zwłaszcza na telefonie: podbij numer wersji, zacommituj i zsynchronizuj z `origin`.** Bez pusha Henrich ogląda na telefonie starą stronę i szuka błędu, którego nie ma. Bez podbitej wersji nie ma jak stwierdzić, którą wersję właściwie widzi. Numer siedzi w dwóch miejscach naraz — `#wersja` w `template.html` i `.landing-wersja` w `index.html` — i musi się zgadzać w obu. **Podbijaj wersję głównie przed czymś, co Henrich ma faktycznie przetestować w przeglądarce** (zmiana widoczna na stronie) — po zmianach, które strony jako takiej nie dotyczą (np. porządki w repo, dokumentacja, konfiguracja gita), podbicie można pominąć.
- **Granulacja commitów: jedna paczka zmian = jeden commit**, nawet jeśli dotyka wielu plików i jest duży. Rozdzielaj dopiero wtedy, gdy tematyka naprawdę się rozjeżdża (instalacja Playwrighta ≠ transkrypt tablicy wzorów). Zmiana wyglądu strony obejmująca HTML i CSS naraz to jeden commit, nie trzy.

## Commit attribution (added 2026-08-09)

Every commit (local or cloud) gets a `Co-Authored-By:` trailer in the form **`Local/Cloud Model Effort`** — e.g. `Co-Authored-By: Local Opus 5 Medium <noreply@anthropic.com>` or `Co-Authored-By: Cloud Sonnet 5 High <noreply@anthropic.com>`. No prefix in the commit message/subject — that convention was dropped in favor of this trailer.

## Claude Code — plugins / skills

`.claude/settings.json` (tracked) enables the **superpowers** plugin at scope `project`, so it travels with the repo; its 14 skills (`brainstorming`, `systematic-debugging`, `writing-plans`, …) only appear **after a Claude Code session restart**. Install details, the marketplace-cache search trap and why `vendor/superpowers/` holds no plugin code: [issues/claude-code-pluginy.md](issues/claude-code-pluginy.md).

## Test przed implementacją, ale tylko przy trudnych zmianach (dodane 2026-08-21)

**Zasada dotyczy WYŁĄCZNIE zmian, w których naprawdę grozi błąd.** Przy takiej zmianie kolejność jest stała: (1) zaprojektuj test, (2) wprowadź zmianę, (3) odpal test i pokaż wynik. Przy wszystkim pozostałym testu się NIE pisze, bo powstaje skrypt, którego nikt nigdy więcej nie odpali.

- **Kiedy test jest obowiązkowy** (wystarczy jeden z tych warunków):
  - zmiana w logice, która ma stan albo czas: odtwarzacz kroków (`app/steps.js`), tryb egzaminu z timerem, zapis w localStorage,
  - sprawdzanie odpowiedzi i logika widżetów, czyli wszystko, co decyduje „dobrze/źle",
  - coś, co już raz się popsuło, albo poprawka błędu: test ma najpierw odtworzyć ten błąd,
  - zmiana dotykająca wielu zadań albo wielu arkuszy naraz, gdzie ręczne klikanie po prostu nie obejdzie wszystkiego,
  - błąd niewidoczny gołym okiem: rozjazd o jeden krok, wyścig przy wolnym łączu, zły plik w kadrze.
- **Kiedy testu NIE piszesz**: treść zadań, teksty, dokumentacja, CSS i wygląd, drobne poprawki w jednym miejscu, porządki w repo. Tu wystarczy otworzyć stronę i kliknąć, a przy zmianach wizualnych zrzuty przed/po z [tools/zrzuty.js](tools/zrzuty.js).
- **Test ma najpierw padać.** Puść go przed zmianą i sprawdź, że świeci na czerwono. Test, który przechodzi od razu, niczego nie pilnuje.
- **Czym testować** (nie ma tu frameworka testowego): [tools/test-krokow.js](tools/test-krokow.js) dla odtwarzacza kroków, [tools/statystyki.py](tools/statystyki.py) dla danych w `exercises.json`, a poza tym krótki skrypt Playwrighta. Jeżeli taki skrypt przyda się jeszcze raz, dołóż go do `tools/` zamiast zostawiać w `/tmp`.
- **Po zmianie odpal test i wklej przebieg.** Nie pisz „działa" bez wyniku. Test padł, to zmiana nie jest skończona.
- **Nie da się tego sprawdzić skryptem? Powiedz wprost jednym zdaniem** ("tego nie sprawdzę skryptem, bo ...") i dopiero wtedy rozważ wpis do `TODO.md` w sekcji `TESTOWANIE HENRICH:` wg progu z sekcji wyżej.

## Running / previewing

No build or test tooling. **Serve the directory with a static file server** (e.g. `npx serve`, `python -m http.server`) — since the exercises.json migration the exam page loads its data with `fetch`, which does not work over `file://` (the page then shows a message explaining exactly this; index.html alone still opens fine from a file). No linter/test suite — verify changes by opening the page and clicking through the exercise(s) you touched.

**Wyjątek — praca nad wideo: `python3 -m http.server` NIE nadaje się.** Nie obsługuje żądań zakresowych (`Range`), a bez nich przeglądarka nie potrafi przewinąć filmu: `video.seekable` zostaje puste, a każde ustawienie `currentTime` cicho wraca do zera. Wygląda to jak błąd w kodzie odtwarzacza kroków i raz już nim nie było (2026-08-11). Do wszystkiego, co przewija film — kropki, rewersy — użyj **[tools/serwer.js](tools/serwer.js)** (`node tools/serwer.js 8000`; obsługuje `Range`, nie wymaga sieci) i sprawdź, że `curl -r 0-100` na plik wideo zwraca **206**, nie 200. Ten sam skrypt umie dławić łącze (`--wolno=<ms> --bps=<bajty/s>`, tylko na plikach wideo) — bez tego cała klasa błędów odtwarzacza jest niewidoczna, bo na localhoście krok podmienia się w milisekundach. Szczegóły w [issues/krok-po-kroku-produkcja.md](issues/krok-po-kroku-produkcja.md).

Odtwarzacz kroków ma też własny test: **[tools/test-krokow.js](tools/test-krokow.js)** (Playwright) okłada sterowanie losowymi kliknięciami i pilnuje niezmienników, których okiem nie widać — czy film w kadrze zgadza się z licznikiem i czy odtwarzacz dochodzi do spoczynku. Puść go po każdej zmianie w `app/steps.js`, na szybkim i na zdławionym serwerze. Chromium w tym kontenerze **odtwarza H.264**, więc testuje się wprost na plikach arkusza (notatka o braku kodeka z 2026-08-11 dotyczyła kontenera chmurowego).

Inside the devcontainer there **is** a browser: Playwright + Chromium, for screenshotting your own visual/CSS changes. The browser binary is not downloaded in the container (the firewall blocks Playwright's CDN) — it comes from a read-only bind of the host's `~/.cache/ms-playwright`, and its version is pinned in `.devcontainer/Dockerfile`. See [issues/playwright-podglad.md](issues/playwright-podglad.md) for usage and how to bump the version.

Don't hand-roll a Playwright script for routine visual work — [tools/zrzuty.js](tools/zrzuty.js) already takes the standard set (arkusz / landing / sidebar / exam mode × desktop + phone × light + dark) into `/tmp/zrzuty/<label>/`, so two runs can be compared frame by frame. Its header documents the flags and the two traps that make screenshots silently lie (the mandatory `NODE_PATH`, and the theme key/class mismatch it now guards against).

## Hosting (dodane 2026-08-22)

Strona stoi w dwóch miejscach naraz, z tego samego repozytorium, każde z innej gałęzi:

| adres | hosting | gałąź | rola |
|---|---|---|---|
| `matematykazen.pl` i `www.matematykazen.pl` | Cloudflare (Worker serwujący same pliki statyczne) | `main` | adres oficjalny, ten podawany uczniom |
| `henrich2137.github.io/matematykazen/` | GitHub Pages | `dev` | wersja robocza do testów |

Domena kupiona u rejestratora hitme, obsługiwana przez serwery nazw Cloudflare; certyfikat HTTPS wystawia Cloudflare. **Obie postacie adresu działają**, z www i bez, i obie pokazują tę samą stronę.

Cztery pliki w korzeniu obsługują wariant Cloudflare: `wrangler.jsonc` (ustawienia wdrożenia), `.assetsignore` (czego nie wysyłać), `_headers` (nagłówki HTTP), `404.html` (własna strona błędu, działa też na GitHub Pages).

- **Dokładasz albo przenosisz plik potrzebny stronie w przeglądarce? Odpal `python3 tools/sprawdz-cloudflare.py`.** Skrypt pilnuje limitów Cloudflare (25 MiB na plik) i tego, żeby `.assetsignore` nie wyciął czegoś, bez czego strona się sypie. Cichy, gdy wszystko gra.
- **Nie wpisuj w kodzie ścieżek od korzenia** (`/style/...`, `/app/...`). Na Cloudflare strona leży w korzeniu domeny, a na GitHub Pages w podkatalogu, więc taka ścieżka działa tylko w jednym z tych miejsc. Wszystkie odwołania są dziś względne i mają takie zostać.
- **To, co wypchniesz na `dev`, nie pojawi się od razu na `matematykazen.pl`.** Domena jedzie z `main`, więc zmiana widoczna pod domeną wymaga osobnego scalenia, które robi Henrich (patrz sekcja Git). Prosząc go o test na telefonie, powiedz wprost, pod którym adresem ma patrzeć.
- Reszta (dlaczego Worker, a nie Pages; co dokładnie odsiewamy i czego odsiewać nie wolno; co Henrich klikał w panelu Cloudflare i u rejestratora domeny): [issues/cloudflare-hosting.md](issues/cloudflare-hosting.md).

## Content notes

- All user-facing content and code comments are Polish; keep new content in Polish, direct exam-prep tone.
- **Nie używaj pauzy ani półpauzy (znaki `—` i `–`), nawet w zwykłych zdaniach.** Zamiast nich przecinek, dwukropek, kropka albo nawias; przy wyliczeniach zwykły dywiz `-`. Obowiązuje wszędzie: treść dla ucznia, komentarze w kodzie, dokumentacja, opisy commitów, odpowiedzi w czacie. Powód nie jest taki, że pisanie modelem jest czymś złym. Po prostu ten znak kojarzy się czytelnikom z tekstem wklejonym na odczepnego, więc psuje wrażenie niezależnie od tego, jak dobra jest treść pod spodem. (W opisach kroków pod filmem obowiązuje osobny, ostrzejszy zakaz: żadnych myślników ani podkreśleń poza wzorami, bo czytają się jak minus. Patrz `manimations/README.md`.)
- Videos are now rendered **inside the devcontainer** (Manim + TeX Live live in the image) — see `manimations/README.md`. The old 5⁻⁴ defect in `zad2rozw_step6.mp4` was a typo in the scene, fixed 2026-08-11.
- **Step-by-step solutions have their own house rules, given by Henrich and written down in [manimations/README.md](manimations/README.md)** — three for the animation (a step's last frame must equal the next step's first frame; movement must follow the arithmetic, so pair glyphs explicitly instead of trusting `TransformMatchingShapes`; colour marks only what the student should look at) and five for the `text` under the film (don't narrate what the film already shows; explain in plain language rather than textbook phrasing; short lines with formulas on their own; a boxed `\[ … \]` formula only if it is actually in the formula sheet; no dashes or underscores outside formulas, they read as a minus). Read that section before writing a scene or a step description.


## User notes

- Ostrzegaj mnie przed włączeniem ciężkiego zadania np subagent-heavy sessions, które ostatnio wciągnęły mi 60% session limit dosyć szybko gdy robiłem code-review ultra
- Odpowiadaj zwięźle — krótsze wypowiedzi, mniej technicznego żargonu; tłumacz pojęcia techniczne prostymi słowami zamiast zakładać, że są znane.
- **Pisz prosto — to jest ważniejsze niż precyzja techniczna.** Henrich jest nauczycielem matematyki, nie inżynierem od kontenerów. Zasady:
  - **Zacznij od tego, co to znaczy DLA NIEGO**, a dopiero potem (i tylko jeśli trzeba) jak to działa pod spodem. Nie odwrotnie.
  - **Nie wklejaj surowych nazw z systemu jako wyjaśnienia.** `CapEff: 0000...0`, `GITHUB_PERSONAL_ACCESS_TOKEN`, `--cap-drop=ALL` to nie jest odpowiedź na pytanie „czy jest bezpiecznie". Jeśli nazwa musi paść (bo trzeba coś wkleić w terminal), najpierw powiedz zwykłym zdaniem, co to jest.
  - **Używaj porównań z życia** zamiast definicji. Klucz do mieszkania, zapasowe koło, zamknięte drzwi — to działa lepiej niż poprawna definicja.
  - **Jedna myśl na punkt.** Jeśli w punkcie są trzy średniki i nawias, to jest za długi.
  - **Kończ zdaniem, co z tym zrobić**: „nic nie musisz", „to jedna komenda u Ciebie", „daj znać, zrobię".
  - Techniczne szczegóły i dowody idą do plików (`issues/`, `done/`) — tam mają być dokładne. W czacie ma być zrozumiale.
- Gdy treść do tego pasuje (wyjaśnienia, oceny, listy opcji, podsumowania), prezentuj informacje w punktach w stylu TODO.md — pogrubiony nagłówek/tytuł punktu, pod nim zagnieżdżone podpunkty z detalami — zamiast ciągłej prozy z nagłówkami. Tabelki i inne wizualne reprezentacje też mile widziane, jeśli pasują do treści. W takich zestawieniach można też używać kolorowych emotikonek jako oznaczeń stanu/oceny (np. ❌/✅ dla „niepotrzebne"/„potrzebne", „nie działa"/„działa"). ⭐ tylko dla faktycznej skali ocen (np. „4/5 gwiazdek") — NIE jako zamiennik neutralnego/nieokreślonego stanu. Do stanu neutralnego/„zależy od Ciebie" używaj 🟨 (żółty kwadrat) — trzeci stan obok ✅/❌. Nie dotyczy to nastrojowych emotikon/buźek (np. :), 🙂) — tych unikaj zawsze, także w punktach/tabelkach. Poza oznaczeniami stanu/oceny obowiązuje domyślny zakaz emoji z sekcji "Tone and style".

## Cloud sessions / routines

- Pushuj na `dev` (gałąź codziennej pracy, patrz sekcja Git) zamiast tworzyć nową gałąź. Samo „zrób push" nigdy nie znaczy `main`: tam idzie tylko to, o czym użytkownik wprost powie, że ma być widoczne publicznie dla zwykłych użytkowników.
- Nie zaglądaj do brancha `backup-przed-squash-gitdoc` (lokalnie ani `origin/`) — to tylko archiwalny backup sprzed squasha autozapisów gitdoc. Wyjątek: gdy chcesz sprawdzić bardzo szczegółową historię automatycznych commitów generowanych przez gitdoca.