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
#   .devcontainer/host-firewall.sh                 – nałóż teraz i wypisz wynik (ręcznie)
#   .devcontainer/host-firewall.sh --spawn         – oddaj obserwatorów systemd-owi (z initializeCommand)
#   .devcontainer/host-firewall.sh --watch         – pilnuj, aż firewall stanie (woła to --spawn)
#   .devcontainer/host-firewall.sh --openai        – dopisz teraz aktualne adresy OpenAI (jednorazowo)
#   .devcontainer/host-firewall.sh --openai-watch  – dopisuj je w kółko (woła to --spawn)
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

# ODŚWIEŻANIE ADRESÓW OPENAI
#
# Codex gada z domenami stojącymi za Cloudflare, a te zwracają adresy z puli,
# która zmienia się w ciągu dnia. init-firewall.sh wypełnia ipset RAZ, przy
# starcie kontenera, więc po kilku godzinach Codex zaczyna trafiać na adresy
# spoza listy i dostaje same timeouty. To jest znany problem, nie egzotyka.
#
# Odświeżanie MUSI iść z hosta: kontener ma --cap-drop=ALL, więc sam nie ma
# prawa dotknąć ipsetu (i o to chodzi — inaczej mógłby sobie dopisać, co chce).
#
# Dopisujemy tylko adresy, nigdy nie kasujemy. Stare wpisy zostają do restartu
# kontenera; to garść adresów Cloudflare, czyli ta sama infrastruktura, którą
# ten wyjątek i tak otwiera.
OPENAI_DOMAINS=(auth.openai.com chatgpt.com api.openai.com)
OPENAI_UNIT=matematykazen-openai-ips
OPENAI_REFRESH_SECONDS=120
# Po tylu kolejnych próbach bez kontenera odświeżacz kończy pracę (kontener
# zamknięty albo przebudowywany — nowy start i tak odpali go od nowa).
OPENAI_MAX_MISSES=5
# Górny limit czekania, nie długość pracy: obserwator kończy sam, gdy tylko
# firewall stoi (patrz tryb --watch). 900 s jest po to, żeby przetrwać PEŁNĄ
# przebudowę obrazu — odkąd siedzi w nim TeX Live, potrafi ona trwać ~10 minut,
# a przy poprzednim limicie 180 s okno zamykało się, zanim kontener wystartował,
# i firewall nie był nakładany (zdarzyło się 2026-08-11). Przy zwykłym starcie
# ta liczba nie ma znaczenia — obserwator znika po kilkudziesięciu sekundach.
WATCH_SECONDS=900
POLL_SECONDS=5
# Ile jeszcze pilnować po nałożeniu firewalla, zanim uznamy robotę za skończoną.
# Zapas na podmianę kontenera tuż po starcie; bez niego wychodzilibyśmy w chwili,
# gdy VS Code może jeszcze wymienić kontener pod nami.
GRACE_SECONDS=60

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

# Rozwiązuje nazwę na adresy IPv4. `dig` jest pewniejszy (pyta DNS wprost i
# widzi całą pulę), ale nie na każdym hoście jest zainstalowany, więc jest
# zapasowe `getent`, które idzie przez systemowe rozwiązywanie nazw.
resolve_ipv4() {
  local domain=$1
  if command -v dig >/dev/null 2>&1; then
    dig +short +time=3 +tries=1 A "$domain" 2>/dev/null | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'
  else
    getent ahostsv4 "$domain" 2>/dev/null | awk '{print $1}' | sort -u
  fi
}

