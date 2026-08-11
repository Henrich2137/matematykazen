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

### `.devcontainer/` i `.vscode/` tylko do odczytu

Repo jest podmontowane do zapisu, więc bez tego kontener mógłby podmienić własną
konfigurację. Najgroźniejszy jest `host-firewall.sh`, bo wykonuje się **na
hoście jako Ty** — podmieniony oznacza dowolny kod poza całą izolacją przy
następnym otwarciu kontenera. Podmiana `devcontainer.json` pozwoliłaby przy
następnej przebudowie dorzucić `runArgs` (zamontować `/`, przywrócić
`NET_ADMIN`), a podmiana `verify-firewall.sh` — uciszyć alarm.

**`.vscode/` doszło z tego samego powodu (2026-08-10), choć wektor jest mniej
oczywisty.** `tasks.json` ma zadanie z `"runOn": "folderOpen"` — czyli polecenie
powłoki, które VS Code odpala **sam, bez pytania**, przy każdym otwarciu tego
folderu. Kontener mógłby podmienić `git pull --ff-only` na cokolwiek i po prostu
czekać. Odpali się to tam, gdzie folder zostanie otwarty, a więc **na hoście,
poza izolacją**, gdy kiedyś otworzysz repo lokalnie zamiast w kontenerze.
`settings.json` jest drugim, słabszym wektorem (choćby ścieżki do podmana).

Zwróć uwagę na sprzężenie: `"runOn": "folderOpen"` działa po cichu tylko dlatego,
że w globalnych ustawieniach VS Code stoi `"task.allowAutomaticTasks": "on"` —
czyli sam wyłączyłeś pytanie, które normalnie byłoby ostatnią barierą przed
uruchomieniem takiego polecenia. Tym bardziej ten plik nie może być zapisywalny
z kontenera.

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

### Logowanie `gh` przeżywa przebudowę (wolumen)

`~/.config/gh` w kontenerze to **wolumen** `matematykazen-gh-config`, dokładnie
jak `~/.claude`. Bez tego katalog leżałby w warstwie zapisywalnej kontenera
i ginął przy każdym rebuildzie, więc `gh auth login` trzeba by powtarzać
w kółko.

Dlaczego wolumen, a nie bind hostowego `~/.config/gh`: na hoście `gh` trzyma
token w **keyringu**, a `hosts.yml` zawiera samą nazwę użytkownika bez
`oauth_token`. Podmontowanie tego pliku dałoby w kontenerze usera bez tokenu,
czyli nic.

`/home/node/.config/gh` jest przy tym **pre-tworzony w `Dockerfile`** i chown-owany
na `node`. To nie jest nadmiarowe: podman inicjalizuje nowy, pusty wolumen
zawartością i właścicielem katalogu z obrazu — gdyby tej ścieżki w obrazie nie
było, wolumen powstałby jako `root:root` i `gh` (działający jako `node`) nie
zapisałby do niego tokenu.

W kontenerze nie ma keyringu, więc token leży tam plaintextem. To nie regres —
dotąd leżał plaintextem tak samo, tyle że w efemerycznej warstwie kontenera.

**Czego to nie dotyczy** (i co nigdy nie wymagało logowania po rebuildzie):

- `git push`/`pull` — Dev Containers wstrzykuje do `~/.gitconfig` w kontenerze
  własny credential helper (`…/vscode-remote-containers-….js`), który pyta host
  przez socket. Działa nawet przy wylogowanym `gh`.
- Copilot w VS Code — sesja GitHub żyje po stronie hosta (UI), nie w kontenerze;
  w `~/.vscode-server/data/User/globalStorage/` nie ma nawet `state.vscdb`.

Reset logowania, gdyby kiedyś trzeba: `podman volume rm matematykazen-gh-config`
przy zatrzymanym kontenerze.

### Brama: `/24` → `/32` → tylko port 53

Zawężana dwukrotnie i warto rozumieć oba kroki, bo mylą się przy diagnozie.

Oryginał przepuszczał **całą podsieć bramy**, bo pod Dockerem bramą jest most
dockerowy — czyli w praktyce sam host. Pod rootless podmanem z pastą kontener
widzi **prawdziwą sieć lokalną**, więc `/24` otwierało cały LAN i usługi na
hoście. Pierwsze zawężenie: tylko sama brama (`/32`).

To wciąż było za dużo, bo brama to prawdziwy router — a `/32` bez podania portu
otwiera **wszystkie** jego porty. Skan `192.168.1.1` z wnętrza kontenera pokazał
otwarte `80`, `443`, `445` (SMB) i `631` (IPP): nie tylko panel WWW, ale też
udziały plików i drukarkę. Do niczego w tym kontenerze niepotrzebne. Drugie
zawężenie (2026-08-10): przechodzi już **wyłącznie `53/udp` i `53/tcp`**.

