#!/usr/bin/env bash
# Czy ostatnia klatka kroku N wygląda tak samo jak pierwsza klatka kroku N+1?
#
# W odtwarzaczu to jest JEDNO I TO SAMO MIEJSCE: uczeń zatrzymuje się na końcu
# kroku N i dopiero potem puszcza krok N+1. Jeśli klatki się różnią (bo krok N
# skończył się na podświetlonym albo przyciemnionym zapisie, a krok N+1 startuje
# czysty), przy przejściu widać przeskok. Zgłoszone przez Henricha na zad. 3,
# kroki 4/5 — stąd ten skrypt, żeby to samo nie przeszło drugi raz.
#
# Zasada i jej uzasadnienie: manimations/README.md, sekcja „Jak ma wyglądać animacja".
#
# Użycie:
#   tools/styk-klatek.sh matura/2024-grudzien/media/zad5/solution-step-by-step
#   tools/styk-klatek.sh matura/2024-grudzien/media/zad*/solution-step-by-step
#
# Wynik: linia na każdą parę kroków z miarą SSIM (1,000000 = klatki identyczne)
# i kod wyjścia 1, gdy któraś para wypadła poniżej progu.

set -u

PROG=${PROG:-0.999}
ROBOCZY=$(mktemp -d)
trap 'rm -rf "$ROBOCZY"' EXIT

if [ $# -eq 0 ]; then
    echo "użycie: $0 <katalog solution-step-by-step> [...]" >&2
    exit 2
fi

zastrzezenia=0

for katalog in "$@"; do
    [ -d "$katalog" ] || { echo "brak katalogu: $katalog" >&2; zastrzezenia=1; continue; }
    # Kroki liczymy z plików stepN.mp4 (bez rewersów) i sortujemy liczbowo.
    mapfile -t kroki < <(find "$katalog" -maxdepth 1 -name 'step*.mp4' ! -name '*reverse*' -printf '%f\n' \
        | sed 's/^step\([0-9]*\)\.mp4$/\1/' | sort -n)
    [ "${#kroki[@]}" -gt 1 ] || { echo "$katalog: mniej niż dwa kroki, nie ma czego porównywać"; continue; }

    echo "== $katalog"
    for ((i = 0; i < ${#kroki[@]} - 1; i++)); do
        a="$katalog/step${kroki[$i]}.mp4"
        b="$katalog/step${kroki[$((i + 1))]}.mp4"

        # -sseof cofa się od końca pliku, a -update nadpisuje ten sam plik, więc
        # zostaje ostatnia zdekodowana klatka.
        ffmpeg -v error -sseof -0.2 -i "$a" -update 1 -frames:v 1000 "$ROBOCZY/koniec.png" -y 2>/dev/null
        ffmpeg -v error -i "$b" -frames:v 1 "$ROBOCZY/poczatek.png" -y 2>/dev/null

        if [ ! -s "$ROBOCZY/koniec.png" ] || [ ! -s "$ROBOCZY/poczatek.png" ]; then
            echo "  kroki ${kroki[$i]}→${kroki[$((i + 1))]}: nie udało się wyciągnąć klatek"
            zastrzezenia=1
            continue
        fi

        # Bez -v error: filtr ssim wypisuje wynik na poziomie „info", więc
        # wyciszenie logu zabrałoby jedyną rzecz, po którą tu przychodzimy.
        ssim=$(ffmpeg -i "$ROBOCZY/koniec.png" -i "$ROBOCZY/poczatek.png" \
            -lavfi ssim -f null - 2>&1 | sed -n 's/.*All:\([0-9.]*\).*/\1/p' | tail -1)
        [ -n "$ssim" ] || ssim=0

        if awk -v s="$ssim" -v p="$PROG" 'BEGIN { exit !(s < p) }'; then
            echo "  kroki ${kroki[$i]}→${kroki[$((i + 1))]}: SSIM $ssim  ← klatki się różnią"
            zastrzezenia=1
        else
            echo "  kroki ${kroki[$i]}→${kroki[$((i + 1))]}: SSIM $ssim"
        fi
    done
done

if [ "$zastrzezenia" -ne 0 ]; then
    echo
    echo "Są zastrzeżenia. Podświetlenia zdejmuj PRZED końcowym self.wait(0.25) w scenie."
    exit 1
fi
echo
echo "Styki klatek bez zastrzeżeń."
