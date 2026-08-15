#!/usr/bin/env python3
"""Liczy, co ciemny motyw zrobi z kolorem na obrazku albo w filmie.

PO CO TO JEST. Grafiki CKE i filmy z Manima to jeden plik na oba motywy —
ciemny nakłada na nie `filter: invert(92%)` (`--filtr-grafik-zadan`
w style/base.css). Koloru w ciemnym motywie NIE wybierasz więc osobno:
wybierasz jasny, a ciemny się z niego wylicza. Ten skrypt liczy to zamiast
zgadywania, którego nie da się sprawdzić inaczej niż renderując film.

Nie dotyczy kolorów w widżetach ani w CSS — tam każdy motyw ma własną
wartość i nic się nie odwraca. Szczegóły: COLORS.md.

UŻYCIE:
    python3 tools/odwroc-kolor.py '#7030a0'          # co z tego wyjdzie
    python3 tools/odwroc-kolor.py '#7030a0' '#8dc164' # czy to jest para
    python3 tools/odwroc-kolor.py --szukaj '#3ccf5a'  # jaki jasny da ten ciemny

Filtr jest sam dla siebie odwrotnością (invert dwa razy wraca do punktu
wyjścia tylko przy 100%), więc --szukaj liczy naprawdę, a nie „odwraca jeszcze raz".
"""

import sys

MOC = 0.92  # invert(92%) — musi zgadzać się z --filtr-grafik-zadan w style/base.css


def czytaj(hx):
    hx = hx.strip().lstrip("#")
    if len(hx) == 3:
        hx = "".join(c * 2 for c in hx)
    if len(hx) != 6:
        raise ValueError(f'„{hx}” nie wygląda jak kolor w zapisie #rrggbb')
    return [int(hx[i:i + 2], 16) for i in (0, 2, 4)]


def pisz(kanaly):
    return "#" + "".join(f"{max(0, min(255, round(k))):02x}" for k in kanaly)


def odwroc(kanaly, moc=MOC):
    # CSS invert(a): każdy kanał c → c + a*(255 - 2c)
    return [k + moc * (255 - 2 * k) for k in kanaly]


def szukaj(cel, moc=MOC):
    """Jaki kolor jasny da po filtrze zadany ciemny — z odwrócenia wzoru."""
    # c' = c + a*(255-2c)  ⇒  c = (c' - 255a) / (1 - 2a)
    return [(k - 255 * moc) / (1 - 2 * moc) for k in cel]


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
        print(f"jasny {pisz(zrodlo)}  →  po invert(92%)  {pisz(odwroc(czytaj(pisz(zrodlo))))}")
        print(f"cel   {pisz(cel)}")
        return 0

    zrodlo = czytaj(argv[0])
    wynik = odwroc(zrodlo)
    print(f"jasny (w pliku)     {pisz(zrodlo)}")
    print(f"ciemny (po filtrze) {pisz(wynik)}")

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
