# Osierocone dane po flatpakach (na przykładzie VS Code)

**Status:** rozwiązane 2026-08-10 dla VS Code. Plik zostaje jako **przepis na następny raz** —
sytuacja się powtórzy przy każdej odinstalowanej aplikacji flatpakowej.

## Na czym polega problem

`flatpak uninstall` **nie kasuje danych użytkownika**. Zostają one w `~/.var/app/<id-aplikacji>/`
i nikt ich potem nie sprząta ani nie pokazuje. Katalog nie pojawia się w żadnym `flatpak list`,
więc jedynym sposobem, żeby go zauważyć, jest porównanie zawartości `~/.var/app/` z listą
faktycznie zainstalowanych aplikacji.

Skala bywa spora: po flatpakowym VS Code zostało **852 MB** (621 MB samych rozszerzeń),
mimo że aplikacji nie było w systemie od dawna.

## Jak znaleźć sieroty

```bash
installed=$(flatpak list --app --columns=application)
for d in ~/.var/app/*/; do
  app=$(basename "$d")
  echo "$installed" | grep -qx "$app" || du -sh "$d" | sed 's/$/  <- SIEROTA/'
done
```

Do kompletu warto puścić `flatpak uninstall --unused` (kasuje nieużywane *runtime'y*, co jest
zwykle znacznie większym zyskiem niż same dane aplikacji).

## Jak sprawdzić, czy na pewno można skasować

Kolejność ma znaczenie — **`rm -rf` dopiero po tych czterech krokach.**

1. **Czy aplikacja faktycznie jest odinstalowana.**
   `flatpak list --app --columns=application | grep <id>` — brak wyniku = brak aplikacji.
   Jeśli aplikacja JEST zainstalowana, nie kasuj ręcznie, użyj
   `flatpak uninstall --delete-data <id>`.

2. **Czy w danych nie ma czegoś nieodtwarzalnego.** Dla edytorów/IDE najbardziej podejrzane są:
   - `config/…/User/History/` — **lokalna historia edycji plików**, jedyne miejsce, gdzie może
     leżeć wersja pliku, której nie ma w gicie. Sprawdź, czego dotyczy:
     ```bash
     find History -name entries.json -exec python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['resource'])" {} \;
     ```
   - `config/…/User/workspaceStorage/*/workspace.json` — których projektów dotyczy stan UI.
   - `config/…/User/profiles/` — osobne profile mogą mieć własne ustawienia.
   - `settings.json`, `keybindings.json`, `snippets/`.

3. **Czy nic w systemie nie wskazuje na tę ścieżkę.**
   ```bash
   grep -rl "com.visualstudio.code" ~/.config ~/.vscode <repo> 2>/dev/null
   ```

4. **Backup tego, co małe i osobiste** (ustawienia to kilka kB, nie ma powodu ich nie zachować):
   ```bash
   mkdir -p ~/backup-vscode-flatpak
   cp <flatpak>/config/Code/User/{settings,keybindings}.json ~/backup-vscode-flatpak/ 2>/dev/null
   cp -r <flatpak>/config/Code/User/snippets ~/backup-vscode-flatpak/ 2>/dev/null
   ls <flatpak>/data/vscode/extensions > ~/backup-vscode-flatpak/rozszerzenia.txt
   diff ~/backup-vscode-flatpak/settings.json ~/.config/Code/User/settings.json
   ```
   Ten `diff` to najważniejszy krok — pokazuje ustawienia, które istnieją TYLKO w kasowanej
   instalacji. **Nie przenoś ich automatycznie**: część jest specyficzna dla flatpaka i w natywnej
   instalacji byłaby wręcz szkodliwa (patrz niżej).

## Co z tego wyszło konkretnie dla VS Code (2026-08-10)

Skasowano `~/.var/app/com.visualstudio.code/` (852 MB). Zostaje **jedna instalacja: natywna
przez rpm-ostree**, `~/.config/Code/User/` + `~/.vscode/extensions`.

- **Rozszerzenia**: 14 we flatpaku, 13 natywnie; tylko 4 nie miały odpowiednika (GitLens,
  Containers, gitdoc, Claude Code) — wszystkie wracają z marketplace'u.
- **`History/`**: wyłącznie stare wersje `settings.json` i `.devcontainer/devcontainer.json`
  (ten drugi i tak jest w gicie).
- **`workspaceStorage/`**: tylko to repo, i to sam stan UI.

**Ustawienia specyficzne dla flatpaka, których NIE WOLNO przenosić do natywnej instalacji** —
to jest pułapka, bo wyglądają na zwykłe różnice w `diff`ie:

| flatpak | natywnie |
|---|---|
| `"dev.containers.dockerPath": "flatpak-spawn --host podman"` | `"podman"` |
| `"dev.containers.dockerComposePath": "flatpak-spawn --host podman-compose"` | `"podman-compose"` |
| `settingsSync.ignoredSettings` z powyższymi | niepotrzebne |

Flatpakowy VS Code siedzi w piaskownicy i musi wołać podmana **przez `flatpak-spawn --host`**.
Natywny woła go wprost. Skopiowanie tych linii do natywnej instalacji zepsułoby devcontainery.

**Ustawienia, które istniały tylko we flatpaku i świadomie ich nie przeniesiono** (spisane
tutaj w całości — sam backup `~/backup-vscode-flatpak/` został skasowany 2026-08-14, decyzją
Henricha, bo poza tymi trzema liniami nie było w nim nic, czego nie ma w bieżących
ustawieniach; `snippets/` był pusty, a `rozszerzenia.txt` to była lista nazw paczek):

- `"chat.viewSessions.orientation": "stacked"`
- `"chat.agent.sandbox.enabled": "on"`
- `"terminal.integrated.gpuAcceleration": "off"` — natywnie ta linia jest **zakomentowana**,
  z dopiskiem Henricha „warto to sprawdzić jeśli sideview nie działa". Jeśli manim-sideview
  zacznie się krzaczyć, to pierwsza rzecz do odkomentowania.

## Pozostałe sieroty — posprzątane 2026-08-10

Po VS Code skasowano jeszcze osiem drobnych sierot: `com.github.wwmm.easyeffects` (283 kB),
`com.geekbench.Geekbench6` (45 kB) oraz sześć **pustych** skorup po przeglądarkach
(`org.chromium.Chromium`, `net.waterfox.waterfox`, `io.gitlab.librewolf-community`,
`io.github.ungoogled_software.ungoogled_chromium`, `com.google.ChromeDev`, `com.google.Chrome`).
Razem ~328 kB — zysk symboliczny, chodziło o to, żeby `~/.var/app` dało się czytać jako
wiarygodną listę „co jest zainstalowane".

Stan po sprzątaniu: **23 katalogi, każdy z zainstalowaną aplikacją, zero sierot** (zweryfikowane
pętlą z sekcji „Jak znaleźć sieroty").

Na przyszłość: realny zysk miejsca daje nie to, tylko `flatpak uninstall --unused` — nieużywane
runtime'y idą w gigabajty, dane aplikacji zwykle w kilobajty. Wyjątkiem są aplikacje, które
trzymają w danych własne wtyczki/rozszerzenia (jak VS Code — 621 MB samych rozszerzeń).

## Powiązane

- `CLAUDE.md`, sekcja „Auto-fetch / auto-pull" — dlaczego liczy się tylko natywna instalacja
  i gdzie siedzi `task.allowAutomaticTasks`.
- `done/04-biezace.md`, wpis z 2026-08-10 — pełny kontekst paczki, w której to wypłynęło.
