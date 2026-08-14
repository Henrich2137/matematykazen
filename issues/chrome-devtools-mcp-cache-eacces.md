# chrome-devtools-mcp: EACCES przy tworzeniu ~/.cache/chrome-devtools-mcp

Status: **NAPRAWIONE I POTWIERDZONE 2026-08-14 (Opus 5, medium), po Rebuild Container.**
Zastosowano wariant 1 z tabeli niżej: `/home/node/.cache` powstaje w obrazie razem
z `.claude`/`.config` i dostaje `chown node:node`. Sprawdzone po przebudowie:
`ls -ld ~/.cache` → `node node`, `mkdir` przez usera `node` przechodzi, a plugin sam
założył sobie `~/.cache/chrome-devtools-mcp/chrome-profile`. Przypuszczenie o przyczynie
(niżej) było więc trafne.

## Co WYSZŁO SPOD SPODU (nowy, osobny problem, 2026-08-14)

Po zniknięciu EACCES pierwsze `navigate_page` rzuca już czym innym:

```
Could not find Google Chrome executable for channel 'stable' at:
 - /opt/google/chrome/chrome.
```

To nie jest ten sam błąd i nie jest to regres — w kontenerze po prostu **nie ma
Google Chrome'a**. Jest wyłącznie Chromium Playwrighta, przychodzący read-only bindem
z hosta: `/home/node/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome`
(działa — `tools/zrzuty.js` i `tools/test-krokow.js` chodzą na nim bez zarzutu).

`chrome-devtools-mcp` przyjmuje `--executablePath` (oraz `--headless`), więc technicznie
wystarczyłoby wskazać mu tamtą binarkę. Kłopot jest z MIEJSCEM na tę flagę: `args`
serwera siedzą w `~/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/<wersja>/.claude-plugin/plugin.json`
— poza repo i nadpisywane przy każdej aktualizacji pluginu.

| Wariant | Uwagi |
|---|---|
| Własny wpis `chrome-devtools` w repo (`.mcp.json`) z `--executablePath` i `--headless`, plugin wyłączony | ✅ jedzie z repo, przeżywa aktualizacje · 🟨 dublujemy to, co daje plugin, i trzeba pilnować wersji `chrome-devtools-mcp@x` samemu |
| Doinstalować Google Chrome w `.devcontainer/Dockerfile` | ✅ plugin działa bez żadnych sztuczek · ❌ ~150 MB obrazu, kolejny Rebuild Container po stronie hosta, a repozytorium Google trzeba by wpuścić przez firewall |
| Zostawić jak jest | ✅ zero pracy · ❌ plugin bezużyteczny, ale Playwright i tak pokrywa zrzuty ekranu i testy odtwarzacza |

Do decyzji Henricha. Uwaga na read-only bind: Chromium z `ms-playwright` jest tylko do
odczytu, więc profil (`--user-data-dir`) musi zostać tam, gdzie jest domyślnie
(`~/.cache/chrome-devtools-mcp/chrome-profile`) — to już jest zapisywalne.

Znalezione 2026-08-13 przy pierwszym teście po instalacji pluginu
`chrome-devtools-mcp@claude-plugins-official` (`/plugin`, kontener na Bazzite).

## Co się dzieje

`claude mcp list` pokazuje serwer jako połączony:

```
plugin:chrome-devtools-mcp:chrome-devtools: npx chrome-devtools-mcp@1.7.0 - ✔ Connected
```

ale to tylko health-check samego procesu MCP. Pierwsze realne wywołanie narzędzia
(`new_page`, otwarcie dowolnego URL-a) rzuca:

```
EACCES: permission denied, mkdir '/home/node/.cache/chrome-devtools-mcp'
```

Sprawdzone: to nie firewall (błąd jest lokalny, o systemie plików, zero prób sieciowych
w komunikacie) i nie literówka w URL-u — sam `mkdir` się nie udaje.

## Przypuszczalna przyczyna (PRZYPUSZCZENIE, nie potwierdzone naprawą)

```
$ stat ~/.cache
  Uid: (    0/    root)   Gid: (    0/    root)
  Access: (1755/drwxr-xr-t)
$ id
uid=1000(node) gid=1000(node) groups=1000(node)
```

