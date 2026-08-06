# Kontener deweloperski — jak i dlaczego

Izolowane środowisko do pracy z agentami AI (Claude Code) nad tym repo. Cel jest
jeden: **agent ma móc swobodnie działać w projekcie, ale nie ma móc narobić szkód
w systemie ani wynieść danych do internetu.**

Podstawa to referencyjny devcontainer Anthropica dla Claude Code — `Dockerfile`
i `init-firewall.sh` pochodzą stamtąd. Reszta plików i większość decyzji
w `devcontainer.json` to poprawki pod **rootless podmana**, bo oryginał jest
projektowany pod Dockera i pod podmanem jego kluczowe założenie się nie
sprawdza (szczegóły niżej, sekcja „Ambient capabilities").

## Model zagrożeń

Chronimy się przed agentem, który — przez błąd, halucynację albo wstrzyknięty
prompt — zrobi coś szkodliwego: skasuje pliki poza projektem, wyśle zawartość
repo na obcy serwer, sięgnie po klucze. **Nie** chronimy się przed sprawcą
z exploitem na jądro; do tego potrzebna byłaby maszyna wirtualna.

Granice są dwie i warto je rozróżniać:

- **System plików i procesy** — pilnuje ich user namespace podmana. Kontener
  widzi tylko to, co mu zamontowano (repo + wolumen z konfiguracją Claude'a),
  a jego „root" to na hoście subuid, nie Ty. Tego nie da się obejść od środka.
- **Sieć** — pilnuje jej firewall nakładany z hosta. Ruch wychodzi tylko do
  wypisanych domen.

## Pliki

| Plik | Gdzie działa | Rola |
|---|---|---|
| `devcontainer.json` | host (konfiguracja) | Spina całość: co zbudować, z jakimi uprawnieniami uruchomić, co odpalić przed i po starcie. |
| `Dockerfile` | build | Obraz: Debian + Node 20, git, gh, zsh, iptables/ipset, Claude Code. Prosto od Anthropica, nietykany. |
| `host-firewall.sh` | **host** | Nakłada firewall na kontener z zewnątrz. Uruchamiany przez Ciebie i przez `initializeCommand` — nigdy przez kontener. |
| `init-firewall.sh` | **w kontenerze** (wołany z hosta) | Właściwe reguły iptables/ipset. |
| `verify-firewall.sh` | **w kontenerze** | Sprawdza, czy firewall się nałożył; blokuje start sesji, jeśli nie. |

## Przebieg uruchomienia

Co się dzieje po „Reopen in Container":

1. **`initializeCommand`** (na hoście, przed powstaniem kontenera) woła
   `host-firewall.sh --spawn`. Ten rejestruje obserwatora jako jednostkę systemd
   i wraca po ~30 ms.
2. **Obserwator** (`--watch`, pod systemd) co 5 s przez 3 minuty szuka
   działającego kontenera tego repo po etykiecie `devcontainer.local_folder`.
3. **VS Code buduje obraz i startuje kontener** — bez żadnych uprawnień
   (`--cap-drop=ALL`).
4. **Obserwator znajduje kontener** i wchodzi do niego przez
   `exec --privileged`, żeby uruchomić `init-firewall.sh`. To zajmuje ~20 s,
   głównie pobranie zakresów IP GitHuba.
5. **`postStartCommand`** (w kontenerze) woła `verify-firewall.sh`, który czeka
   do 90 s, aż ruch na zewnątrz zacznie być blokowany. Jeśli się nie doczeka —
   przerywa start sesji.

Punkt 5 jest **fail-closed**: lepiej nie wejść do kontenera, niż wejść do niego
bez ochrony. Gdybyś kiedyś musiał wejść mimo wszystko, zakomentuj
`postStartCommand`.

## Kluczowe decyzje i dlaczego

### Ambient capabilities — dlaczego firewall nakłada host

To jest sedno różnicy względem oryginału. Podman wkłada uprawnienia dodane przez
`--cap-add` do **zestawu ambient**, czyli daje je również zwykłemu użytkownikowi,
nie tylko rootowi. Sprawdzone w kontenerze jako `node`:

```
CapEff: 00000000200031c0   ← zawiera NET_ADMIN
iptables -F  →  exit=0
```

Oryginalny projekt daje kontenerowi `NET_ADMIN`, żeby ten sam nałożył sobie
firewall w `postStartCommand`, i ogranicza `sudo` regułą w sudoers do jednego
skryptu. Pod Dockerem to działa, bo proces nie-root dostaje pusty zestaw
efektywny. **Pod podmanem cała ta konstrukcja jest dekoracją** — każdy proces
w kontenerze kasuje firewall jednym `iptables -F`, bez sudo.

Uprawnień nie da się odebrać po starcie: są zamrożone w konfiguracji kontenera,
a `podman update` umie zmieniać tylko limity cgroups i healthchecki. Dlatego
kontener nie dostaje `NET_ADMIN` wcale, a reguły nakłada host przez
`exec --privileged`. Wtedy w środku nie ma czym ich zdjąć — sprawdzone,
`iptables` odbija się o `Permission denied`.

Reguły trafiają wyłącznie do network namespace kontenera. Sieć hosta jest
nietknięta, a przy rootless podmanie ten „uprzywilejowany" proces jest rootem
tylko wewnątrz Twojego user namespace i fizycznie nie może zmienić netfiltera
hosta.

### Dlaczego systemd, a nie proces w tle

`initializeCommand` musi wrócić szybko, więc obserwator musi działać w tle. Dwie
próby zrobienia tego zwyczajnie — `nohup ... &`, potem `setsid nohup ... &` —
kończyły się śmiercią procesu **zanim zdążył zapisać pierwszą linię do logu**
(mierzone: skrypt potrzebuje ~19 ms, VS Code kończy `initializeCommand` po
~16 ms i wtedy sprząta). Jednostka systemd żyje we własnym cgroupie, poza
drzewem procesów VS Code, więc nie ma czego sprzątać. Gdyby `systemd-run`
zawiódł, skrypt spada na `setsid` i **zapisuje to w logu**.

### `--cap-drop=ALL` bez wyjątków, czyli koniec z `sudo`

Skoro firewall nakłada host, kontener nie potrzebuje już żadnych uprawnień.
Efekt uboczny: `sudo` w kontenerze nie działa (brak SETUID/SETGID). Instalacja
pakietów idzie przez `Dockerfile` i przebudowę obrazu. Gdyby `sudo` okazało się
naprawdę potrzebne, dodaj `--cap-add=SETUID --cap-add=SETGID` — ale **nigdy**
`NET_ADMIN`, bo to odtwarza dziurę opisaną wyżej.

### Brak `--userns=keep-id` w `runArgs`

To flaga wyłącznie podmanowa, Docker odrzuca ją błędem — a config ma działać też
na Kubuntu z Docker Engine. Nie jest potrzebna: rozszerzenie Dev Containers samo
dokłada `--userns=keep-id` i `--security-opt label=disable`, gdy wykryje podmana
i `remoteUser` inny niż root.

### `workspaceFolder` musi pasować do montowania

Bez własnego `workspaceMount` repo montuje się pod
`/workspaces/${localWorkspaceFolderBasename}`. Jeśli `workspaceFolder` wskaże
gdzie indziej (np. `/workspace`), VS Code otworzy pusty katalog i wygląda to na
awarię serwera.

### DNS tylko do własnego resolwera

Oryginał przepuszczał UDP 53 **do dowolnego adresu**. To gotowy kanał
eksfiltracji: dane koduje się w etykietach zapytania do własnego serwera
autorytatywnego, a odpowiedzi odbiera w rekordach TXT — lista domen tego nie
widzi, bo filtruje po docelowym IP. Teraz skrypt czyta `/etc/resolv.conf`
i przepuszcza DNS tylko do wypisanych tam adresów. Jest to przenośne: pod
podmanem/pastą jest tam `169.254.1.1`, pod Dockerem `127.0.0.11`.

Ta reguła ma **bezpiecznik**: po nałożeniu skrypt sprawdza, czy rozwiązywanie
nazw nadal działa, i jeśli nie — przywraca ogólną regułę i pisze o tym w logu.
Bez tego zepsuty DNS oznaczałby sesję, która się nie podnosi.

### IPv6 na DROP

Lista dozwolonych adresów jest wyłącznie IPv4, więc egress po IPv6 omijałby cały
firewall jednym `curl -6`. Dziś kontener ma tylko ULA bez trasy globalnej, więc
to zabezpieczenie na zapas. Blok jest miękki — brak `ip6tables` daje ostrzeżenie,
nie wywala skryptu.

### `.devcontainer/` tylko do odczytu

Repo jest podmontowane do zapisu, więc bez tego kontener mógłby podmienić własną
konfigurację. Najgroźniejszy jest `host-firewall.sh`, bo wykonuje się **na
hoście jako Ty** — podmieniony oznacza dowolny kod poza całą izolacją przy
następnym otwarciu kontenera. Podmiana `devcontainer.json` pozwoliłaby przy
następnej przebudowie dorzucić `runArgs` (zamontować `/`, przywrócić
`NET_ADMIN`), a podmiana `verify-firewall.sh` — uciszyć alarm.

Dlatego `mounts` nakłada na ten katalog drugi, `readonly`. Pliki nadal się
czytają i **uruchamiają** (sprawdzone: `verify-firewall.sh` odpala się z takiego
montażu bez problemu), nie da się ich tylko zapisać.

Konsekwencja pierwsza: zmiany w `.devcontainer/` robisz z hosta.

Konsekwencja druga, mniej oczywista: **operacje gita, które musiałyby zapisać do
tego katalogu, kończą się w połowie.** Nie chodzi o to, czy Ty tam coś zmieniasz
— chodzi o to, czy git musi podmienić zawartość. Zwykła praca (commit, push,
diff, przełączanie gałęzi nieruszających tego katalogu) działa normalnie, ale
`checkout` na gałąź z innym `.devcontainer/` albo `pull` z takimi zmianami daje:

```
error: unable to unlink old '.devcontainer/cfg.json': Read-only file system
Switched to branch 'fw'
M	.devcontainer/cfg.json
```

Gałąź przełączona, plik stary, repo niespójne — a kolejne operacje dotykające
tego katalogu też padają (`stash` zwróci „Could not reset index file to revision
HEAD"). Nic nie ginie, `.git` jest nietknięte. **Wyjście: dokończ z hosta** —
`git checkout -- .devcontainer` albo powtórzenie polecenia w terminalu hosta.

Jeśli to zacznie uwierać, można zamontować read-only tylko sam
`host-firewall.sh` zamiast całego katalogu — to on jest naprawdę groźny, bo
wykonuje się na hoście. Ochrona słabsza, tarcie mniejsze.

### Brama `/32`, nie `/24`

Oryginał przepuszczał całą podsieć bramy, bo pod Dockerem bramą jest most
dockerowy. Pod rootless podmanem z pastą kontener widzi **prawdziwą sieć
lokalną**, więc `/24` otwierało cały LAN i usługi na hoście. Zawężone do samej
bramy.

## Co firewall przepuszcza

Zakresy IP GitHuba (pobierane z `api.github.com/meta`), `registry.npmjs.org`,
`api.anthropic.com`, `sentry.io`, trzy domeny VS Code, DNS do własnego resolwera,
localhost i bramę. Wszystko inne dostaje `REJECT`. Filtrowanie jest **po
docelowym IP**, nie po porcie.

## Czego to NIE chroni

Warto mieć świadomość, bo część przecieków omija firewall z definicji:

- **Sockety wpuszczane przez VS Code** — ssh-agent, gpg-agent, X11, Wayland oraz
  git credential helper hosta. To nie jest ruch sieciowy, więc iptables ich nie
  widzi. Częściowo wyłączalne: `dev.containers.mountWaylandSocket: false`,
  `dev.containers.gitCredentialHelperConfigLocation: "none"`. Dla ssh-agenta
  i X11 rozszerzenie nie ma przełącznika (sprawdzone w wersji 0.463.0).
- **Dozwolone domeny jako kanał danych** — mając dostęp do GitHuba można wypchnąć
  dane do repo czy gista. Nie da się usunąć bez odcięcia gita.
- **Panel WWW routera** — brama jest przepuszczona, więc jest widoczna.
- **`--security-opt label=disable`** — rozszerzenie samo wyłącza konfinację
  SELinuksa dla kontenera. To utrata warstwy, nie dziura: namespace'y i tak
  odcinają dostęp do niezamontowanych plików.

## Diagnostyka

```bash
cat /tmp/matematykazen-host-firewall.log     # co robił obserwator
cat /tmp/matematykazen-firewall-spawn.log    # czy initializeCommand w ogóle ruszył
systemctl --user status matematykazen-firewall-watch
.devcontainer/host-firewall.sh               # nałóż firewall ręcznie (z hosta!)
```

Skrypt uruchomiony ręcznie bez argumentów znajduje kontener, sprawdza, czy
firewall już stoi, i nakłada go, jeśli nie. Przydaje się po restarcie kontenera,
gdy VS Code nie przechodził przez `initializeCommand`.

Objawy i przyczyny:

- **Sesja nie startuje, komunikat o nienałożonym firewallu** — obserwator nie
  zadziałał. Zajrzyj do obu logów; najczęściej wystarczy odpalić skrypt ręcznie.
- **VS Code otwiera pusty katalog** — rozjechał się `workspaceFolder`.
- **`sudo: unable to change to root gid`** — ktoś dodał `--cap-drop=ALL` bez
  SETUID/SETGID, a coś nadal próbuje używać `sudo`.

## Zmiany wymagające przebudowy

`init-firewall.sh` jest kopiowany do obrazu, więc po jego edycji potrzebny jest
**Rebuild Container** (zwykły, bez `--no-cache` — przebuduje się tylko warstwa
`COPY` i te pod nią). `host-firewall.sh` działa na hoście, a
`verify-firewall.sh` uruchamia się z podmontowanego repo — te dwa nie wymagają
przebudowy, wystarczy „Reopen".

`--no-cache` przyda się tylko wtedy, gdy zechcesz odświeżyć wersję Claude Code
albo pakiety systemowe — warstwa `npm install -g @anthropic-ai/claude-code` jest
zamrożona z dnia pierwszego builda.

## Podman vs Docker

Konfiguracja jest wspólna dla obu. Różnice, o których warto pamiętać:

| | rootless podman | Docker Engine |
|---|---|---|
| root w kontenerze | subuid na hoście | prawdziwy root hosta |
| ambient capabilities | tak (stąd cała ta konstrukcja) | nie |
| brama | prawdziwy router w LAN | most dockerowy = host |
| resolver | `169.254.1.1` (pasta) | `127.0.0.11` |

Firewall z hosta działa w obu przypadkach — `docker exec --privileged` zachowuje
się tak samo jak podmanowy. **Uwaga: całość testowana była pod rootless podmanem
na Bazzite; wariant dockerowy nie był uruchamiany.**