# Dopisuje do ipsetu kontenera adresy, pod którymi AKTUALNIE stoi OpenAI.
# Bezpieczne przy wielokrotnym wywołaniu: `ipset add -exist` nie protestuje na
# duplikat, a licznik pokazuje tylko to, czego wcześniej nie było.
refresh_openai() {
  local cid=$1 domain ip added=0
  for domain in "${OPENAI_DOMAINS[@]}"; do
    while read -r ip; do
      [ -n "$ip" ] || continue
      [[ "$ip" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]] || continue
      if "$CLI" exec --privileged -u root "$cid" \
           ipset test allowed-domains "$ip" >/dev/null 2>&1; then
        continue
      fi
      if "$CLI" exec --privileged -u root "$cid" \
           ipset add allowed-domains "$ip" -exist >/dev/null 2>&1; then
        added=$((added + 1))
      fi
    done < <(resolve_ipv4 "$domain")
  done
  if [ "$added" -gt 0 ]; then
    log "OpenAI: dopisano $added nowych adresów do ipsetu ${cid:0:12}"
  fi
  return 0
}

if [ "${1:-}" = "--spawn" ]; then
  # Tryb dla initializeCommand. Wykonuje się SYNCHRONICZNIE i szybko, po czym
  # oddaje obserwatora systemd-owi. Dlaczego nie zwykłe `... &`: dwie takie
  # próby (z nohup, potem z setsid) ginęły bez zapisania ani jednej linii do
  # logu — VS Code sprząta po initializeCommand agresywniej, niż da się obejść
  # samym odczepieniem procesu. Jednostka systemd żyje we własnym cgroupie,
  # poza drzewem procesów VS Code, więc nie ma czego sprzątać.
  log "spawn: PATH=$PATH"
  # $1 = nazwa jednostki systemd, $2 = tryb, z którym odpalamy sami siebie.
  spawn_unit() {
    local unit=$1 mode=$2
    if command -v systemd-run >/dev/null 2>&1; then
      systemctl --user stop "$unit" >/dev/null 2>&1
      systemctl --user reset-failed "$unit" >/dev/null 2>&1
      if systemd-run --user --collect --unit="$unit" \
           bash "$SCRIPT_DIR/$(basename "${BASH_SOURCE[0]}")" "$mode" >/dev/null 2>&1; then
        log "spawn: $mode oddany systemd (jednostka $unit)"
        return 0
      fi
      log "spawn: systemd-run zawiódł dla $mode, próbuję setsid"
    fi
    setsid nohup bash "$SCRIPT_DIR/$(basename "${BASH_SOURCE[0]}")" "$mode" >/dev/null 2>&1 </dev/null &
    log "spawn: $mode odpalony przez setsid (pid $!)"
  }
  spawn_unit "$UNIT" --watch
  # Drugi obserwator, osobny i długowieczny: pierwszy kończy pracę zaraz po
  # nałożeniu firewalla, a adresy OpenAI trzeba odświeżać przez cały czas
  # życia kontenera (patrz komentarz przy OPENAI_DOMAINS wyżej).
  spawn_unit "$OPENAI_UNIT" --openai-watch
  exit 0
fi

if [ "${1:-}" = "--openai-watch" ]; then
  # Dopisuje bieżące adresy OpenAI do ipsetu, dopóki kontener żyje. Bez tego
  # Codex działa po starcie kontenera, a po kilku godzinach cichnie na timeoutach.
  log "odświeżam adresy OpenAI co ${OPENAI_REFRESH_SECONDS}s, repo: $TARGET"
  misses=0
  while true; do
    if cid=$(find_container); then
      misses=0
      # Tylko na uzbrojonym kontenerze: przed nałożeniem firewalla ipset
      # jeszcze nie istnieje, a init-firewall.sh i tak zaraz wypełni go sam.
      if is_armed "$cid"; then
        refresh_openai "$cid"
      fi
    else
      misses=$((misses + 1))
      if [ "$misses" -ge "$OPENAI_MAX_MISSES" ]; then
        log "brak kontenera od $OPENAI_MAX_MISSES prób — kończę odświeżanie adresów OpenAI"
        exit 0
      fi
    fi
    sleep "$OPENAI_REFRESH_SECONDS"
  done
fi

