#!/bin/bash
set -euo pipefail  # Exit on error, undefined vars, and pipeline failures
IFS=$'\n\t'       # Stricter word splitting

# 1. Extract Docker DNS info BEFORE any flushing
DOCKER_DNS_RULES=$(iptables-save -t nat | grep "127\.0\.0\.11" || true)

# Flush existing rules and delete existing ipsets
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
ipset destroy allowed-domains 2>/dev/null || true

# 2. Selectively restore ONLY internal Docker DNS resolution
if [ -n "$DOCKER_DNS_RULES" ]; then
    echo "Restoring Docker DNS rules..."
    iptables -t nat -N DOCKER_OUTPUT 2>/dev/null || true
    iptables -t nat -N DOCKER_POSTROUTING 2>/dev/null || true
    echo "$DOCKER_DNS_RULES" | xargs -L 1 iptables -t nat
else
    echo "No Docker DNS rules to restore"
fi

# DNS: TYLKO do resolwerów z /etc/resolv.conf, nie do dowolnego adresu.
# Oryginał przepuszczał UDP 53 wszędzie, co jest gotowym kanałem eksfiltracji —
# dane koduje się w etykietach zapytania do własnego serwera autorytatywnego,
# a odpowiedzi odbiera w rekordach TXT. Lista domen tego nie widzi, bo filtruje
# po docelowym IP. Czytanie resolv.conf jest przenośne: pod podmanem/pastą jest
# tam 169.254.1.1, pod Dockerem 127.0.0.11.
DNS_SERVERS=$(awk '$1 == "nameserver" && $2 ~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/ {print $2}' /etc/resolv.conf)
if [ -z "$DNS_SERVERS" ]; then
    echo "ERROR: brak resolwera IPv4 w /etc/resolv.conf — nie wiem, komu zezwolić na DNS"
    exit 1
fi
while read -r ns; do
    echo "Allowing DNS to $ns"
    iptables -A OUTPUT -p udp --dport 53 -d "$ns" -j ACCEPT
    iptables -A OUTPUT -p tcp --dport 53 -d "$ns" -j ACCEPT
    iptables -A INPUT -p udp --sport 53 -s "$ns" -j ACCEPT
done < <(echo "$DNS_SERVERS")
# SSH na zewnątrz jest ŚWIADOMIE zablokowany: przy zdalnym repo po HTTPS jest
# niepotrzebny, a w połączeniu z forwardowanym ssh-agentem hosta byłby gotowym
# kanałem eksfiltracji (scp/git push na dowolny serwer).
# Jeśli kiedyś przejdziesz na remote po SSH, odkomentuj:
# iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT
# iptables -A INPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

# Allow localhost
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Create ipset with CIDR support
ipset create allowed-domains hash:net

# Fetch GitHub meta information and aggregate + add their IP ranges
echo "Fetching GitHub IP ranges..."
gh_ranges=$(curl -s https://api.github.com/meta)
if [ -z "$gh_ranges" ]; then
    echo "ERROR: Failed to fetch GitHub IP ranges"
    exit 1
fi

if ! echo "$gh_ranges" | jq -e '.web and .api and .git' >/dev/null; then
    echo "ERROR: GitHub API response missing required fields"
    exit 1
fi

echo "Processing GitHub IPs..."
while read -r cidr; do
    if [[ ! "$cidr" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2}$ ]]; then
        echo "ERROR: Invalid CIDR range from GitHub meta: $cidr"
        exit 1
    fi
    echo "Adding GitHub range $cidr"
    ipset add allowed-domains "$cidr"
done < <(echo "$gh_ranges" | jq -r '(.web + .api + .git)[]' | aggregate -q)

# Resolve and add other allowed domains.
#
# Lista jest ROZDZIELONA na dwie, bo nie każda domena jest tak samo ważna:
#
# KRYTYCZNE — bez nich sesja nie ma sensu (git, model, pakiety, rozszerzenia).
# Nierozwiązana domena przerywa skrypt, a że postStartCommand jest fail-closed,
# to znaczy "nie wchodzisz do kontenera". Tak ma być: lepiej nie wejść, niż
# pracować w środowisku, w którym połowa narzędzi milczy.
#
# TREŚCIOWE — źródła arkuszy i kluczy CKE. Te serwisy bywają chwilowo
# niedostępne, a to żaden powód, żeby zablokować wejście do kontenera. Brak
# rozwiązania daje OSTRZEŻENIE i lecimy dalej; jedyny skutek to tyle, że ruch
# do tej domeny nie zostanie przepuszczony w tej sesji (firewall zostaje
# szczelny — nie otwieramy niczego "na wszelki wypadek").
#
# Czego tu ŚWIADOMIE NIE MA:
# - github.io / GitHub Pages — już przepuszczone przez zakres 185.199.108.0/22
#   z api.github.com/meta (pole .web). Dopisanie pola .pages nie zmienia ani
#   jednego wpisu w ipsecie — sprawdzone 2026-08-09.
# - matematykazen.pl — domena jeszcze nie istnieje w DNS, więc dopisanie jej
#   dziś = pewny `exit 1` i zablokowana sesja. Dodać dopiero, gdy ruszy.
# - formspree.io — anycast Cloudflare. Filtrujemy po IP, nie po SNI, więc
#   wpuszczenie tych adresów otwiera kawałek współdzielonej infrastruktury.
#   Formularz zgłoszeń i tak testuje się w przeglądarce na hoście.
CRITICAL_DOMAINS=(
    "registry.npmjs.org"
    "api.anthropic.com"
    "sentry.io"
    "marketplace.visualstudio.com"
    "vscode.blob.core.windows.net"
    "update.code.visualstudio.com"
)

