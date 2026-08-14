# Claude Code — pluginy i skille w tym repo

Opis konstrukcji, nie problem. Wyniesione z CLAUDE.md 2026-08-12 — szczegóły instalacji
przydają się raz na kilka miesięcy, nie co sesję. CLAUDE.md ma z tego dwie linijki.
Kontekst zrobienia: `done/04-biezace.md`, wpis 2026-08-07.

## Deklaracja w repo

`.claude/settings.json` jest śledzony przez gita i deklaruje `enabledPlugins`, więc plugin
jedzie razem z repo:

```json
{ "enabledPlugins": { "superpowers@claude-plugins-official": true } }
```

## superpowers

[obra/superpowers](https://github.com/obra/superpowers), MIT, Jesse Vincent — 14 skilli
(`brainstorming`, `systematic-debugging`, `test-driven-development`, `writing-plans`,
`using-git-worktrees`, …).

- Zainstalowany w **scope `project`**, świadomie nie `user`: ma dotyczyć tego repo,
  a nie każdego projektu Henricha.
- Z oficjalnego marketplace'u Anthropic `claude-plugins-official`, nie z upstreamowego
  `superpowers-marketplace`. Oficjalny wpis przypina SHA (`44c9b2d` = v6.2.0) — sprawdzone
  2026-08-07: to dokładnie ten sam commit co ówczesny HEAD upstreamu, więc przypięcie nic
  nie kosztuje, a chroni przed podmianą kodu pod tagiem.
- **Pułapka przy szukaniu**: superpowers **nie jest** podkatalogiem w lokalnym cache'u
  marketplace'u (`~/.claude/plugins/marketplaces/claude-plugins-official/`) — ani w `plugins/`,
  ani w `external_plugins/`, bo jego wpis w `marketplace.json` używa źródła `url`, klonowanego
  dopiero przy instalacji. `ls` po tych katalogach fałszywie sugeruje, że pluginu nie ma
  (na to nabrałem się 2026-08-07).
- Kod pluginu siedzi w cache'u użytkownika (`~/.claude/plugins/cache/…`), **nie w repo** —
  świeża maszyna musi go ściągnąć z GitHuba. W kontenerze to przechodzi przez firewall
  (zakresy GitHuba są na allowliście).
- Instaluje **hook `SessionStart`** (`startup|clear|compact`, synchroniczny), uruchamiany przy
  każdym starcie sesji, `/clear` i kompaktowaniu.
- Skille pojawiają się dopiero **po restarcie sesji Claude Code**.

## frontend-design

Zainstalowany 2026-08-13 (Henrich, `/plugin`) w kontenerze na Bazzite — jeden skill
(`frontend-design:frontend-design`, wskazówki do wyglądu/UI).

- W odróżnieniu od superpowers, włącznik wylądował w **`.claude/settings.local.json`**
  (scope `project`, ale plik lokalny/nieśledzony), nie w `.claude/settings.json` — więc
  deklaracja **nie jedzie z repo**, zostaje tylko na tej maszynie/tym devcontainerze.
  Świadomie dodany wpis do `.gitignore` (`.claude/settings.local.json`), żeby ten plik
  nie trafił do gita przez przypadek na innej maszynie bez globalnego gitignore Henricha.
- Kod pluginu leży tak samo jak superpowers: w cache'u na wolumenie
  `matematykazen-claude-config` (`~/.claude/plugins/cache/…`), nie w repo.
- Jeśli ma zacząć jechać z repo (jak superpowers), trzeba ręcznie przenieść wpis
  `"frontend-design@claude-plugins-official": true` do `.claude/settings.json`.

## chrome-devtools-mcp

Zainstalowany 2026-08-13 (Henrich, `/plugin`) w kontenerze na Bazzite, tak samo lokalnie
jak frontend-design (`.claude/settings.local.json`, poza gitem). MCP server (`npx
chrome-devtools-mcp@1.7.0`), 5 skilli (debugowanie ogólne, a11y, LCP, wycieki pamięci,
troubleshooting).

- **`EACCES` przy zapisie do `~/.cache`** — naprawione w `.devcontainer/Dockerfile`
  2026-08-14 (`/home/node/.cache` zakładane w obrazie i chownowane na `node`),
  potwierdzone po Rebuild Container tego samego dnia.
- **Nadal nie otwiera strony, ale z innego powodu**: w kontenerze nie ma Google Chrome'a
  (`Could not find Google Chrome executable for channel 'stable'`), jest tylko Chromium
  Playwrighta. Warianty wyjścia — własny wpis serwera w repo z `--executablePath` albo
  Chrome w obrazie — w [chrome-devtools-mcp-cache-eacces.md](chrome-devtools-mcp-cache-eacces.md).
  Do zrzutów ekranu i tak używa się `tools/zrzuty.js` (Playwright), więc to nie blokuje pracy.

## github

Zainstalowany 2026-08-13 (Henrich, `/plugin`), lokalnie jak wyżej. Oficjalny zdalny MCP
server GitHuba (`https://api.githubcopilot.com/mcp/`, HTTP, nie stdio).

- **`claude mcp list` pokazuje „✘ Failed to connect — HTTP 400: Authorization header
  badly formatted"**.
- Przyczyna: konfiguracja pluginu (`.mcp.json` w cache'u pluginu) wysyła nagłówek
  `Authorization: Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}` — ta zmienna środowiskowa
  **nie jest ustawiona** w kontenerze, więc nagłówek wychodzi jako `Bearer ` (pusty token).
- To **inny mechanizm logowania niż `gh auth login`** — `gh` ma już własny, działający
  token (`gh auth status` → zalogowany jako Henrich2137), ale ten plugin go nie czyta,
  bo to osobny serwer MCP, nie wrapper na `gh` CLI. `claude mcp login` też nie pomaga —
  ten serwer autoryzuje się statycznym nagłówkiem z configu, nie OAuth-em.
- **Naprawione w `.devcontainer/Dockerfile` 2026-08-14** (Opus 5, medium, decyzja Henricha),
  potwierdzone po Rebuild Container tego samego dnia — `claude mcp list` pokazuje `github`
  jako ✔ Connected (przy pierwszym wywołaniu potrafi zwrócić „tools fetch failed — timeout",
  drugie przechodzi). Do `~/.zshrc` i `~/.bashrc` dopisywany jest
  `export GITHUB_PERSONAL_ACCESS_TOKEN="$(cat ~/.config/gh/mcp-token 2>/dev/null || gh auth token 2>/dev/null)"`.
  - W repo **nie ma sekretu** — jest polecenie, które czyta token lokalnie. U kogoś innego
    zwróci jego własny token albo pustkę, więc klon repo nie dostaje niczyich uprawnień.
  - Domyślne źródło to zwykłe logowanie `gh`, czyli **pełne uprawnienia Henricha**, i po
    eksporcie widzi je każdy proces w kontenerze, nie tylko plugin. Żeby zawęzić, wystarczy
    położyć wąski fine-grained PAT w `~/.config/gh/mcp-token` (wolumen
    `matematykazen-gh-config`, poza gitem) — ma pierwszeństwo przed `gh auth token`.
  - Gdy `gh` nie jest zalogowany i pliku nie ma, zmienna wychodzi pusta i jest jak dotąd.
  - Jeśli po przebudowie `claude mcp list` dalej pokazuje 400, sprawdź `echo
    $GITHUB_PERSONAL_ACCESS_TOKEN` w tym samym terminalu — pusto oznacza brak logowania
    `gh`, a nie błąd w tej konstrukcji.

## vendor/superpowers/

Zawiera tylko `LICENSE` (MIT) + `NOTICE.md` — miejsce na skille, które kiedyś ewentualnie
zostaną skopiowane i dostrojone. Świadomie **nie ma tam kodu pluginu**; nie kopiuj go tam
„dla porządku".
