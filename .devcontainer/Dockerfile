FROM node:20

ARG TZ
ENV TZ="$TZ"

ARG CLAUDE_CODE_VERSION=latest

# Install basic development tools and iptables/ipset
RUN apt-get update && apt-get install -y --no-install-recommends \
  less \
  git \
  procps \
  sudo \
  fzf \
  zsh \
  man-db \
  unzip \
  gnupg2 \
  gh \
  iptables \
  ipset \
  iproute2 \
  dnsutils \
  aggregate \
  jq \
  nano \
  vim \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Ensure default node user has access to /usr/local/share
RUN mkdir -p /usr/local/share/npm-global && \
  chown -R node:node /usr/local/share

ARG USERNAME=node

# Persist bash history.
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  && mkdir /commandhistory \
  && touch /commandhistory/.bash_history \
  && chown -R $USERNAME /commandhistory

# Set `DEVCONTAINER` environment variable to help with orientation
ENV DEVCONTAINER=true

# Create workspace and config directories and set permissions.
# /home/node/.config/gh MUSI powstać tutaj, mimo że montuje się na nie wolumen:
# podman inicjalizuje nowy, pusty wolumen zawartością i właścicielem katalogu z
# obrazu. Gdyby tej ścieżki w obrazie nie było, wolumen powstałby jako root:root
# i `gh` (działający jako node) nie zapisałby do niego tokenu. Ta sama zasada
# co przy /home/node/.claude.
#
# /home/node/.cache jest tu z innego powodu: powstawał wcześniej jako root:root
# (tworzył go runtime przy montowaniu bindu ~/.cache/ms-playwright), więc node nie
# mógł założyć w nim NICZEGO nowego. Wywracało to każde narzędzie, które chce sobie
# zrobić własny podkatalog cache'a — pierwszy padł chrome-devtools-mcp
# (EACCES: mkdir '/home/node/.cache/chrome-devtools-mcp', issues/chrome-devtools-mcp-cache-eacces.md).
# Katalog istniejący w obrazie zachowuje swojego właściciela przy montowaniu bindu
# na podkatalog, więc to wystarczy.
RUN mkdir -p /workspace /home/node/.claude /home/node/.config/gh /home/node/.cache && \
  chown -R node:node /workspace /home/node/.claude /home/node/.config /home/node/.cache

WORKDIR /workspace

ARG GIT_DELTA_VERSION=0.18.2
RUN ARCH=$(dpkg --print-architecture) && \
  wget "https://github.com/dandavison/delta/releases/download/${GIT_DELTA_VERSION}/git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb" && \
  sudo dpkg -i "git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb" && \
  rm "git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb"

# Set up non-root user
USER node

# Install global packages
ENV NPM_CONFIG_PREFIX=/usr/local/share/npm-global
ENV PATH=$PATH:/usr/local/share/npm-global/bin

# Set the default shell to zsh rather than sh
ENV SHELL=/bin/zsh

# Set the default editor and visual
ENV EDITOR=nano
ENV VISUAL=nano

# Default powerline10k theme
ARG ZSH_IN_DOCKER_VERSION=1.2.0
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v${ZSH_IN_DOCKER_VERSION}/zsh-in-docker.sh)" -- \
  -p git \
  -p fzf \
  -a "source /usr/share/doc/fzf/examples/key-bindings.zsh" \
  -a "source /usr/share/doc/fzf/examples/completion.zsh" \
  -a "export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  -x

# Install Claude
RUN npm install -g @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}

# Playwright — do robienia zrzutów strony przy zadaniach wizualnych.
# Sama przeglądarka NIE jest tu pobierana: przychodzi bindem z hosta
# (~/.cache/ms-playwright), bo firewall kontenera blokuje CDN Playwrighta.
# Szczegóły: issues/playwright-podglad.md.
#
# Wersja przypięta na sztywno i MUSI się zgadzać z buildem pobranym na hoście —
# przy rozjeździe Playwright odmawia startu. Podbicie = pobranie nowej wersji na
# hoście + zmiana tej liczby, oba naraz.
ARG PLAYWRIGHT_VERSION=1.62.1