# www.cke.gov.pl to CNAME na apex (ten sam adres) — wpis jest redundantny,
# trzymany wyłącznie na wypadek, gdyby CKE kiedyś rozdzieliło te hosty.
CONTENT_DOMAINS=(
    "cke.gov.pl"
    "www.cke.gov.pl"
    "arkusze.pl"
    "zpe.gov.pl"      # Zintegrowana Platforma Edukacyjna (MEN)
    "ore.edu.pl"      # Ośrodek Rozwoju Edukacji — podstawa programowa
    "men.gov.pl"      # rozporządzenia, komunikaty o formule egzaminu

    # ODKOMENTUJ, GDY matematykazen.pl RUSZY. Dziś domena nie istnieje w DNS.
    # Siedzi na liście treściowej, więc nie wywaliłaby skryptu (dostałaby tylko
    # ostrzeżenie), ale wisiałby tu martwy wpis mylący przy każdej diagnozie.
    # "matematykazen.pl"

    # KANDYDACI — bezpieczni, ale niepotrzebni na dziś. Każdy ma własny,
    # pojedynczy adres IP, więc odkomentowanie wpuszcza dokładnie ten serwer
    # i nic poza nim. Odkomentuj, gdy zaczniesz ściągać arkusze z konkretnej
    # okręgowej komisji (OKE publikują je równolegle do CKE).
    # "oke.waw.pl"
    # "oke.krakow.pl"
    # "oke.poznan.pl"
    # "oke.wroc.pl"
    # "oke.gda.pl"
    # "oke.lomza.pl"
    # "oke.jaworzno.pl"

    # ODRZUCONE ŚWIADOMIE — odkomentuj TYLKO wtedy, gdy coś konkretnego przez
    # nie nie działa, i wiedząc, co dokładnie otwierasz. Powód odrzucenia jest
    # ten sam dla pierwszych czterech: filtrujemy po docelowym IP, nie po SNI,
    # więc wpuszczenie adresu współdzielonego anycastu CDN-a otwiera kawałek
    # infrastruktury obsługującej tysiące cudzych serwisów — a same adresy
    # jeszcze do tego rotują, więc lista i tak potrafi się zdezaktualizować.
    #
    # "formspree.io"              # anycast Cloudflare (172.66.x). Backend
    #                             # formularza zgłoszeń z app/report.js.
    #                             # Odkomentuj, gdybyś chciał testować wysyłkę
    #                             # zgłoszeń Z WNĘTRZA kontenera — normalnie
    #                             # klika się to w przeglądarce na hoście.
    # "pypi.org"                  # anycast Fastly (151.101.x). Odkomentuj,
    # "files.pythonhosted.org"    # gdyby Manim albo inne narzędzia pythonowe
    #                             # miały renderować wideo w kontenerze;
    #                             # POTRZEBNE SĄ OBA naraz (metadane + pliki).
    # "developer.mozilla.org"     # anycast Fastly. Dokumentacja CSS/JS.
    #                             # Odkomentuj, jeśli chcesz do niej sięgać
    #                             # z kontenera zamiast z przeglądarki hosta.
    #
    # "katex.org"                 # dedykowane IP, więc bezpieczne — po prostu
    #                             # zbędne: KaTeX jest zwendorowany w vendor/,
    #                             # a aktualizacja idzie z registry.npmjs.org.
    # "nodejs.org"                # anycast Cloudflare, a Node jest w obrazie.
    # "console.anthropic.com"     # przydatne tylko w przeglądarce, której
    #                             # w kontenerze nie ma.
    #
    # NIE DODAWAJ: statsig.anthropic.com — ta nazwa w ogóle się nie rozwiązuje
    # (sprawdzone 2026-08-09), Claude Code działa bez niej.
    # NIE DODAWAJ: cdn.jsdelivr.net, unpkg.com, fonts.googleapis.com — wprost
    # sprzeczne z offline-first tego projektu, który wendoruje KaTeX właśnie
    # po to, żeby nie zależeć od CDN-ów.
)

