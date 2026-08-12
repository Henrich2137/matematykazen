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

## vendor/superpowers/

Zawiera tylko `LICENSE` (MIT) + `NOTICE.md` — miejsce na skille, które kiedyś ewentualnie
zostaną skopiowane i dostrojone. Świadomie **nie ma tam kodu pluginu**; nie kopiuj go tam
„dla porządku".