`~/.cache` w tym devcontainerze należy do `root`, tryb `1755` (rwxr-xr-t) — właściciel
(`root`) może w nim tworzyć pliki/foldery, grupa i inni tylko czytać/wchodzić. Użytkownik
`node` (uid 1000), pod którym działa Claude Code i cały `npx chrome-devtools-mcp`, **nie
ma prawa zapisu w samym `~/.cache`** — może czytać/wchodzić do już istniejących
podkatalogów, ale nie założyć nowego.

Istniejący podkatalog `~/.cache/ms-playwright` **nie jest kontrprzykładem** — to osobny,
read-only bind mount z hosta (`devcontainer.json`, `mounts`:
`source=${localEnv:HOME}/.cache/ms-playwright,target=/home/node/.cache/ms-playwright,type=bind,readonly`),
czyli katalog istnieje z zewnątrz, node nigdy nie musiał go sam tworzyć.

`chrome-devtools-mcp` (przez Puppeteer, żeby zarządzać profilem przeglądarki/cache'em)
chce sobie założyć **własny, zapisywalny** podkatalog pod `~/.cache` w locie — i to się
wysypuje, bo `~/.cache` samo jest `root:root`.

Prawdopodobnie `~/.cache` dostało takiego właściciela przy budowie obrazu (coś w
`.devcontainer/Dockerfile` tworzy ten katalog jako root, zanim przełączy na `node`, i
nigdy go nie chownuje) — nie sprawdzałem samego `Dockerfile` linia po linii, więc to
też jest przypuszczenie, nie pewnik.

`sudo` nie jest tu ścieżką naprawy z sesji — świadomie wyłączone w kontenerze
(`--cap-drop=ALL`, patrz CLAUDE.md / `.devcontainer/README.md`), więc nie da się nawet
doraźnie zrobić `sudo chown` z wnętrza sesji.

## Warianty naprawy

| # | Wariant | Naprawia | Koszt |
|---|---|---|---|
| 1 | W `.devcontainer/Dockerfile` zmienić właściciela `~/.cache` na `node:node` (`chown -R node:node /home/node/.cache` po utworzeniu, przed przełączeniem na usera) | ✅, najprościej | ✅ jedna linia w Dockerfile, wymaga Rebuild Container |
| 2 | Dodać w `.devcontainer/Dockerfile` jawny `mkdir -p /home/node/.cache/chrome-devtools-mcp && chown node:node ...` | ✅, węziej niż #1 | 🟨 trzeba pamiętać o każdym nowym narzędziu, które chce własny podkatalog w `~/.cache` |
| 3 | Osobny zapisywalny wolumen pod `~/.cache/chrome-devtools-mcp`, wzorem `matematykazen-claude-config` czy `matematykazen-gh-config` | ✅, przeżywa też rebuildy obrazu | ❌ kolejny wolumen do pamiętania |
| 4 | Przekierować cache pluginu gdzie indziej przez zmienną środowiskową (jeśli `chrome-devtools-mcp`/Puppeteer to respektuje — NIE sprawdzone) | 🟨 nie wiadomo, czy pomoże | 🟨 wymaga najpierw sprawdzenia, czy narzędzie w ogóle czyta taką zmienną |

## Rekomendacja

Wariant 1 — najmniejsza zmiana, naprawia całą klasę problemu (nie tylko tego jednego
pluginu — każde kolejne narzędzie, które zechce coś zapisać bezpośrednio pod `~/.cache`,
trafi w to samo). Wymaga Rebuild Container po zmianie w `Dockerfile`, więc naprawa nie
jest możliwa z samej sesji Claude Code — decyzja i wykonanie po stronie Henricha
(host/Dockerfile są poza zasięgiem edycji z kontenera w tym repo, patrz zasady „na hoście"
w CLAUDE.md).

Do potwierdzenia po naprawie: `new_page` na dowolny URL (np. lokalny serwer
`node tools/serwer.js`) powinno przejść bez `EACCES`, a `take_screenshot` zwrócić realny
zrzut.

---
Sonnet 5, medium.
