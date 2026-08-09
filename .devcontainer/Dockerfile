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
RUN mkdir -p /workspace /home/node/.claude /home/node/.config/gh && \
  chown -R node:node /workspace /home/node/.claude /home/node/.config

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


# Copy and set up firewall script
COPY init-firewall.sh /usr/local/bin/
USER root
RUN chmod +x /usr/local/bin/init-firewall.sh && \
  echo "node ALL=(root) NOPASSWD: /usr/local/bin/init-firewall.sh" > /etc/sudoers.d/node-firewall && \
  chmod 0440 /etc/sudoers.d/node-firewall
USER node
