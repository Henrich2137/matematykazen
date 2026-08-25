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

## Wszystko przeniesione do scope `project` (2026-08-25)

Na prośbę Henricha wszystkie cztery pluginy siedzą dziś w scope `project`, czyli w śledzonym
`.claude/settings.json`. `.claude/settings.local.json` ma już puste `enabledPlugins` i trzyma
wyłącznie ustawienia sandboxa.

Powód: `local` nie przeżywa przeprowadzki na inną maszynę, bo plik jest w `.gitignore`.
Po tej zmianie świeży klon wie, które pluginy mają być włączone, i kod dociąga się do cache'u
sam, tak jak od początku robił to `superpowers`.

Przeniesienie zrobione przez CLI, nie ręczną edycją JSON-a, żeby zgadzał się też zapis
instalacji w `~/.claude/plugins/installed_plugins.json`:

```sh
claude plugin install <nazwa>@claude-plugins-official --scope project -y
claude plugin uninstall <nazwa>@claude-plugins-official --scope local -y
```

**Uwaga na duplikaty:** sama instalacja w `project` NIE kasuje starego wpisu `local` —
`claude plugin list` pokazuje wtedy ten sam plugin dwa razy, raz z każdym scope. Dopiero
`uninstall --scope local` porządkuje listę.

**Co dalej zostaje per maszyna:** deklaracja jedzie z repo, ale środowisko nie. `github` dalej
wymaga `gh auth login` na każdej nowej maszynie (patrz sekcja niżej), a `chrome-devtools-mcp`
dalej nie ma w tym kontenerze przeglądarki Chrome. Tabelka poniżej opisuje stan sprzed tej
zmiany i została dla historii.

## Świeży kontener gubi pluginy — jak je wrócić (2026-08-15)

Sprawdzone w kontenerze, w którym z czterech pluginów działał tylko `superpowers`. Nie był
to regres w konfiguracji, tylko **normalna konsekwencja tego, gdzie co leży** — warto znać,
bo powtórzy się przy każdym świeżym wolumenie/nowej maszynie.

Co ginie i dlaczego:

| Plugin | Deklaracja | Czy jedzie z repo | Co trzeba zrobić |
|---|---|---|---|
| `superpowers` | `.claude/settings.json` (śledzony) | ✅ tak | nic — cache dociąga się sam |
| `frontend-design` | `.claude/settings.json` (śledzony) | 🟨 deklaracja tak, kod nie | `claude plugin install frontend-design@claude-plugins-official --scope project -y` |
| `chrome-devtools-mcp` | `.claude/settings.local.json` (**w `.gitignore`**) | ❌ nie | `claude plugin install chrome-devtools-mcp@claude-plugins-official --scope local -y` |
| `github` | `.claude/settings.local.json` (**w `.gitignore`**) | ❌ nie | jak wyżej, `--scope local`, plus logowanie `gh` |

**Kluczowa obserwacja:** sama deklaracja w `settings.json` nie wystarcza — kod pluginu żyje
w cache'u użytkownika (`~/.claude/plugins/cache/`), poza repo. Włączony plugin bez kodu
w cache'u po prostu nie ma skilli, choć `enabledPlugins` mówi `true`. `claude plugin list`
pokazuje wtedy tylko to, co faktycznie jest zainstalowane — to jest wiarygodne źródło, nie
plik ustawień.

Instalacja z CLI (`claude plugin install … --scope project|local -y`) odtwarza dokładnie ten
sam podział plików co ręczne `/plugin`: `project` → `settings.json`, `local` →
`settings.local.json`. Sprawdzone — `git status` po instalacji został czysty.

**Pluginy wchodzą dopiero po restarcie sesji.** Serwery MCP da się przetestować od razu,
bez restartu, ręcznym klientem po stdio (jak w
[chrome-devtools-mcp-cache-eacces.md](chrome-devtools-mcp-cache-eacces.md)).

### Kolejność przy `github`: logowanie PRZED restartem

`gh auth login` jest interaktywne, więc robi to Henrich (`! gh auth login` w sesji).
Kolejność ma znaczenie i łatwo ją odwrócić:

1. najpierw `gh auth login`,
2. potem restart Claude Code.

Bo `GITHUB_PERSONAL_ACCESS_TOKEN` powstaje przy starcie powłoki (`~/.zshrc`/`~/.bashrc`),
a proces Claude Code dziedziczy środowisko z momentu swojego startu. Zalogowanie się **po**
restarcie nie wypełni zmiennej w już działającym procesie i plugin dalej zwróci HTTP 400 —
wygląda to jak niedziałająca naprawa, a jest tylko złą kolejnością.

Wolumen `matematykazen-gh-config` jest zapisywalny, ale w świeżym kontenerze bywa pusty
(`~/.config/gh/` bez `hosts.yml`) — to znak, że logowania nie było, nie że coś się zepsuło.

### Wersja superpowers idzie w górę sama

Marketplace przypina SHA i ten SHA **się zmienia**: 2026-08-07 było `44c9b2d` (6.2.0),
2026-08-15 jest `b36e082` (6.3.0). Po `claude plugin details superpowers` cache dociąga
nowszą wersję i `claude plugin list` pokazuje już 6.3.0, obok starego katalogu 6.2.0.
`claude plugin update superpowers` odpowiedziało przy tym `✘ … not found`, choć pobranie
się udało — **komunikat jest mylący, sprawdzaj katalogi w cache'u, nie jego treść**.
Oba katalogi (6.2.0 i 6.3.0) mają pełne 14 skilli.

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

### Decyzja Henricha 2026-08-14: zostawiamy szeroki token

Pytanie padło wprost i warto mieć odpowiedź pod ręką, zamiast odtwarzać ją za pół roku.

- **Czy klucz istnieje tylko przy zalogowanym `gh`?** Tak. Nigdzie nie jest zapisany na
  stałe — powstaje przy każdym starcie powłoki z `gh auth token`. Po wylogowaniu zmienna
  wychodzi pusta i przestaje działać sama wtyczka, nic poza nią.
- **Czy klon repo daje dostęp do konta Henricha?** Nie. W repo leży polecenie, nie sekret;
  u kogoś innego sięgnie po jego własny token albo po nic. Zweryfikowane 2026-08-14
  przeszukaniem **całej historii** repo pod kątem wzorca `gh[pousr]_…` — zero trafień
  (`git grep -E "gh[pousr]_[A-Za-z0-9]{20,}" $(git rev-list --all)`). Warto powtórzyć ten
  jednolinijkowiec, jeśli kiedyś pojawi się podejrzenie wycieku.
- **Zawężenie do fine-grained PAT odłożone** — świadomie, jako nieproporcjonalne do
  ryzyka na tym etapie. Furtka (`~/.config/gh/mcp-token`) jest gotowa i działa bez żadnej
  przebudowy, więc decyzję da się odwrócić w każdej chwili. Realne ryzyko, gdyby wracać do
  tematu: token ma pełne uprawnienia (`repo`, `workflow`, `gist`, `read:org`) i widzi go
  każdy proces w kontenerze, więc wystarczyłaby jedna wroga zależność npm.

## vendor/superpowers/

Zawiera tylko `LICENSE` (MIT) + `NOTICE.md` — miejsce na skille, które kiedyś ewentualnie
zostaną skopiowane i dostrojone. Świadomie **nie ma tam kodu pluginu**; nie kopiuj go tam
„dla porządku".
