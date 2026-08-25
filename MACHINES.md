## Sprzęt i środowiska deweloperskie

Laptop Thinkpad:
* Windows 10 (czasem też koduję)
* Kubuntu -> vs code + dev-container podman z firewallem
  (możliwe, że ulepszona wersja firewalla niż na Bazzite — niepotwierdzone)

Komputer:
- Windows 10 (HenrichFromHome, czasem też koduję)
- Bazzite (HenrichBazzite) -> vs code zainstalowane przy pomocy rpm-ostree + dev-container podman z firewallem

Wspólne: Dev Containers na obu maszynach oparte o Podman (nie Docker),
firewall default-deny z allowlistą (wzorowany na init-firewall.sh).

## Jak rozpoznać, na której maszynie jesteś

Działa też z wnętrza kontenera, bo jądro jest wspólne z hostem. Pełne markery
i sposób sprawdzenia „host czy kontener": [issues/host-czy-kontener.md](issues/host-czy-kontener.md).

| | Bazzite (zmierzone 2026-08-25) | Kubuntu (NIESPRAWDZONE) |
|---|---|---|
| `uname -r` | `7.2.0-ogc6.1.fc44.x86_64`, czyli `fc` = Fedora | spodziewane `-generic`, nikt nie potwierdził |
| `git config user.name` | `HenrichBazzite` | nieznane |
| system plików repo | btrfs + SELinux (`seclabel`) | nieznane |
| katalog domowy na hoście | `/home/wojciech` | nieznane |

Najkrótsza reguła: `fc` w `uname -r` znaczy Bazzite. Kolumny „Kubuntu" nikt
jeszcze nie zmierzył, więc pierwsza sesja na laptopie ma odpalić te trzy
komendy i wpisać wyniki tutaj.