USER root
# Biblioteki systemowe Chromium, lista z samego Playwrighta
# (lib/server/registry/nativeDeps.js, wpis "debian12-x64" → chromium).
# Fonty osobno: obraz node:20 jest praktycznie bez fontów, a strona jest po
# polsku — bez pokrycia Latin Extended-A zrzuty pokazują puste prostokąty.
RUN apt-get update && apt-get install -y --no-install-recommends \
  libasound2 \
  libatk-bridge2.0-0 \
  libatk1.0-0 \
  libatspi2.0-0 \
  libcairo2 \
  libcups2 \
  libdbus-1-3 \
  libdrm2 \
  libgbm1 \
  libglib2.0-0 \
  libnspr4 \
  libnss3 \
  libpango-1.0-0 \
  libx11-6 \
  libxcb1 \
  libxcomposite1 \
  libxdamage1 \
  libxext6 \
  libxfixes3 \
  libxkbcommon0 \
  libxrandr2 \
  fonts-liberation \
  fonts-dejavu-core \
  fonts-noto-color-emoji \
  && apt-get clean && rm -rf /var/lib/apt/lists/*
USER node

# PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1, bo inaczej postinstall próbuje ściągnąć
# przeglądarkę drugi raz — tym razem w kontenerze, czyli przez firewall, czyli
# build pada.
RUN PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm install -g playwright@${PLAYWRIGHT_VERSION}


# Manim — do renderowania animacji z manimations/ wewnątrz kontenera, żeby dało
# się obejrzeć wynik zamiast pisać scenę w ciemno i czekać na render na hoście.
# Render na hoście (Windows, MiKTeX) zostaje — to druga ścieżka, nie zamiennik.
#
# Wersja przypięta na sztywno i celowo równa tej z hosta (Manim CE 0.18.1):
# ten sam skrypt ma dawać ten sam obraz w obu środowiskach. Rozjazd wersji
# Manima to cichy błąd — nic nie pada, tylko klatki wychodzą inaczej i widać to
# dopiero, gdy zmiksuje się pliki z obu źródeł w jednym arkuszu. Ta sama zasada
# co przy PLAYWRIGHT_VERSION wyżej.
ARG MANIM_VERSION=0.18.1

USER root
# Zależności systemowe:
# - python3/python3-pip — Manim jest paczką pythonową, a node:20 Pythona nie ma;
# - ffmpeg — Manim składa nim klatki w plik MP4, bez tego render nie ma wyjścia;
# - pkg-config + libcairo2-dev + libpango1.0-dev — pycairo i ManimPango budują
#   się ze źródeł (nie ma dla nich gotowych wheeli), więc potrzebują nagłówków,
#   nie samych bibliotek runtime;
# - python3-dev — nagłówki samego Pythona, z tego samego powodu. Bez niego
#   build pada już na pycairo: "Run-time dependency python found: NO (tried
#   pkgconfig and sysconfig)" (sprawdzone 2026-08-11 — pierwszy rebuild padł
#   dokładnie tak). Kompilatora nie dokładamy: node:20 stoi na buildpack-deps,
#   więc gcc/make są w obrazie od początku.
#
# LaTeX-a wymaga MathTex, czyli praktycznie każda nasza scena. Świadomie NIE
# texlive-full (~5 GB) — to jest minimalny zestaw z dokumentacji Manima (~1–1,5
# GB), który pokrywa wszystko, czego używają istniejące sceny (ułamki, potęgi,
# pierwiastki). dvisvgm zamienia wyjście LaTeX-a na SVG, którym Manim rysuje.
# Gdyby kiedyś render zapłakał o brakujący plik .sty — dopisz konkretny pakiet
# tutaj, zamiast sięgać po texlive-full.
#
# --no-install-recommends jak w pozostałych blokach: wszystkie potrzebne
# kawałki TeX Live są wymienione z nazwy, więc nie ma po co ciągnąć
# rekomendacji (głównie dokumentacja) i puchnąć obrazu.
RUN apt-get update && apt-get install -y --no-install-recommends \
  python3 \
  python3-dev \
  python3-pip \
  ffmpeg \
  pkg-config \
  libcairo2-dev \
  libpango1.0-dev \
  texlive-latex-base \
  texlive-latex-extra \
  texlive-latex-recommended \
  texlive-fonts-extra \
  texlive-science \
  dvisvgm \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# --break-system-packages, bo Debian 12 (baza node:20) oznacza systemowego
# Pythona jako "externally managed" i bez tej flagi pip odmawia instalacji.
# W obrazie jednorazowego użytku nie ma tu czego chronić — nie ma innych
# pythonowych narzędzi, z którymi Manim mógłby wejść w konflikt.
#
# Ten pip install NIE potrzebuje żadnego wyjątku w firewallu, mimo że pypi.org
# jest poza allowlistą: obraz buduje się zanim host nałoży firewall (robi to
# host-firewall.sh na już działającym kontenerze). Po starcie kontenera Manim
# nie pobiera już niczego, więc — inaczej niż Chromium — nie potrzebuje też
# binda z hosta.
RUN pip3 install --break-system-packages manim==${MANIM_VERSION}
USER node


# Token dla pluginu `github` Claude Code. Ten plugin gada z api.githubcopilot.com
# osobnym serwerem MCP i NIE czyta logowania `gh` — chce gotowej zmiennej, a bez
# niej wysyła pusty nagłówek "Bearer " i dostaje HTTP 400
# (issues/claude-code-pluginy.md, sekcja „github").
#
# W REPO NIE MA ŻADNEGO TOKENU — jest tu tylko polecenie, które czyta go u siebie.
# Kto sklonuje repo, dostanie tę samą linijkę, ale u niego zwróci ona jego własny
# token albo pustkę; niczyich uprawnień to nie rozdaje.
#
# Kolejność źródeł:
# 1. ~/.config/gh/mcp-token — jeśli ten plik istnieje, bierzemy go. Miejsce na
#    osobny, wąski token (fine-grained PAT tylko do tego repo), gdyby oddawanie
#    pluginowi pełnych uprawnień `gh` było za szerokie. Plik leży na wolumenie
#    matematykazen-gh-config, więc przeżywa rebuildy i nigdy nie widzi go git.
# 2. `gh auth token` — token z normalnego logowania, czyli pełne uprawnienia
#    Henricha do GitHuba. Uwaga: zmienna środowiskowa jest widoczna dla każdego
#    procesu w kontenerze, nie tylko dla pluginu.
# Gdy nie ma ani jednego, ani drugiego, zmienna wychodzi pusta — czyli dokładnie
# tak jak dziś, nic się nie psuje.
#
# Dopisane do OBU rc-ków: zsh jest domyślną powłoką, ale VS Code i część narzędzi
# odpalają bash.
RUN for rc in /home/node/.zshrc /home/node/.bashrc; do \
  printf '\n# Token dla pluginu github Claude Code (patrz .devcontainer/Dockerfile)\nexport GITHUB_PERSONAL_ACCESS_TOKEN="$(cat ~/.config/gh/mcp-token 2>/dev/null || gh auth token 2>/dev/null)"\n' >> "$rc"; \
  done

# Copy and set up firewall script
COPY init-firewall.sh /usr/local/bin/
USER root
RUN chmod +x /usr/local/bin/init-firewall.sh && \
  echo "node ALL=(root) NOPASSWD: /usr/local/bin/init-firewall.sh" > /etc/sudoers.d/node-firewall && \
  chmod 0440 /etc/sudoers.d/node-firewall
USER node