Dlaczego akurat 53 zostaje, skoro DNS ma wyżej własne reguły z `resolv.conf`:
w konfiguracjach, w których **resolwerem jest sam router**, oba miejsca wskazują
ten sam adres i ta reguła jest tylko duplikatem — ale gdy `resolv.conf` pokazuje
co innego (pod pastą `169.254.1.1`, pod Dockerem `127.0.0.11`), zostaje ona
jedyną furtką na wypadek, gdyby zapytania jednak trafiały do bramy. Koszt zerowy,
a alternatywą jest kontener bez DNS, czyli — przy fail-closed `postStartCommand`
— sesja, która się nie podnosi.

TCP obok UDP nie jest ozdobą: odpowiedź powyżej 512 B (albo ustawiona flaga TC)
wymusza ponowienie zapytania po TCP, więc bez tej reguły część nazw rozwiązywałaby
się zależnie od rozmiaru odpowiedzi.

Ruch zwrotny **nie ma** własnej reguły — łańcuch `INPUT` ma niżej
`ESTABLISHED,RELATED`, a conntrack śledzi także przepływy UDP.

Jeśli DNS przestanie działać po zmianach w tych regułach → patrz „Diagnostyka"
niżej; jest bezpiecznik, który sam się włącza i pisze o tym w logu.

## Co firewall przepuszcza

