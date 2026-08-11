# Manim w devkontenerze — środowisko (paczka 1)

Data: 2026-08-11
Status: zaakceptowany zakres — warstwy 1 i 4 (środowisko + porządki w repo).
Warstwy 2 (sekcje w scenach) i 3 (skrypt `tools/manim-kroki.sh`) świadomie
odłożone: wracamy do nich po przetestowaniu tej paczki.

## Cel

Umożliwić renderowanie animacji Manim **wewnątrz devkontenera**, żeby asystent
mógł sam wyrenderować scenę i obejrzeć wynik, zamiast pisać skrypty w ciemno i
czekać na render u Henricha na hoście. Render na hoście (Windows, MiKTeX)
pozostaje w mocy — kontener go nie zastępuje, tylko dokłada drugą ścieżkę.

## Stan wyjściowy

- `manimations/` — 4 skrypty scen (`solutionZad1..4.py`), `manim.cfg`
  (białe tło, 840×360, 60 fps), README opisujący wyłącznie środowisko hosta:
  Python 3.12.8, Manim CE 0.18.1, ffmpeg 7.1, MiKTeX 25.4.
- Kontener: `node:20`, bez Pythona, bez ffmpega, bez LaTeX-a.
- Firewall kontenera nie przepuszcza `pypi.org` (świadomie — anycast Fastly,
  komentarz w `init-firewall.sh`).
- Repo **nie ma `.gitignore`** — cache Manima (`manimations/media/`) nic nie
  wyklucza, choć README mówi, że nie musi być commitowany.

## Kluczowe ustalenia techniczne

**Firewall zostaje bez zmian.** Obraz buduje się, zanim firewall zostanie
nałożony (nakłada go host przez `host-firewall.sh` na już istniejący kontener),
więc `pip install` w `Dockerfile` przechodzi. To ten sam wzorzec, co przy
Playwrighcie, z jedną różnicą na korzyść: Manim nie potrzebuje binda z hosta,
bo nie pobiera nic po starcie kontenera.

**Wersja Manima przypięta na `0.18.1`** — dokładnie ta, którą ma host. Cel:
render w kontenerze i na hoście ma dawać ten sam obraz. Ta sama zasada, co
przypięcie `PLAYWRIGHT_VERSION`, i z tego samego powodu: rozjazd wersji to
cichy błąd, który widać dopiero w wyniku.

