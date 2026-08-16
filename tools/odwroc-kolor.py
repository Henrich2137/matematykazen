#!/usr/bin/env python3
"""Liczy, co ciemny motyw zrobi z kolorem na obrazku albo w filmie.

PO CO TO JEST. Grafiki CKE i filmy z Manima to jeden plik na oba motywy —
ciemny nakłada na nie `filter: invert(92%) hue-rotate(180deg)`
(`--filtr-grafik-zadan` w style/base.css). Koloru w ciemnym motywie NIE
wybierasz więc osobno: wybierasz jasny, a ciemny się z niego wylicza. Ten skrypt
liczy to zamiast zgadywania, którego nie da się sprawdzić inaczej niż renderując
film.

CO ROBI TEN FILTR (zmiana z 2026-08-16). Dawniej stało tu samo `invert(92%)`,
które odwracało każdy kanał osobno, więc barwa lądowała po przeciwnej stronie
koła kolorów: niebieski wychodził pomarańczowy, zielony różowy. Dołożone
`hue-rotate(180deg)` zawraca odcień, przez co odwraca się SAMA JASNOŚĆ:
ciemnoniebieski robi się jasnoniebieski. Ograniczenie: bardzo jaskrawe barwy nie
mieszczą się w skali i są przycinane (żółty #ffcc00 wychodzi brązowy) — skrypt
to sygnalizuje.

Nie dotyczy kolorów w widżetach ani w CSS — tam każdy motyw ma własną
wartość i nic się nie odwraca. Szczegóły: COLORS.md.

UŻYCIE:
    python3 tools/odwroc-kolor.py '#7030a0'          # co z tego wyjdzie
    python3 tools/odwroc-kolor.py '#7030a0' '#8dc164' # czy to jest para
    python3 tools/odwroc-kolor.py --szukaj '#3ccf5a'  # jaki jasny da ten ciemny

`--szukaj` liczy naprawdę, z odwrócenia wzoru, a nie „przepuszcza jeszcze raz".
"""

import sys

MOC = 0.92  # invert(92%) — musi zgadzać się z --filtr-grafik-zadan w style/base.css

# Macierz hue-rotate(180deg) wprost ze specyfikacji CSS Filter Effects
# (współczynniki 0.213/0.715/0.072 dla kąta 180°, czyli cos = -1, sin = 0).
# Jest sama dla siebie odwrotnością: obrót o 180° dwa razy to obrót o 360°.
OBROT = [
    [-0.574, 1.430, 0.144],
    [0.426, 0.430, 0.144],
    [0.426, 1.430, -0.856],
]


def czytaj(hx):
    hx = hx.strip().lstrip("#")
    if len(hx) == 3:
        hx = "".join(c * 2 for c in hx)
    if len(hx) != 6:
        raise ValueError(f'„{hx}” nie wygląda jak kolor w zapisie #rrggbb')
    return [int(hx[i:i + 2], 16) for i in (0, 2, 4)]


def pisz(kanaly):
    return "#" + "".join(f"{max(0, min(255, round(k))):02x}" for k in kanaly)


def przez_macierz(m, kanaly):
    return [sum(m[i][j] * kanaly[j] for j in range(3)) for i in range(3)]


def odwroc(kanaly, moc=MOC):
    # CSS invert(a): każdy kanał c → c + a*(255 - 2c), potem obrót odcienia.
    po_invercie = [k + moc * (255 - 2 * k) for k in kanaly]
    return przez_macierz(OBROT, po_invercie)


def szukaj(cel, moc=MOC):
    """Jaki kolor jasny da po filtrze zadany ciemny — z odwrócenia wzoru."""
    # Najpierw cofamy obrót odcienia (jest swoją własną odwrotnością),
    # potem invert: c' = c + a*(255-2c)  ⇒  c = (c' - 255a) / (1 - 2a)
    przed_obrotem = przez_macierz(OBROT, cel)
    return [(k - 255 * moc) / (1 - 2 * moc) for k in przed_obrotem]


def poza_skala(kanaly):
    """Czy filtr musiał przyciąć wynik, bo kolor nie zmieścił się w skali 0-255."""
    return any(k < -0.5 or k > 255.5 for k in kanaly)


def roznica(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def main(argv):
    if not argv:
        print(__doc__)
        return 1

    if argv[0] == "--szukaj":
        if len(argv) < 2:
            print("Podaj kolor, który ma wyjść w ciemnym motywie.")
            return 1
        cel = czytaj(argv[1])
        zrodlo = szukaj(cel)
        if any(k < -1 or k > 256 for k in zrodlo):
            print(f"Nie da się: żaden kolor nie da po filtrze {pisz(cel)}.")
            print("Filtr ściąga wszystko do środka skali, więc bardzo jasne")
            print("i bardzo ciemne wyniki są poza jego zasięgiem.")
            return 2
        print(f"jasny {pisz(zrodlo)}  →  po filtrze  {pisz(odwroc(czytaj(pisz(zrodlo))))}")
        print(f"cel   {pisz(cel)}")
        return 0

    zrodlo = czytaj(argv[0])
    wynik = odwroc(zrodlo)
    print(f"jasny (w pliku)     {pisz(zrodlo)}")
    print(f"ciemny (po filtrze) {pisz(wynik)}")
    if poza_skala(wynik):
        print("\nUWAGA: ten kolor jest za jaskrawy, żeby zmieścić się po odwróceniu.")
        print("Filtr uciął to, co wystaje, więc w ciemnym motywie barwa ucieknie")
        print("i zblednie. Weź odcień przytłumiony, a nie czysty.")

    if len(argv) > 1:
        oczekiwany = czytaj(argv[1])
        d = roznica([round(k) for k in wynik], oczekiwany)
        if d < 20:
            print(f"\nTo jest para — różnica {d}/255, oko tego nie zauważy.")
        else:
            print(f"\nTo NIE jest para — różnica {d}/255.")
            print(f"Żeby w ciemnym wyszło {pisz(oczekiwany)}, w pliku musi być {pisz(szukaj(oczekiwany))}.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except ValueError as e:
        print(e)
        sys.exit(1)