if [ "${1:-}" = "--openai" ]; then
  # Jednorazowe dopisanie adresów, do ręcznego użycia: gdy Codex nagle przestał
  # odpowiadać, a nie chcesz restartować kontenera.
  if ! cid=$(find_container); then
    echo "Nie znalazłem działającego kontenera dla $TARGET." >&2
    exit 1
  fi
  if ! is_armed "$cid"; then
    echo "Firewall nie jest jeszcze nałożony — uruchom skrypt bez argumentów." >&2
    exit 1
  fi
  refresh_openai "$cid"
  echo "Adresy OpenAI odświeżone na kontenerze ${cid:0:12}."
  exit 0
fi

if [ "${1:-}" = "--watch" ]; then
  # Tryb dla initializeCommand: rozszerzenie odpala nas ZANIM kontener powstanie,
  # więc czekamy, aż się pojawi. Kolejne przejścia są bezpieczne: gdy firewall
  # już stoi, nic nie robimy.
  #
  # Wyjście jest warunkowe, nie czasowe: kończymy GRACE_SECONDS po tym, jak
  # firewall stanął — czyli przy zwykłym starcie po kilkudziesięciu sekundach,
  # a pełny limit WATCH_SECONDS zużywamy tylko wtedy, gdy naprawdę trzeba, czyli
  # gdy kontener buduje się kilkanaście minut. Dzięki temu długie okno nic nie
  # kosztuje w codziennym użyciu.
  #
  # Zniknięcie pilnowanego kontenera kasuje odliczanie i wracamy do czekania:
  # przy przebudowie stary kontener bywa jeszcze przez chwilę widoczny (i już
  # uzbrojony), a zaraz znika — gdybyśmy liczyli grace od niego, wyszlibyśmy,
  # zanim pojawi się nowy.
  log "obserwuję (do ${WATCH_SECONDS}s, wyjście ${GRACE_SECONDS}s po nałożeniu firewalla), repo: $TARGET, cli: $CLI"
  deadline=$((SECONDS + WATCH_SECONDS))
  watched_cid=""
  grace_end=0
  while [ "$SECONDS" -lt "$deadline" ]; do
    if cid=$(find_container); then
      # Nowy (albo pierwszy) kontener — odliczanie liczymy od zera.
      if [ "$cid" != "$watched_cid" ]; then
        watched_cid=$cid
        grace_end=0
      fi
      if is_armed "$cid" || arm "$cid"; then
        if [ "$grace_end" -eq 0 ]; then
          grace_end=$((SECONDS + GRACE_SECONDS))
        elif [ "$SECONDS" -ge "$grace_end" ]; then
          log "firewall stoi na ${cid:0:12} od ${GRACE_SECONDS}s — kończę obserwację"
          exit 0
        fi
      fi
    else
      # Brak kontenera: albo jeszcze się buduje, albo właśnie znika przy
      # przebudowie. W obu przypadkach czekamy dalej, bez odliczania.
      watched_cid=""
      grace_end=0
    fi
    sleep "$POLL_SECONDS"
  done
  log "koniec okna obserwacji (limit ${WATCH_SECONDS}s)"
  exit 0
fi

# Tryb ręczny.
if ! cid=$(find_container); then
  echo "Nie znalazłem działającego kontenera dla $TARGET." >&2
  echo "Otwórz projekt w kontenerze (Reopen in Container) i uruchom skrypt ponownie." >&2
  exit 1
fi
if is_armed "$cid"; then
  echo "Firewall już aktywny na kontenerze ${cid:0:12} — nie nakładam go drugi raz."
  # Przy okazji dopisujemy bieżące adresy OpenAI: jak ktoś odpala ten skrypt
  # ręcznie, to zwykle dlatego, że coś w kontenerze przestało mieć sieć.
  refresh_openai "$cid"
  exit 0
fi

# Firewalla jeszcze nie ma — nakładamy. (Do 2026-08-29 tej linii tu nie było,
# więc tryb ręczny kończył się po samym sprawdzeniu i nic nie robił.)
if arm "$cid"; then
  echo "Firewall nałożony na kontener ${cid:0:12}."
  exit 0
fi
echo "Nie udało się nałożyć firewalla — szczegóły w $LOG" >&2
exit 1
