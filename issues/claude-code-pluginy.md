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

- **Nie działa dziś w tym kontenerze** — `EACCES` przy zapisie do `~/.cache`, wymaga
  Rebuild Container po zmianie w `.devcontainer/Dockerfile`. Pełna diagnoza, przyczyna
  i warianty naprawy: [chrome-devtools-mcp-cache-eacces.md](chrome-devtools-mcp-cache-eacces.md).

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
- Do naprawy: ustawić `GITHUB_PERSONAL_ACCESS_TOKEN` w środowisku kontenera (np.
  `containerEnv` w `devcontainer.json`, albo `.bashrc`) — wartością może być świeży PAT
  z uprawnieniami repo, albo `$(gh auth token)`, jeśli ma wystarczyć do repo/issues/PR.
  Świadomie NIE zrobione automatycznie w tej sesji — to wstawienie/przechowywanie
  sekretu, decyzja do Henricha.

## vendor/superpowers/

Zawiera tylko `LICENSE` (MIT) + `NOTICE.md` — miejsce na skille, które kiedyś ewentualnie
zostaną skopiowane i dostrojone. Świadomie **nie ma tam kodu pluginu**; nie kopiuj go tam
„dla porządku".