**`.devcontainer/` jest zamontowany read-only**, więc zmiany w `Dockerfile`
**muszą zostać wprowadzone z hosta** — z wnętrza kontenera asystent ich nie
zapisze. Po edycji: pełny rebuild obrazu (Dev Containers → „Rebuild
Container"). Sprawdzone 2026-08-11: `touch .devcontainer/.probe` →
`Read-only file system`.

## Zakres zmian

### 1. `.devcontainer/Dockerfile` — Manim + LaTeX + ffmpeg

Dokładany blok (jako `root`, przed blokiem firewalla, obok bloku Playwrighta),
z komentarzem w tym samym stylu, co reszta pliku:

- **Zależności systemowe**: `python3`, `python3-pip`, `python3-venv`,
  `ffmpeg`, `pkg-config`, `libcairo2-dev`, `libpango1.0-dev`
  (Manim buduje `pycairo`/`ManimPango` ze źródeł, bez nagłówków build pada).
- **LaTeX — minimalny zestaw z oficjalnej dokumentacji Manima**:
  `texlive-latex-base`, `texlive-latex-extra`, `texlive-latex-recommended`,
  `texlive-fonts-extra`, `texlive-science`, `dvisvgm`. Ok. 1–1,5 GB.
  Świadomie **nie** `texlive-full` (~5 GB) — pokrycie tego zestawu obejmuje
  wszystko, czego używają istniejące sceny (ułamki, potęgi, pierwiastki).
- **Manim**: `pip install --break-system-packages manim==${MANIM_VERSION}`
  z `ARG MANIM_VERSION=0.18.1` (wersja widoczna na górze bloku, tak jak
  `PLAYWRIGHT_VERSION`). `--break-system-packages`, bo Debian 12 (baza
  `node:20`) oznacza środowisko jako externally-managed, a w obrazie
  jednorazowego użytku nie ma czego chronić przed konfliktem. Venv w
  `/opt/manim` traktujemy jako plan B — tylko jeśli `--break-system-packages`
  z jakiegoś powodu nie przejdzie.
- `apt-get clean && rm -rf /var/lib/apt/lists/*` na koniec, jak w pozostałych
  blokach.

### 2. `.gitignore` (nowy plik w katalogu głównym)

Jedyny wpis w tej paczce:

```
manimations/media/
```

Cache Manima (Tex/SVG, klatki, wideo pośrednie) — w pełni odtwarzalny ze
skryptów `.py`, nie ma po co siedzieć w historii repo.

### 3. `manimations/README.md` — przepisany

- Sekcja **„Środowisko"** dostaje drugą kolumnę/podsekcję: obok hosta
  (Windows/MiKTeX) — kontener (Debian/TeX Live, ta sama wersja Manima),
  z informacją, że wersje Manima są celowo zrównane.
- Usunięte zdanie „**domysł, niepotwierdzone**" o cięciu na kroki. Zastąpione
  uczciwym: pliki `_stepN.mp4` powstały historycznie ręcznie, docelowy
  mechanizm (sekcje Manima + skrypt) jest zaprojektowany i czeka na
  osobną paczkę — z odsyłaczem do tego spec-a.
- Dopisana instrukcja: **zmiany w `Dockerfile` robi się z hosta** + rebuild.

### 4. `.devcontainer/README.md` — jedna poprawka faktu

Sekcja „Czego na liście świadomie nie ma" mówi o `pypi.org`: „Do rozważenia
dopiero, gdyby Manim albo inne narzędzia pythonowe miały działać w kontenerze".
Manim właśnie zaczyna działać w kontenerze, a wpis **nadal jest niepotrzebny** —
i to jest ciekawy fakt, nie formalność. Dopisek wyjaśnia dlaczego: instalacja
dzieje się w czasie budowy obrazu, czyli przed nałożeniem firewalla.

## Weryfikacja (co uznajemy za „działa")

Po rebuildzie obrazu, z wnętrza kontenera:

1. `manim --version` → `Manim Community v0.18.1`.
2. Render istniejącej sceny ze wzorami:
   `cd manimations && manim -qh solutionZad2.py ScenaZadania2`
   — kończy się bez błędu i produkuje plik MP4. To jest właściwy test LaTeX-a:
   scena używa `MathTex`, więc przejście oznacza, że minimalny TeX Live
   wystarcza.
3. **Porównanie z hostem**: wyrenderowany plik zestawiony klatka w klatkę z
   istniejącym `matura/2024-grudzien/media/zad2/zad2rozw_step*.mp4`.
   Szukamy różnic w metrykach fontu i grubości kresek. Wynik porównania
   zapisujemy w `manimations/README.md` — jeśli różnice są widoczne, kontener
   nadaje się tylko do podglądu, a finalne rendery zostają na hoście.

## Ryzyka

- **Rozjazd wizualny host ↔ kontener** — inny silnik LaTeX (MiKTeX vs TeX Live)
  i inne fonty systemowe mogą dać minimalnie inny obraz. Nic się nie zepsuje,
  ale mieszanie filmów z obu źródeł w jednym arkuszu mogłoby być widoczne.
  Adresowane punktem 3 weryfikacji — dopóki porównanie nie przejdzie, kontener
  traktujemy jako środowisko podglądu, nie produkcji.
- **Waga obrazu** — rebuild po zmianie urośnie o ok. 1,5–2 GB i potrwa
  zauważalnie dłużej. Cena świadoma, wybrana zamiast 5 GB `texlive-full`.
- **Build wymaga sieci do PyPI i repozytoriów Debiana** — jeśli kiedyś firewall
  hosta obejmie też fazę budowy, ten blok przestanie się budować. Wtedy
  wzorzec do naśladowania jest już w repo: bind z hosta, jak przy Chromium.

## Poza zakresem tej paczki

- Przeróbka `solutionZad1..4.py` na `self.next_section()` (warstwa 2).
- `tools/manim-kroki.sh` — render + zmiana nazw + kopiowanie do
  `matura/<id>/media/zadN/` (warstwa 3).
- Przerenderowanie feralnego `zad2rozw_step6.mp4` (5⁻⁴ zamiast 5⁴) — czeka na
  warstwy 2–3, pozycja jest w `TODO.md`.