# $1 = domena, $2 = "critical" | "content"
add_domain() {
    local domain=$1 mode=$2 ips ip
    echo "Resolving $domain..."
    ips=$(dig +noall +answer A "$domain" | awk '$4 == "A" {print $5}')
    if [ -z "$ips" ]; then
        if [ "$mode" = "critical" ]; then
            echo "ERROR: Failed to resolve $domain"
            exit 1
        fi
        echo "UWAGA: nie udało się rozwiązać $domain — pomijam (ruch tam będzie zablokowany)"
        return 0
    fi

    while read -r ip; do
        if [[ ! "$ip" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
            if [ "$mode" = "critical" ]; then
                echo "ERROR: Invalid IP from DNS for $domain: $ip"
                exit 1
            fi
            echo "UWAGA: podejrzany adres z DNS dla $domain: $ip — pomijam"
            continue
        fi
        echo "Adding $ip for $domain"
        # -exist, bo różne domeny potrafią wskazywać ten sam adres (np.
        # www.cke.gov.pl to CNAME na cke.gov.pl). Bez tego `ipset add` zwraca
        # błąd na duplikacie i pod `set -e` zabija cały skrypt.
        ipset add allowed-domains "$ip" -exist
    done < <(echo "$ips")
}

for domain in "${CRITICAL_DOMAINS[@]}"; do
    add_domain "$domain" critical
done
for domain in "${CONTENT_DOMAINS[@]}"; do
    add_domain "$domain" content
done

# Get host IP from default route
HOST_IP=$(ip route | grep default | cut -d" " -f3)
if [ -z "$HOST_IP" ]; then
    echo "ERROR: Failed to detect host IP"
    exit 1
fi

# UWAGA: oryginał (pisany pod Dockera) rozszerzał adres bramy na całe /24, bo
# tam bramą jest most dockerowy. Pod rootless podmanem z pastą kontener widzi
# PRAWDZIWĄ sieć lokalną, więc /24 otwierałoby dostęp do całego LAN-u i do usług
# na hoście. Przepuszczamy tylko samą bramę (/32).
echo "Gateway detected as: $HOST_IP (przepuszczamy /32, nie całe /24)"

# Set up remaining iptables rules
iptables -A INPUT -s "$HOST_IP" -j ACCEPT
iptables -A OUTPUT -d "$HOST_IP" -j ACCEPT

# Set default policies to DROP first
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# First allow established connections for already approved traffic
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Then allow only specific outbound traffic to allowed domains
iptables -A OUTPUT -m set --match-set allowed-domains dst -j ACCEPT

# Explicitly REJECT all other outbound traffic for immediate feedback
iptables -A OUTPUT -j REJECT --reject-with icmp-admin-prohibited

# BEZPIECZNIK. Gdyby zawężenie DNS z jakiegokolwiek powodu zabiło rozwiązywanie
# nazw (inny resolver, resolv.conf podmieniony po starcie, IPv6-only DNS),
# wracamy do ogólnej reguły. Lepiej działający kontener z jedną znaną słabością
# niż sesja, która się nie podnosi — postStartCommand jest fail-closed, więc
# zepsuty DNS oznaczałby brak możliwości pracy.
# Reguły wchodzą przez -I (na początek łańcucha), bo -A trafiłoby za REJECT.
if ! dig +short +time=3 +tries=1 api.github.com 2>/dev/null | grep -qE '^[0-9]+\.'; then
    echo "UWAGA: DNS nie działa po zawężeniu — przywracam ogólną regułę UDP 53"
    iptables -I OUTPUT -p udp --dport 53 -j ACCEPT
    iptables -I INPUT -p udp --sport 53 -j ACCEPT
else
    echo "DNS po zawężeniu działa poprawnie"
fi

# IPv6: pełna blokada. Lista dozwolonych adresów jest wyłącznie IPv4, więc
# gdyby kontener kiedykolwiek dostał egress po IPv6, cały firewall dałoby się
# ominąć jednym `curl -6`. Dziś kontener ma tylko ULA Tailscale bez trasy
# globalnej, czyli to zabezpieczenie na zapas. Blok jest miękki: brak obsługi
# IPv6 w jądrze/netns ma dać ostrzeżenie, a nie wywalić skrypt.
if ip6tables -L >/dev/null 2>&1; then
    ip6tables -F 2>/dev/null || true
    ip6tables -X 2>/dev/null || true
    ip6tables -A INPUT -i lo -j ACCEPT
    ip6tables -A OUTPUT -o lo -j ACCEPT
    ip6tables -P INPUT DROP
    ip6tables -P FORWARD DROP
    ip6tables -P OUTPUT DROP
    echo "IPv6 zablokowane (poza loopbackiem)"
else
    echo "UWAGA: ip6tables niedostępne — IPv6 nie jest filtrowane"
fi

echo "Firewall configuration complete"
echo "Verifying firewall rules..."
if curl --connect-timeout 5 https://example.com >/dev/null 2>&1; then
    echo "ERROR: Firewall verification failed - was able to reach https://example.com"
    exit 1
else
    echo "Firewall verification passed - unable to reach https://example.com as expected"
fi

# Verify GitHub API access
if ! curl --connect-timeout 5 https://api.github.com/zen >/dev/null 2>&1; then
    echo "ERROR: Firewall verification failed - unable to reach https://api.github.com"
    exit 1
else
    echo "Firewall verification passed - able to reach https://api.github.com as expected"
fi
