#!/usr/bin/env python3
"""Sprawdza, co pojedzie na hosting Cloudflare (Worker ze statycznymi plikami).

Wrangler bierze KAŻDY plik z katalogu podanego w `assets.directory` (u nas korzeń
repo), także pliki ukryte i katalog `.git`, i odsiewa tylko to, co wymieni
`.assetsignore`. Tu odtwarzamy ten sam przemarsz i pilnujemy trzech rzeczy:

1. limitów Cloudflare: 25 MiB na plik i 20 000 plików na wersję,
2. że NIE wysyłamy rzeczy roboczych (historia gita, dokumentacja, zrzuty, narzedzia),
3. że wysyłamy WSZYSTKO, czego strona potrzebuje w przeglądarce.

Punkt 3 jest tu najważniejszy: `.assetsignore` napisany za grubo (np. samo `*.md`
plus przypadkowy katalog) po cichu wycina plik, bez którego strona się sypie,
a zobaczyłby to dopiero uczeń.

    python3 tools/sprawdz-cloudflare.py           # cicho, gdy dobrze
    python3 tools/sprawdz-cloudflare.py --lista   # wypisz wszystkie wysyłane pliki

Kod wyjścia 1 = coś jest nie tak.
"""

import os
import re
import sys

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMIT_PLIKU = 25 * 1024 * 1024      # 25 MiB, twardy limit Cloudflare
LIMIT_LICZBY = 20_000               # plików na jedną wersję Workera

# Musi pojechać. Bez tego strona nie działa w przeglądarce.
WYMAGANE = [
    "index.html",
    "template.html",
    "404.html",
    "_headers",
    "tablica-wzorow.pdf",
    "app/state.js",
    "app/bootstrap.js",
    "app/render.js",
    "style/base.css",
    "style/responsive.css",
    "widgets/osLiczbowa.js",
    "vendor/katex/katex.min.css",
    "vendor/fonts/fonts.css",
    "matura/2026-maj/exercises.json",
    "matura/2026-maj/odpowiedzi.pdf",
    "matura/2024-grudzien/exercises.json",
    "matura/2024-grudzien/odpowiedzi.pdf",
]

# Nie ma prawa pojechać. To praca wewnętrzna, nie strona.
ZAKAZANE_PREFIKSY = [
    ".git/", ".github/", ".vscode/", ".claude/", ".devcontainer/",
    "done/", "issues/", "docs/", "tools/", "zrzuty/", "manimations/",
    "tablica-wzorow-transkrypt/",
]
ZAKAZANE_PLIKI = ["CLAUDE.md", "TODO.md", "HOSTRULES.md", "AGENTS.md", "wrangler.jsonc"]


def wzorzec_na_regex(wzor):
    """Zamienia jedną linię w składni .gitignore na wyrażenie regularne.

    Obsługujemy podzbiór, który faktycznie występuje w naszym `.assetsignore`:
    `*` nie przechodzi przez ukośnik, `**` przechodzi, końcowy `/` znaczy katalog,
    początkowy `/` przypina wzorzec do korzenia, a wzorzec bez ukośnika w środku
    łapie nazwę na dowolnej głębokości.
    """
    katalog = wzor.endswith("/")
    wzor = wzor.rstrip("/")
    zakotwiczony = wzor.startswith("/") or "/" in wzor.strip("/")
    wzor = wzor.lstrip("/")

    czesci = []
    i = 0
    while i < len(wzor):
        z = wzor[i]
        if wzor.startswith("**", i):
            czesci.append(".*")
            i += 2
        elif z == "*":
            czesci.append("[^/]*")
            i += 1
        elif z == "?":
            czesci.append("[^/]")
            i += 1
        else:
            czesci.append(re.escape(z))
            i += 1
    rdzen = "".join(czesci)
    poczatek = "" if zakotwiczony else "(?:.*/)?"
    ogon = "/.*" if katalog else "(?:/.*)?"
    return re.compile("^" + poczatek + rdzen + ogon + "$")


def wczytaj_ignore(sciezka):
    wzorce = []
    if not os.path.exists(sciezka):
        return wzorce
    with open(sciezka, encoding="utf-8") as f:
        for linia in f:
            linia = linia.strip()
            if not linia or linia.startswith("#"):
                continue
            wzorce.append((linia, wzorzec_na_regex(linia)))
    return wzorce


def zbierz(wzorce):
    """Lista ścieżek względnych, które wrangler wysłałby na Cloudflare."""
    pliki = []
    for katalog, podkatalogi, nazwy in os.walk(KORZEN):
        wzgledny = os.path.relpath(katalog, KORZEN)
        wzgledny = "" if wzgledny == "." else wzgledny + "/"
        # Ucinamy całe gałęzie, żeby nie chodzić po .git, to setki tysięcy plików.
        podkatalogi[:] = [
            p for p in podkatalogi
            if not any(r.match(wzgledny + p) for _, r in wzorce)
        ]
        for nazwa in nazwy:
            sciezka = wzgledny + nazwa
            if any(r.match(sciezka) for _, r in wzorce):
                continue
            pliki.append(sciezka)
    return sorted(pliki)


def main():
    wzorce = wczytaj_ignore(os.path.join(KORZEN, ".assetsignore"))
    pliki = zbierz(wzorce)
    zbior = set(pliki)
    bledy = []

    if not wzorce:
        bledy.append("brak pliku .assetsignore, wrangler wysłałby cały korzeń repo")

    suma = 0
    for sciezka in pliki:
        rozmiar = os.path.getsize(os.path.join(KORZEN, sciezka))
        suma += rozmiar
        if rozmiar > LIMIT_PLIKU:
            bledy.append(
                "plik ponad limit 25 MiB: %s (%.1f MiB)" % (sciezka, rozmiar / 1024 / 1024)
            )

    if len(pliki) > LIMIT_LICZBY:
        bledy.append("plików %d, limit Cloudflare to %d" % (len(pliki), LIMIT_LICZBY))

    for wymagany in WYMAGANE:
        if wymagany not in zbior:
            bledy.append("brakuje pliku, bez którego strona nie działa: " + wymagany)

    for sciezka in pliki:
        if any(sciezka.startswith(p) for p in ZAKAZANE_PREFIKSY) or sciezka in ZAKAZANE_PLIKI:
            bledy.append("plik roboczy trafiłby na hosting: " + sciezka)

    if "--lista" in sys.argv:
        for sciezka in pliki:
            print(sciezka)

    print("Na Cloudflare pojedzie %d plików, razem %.1f MB." % (len(pliki), suma / 1024 / 1024))

    if bledy:
        print("\nBŁĘDY (%d):" % len(bledy))
        for b in bledy[:25]:
            print("  - " + b)
        if len(bledy) > 25:
            print("  ... i jeszcze %d" % (len(bledy) - 25))
        return 1
    print("Wszystko się zgadza.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
