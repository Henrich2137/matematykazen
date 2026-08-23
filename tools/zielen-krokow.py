#!/usr/bin/env python3
"""Ile zielonych pikseli ma każda klatka kroku, i czy zieleń gaśnie jednym ruchem.

Sprawdzian z manimations/README.md, punkt 26 („Po renderze"). Pilnuje trzech
rzeczy, których styk klatek nie złapie, bo ten patrzy tylko na styki:

1. PIERWSZA klatka kroku ma ZERO zielonych pikseli. Kolor zapalany przed
   pierwszym `play` daje podświetloną pierwszą klatkę, czyli przeskok wobec
   czystej ostatniej klatki kroku poprzedniego.
2. OSTATNIA klatka kroku ma ZERO zielonych pikseli, z tego samego powodu.
3. W ŚRODKU kroku zieleń ma być (poza krokami, w których nic się nie zmienia)
   i ma zjechać do zera JEDNYM RUCHEM. Zatrzymanie się na małej, stałej
   wartości tuż przed końcem znaczy, że jeden glif nie gaśnie razem z resztą:
   `Transform` zostawia w kadrze obiekt ŹRÓDŁOWY, więc wpisanie do gaszenia
   celu zamiast źródła gasi połowę zapisu.

Użycie:
    tools/zielen-krokow.py matura/2024-grudzien/media/zad2/solution-step-by-step
    tools/zielen-krokow.py .../zad8/... --krok 3      # tylko jeden krok, gęściej

Wynik: linia na każdy krok z liczbą zielonych pikseli na starcie, w szczycie
i na końcu, plus ostrzeżenie przy każdym złamaniu któregoś z trzech punktów.
Kod wyjścia 1, gdy cokolwiek jest nie tak.
"""

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# Piksel uznajemy za zielony, gdy kanał G wyraźnie przewyższa oba pozostałe.
# Próg 25 przepuszcza antyaliasing na krawędziach glifów, a odrzuca szarości
# kompresji. Ta sama definicja co w README.
PROG_KANALU = 25

# Poniżej tylu zielonych pikseli klatka uchodzi za czystą: pojedyncze piksele
# na krawędziach zostają po kompresji H.264 nawet w kadrze bez koloru.
PROG_CZYSTOSCI = 40

# Ile klatek na sekundę wycinamy do pomiaru. 10 wystarcza, żeby zobaczyć
# kształt krzywej, a nie zasypuje dysku przy krokach po kilka sekund.
FPS_PROBKI = 10


def klatki(plik, katalog, fps):
    subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(plik), "-vf", f"fps={fps}",
         str(Path(katalog) / "f%04d.png")],
        check=True,
    )
    return sorted(Path(katalog).glob("f*.png"))


def zielone(obrazek):
    from PIL import Image
    import numpy as np

    tab = np.asarray(Image.open(obrazek).convert("RGB")).astype(int)
    r, g, b = tab[:, :, 0], tab[:, :, 1], tab[:, :, 2]
    return int(((g > r + PROG_KANALU) & (g > b + PROG_KANALU)).sum())


def numer_kroku(plik):
    dopasowanie = re.search(r"step(\d+)\.mp4$", plik.name)
    return int(dopasowanie.group(1)) if dopasowanie else 0


def zbadaj(plik, fps):
    with tempfile.TemporaryDirectory() as katalog:
        return [zielone(k) for k in klatki(plik, katalog, fps)]


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("katalog", help="katalog solution-step-by-step")
    parser.add_argument("--krok", type=int, help="zbadaj tylko ten krok")
    parser.add_argument("--fps", type=int, default=FPS_PROBKI, help="klatek na sekundę")
    parser.add_argument("--krzywa", action="store_true", help="wypisz wszystkie klatki")
    args = parser.parse_args()

    katalog = Path(args.katalog)
    pliki = sorted(katalog.glob("step*.mp4"), key=numer_kroku)
    pliki = [p for p in pliki if "reverse" not in p.name]
    if args.krok:
        pliki = [p for p in pliki if numer_kroku(p) == args.krok]
    if not pliki:
        print(f"brak plików step*.mp4 w {katalog}", file=sys.stderr)
        return 2

    print(f"== {katalog}")
    zastrzezenia = 0
    for plik in pliki:
        licznik = zbadaj(plik, args.fps)
        if not licznik:
            print(f"  {plik.name}: nie udało się wyciąć klatek")
            zastrzezenia += 1
            continue

        start, koniec, szczyt = licznik[0], licznik[-1], max(licznik)
        uwagi = []
        if start > PROG_CZYSTOSCI:
            uwagi.append(f"pierwsza klatka nie jest czysta ({start})")
        if koniec > PROG_CZYSTOSCI:
            uwagi.append(f"ostatnia klatka nie jest czysta ({koniec})")

        # Ogon: klatki od ostatniej powyżej progu czystości do końca. Zieleń ma
        # zjechać do zera jednym ruchem, więc ogon ma być krótki. Długi ogon na
        # małej wartości to glif, który nie gaśnie razem z resztą.
        nad_progiem = [i for i, ile in enumerate(licznik) if ile > PROG_CZYSTOSCI]
        if nad_progiem and szczyt > PROG_CZYSTOSCI:
            reszta = licznik[nad_progiem[-1]:]
            resztka = [ile for ile in reszta if 0 < ile <= max(szczyt // 10, PROG_CZYSTOSCI)]
            if len(resztka) > 4:
                uwagi.append(f"zieleń gaśnie ratami, ogon {len(resztka)} klatek")

        stan = "; ".join(uwagi) if uwagi else "ok"
        print(f"  {plik.name}: start {start}, szczyt {szczyt}, koniec {koniec} -> {stan}")
        if args.krzywa:
            print("      " + " ".join(str(ile) for ile in licznik))
        if uwagi:
            zastrzezenia += 1

    if zastrzezenia:
        print(f"\nZastrzeżenia: {zastrzezenia}")
        return 1
    print("\nZieleń bez zastrzeżeń.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
