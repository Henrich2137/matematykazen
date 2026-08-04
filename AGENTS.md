# AI agent instructions for MatematykaZen

This repository is a static, frontend-only teaching site for Polish matura exam sheets.

## What matters most

- The app is pure HTML/CSS/JavaScript with no bundler or package manager.
- Serve files over HTTP when testing: `npx serve` or `python -m http.server`.
- `template.html` is the single renderer for all sheets.
- Sheet data lives in `matura/<sheet-id>/exercises.json`.
- Media files are referenced relative to the sheet folder and resolved by `app/state.js`.
- Widget scripts in `widgets/` must load before `app/*.js` because they share a global scope.
- `ARCHITECTURE.md` and `ARCHITECTURE_CSS.md` explain the page structure, data schema, and style rules.
- `matura/README.md` is the source of truth for which sheets exist and how sheet folders are organized.

## What to avoid

- Do not introduce npm dependencies or build tooling.
- Do not duplicate or hardcode content that belongs in `ARCHITECTURE.md`, `ARCHITECTURE_CSS.md`, or `matura/README.md`.
- Do not change KaTeX vendor files in `vendor/katex/`.
- Do not add sheet-specific paths directly into the renderer; use the sheet-relative `media/…` convention and `mediaPath()`.

## Useful files

- `template.html` — common page template for all exam sheets
- `index.html` — landing page linking to sheets
- `app/` — rendering and app logic
- `widgets/` — interactive solution widgets
- `style/` — CSS for layout, sheet, landing, exam mode, and responsive rules
- `ARCHITECTURE.md` / `ARCHITECTURE_CSS.md` — architecture and style reference
- `README.md` / `CONTRIBUTING.md` — repo overview and contribution conventions
- `.github/copilot-instructions.md` — session-specific assistant behavior guidance
