# Git: gitdoc + automatyczny fetch/pull

Opis konstrukcji, nie problem. Wyniesione z CLAUDE.md 2026-08-12, bo do codziennej pracy
nad stroną nie jest to potrzebne — CLAUDE.md ma z tego tylko cztery linijki i odnośnik tutaj.
Otwórz ten plik, gdy: historia `origin` wygląda dziwnie, ktoś chce włączyć/wyłączyć gitdoc,
albo trzeba zmienić cadencję autocommitów.

## gitdoc — STATUS: WYŁĄCZONY (stan na 2026-08-01, zweryfikuj zanim zaufasz)

`gitdoc.enabled` domyślnie jest `false` i nigdzie nie jest ustawione: nie ma go ani
w `.vscode/settings.json` (opróżnionym commitem `3a985b5`, „usunięcie settingsów z repo
i przeniesienie do user settings"), ani w globalnym user settings.json
(`C:\Users\<user>\AppData\Roaming\Code\User\settings.json`) — „przeniesienie do user settings"
nigdy się nie odbyło, klucz po prostu skasowano. **Nie zakładaj więc, że `git status` / `git log`
zawierają autocommity gitdoca.**

## Dlaczego tak wyszło i co to ogranicza

Mechanika (źródło: `out/config.js` zainstalowanego rozszerzenia): **`gitdoc.enabled` da się ustawić
wyłącznie na poziomie `ConfigurationTarget.Workspace`** — setter rozszerzenia ma to zaszyte na sztywno:

```js
set enabled(value) {
    config().update(ENABLED_KEY, value, vscode.ConfigurationTarget.Workspace);
}
```

Komenda Enable/Disable (czyli też przełącznik w UI GitDoca) zawsze zapisuje do
`.vscode/settings.json` **tego repo**, nigdy do globalnych ustawień użytkownika. Wpisanie
`gitdoc.enabled: true` w globalnym pliku nie zadziała tak, jak reszta kluczy `gitdoc.*` —
jeśli chcesz gitdoca z powrotem, ustaw go w `.vscode/settings.json` (albo przełącz w UI).
Globalny settings.json nadal jest właściwym miejscem na *pozostałe* klucze `gitdoc.*`
(delay/push/pull) — tylko `enabled` ma to ograniczenie do workspace'u.

## Czego się spodziewać, gdyby gitdoc został włączony

Wszystkie te wartości (`autoPush: "onCommit"`, `autoPull: "onPush"`, `pullOnOpen: true`,
`commitOnClose: true`, `pushMode: "forcePush"`, `autoCommitDelay: 30000`) to **wbudowane domyślne
rozszerzenia** — żadna nie jest jawnie ustawiona w jakimkolwiek settings.json na tej maszynie.
Nie zakładaj, że dokumentuje je jakiś plik konfiguracyjny; biorą się z samego rozszerzenia
(`out/config.js`).

- Autocommit przy każdym zapisie (wiadomość to sam timestamp, bez prefiksu) i **natychmiastowy
  push do `origin`** (`autoPush: "onCommit"`) — to omija zasadę „potwierdź przed pushem" akurat
  dla tych commitów, bo nie inicjuje ich asystent.
- `git log` pokazywałby wtedy ciągi commitów z samą datą pomiędzy „prawdziwymi" commitami —
  to gitdoc, nie asystent, nawet w trakcie sesji asystenta (np. Henrich edytujący TODO.md
  w edytorze).
- Przed squashem zakresu commitów sprawdź `git show --stat` każdego z nich — autocommit
  z edycji Henricha potrafi wpaść w środek zakresu (zdarzyło się 2026-07-26, patrz
  `done/03-2026-07-27.md`).
- Skoro push jest natychmiastowy, traktuj każdy commit jako **już na `origin`**, dopóki nie
  udowodnisz inaczej — nie ma lokalnego okna przejściowego.

## Mechanika cadencji (zweryfikowana `vsls-contrib.gitdoc-0.2.3`, VS Code 1.130.0; 2026-07-26 i 2026-08-01)

- **`gitdoc.autoCommitDelay` (domyślnie 30000 ms) to debounce, nie interwał** (`out/watcher.js`:
  `debounce(() => commit(repo), autoCommitDelay)`, licznik resetowany przy każdej zmianie stanu repo).
  Podniesienie do np. 20 min znaczy „commit 20 min po *ostatniej* edycji", nie „commit co 20 min" —
  przy ciągłym pisaniu nie commituje się nic, dopóki nie zrobisz przerwy (albo nie zamkniesz
  VS Code, co łapie `commitOnClose`).
- Zdebounce'owana funkcja jest cache'owana per obiekt repozytorium w `commitMap`, która nigdy nie
  jest czyszczona — więc **zmiana `autoCommitDelay` działa dopiero po `Developer: Reload Window`**,
  nie po zapisaniu ustawień.
- **Nie ma opcji „commit co N zapisów"** — jedyne pokrętła to `autoCommitDelay`, `filePattern`
  (które pliki wyzwalają commit), `excludeBranches` i tryb w pełni ręczny
  (`gitdoc.enabled: false` + komenda `GitDoc: Commit`).
- `gitdoc.pushMode` domyślnie to **`"forcePush"`** — warto wiedzieć, zanim zacznie się diagnozować
  dziwną historię na `origin`.

## Auto-fetch / auto-pull (2026-08-07) — to NIE jest gitdoc

Repo konfiguruje dwie **natywne funkcje VS Code**, świadomie zamiast `gitdoc.pullOnOpen`: gitdoc
jest wszystko-albo-nic, więc włączenie go dla samego pull-on-open przyciągnęłoby z powrotem
autocommit + `forcePush` (wyłączone celowo, patrz wyżej).

- `.vscode/settings.json` → `"git.autofetch": true` — `git fetch` w tle co ~3 min. Tylko fetch,
  nigdy merge; widoczny efekt to licznik „↓N" w Source Control.
- `.vscode/tasks.json` → zadanie `git pull --ff-only` z `"runOn": "folderOpen"` — pulluje **raz,
  przy otwarciu folderu**. `--ff-only` to zabezpieczenie: nie nadpisze lokalnych commitów ani nie
  zrobi merge'a; na rozjechanych gałęziach po prostu się nie uda i pokaże terminal.

Oba pliki są śledzone przez gita, więc jadą z repo i zachowują się tak samo w kontenerze
i poza nim (o tę równość chodzi).

**`runOn: folderOpen` odpala się po cichu tylko wtedy, gdy *globalny* (User) `settings.json`
maszyny ma `"task.allowAutomaticTasks": "on"`** — inaczej VS Code przy każdym otwarciu pyta
„Allow Automatic Tasks in Folder?" i do czasu odpowiedzi nie pulluje. Tego przełącznika **nie da
się ustawić z ustawień workspace'u**, i to celowo: repo nie może samo sobie przyznać prawa do
uruchamiania komend. Na tej maszynie ustawiony 2026-08-10, w `~/.config/Code/User/settings.json` —
w **instalacji natywnej (rpm-ostree), jedynej jaka została**: flatpakowy VS Code był już wtedy
odinstalowany, a jego 852 MB osieroconych danych w `~/.var/app/com.visualstudio.code/` skasowane
tego samego dnia (ustawienia + lista rozszerzeń zachowane w `~/backup-vscode-flatpak/`).
Nie przywracaj ścieżki flatpakowej w dokumentacji ani konfiguracji — tam
`dev.containers.dockerPath` wymagał `flatpak-spawn --host podman`, natywna używa zwykłego `podman`.
Na świeżej maszynie/profilu przełącznik trzeba ustawić od nowa — repo tego nie przeniesie.

Ponieważ to usuwa jedyną interaktywną barierę przed komendą, którą VS Code uruchamia sam,
**`.vscode/` jest montowany `readonly` w devkontenerze** (tak samo jak `.devcontainer/`, dodane
tego samego dnia), żeby kontener nie mógł przepisać zadania, które potem uruchomi. Konsekwencja:
`.vscode/` edytuj z hosta, a `checkout`/`pull` dotykający tego katalogu z wnętrza kontenera
wywali się w połowie dokładnie tak jak przy `.devcontainer/` — patrz `.devcontainer/README.md`,
sekcja „`.devcontainer/` i `.vscode/` tylko do odczytu".
