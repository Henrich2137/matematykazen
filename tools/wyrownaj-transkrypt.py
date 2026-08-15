#!/usr/bin/env python3
"""Wyrównuje do lewej transkrypty PDF-ów (arkusz.txt / odpowiedzi.txt).

PO CO TO JEST. `pdftotext -layout` zachowuje układ kolumn ze strony, a arkusze
CKE mają treść w wąskiej kolumnie po prawej. Efekt: KAŻDA linia zaczyna się od
~50 spacji, które nic nie znaczą i za które model płaci przy każdym czytaniu.
W `matura/2026-maj/odpowiedzi.txt` było to 60% pliku.

CO ROBI. Zdejmuje wspólny lewy margines — czyli tyle spacji, ile ma najczęstsza
kolumna w pliku. Wcięcia WZGLĘDNE zostają nietknięte, bo one niosą strukturę
(podpunkty pod „2 pkt –", wypunktowania, wyrównanie „ALBO"). To jest przesunięcie
całego tekstu w lewo, nie kasowanie wcięć.

CZEGO NIE RUSZA. Treści — ani jednego bajtu innego niż spacja na początku linii.
Nie usuwa watermarku, nagłówków ani stopek; to osobna decyzja i osobna zmiana.

DLACZEGO NA BAJTACH, NIE NA TEKŚCIE. Transkrypty bywają w różnych kodowaniach
(arkusz 2024-grudzień jest w cp1250, 2026-maj w UTF-8). Wcięcia to zwykłe spacje
ASCII, więc operacja na bajtach daje ten sam wynik bez dekodowania — i bez ryzyka
rozsypania polskich znaków przy zapisie.

WERYFIKACJA. Po przetworzeniu skrypt sam sprawdza dwie rzeczy i przerywa, jeśli
któraś nie wychodzi:
  1. plik po usunięciu WSZYSTKICH białych znaków jest bajt w bajt taki sam
     jak przed — czyli żadna treść nie zniknęła ani się nie zmieniła,
  2. liczba linii się zgadza.

UŻYCIE:
    python3 tools/wyrownaj-transkrypt.py matura/2026-maj/odpowiedzi.txt
    python3 tools/wyrownaj-transkrypt.py matura/*/[ao]*.txt
    python3 tools/wyrownaj-transkrypt.py --sucho <plik>    # tylko pokaż, nie zapisuj

Nadpisuje plik w miejscu. Kopii nie robi — historię trzyma git.
"""

import sys
import collections

SPACJA = 0x20


def margines(linie):
    """Wspólny lewy margines: najczęstsze wcięcie wśród linii z treścią.

    Nie używamy minimum, bo w pliku są linie spoza głównej kolumny (watermark
    wdrukowany pionowo z boku strony, nagłówek bieżący) — one siedzą na
    pozycji 0 i zaniżyłyby wynik do zera, czyli do braku zmian.
    """
    wciecia = [len(l) - len(l.lstrip(b" ")) for l in linie if l.strip()]
    if not wciecia:
        return 0
    return collections.Counter(wciecia).most_common(1)[0][0]


def wyrownaj(dane):
    linie = dane.split(b"\n")
    m = margines(linie)
    if m == 0:
        return dane, 0
    # Zdejmujemy CO NAJWYŻEJ m spacji. Linie spoza głównej kolumny (elementy
    # strony na pozycji 0 albo 13) mają ich mniej i po prostu tracą wszystkie.
    nowe = [l[m:] if l[:m] == b" " * m else l.lstrip(b" ") if not l[:1].strip() else l
            for l in linie]
    return b"\n".join(nowe), m


def bez_bialych(dane):
    return bytes(b for b in dane if b not in b" \t\r\n\f\v")


def main(argv):
    sucho = "--sucho" in argv
    pliki = [a for a in argv if not a.startswith("--")]
    if not pliki:
        print(__doc__)
        return 1

    for sciezka in pliki:
        with open(sciezka, "rb") as fh:
            przed = fh.read()

        po, m = wyrownaj(przed)

        # Weryfikacja — treść musi być nietknięta.
        if bez_bialych(przed) != bez_bialych(po):
            print(f"BŁĄD: {sciezka} — treść się zmieniła, nic nie zapisuję.")
            return 2
        if przed.count(b"\n") != po.count(b"\n"):
            print(f"BŁĄD: {sciezka} — zmieniła się liczba linii, nic nie zapisuję.")
            return 2

        zysk = len(przed) - len(po)
        proc = 100 * zysk / len(przed) if przed else 0
        stan = "(sucho)" if sucho else ""
        print(f"{sciezka}: margines {m} spacji, "
              f"{len(przed)} → {len(po)} B, mniej o {zysk} B ({proc:.1f}%) {stan}")

        if not sucho:
            with open(sciezka, "wb") as fh:
                fh.write(po)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
