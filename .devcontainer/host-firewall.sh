#!/usr/bin/env bash
# Nakłada firewall na kontener deweloperski Z HOSTA (spoza kontenera).
#
# PO CO TO ISTNIEJE
# Podman wkłada uprawnienia dodane przez --cap-add do zestawu "ambient" także
# zwykłemu użytkownikowi. Gdyby więc kontener dostał NET_ADMIN (żeby sam nałożył
# sobie firewall w postStartCommand), to każdy proces w środku — łącznie z
# agentem AI — mógłby go rozbroić jednym `iptables -F`, bez żadnego sudo.
# Dlatego kontener NIE dostaje NET_ADMIN, a reguły nakłada ten skrypt z zewnątrz
# przez `exec --privileged`. Wtedy w środku nie ma jak ich zdjąć.
#
# ZASIĘG REGUŁ
# `exec` wchodzi do network namespace kontenera, więc reguły dotyczą wyłącznie
# jego. Sieć hosta pozostaje nietknięta. Przy rootless podmanie ten "uprzywilejowany"
# proces jest rootem tylko wewnątrz Twojego user namespace i fizycznie nie może
# zmienić netfiltera hosta.
#
# UŻYCIE
#   .devcontainer/host-firewall.sh           – nałóż teraz i wypisz wynik (ręcznie)
#   .devcontainer/host-firewall.sh --spawn   – oddaj obserwatora systemd-owi (z initializeCommand)
#   .devcontainer/host-firewall.sh --watch   – pilnuj przez 3 min (woła to --spawn)
#
# Wywołanie ręczne przydaje się po restarcie kontenera, gdy VS Code nie
# przechodził przez initializeCommand.

set -uo pipefail

LOG="${TMPDIR:-/tmp}/matematykazen-host-firewall.log"
log() { printf '%s  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" | tee -a "$LOG"; }

# Ślad natychmiast po starcie, przed jakąkolwiek pracą — żeby w razie awarii
# było wiadomo, czy skrypt w ogóle wystartował (przez dwie iteracje log bywał
# pusty i to była najbardziej myląca część diagnozy).
[ "${1:-}" = "--watch" ] || [ "${1:-}" = "--spawn" ] && log "start (${1:-}), pid $$"

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
TARGET=$(realpath -m "$SCRIPT_DIR/..")
FW_IN_CONTAINER=/usr/local/bin/init-firewall.sh
UNIT=matematykazen-firewall-watch
WATCH_SECONDS=180
POLL_SECONDS=5

CLI=""
for candidate in podman docker; do
  if command -v "$candidate" >/dev/null 2>&1; then CLI="$candidate"; break; fi
done
if [ -z "$CLI" ]; then
  log "BŁĄD: nie znaleziono ani podmana, ani dockera."
  exit 1
fi

# Szuka działającego kontenera tego repo po etykiecie, którą nadaje rozszerzenie
# Dev Containers. Porównanie idzie przez realpath, bo na systemach ostree
# (Bazzite) VS Code zapisuje /home/..., a skrypt widzi /var/home/... — to ta
# sama ścieżka przez dowiązanie.
find_container() {
  local id value
  for id in $("$CLI" ps -q --filter "label=devcontainer.local_folder" 2>/dev/null); do
    value=$("$CLI" inspect "$id" --format '{{index .Config.Labels "devcontainer.local_folder"}}' 2>/dev/null) || continue
    [ -n "$value" ] || continue
    if [ "$(realpath -m "$value" 2>/dev/null)" = "$TARGET" ]; then
      echo "$id"
      return 0
    fi
  done
  return 1
}

# Ostatnia reguła nakładana przez init-firewall.sh — jej obecność oznacza, że
# firewall jest już aktywny.
is_armed() {
  "$CLI" exec --privileged -u root "$1" \
    iptables -C OUTPUT -j REJECT --reject-with icmp-admin-prohibited >/dev/null 2>&1
}

arm() {
  local cid=$1 output
  if output=$("$CLI" exec --privileged -u root "$cid" "$FW_IN_CONTAINER" 2>&1); then
    log "OK: firewall nałożony na kontener ${cid:0:12}."
    return 0
  fi
  log "BŁĄD: nie udało się nałożyć firewalla na ${cid:0:12}:"
  printf '%s\n' "$output" | tail -5 | tee -a "$LOG"
  return 1
}

if [ "${1:-}" = "--spawn" ]; then
  # Tryb dla initializeCommand. Wykonuje się SYNCHRONICZNIE i szybko, po czym
  # oddaje obserwatora systemd-owi. Dlaczego nie zwykłe `... &`: dwie takie
  # próby (z nohup, potem z setsid) ginęły bez zapisania ani jednej linii do
  # logu — VS Code sprząta po initializeCommand agresywniej, niż da się obejść
  # samym odczepieniem procesu. Jednostka systemd żyje we własnym cgroupie,
  # poza drzewem procesów VS Code, więc nie ma czego sprzątać.
  log "spawn: PATH=$PATH"
  if command -v systemd-run >/dev/null 2>&1; then
    systemctl --user stop "$UNIT" >/dev/null 2>&1
    systemctl --user reset-failed "$UNIT" >/dev/null 2>&1
    if systemd-run --user --collect --unit="$UNIT" \
         bash "$SCRIPT_DIR/$(basename "${BASH_SOURCE[0]}")" --watch >/dev/null 2>&1; then
      log "spawn: obserwator oddany systemd (jednostka $UNIT)"
      exit 0
    fi
    log "spawn: systemd-run zawiódł, próbuję setsid"
  fi
  setsid nohup bash "$SCRIPT_DIR/$(basename "${BASH_SOURCE[0]}")" --watch >/dev/null 2>&1 </dev/null &
  log "spawn: obserwator odpalony przez setsid (pid $!)"
  exit 0
fi

if [ "${1:-}" = "--watch" ]; then
  # Tryb dla initializeCommand: rozszerzenie odpala nas ZANIM kontener powstanie,
  # więc czekamy, aż się pojawi. Pilnujemy przez cały okres startu, bo przy
  # przebudowie stary kontener bywa jeszcze widoczny i zaraz znika — wtedy nowy
  # zastanie nas gotowych. Kolejne przejścia są bezpieczne: gdy firewall już
  # stoi, nic nie robimy.
  log "obserwuję przez ${WATCH_SECONDS}s, repo: $TARGET, cli: $CLI"
  deadline=$((SECONDS + WATCH_SECONDS))
  while [ "$SECONDS" -lt "$deadline" ]; do
    if cid=$(find_container); then
      is_armed "$cid" || arm "$cid"
    fi
    sleep "$POLL_SECONDS"
  done
  log "koniec okna obserwacji"
  exit 0
fi

# Tryb ręczny.
if ! cid=$(find_container); then
  echo "Nie znalazłem działającego kontenera dla $TARGET." >&2
  echo "Otwórz projekt w kontenerze (Reopen in Container) i uruchom skrypt ponownie." >&2
  exit 1
fi
if is_armed "$cid"; then
  echo "Firewall już aktywny na kontenerze ${cid:0:12} — nic do zrobienia."
  exit 0
fi
