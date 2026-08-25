# Host czy kontener, i na jakiej maszynie

Jak model ma ustalić, gdzie właściwie działa. Powstało 2026-08-25, po sesji,
w której model przez pół rozmowy twierdził, że jest na hoście, siedząc
w devcontainerze.

## Co poszło źle

Model sprawdził istnienie pliku `/.dockerenv` i po jego braku ogłosił „jesteś
na hoście". Plik `/.dockerenv` tworzy **Docker**. Kontenery w tym projekcie
stoją na **rootless podmanie**, który tego pliku nie tworzy w ogóle, więc test
zawsze wychodził negatywnie. Henrich zauważył błąd sam, po tym że terminal
odpalał zsh z kontenera.

Dwie rzeczy warte zapamiętania:

- **Odpowiedź „host" była zgodna z bezpieczną wartością domyślną z CLAUDE.md,
  ale i tak szkodliwa.** Nadmiar ostrożności nic nie psuje, natomiast pewne
  zdanie „jesteśmy na hoście" wypchnęło rozmowę na złą ścieżkę: model zaczął
  doradzać przy gicie tak, jakby montowania tylko do odczytu nie istniały.
  Domyślna ostrożność ma zastępować **wiedzę**, nie zastępować **sprawdzenia**.
- **Fakt był już zapisany w repo.** `MACHINES.md` mówi wprost „Dev Containers
  na obu maszynach oparte o Podman (nie Docker)". Model wybrał marker, zanim
  przeczytał plik opisujący środowisko.

## Poprawne sprawdzenie

Jedna komenda, cztery markery, koszt żaden:

```sh
if [ -n "$REMOTE_CONTAINERS$DEVCONTAINER$container" ] || [ -e /run/.containerenv ] || [ -e /.dockerenv ]; then echo KONTENER; else echo HOST; fi
```

Kolejność jest celowa: najpierw zmienne od VS Code (działają niezależnie od
silnika kontenerów), potem podman, na końcu docker.

| Marker | Kto go ustawia | Na tej maszynie (2026-08-25) |
|---|---|---|
| `$REMOTE_CONTAINERS` | VS Code Dev Containers | `true` |
| `$DEVCONTAINER` | VS Code Dev Containers | `true` |
| `$container` | sam podman | `podman` |
| `/run/.containerenv` | podman | jest |
| `/.dockerenv` | **tylko** docker | brak |

Sprawdzone w obie strony: komenda zwraca `KONTENER` tutaj, a `HOST`, gdy
wyczyścić te zmienne i podstawić nieistniejące ścieżki (`env -u REMOTE_CONTAINERS
-u DEVCONTAINER -u container`), więc nie zwraca „kontener" po prostu zawsze.

**Zasada dla modelu:** brak jednego markera nie jest dowodem na hosta. Zdanie
„jesteśmy na hoście" wolno napisać dopiero wtedy, gdy **żaden** z tych markerów
nie zadziałał. Przy jakimkolwiek rozjeździe obowiązuje reguła z CLAUDE.md:
zakładasz hosta i pracujesz wg `HOSTRULES.md`, ale mówisz Henrichowi wprost,
że to założenie, a nie pomiar.

## Na jakim systemie stoi host

Da się ustalić z wnętrza kontenera, bo **kontener dzieli jądro z hostem**.

```sh
uname -r                                  # jądro HOSTA, nie kontenera
git config user.name                      # nazwa maszyny, VS Code kopiuje z hosta
grep ' /workspaces/matematykazen ' /proc/self/mountinfo   # ścieżka i system plików hosta
```

Zmierzone na tej maszynie 2026-08-25:

| Marker | Wartość | Co z tego wynika |
|---|---|---|
| `uname -r` | `7.2.0-ogc6.1.fc44.x86_64` | `fc44` = Fedora 44, a Bazzite stoi na Fedorze |
| `git config user.name` | `HenrichBazzite` | maszyna nazywa się wprost |
| system plików repo | `btrfs`, z `seclabel` | btrfs i SELinux, czyli rodzina Fedory |
| ścieżka repo na hoście | `/home/wojciech/matematykazen` | login na hoście |

**Najprostsza reguła: `uname -r` zawiera `fc` → Bazzite.** Reszta to potwierdzenie.

### Czego NIE ustalono

- **Jak te markery wyglądają na Kubuntu, nie wiadomo**, bo sesji na laptopie
  jeszcze nie było. Spodziewane, lecz niesprawdzone: jądro z końcówką
  `-generic` zamiast `fc`, brak `seclabel`, inny `git config user.name`.
  Kolejna sesja na Kubuntu ma to zapisać do `MACHINES.md`.
- Nie sprawdzono, jak którykolwiek z tych markerów zachowuje się przy pracy
  z Windowsa (WSL, Git Bash).

### Pułapka: `/etc/os-release` mówi o kontenerze

`cat /etc/os-release` w kontenerze zwraca **Debian 12**, bo taki jest obraz
z `.devcontainer/Dockerfile`. To poprawna odpowiedź na inne pytanie i nie mówi
nic o tym, czy pod spodem jest Bazzite czy Kubuntu. Do systemu hosta służy
`uname -r`, nie `/etc/os-release`.