Zakresy IP GitHuba (pobierane z `api.github.com/meta`), DNS do własnego
resolwera, localhost oraz **port 53 na bramie i nic poza nim** (patrz „Brama:
`/24` → `/32` → tylko port 53"), plus dwie listy domen w `init-firewall.sh`.
Wszystko inne dostaje `REJECT`. Filtrowanie jest **po docelowym IP**, nie po
porcie ani po SNI — to dlatego domeny na współdzielonym anycaście CDN-a są
problematyczne: wpuszczenie ich adresu otwiera kawałek cudzej infrastruktury.

Listy są dwie, bo nie każda domena jest tak samo ważna:

- **`CRITICAL_DOMAINS`** — `registry.npmjs.org`, `api.anthropic.com`,
  `sentry.io` i trzy domeny VS Code. Nierozwiązana domena przerywa skrypt, a że
  `postStartCommand` jest fail-closed, oznacza to brak wejścia do kontenera.
  Tak ma być: lepiej nie wejść, niż pracować z połową milczących narzędzi.
- **`CONTENT_DOMAINS`** — źródła treści i materiałów: `cke.gov.pl`,
  `www.cke.gov.pl`, `arkusze.pl`, `zpe.gov.pl`, `ore.edu.pl`, `men.gov.pl`. Te
  serwisy bywają chwilowo niedostępne, więc brak rozwiązania daje tylko
  ostrzeżenie i skrypt leci dalej. Firewall zostaje szczelny — pominięta domena
  po prostu nie jest przepuszczona w tej sesji.

Pod aktywnymi wpisami w `CONTENT_DOMAINS` leży **blok zakomentowanych domen**:
kandydaci (serwisy OKE) oraz świadomie odrzuceni, każdy z powodem odrzucenia
i warunkiem, w którym warto go odkomentować. Jeśli coś w kontenerze przestanie
działać z powodu sieci, zacznij od przejrzenia tego bloku — jest tam opisane,
co dana domena obsługuje.

### DO ZROBIENIA: odkomentować `matematykazen.pl`, gdy domena ruszy

W `CONTENT_DOMAINS` czeka zakomentowany wpis `matematykazen.pl`. Dziś domena
**nie istnieje w DNS** (`dig +short A matematykazen.pl` nie zwraca nic), więc
trzymanie jej aktywnej byłoby martwym wpisem mylącym przy diagnozie. Gdy
`matematykazen.pl` zacznie działać — odkomentuj tę linię. Ten sam moment
dotyczy `Required Notice:` w `LICENSE.md`, które też wskazuje jeszcze na GitHub
Pages (patrz `TODO.md`).

### Czego na liście świadomie nie ma

Wszystkie poniższe siedzą w `init-firewall.sh` jako **zakomentowane wpisy**
z powodem odrzucenia — nie trzeba ich odtwarzać od zera, wystarczy zdjąć `#`.

- **`henrich2137.github.io` / GitHub Pages** — nie trzeba nic dodawać. Domena
  rozwiązuje się na `185.199.108–111.153`, a to mieści się w zakresie
  `185.199.108.0/22`, który już wchodzi z pola `.web` w `api.github.com/meta`.
  Sprawdzone 2026-08-09: dorzucenie pola `.pages` do zapytania `jq` nie zmienia
  ani jednego wpisu w ipsecie (58 → 58).
- **`formspree.io`** — anycast Cloudflare (`172.66.x`). Filtr po IP otworzyłby
  współdzieloną infrastrukturę, a adresy i tak rotują. Formularz zgłoszeń
  testuje się w przeglądarce na hoście.
- **`pypi.org` / `files.pythonhosted.org` / `developer.mozilla.org`** — anycast
  Fastly (`151.101.x`), ta sama uwaga. Manim od 2026-08-11 **działa** w
  kontenerze i mimo to wpis dalej nie jest potrzebny: `pip install` odpala się
  w `Dockerfile`, czyli w czasie budowy obrazu — a firewall nakłada dopiero
  host, skryptem `host-firewall.sh`, na już zbudowany i uruchomiony kontener.
  Po starcie Manim nie pobiera niczego, więc pypi.org nigdy nie jest odpytywane
  zza firewalla.
- **`statsig.anthropic.com`** — w ogóle się nie rozwiązuje; Claude Code działa
  bez tego.
- **CDN-y frontendowe** (`cdn.jsdelivr.net`, `unpkg.com`, `fonts.googleapis.com`)
  — sprzeczne z offline-first tego projektu, który wendoruje KaTeX właśnie po to.

Kandydaci z dedykowanym, pojedynczym IP, gotowi do dopisania, gdyby się przydali:
`zpe.gov.pl`, `ore.edu.pl`, `men.gov.pl` oraz serwisy okręgowych komisji
(`oke.waw.pl`, `oke.krakow.pl`, `oke.poznan.pl`, `oke.wroc.pl`, `oke.gda.pl`,
`oke.lomza.pl`, `oke.jaworzno.pl`).

## Czego to NIE chroni

Warto mieć świadomość, bo część przecieków omija firewall z definicji:

- **Sockety wpuszczane przez VS Code** — ssh-agent, gpg-agent, X11, Wayland oraz
  git credential helper hosta. To nie jest ruch sieciowy, więc iptables ich nie
  widzi. Częściowo wyłączalne: `dev.containers.mountWaylandSocket: false`,
  `dev.containers.gitCredentialHelperConfigLocation: "none"`. Dla ssh-agenta
  i X11 rozszerzenie nie ma przełącznika (sprawdzone w wersji 0.463.0).
- **Dozwolone domeny jako kanał danych** — mając dostęp do GitHuba można wypchnąć
  dane do repo czy gista. Nie da się usunąć bez odcięcia gita.
- **DNS jako kanał danych** — zapytania do własnego serwera autorytatywnego
  z danymi w etykietach to klasyczny tunel, którego filtr po IP nie widzi.
  Zawężenie do resolwera z `resolv.conf` podnosi poprzeczkę (trzeba przejść
  przez cudzy rekurencyjny), ale nie zamyka kanału. Port 53 musi być otwarty,
  żeby cokolwiek działało.
- ~~**Panel WWW routera**~~ — **już nieaktualne** (2026-08-10). Do bramy
  przechodzi wyłącznie port 53, więc panel WWW, SMB ani IPP routera nie są
  z kontenera osiągalne. Szczegóły w sekcji „Brama: `/24` → `/32` → tylko
  port 53" wyżej.
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
  - **Najczęstszy powód po pełnej przebudowie: obserwator pilnuje tylko 180 s**
    (`WATCH_SECONDS` w `host-firewall.sh`), a `initializeCommand` odpala go
    **przed** budowaniem obrazu. Odkąd w obrazie siedzi TeX Live (paczka Manima,
    2026-08-11), rebuild potrafi trwać ~10 minut — okno obserwacji zamyka się
    długo przed startem kontenera, firewall nie zostaje nałożony i
    `postStartCommand` słusznie przerywa sesję. W logu widać wtedy „koniec okna
    obserwacji" bez wcześniejszego „OK: firewall nałożony". Zwykłe starty
    (bez przebudowy) mieszczą się w 180 s bez problemu, więc lekarstwo jest
    proste: po długim rebuildzie odpal `.devcontainer/host-firewall.sh` ręcznie
    z hosta albo po prostu ponów „Reopen in Container" — drugie podejście idzie
    już z cache'u.
- **VS Code otwiera pusty katalog** — rozjechał się `workspaceFolder`.
- **`sudo: unable to change to root gid`** — ktoś dodał `--cap-drop=ALL` bez
  SETUID/SETGID, a coś nadal próbuje używać `sudo`.
- **DNS nie działa po zmianie reguł bramy** — czyli `dig github.com` milczy,
  a `curl` do dozwolonych domen zwraca „Could not resolve host". W skrypcie jest
  **bezpiecznik**: po nałożeniu reguł sprawdza on `dig api.github.com` i przy
  braku odpowiedzi sam przywraca ogólną regułę UDP 53, wypisując
  `UWAGA: DNS nie działa po zawężeniu — przywracam ogólną regułę UDP 53`.
  Jeśli widzisz tę linię, kontener jedzie z jedną znaną słabością zamiast
  w ogóle nie wstać. Ustal, dokąd naprawdę chodzi DNS:

  ```bash
  cat /etc/resolv.conf          # kto jest resolwerem (pasta: 169.254.1.1)
  ip route | grep default       # kto jest bramą — to samo IP czy inne?
  iptables -L OUTPUT -n -v      # która reguła 53 łapie pakiety (licznik pkts)
  dig +short github.com
  ```

  Najczęstsza przyczyna: resolwer z `resolv.conf` to nie brama i nie ma dla
  niego reguły (albo `resolv.conf` zmieniło się po starcie kontenera).
- **Nie widać czegoś w LAN-ie (NAS, drukarka, panel routera)** — to jest
  **zamierzone**, nie awaria. Patrz sekcja „Brama: `/24` → `/32` → tylko
  port 53". Kontener ma dostawać się tylko do internetu z listy, nie do sieci
  domowej. Jeśli naprawdę potrzebujesz konkretnej usługi w LAN-ie, dopisz do
  `init-firewall.sh` regułę na **ten jeden adres i port**, nie na całą bramę.
- **Nie da się zapisać do `.devcontainer/` lub `.vscode/` z kontenera** — też
  zamierzone, oba katalogi są montowane `readonly`. Patrz sekcja
  „`.devcontainer/` i `.vscode/` tylko do odczytu".

## Świeża maszyna: dwa kroki, których repo nie zrobi za Ciebie

Oba dotyczą rzeczy leżących **poza repozytorium**, w katalogu domowym hosta —
przy pierwszym uruchomieniu na nowym komputerze kontener wywala się na nich,
zanim jeszcze cokolwiek z repo zdąży się wykonać. Oba robi się **raz na
maszynę**; przeżywają Rebuild Container, także z `--no-cache`.

**1. Chromium dla Playwrighta.** `devcontainer.json` montuje hostowy
`~/.cache/ms-playwright`, a podman przy bindzie nieistniejącej ścieżki nie
tworzy jej po cichu, tylko odmawia startu kontenera:

```
Error: statfs /home/<user>/.cache/ms-playwright: no such file or directory
```

Przeglądarkę pobiera się na hoście komendą z
[../issues/playwright-podglad.md](../issues/playwright-podglad.md) (~650 MB) —
wersja musi się zgadzać z `ARG PLAYWRIGHT_VERSION` w `Dockerfile`.

**2. Prawa do wolumenu `vscode`.** Ten wolumen (cache VS Code Servera, wspólny
dla wszystkich kontenerów) dokłada **samo rozszerzenie Dev Containers** — nie ma
go w `devcontainer.json`, więc nie da się go stamtąd skonfigurować. Rootless
podman tworzy go jako własność hostowego uid 1000, czyli użytkownika `node`
w kontenerze. Ale serwer instaluje **root**, a root w kontenerze to zmapowany
subuid, który przez `--cap-drop=ALL` nie ma `DAC_OVERRIDE` — więc do katalogu
`node` nie wejdzie:

```
mkdir: cannot create directory '/vscode/vscode-server': Permission denied
```

Pod Dockerem tego nie widać, bo tam root w kontenerze to root hosta. Jednorazowo
na hoście:

```bash
chmod 0777 "$(podman volume inspect vscode --format '{{.Mountpoint}}')"
```

Wraca to tylko po `podman volume rm vscode`. Alternatywa, jeśli wolisz nie mieć
katalogu 0777: ustaw `"dev.containers.cacheVolume": false` w **globalnym**
`settings.json` — to ustawienie ma zasięg `application`, więc nie da się go
zapisać w `.vscode/settings.json` w repo. Kosztuje ponowne rozpakowanie serwera
przy każdej przebudowie (kilka sekund, archiwum i tak leży w cache hosta).

## Zmiany wymagające przebudowy

`init-firewall.sh` jest kopiowany do obrazu, więc po jego edycji potrzebny jest
**Rebuild Container** (zwykły, bez `--no-cache` — przebuduje się tylko warstwa
`COPY` i te pod nią). `host-firewall.sh` działa na hoście, a
`verify-firewall.sh` uruchamia się z podmontowanego repo — te dwa nie wymagają
przebudowy, wystarczy „Reopen".

Zmiany w `Dockerfile` i w `mounts` w `devcontainer.json` też wymagają
**Rebuild Container** — samo „Reopen" nie doda nowego wolumenu do istniejącego
kontenera.

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
