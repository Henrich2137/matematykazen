#!/usr/bin/env bash
# Uruchamiane jako postStartCommand, czyli WEWNĄTRZ kontenera, jako user node.
#
# Sam firewall nakłada host (patrz host-firewall.sh) i robi to równolegle ze
# startem kontenera, więc tutaj tylko czekamy, aż reguły się pojawią, i mówimy
# głośno, jeśli się nie pojawiły. Nie potrzeba do tego żadnych uprawnień —
# sprawdzamy zachowanie sieci, nie tablice iptables (do których, celowo, nie
# mamy tu dostępu).
#
# Kanarek: adres spoza listy dozwolonych. Póki jest osiągalny, firewalla nie ma.

set -uo pipefail

CANARY="https://example.com"
# ~90 s. Host zwykle nakłada firewall w ~25 s od startu kontenera (5 s na
# wykrycie + ~20 s na pobranie zakresów IP GitHuba), więc to zapas z nawiązką.
ATTEMPTS=45
INTERVAL=2

for _ in $(seq 1 "$ATTEMPTS"); do
  if ! curl -s -o /dev/null -m 3 "$CANARY"; then
    echo "Firewall aktywny — ruch poza listą dozwolonych domen jest blokowany."
    exit 0
  fi
  sleep "$INTERVAL"
done

cat >&2 <<'EOF'

BŁĄD: firewall nie został nałożony — kontener ma nieograniczony dostęp do sieci.

Reguły nakłada host, nie kontener. Uruchom w terminalu NA HOŚCIE (nie tutaj):

    .devcontainer/host-firewall.sh

i sprawdź log: /tmp/matematykazen-host-firewall.log

EOF
exit 1