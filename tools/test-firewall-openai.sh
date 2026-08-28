#!/usr/bin/env bash
# Test odswiezania adresow OpenAI w .devcontainer/host-firewall.sh.
#
# PO CO: bez tego mechanizmu Codex w kontenerze dziala po starcie, a po kilku
# godzinach cichnie na timeoutach, bo Cloudflare podmienia adresy, a ipset jest
# wypelniany raz. Blad jest niewidoczny golym okiem i objawia sie z opoznieniem,
# wiec sprawdzamy go skryptem, a nie klikaniem.
#
# JAK: podstawiamy atrapy `podman` i `dig` na poczatek PATH, wiec test nie
# dotyka ani sieci, ani prawdziwego kontenera. Sprawdzamy dwie rzeczy:
#   1. tryb --openai dopisuje do ipsetu adresy, ktorych tam jeszcze nie ma,
#   2. nie dopisuje tych, ktore juz sa (inaczej log zalewaja falszywe zmiany).
#
# UZYCIE: bash tools/test-firewall-openai.sh   (na hoscie, bez sieci)

set -uo pipefail

REPO=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
REPO=$(realpath -m "$REPO")
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

export STUB_STATE="$WORK"
mkdir -p "$WORK/bin"

# Adres 1.1.1.1 udaje wpis, ktory juz jest w ipsecie; pozostale sa nowe.
printf '1.1.1.1\n' > "$WORK/ipset-existing"
: > "$WORK/ipset-added"

cat > "$WORK/bin/dig" <<'STUB'
#!/usr/bin/env bash
# Kazda z trzech domen dostaje ten sam zestaw: jeden adres znany, dwa nowe.
printf '1.1.1.1\n104.18.32.47\n172.64.155.209\n'
STUB

cat > "$WORK/bin/podman" <<'STUB'
#!/usr/bin/env bash
case "$1" in
  ps)      echo "stubcid000000" ;;
  inspect) echo "$STUB_REPO" ;;
  exec)
    shift
    while [ "$1" = "--privileged" ] || [ "$1" = "-u" ] || [ "$1" = "root" ]; do shift; done
    shift  # id kontenera
    case "$1 ${2:-}" in
      "iptables -C") exit 0 ;;                       # firewall nalozony
      "ipset test")  grep -qx "$4" "$STUB_STATE/ipset-existing" ;;
      "ipset add")   echo "$4" >> "$STUB_STATE/ipset-added"
                     echo "$4" >> "$STUB_STATE/ipset-existing" ;;
      *) exit 0 ;;
    esac
    ;;
  *) exit 0 ;;
esac
STUB

chmod +x "$WORK/bin/dig" "$WORK/bin/podman"
export STUB_REPO="$REPO"
export PATH="$WORK/bin:$PATH"
export TMPDIR="$WORK"

bash "$REPO/.devcontainer/host-firewall.sh" --openai >"$WORK/out1" 2>&1
rc=$?

fail() { echo "PADL: $1"; echo "--- wyjscie ---"; cat "$WORK/out1" "$WORK/out2" 2>/dev/null; exit 1; }

[ "$rc" -eq 0 ] || fail "tryb --openai zwrocil kod $rc"

added=$(sort -u "$WORK/ipset-added" | tr '\n' ' ')
echo "dopisane adresy: $added"
grep -qx "104.18.32.47"  "$WORK/ipset-added" || fail "nie dopisano 104.18.32.47"
grep -qx "172.64.155.209" "$WORK/ipset-added" || fail "nie dopisano 172.64.155.209"
grep -qx "1.1.1.1" "$WORK/ipset-added" && fail "dopisano adres, ktory juz byl w ipsecie"

# Drugie przejscie: wszystko jest juz w ipsecie, wiec nic nowego dopisac sie nie moze.
: > "$WORK/ipset-added"
bash "$REPO/.devcontainer/host-firewall.sh" --openai >"$WORK/out2" 2>&1 || fail "drugie przejscie zwrocilo blad"
[ -s "$WORK/ipset-added" ] && fail "drugie przejscie dopisalo adresy, ktore juz byly"

echo "OK: nowe adresy dopisane, duplikaty pominiete"
