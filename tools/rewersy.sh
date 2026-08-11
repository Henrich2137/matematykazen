#!/usr/bin/env bash
# Generuje rewersy filmów „krok po kroku" — dla każdego stepN.mp4 powstaje
# stepNreverse.mp4 w tym samym katalogu.
#
# PO CO TO JEST. Przeglądarki nie odtwarzają wideo do tyłu (ujemna prędkość nie
# działa), więc przycisk ◄ potrzebuje drugiego pliku. Rewersu nie renderuje
# Manim — powstaje z gotowego pliku, dzięki czemu nie może się z nim rozjechać.
#
# UŻYCIE:
#   tools/rewersy.sh matura/2024-grudzien/media/zad2/krok-po-kroku
#   tools/rewersy.sh matura/2024-grudzien/media/*/krok-po-kroku
#
# Istniejące rewersy są pomijane; --nadpisz przelicza je od nowa.
#
# DLACZEGO `tpad`, a nie samo `reverse`. Odwrócenie zamienia końce miejscami:
# przytrzymanie stanu końcowego (self.wait na końcu sceny) ląduje na POCZĄTKU
# rewersu, a rewers kończy się klatką, której przeglądarka nie zdąży namalować —
# po cofnięciu na ekranie zostałby niepełny obraz. `tpad` doklinia z powrotem
# ćwierć sekundy bezruchu na końcu. Szczegóły: issues/krok-po-kroku-produkcja.md.

set -euo pipefail

PRZYTRZYMANIE=0.25
nadpisz=0
katalogi=()

for arg in "$@"; do
    case "$arg" in
        --nadpisz) nadpisz=1 ;;
        -*) echo "Nieznany przełącznik: $arg" >&2; exit 1 ;;
        *) katalogi+=("$arg") ;;
    esac
done

if [[ ${#katalogi[@]} -eq 0 ]]; then
    echo "Podaj katalog (albo kilka) z plikami stepN.mp4." >&2
    exit 1
fi

command -v ffmpeg >/dev/null || { echo "Brak ffmpeg." >&2; exit 1; }

for katalog in "${katalogi[@]}"; do
    for plik in "$katalog"/step*.mp4; do
        [[ -e "$plik" ]] || continue
        [[ "$plik" == *reverse.mp4 ]] && continue

        wynik="${plik%.mp4}reverse.mp4"
        if [[ -e "$wynik" && $nadpisz -eq 0 ]]; then
            echo "pomijam (już jest): $wynik"
            continue
        fi

        # -an: pliki nie mają dźwięku, a bez tej flagi ffmpeg potrafi dołożyć
        # pustą ścieżkę i niepotrzebnie zwiększyć wagę.
        ffmpeg -v error -y -i "$plik" \
            -vf "reverse,tpad=stop_mode=clone:stop_duration=$PRZYTRZYMANIE" \
            -an -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p \
            -movflags +faststart "$wynik"
        echo "zrobione: $wynik"
    done
done
