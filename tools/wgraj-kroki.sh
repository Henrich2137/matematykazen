#!/usr/bin/env bash
# Renderuje scenę krok po kroku i wgrywa ją do arkusza: cztery kroki workflow
# z manimations/README.md (render → kopia → rewersy → sprawdzenie) w jednym
# poleceniu, bo przy poprawianiu jednej sceny robi się je po kilka razy.
#
# Użycie:
#   tools/wgraj-kroki.sh 5                    # zad. 5, arkusz 2024-grudzien
#   tools/wgraj-kroki.sh 5 2026-maj           # inny arkusz
#
# Uwaga: rewersy są przeliczane OD NOWA (--nadpisz). Po przerenderowaniu sceny
# stare rewersy pokazują poprzednią wersję animacji, a że plik istnieje, zwykłe
# tools/rewersy.sh po cichu je pomija.

set -eu

ZAD=${1:?podaj numer zadania, np. 5}
ARKUSZ=${2:-2024-grudzien}

KORZEN=$(cd "$(dirname "$0")/.." && pwd)
SCENA="solutionZad${ZAD}"
CEL="$KORZEN/matura/$ARKUSZ/media/zad$ZAD/solution-step-by-step"

[ -f "$KORZEN/manimations/$SCENA.py" ] || { echo "brak $SCENA.py" >&2; exit 1; }

# Nazwa klasy sceny czytana z pliku, a nie zgadywana: dwie starsze sceny nazywają
# się ScenaZadaniaN, nowsze ZadN.
KLASA=$(sed -n 's/^class \([A-Za-z0-9_]*\)(Scene).*/\1/p' "$KORZEN/manimations/$SCENA.py" | head -1)
[ -n "$KLASA" ] || { echo "nie znalazłem klasy sceny w $SCENA.py" >&2; exit 1; }
mkdir -p "$CEL"

echo "== render $SCENA"
# Manim sypie paskami postępu na stderr, więc log idzie do pliku i pokazujemy go
# dopiero, gdy render padnie.
LOG=$(mktemp)
if ! (cd "$KORZEN/manimations" && manim --save_sections "$SCENA.py" "$KLASA") >"$LOG" 2>&1; then
    tail -30 "$LOG"
    rm -f "$LOG"
    exit 1
fi
rm -f "$LOG"

SEKCJE="$KORZEN/manimations/media/videos/$SCENA/720p120/sections"
[ -d "$SEKCJE" ] || { echo "brak katalogu sekcji: $SEKCJE" >&2; exit 1; }

echo "== kopiowanie kroków do $CEL"
# Stare kroki i rewersy lecą do kosza: gdyby nowa scena miała mniej kroków,
# zostałyby pliki po poprzedniej wersji i odtwarzacz pokazywałby mieszankę.
rm -f "$CEL"/step*.mp4
for plik in "$SEKCJE"/${KLASA}_*_krok*.mp4; do
    nr=$(basename "$plik" | sed 's/.*_krok\([0-9]*\)\.mp4/\1/')
    cp "$plik" "$CEL/step$nr.mp4"
done
ls "$CEL" | grep -c '^step[0-9]*\.mp4$' | xargs echo "kroków:"

echo "== rewersy"
bash "$KORZEN/tools/rewersy.sh" --nadpisz "$CEL" >/dev/null

echo "== styk klatek"
bash "$KORZEN/tools/styk-klatek.sh" "$CEL"
