# ベースステージ（共通の依存関係をインストール）
FROM ghcr.io/astral-sh/uv:debian-slim AS base



# 開発用ステージ
FROM base AS dev

# FROM node:20
# グループID 1000, ユーザーID 1000の'node'ユーザーを作成
RUN apt update && apt install -y gnupg2 curl xz-utils wget \
  && rm -rf /var/lib/apt/lists/*  
# RUN /bin/sh -c groupadd --gid 1000 node && useradd --uid 1000 --gid node --shell /bin/bash --create-home node # buildkit
# ...existing code...
RUN groupadd --gid 1000 node || true && useradd --uid 1000 --gid node --shell /bin/bash --create-home node || true
# ...existing code...
ENV NODE_VERSION=20.19.3
RUN /bin/sh -c ARCH= && dpkgArch="$(dpkg --print-architecture)" && case "${dpkgArch##*-}" in amd64) ARCH='x64';; ppc64el) ARCH='ppc64le';; s390x) ARCH='s390x';; arm64) ARCH='arm64';; armhf) ARCH='armv7l';; i386) ARCH='x86';; *) echo "unsupported architecture"; exit 1 ;; esac && export GNUPGHOME="$(mktemp -d)" && set -ex && for key in C0D6248439F1D5604AAFFB4021D900FFDB233756 DD792F5973C6DE52C432CBDAC77ABFA00DDBF2B7 CC68F5A3106FF448322E48ED27F5E38D5B0A215F 8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 890C08DB8579162FEE0DF9DB8BEAB4DFCF555EF4 C82FA3AE1CBEDC6BE46B9360C43CEC45C17AB93C 108F52B48DB57BB0CC439B2997B01419BD92F80A A363A499291CBBC940DD62E41F10027AF002F8B0 ; do { gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys "$key" && gpg --batch --fingerprint "$key"; } || { gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key" && gpg --batch --fingerprint "$key"; } ; done && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc && gpgconf --kill all && rm -rf "$GNUPGHOME" && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt && ln -s /usr/local/bin/node /usr/local/bin/nodejs && node --version && npm --version && rm -rf /tmp/* # buildkit


ARG TZ
ENV TZ="$TZ"

# Install basic development tools and iptables/ipset
RUN apt update && apt install -y less \
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
  socat \
  jq \
  curl \
  docker.io

# dockerグループを作成し、nodeユーザーを追加
RUN groupadd -f docker && usermod -aG docker node

# # sudoのパスワード入力を省略
# sudoersにnodeユーザー向けの設定を追加
RUN echo "node ALL=(ALL) NOPASSWD: /bin/chown, /usr/bin/docker" > /etc/sudoers.d/docker \
    && chmod 0440 /etc/sudoers.d/docker

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

# Create workspace and config directories and set permissions
RUN mkdir -p /workspace /home/node/.claude && \
  chown -R node:node /workspace /home/node/.claude

WORKDIR /workspace

RUN ARCH=$(dpkg --print-architecture) && \
  wget "https://github.com/dandavison/delta/releases/download/0.18.2/git-delta_0.18.2_${ARCH}.deb" && \
  sudo dpkg -i "git-delta_0.18.2_${ARCH}.deb" && \
  rm "git-delta_0.18.2_${ARCH}.deb"

# fzfのexamplesを手動で配置（エラー回避）
RUN mkdir -p /usr/share/doc/fzf/examples && \
  wget -O /usr/share/doc/fzf/examples/key-bindings.zsh https://raw.githubusercontent.com/junegunn/fzf/master/shell/key-bindings.zsh && \
  wget -O /usr/share/doc/fzf/examples/completion.zsh https://raw.githubusercontent.com/junegunn/fzf/master/shell/completion.zsh

# Set up non-root user
USER node

# Install global packages
ENV NPM_CONFIG_PREFIX=/usr/local/share/npm-global
ENV PATH=$PATH:/usr/local/share/npm-global/bin

# Set the default shell to zsh rather than sh
ENV SHELL=/bin/zsh

# Default powerline10k theme
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.0/zsh-in-docker.sh)" -- \
  -p git \
  -p fzf \
  -a "source /usr/share/doc/fzf/examples/key-bindings.zsh" \
  -a "source /usr/share/doc/fzf/examples/completion.zsh" \
  -a "export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  -x

# Install Claude
RUN npm install -g @anthropic-ai/claude-code

# # Copy and set up firewall script
# COPY init-firewall.sh /usr/local/bin/
# USER root
# RUN chmod +x /usr/local/bin/init-firewall.sh && \
#   echo "node ALL=(root) NOPASSWD: /usr/local/bin/init-firewall.sh" > /etc/sudoers.d/node-firewall && \
#   chmod 0440 /etc/sudoers.d/node-firewall

# Set up GitHub CLI configuration directory
# This is necessary to avoid errors when using the GitHub CLI in the container.
# The directory is created with the correct permissions for the 'node' user.
RUN mkdir -p /home/node/.config/gh && \
  chown -R node:node /home/node/.config && \
  chown -R node:node /home/node/.config/gh

# Set up socat to forward PostgreSQL connections
# This allows the container to connect to a PostgreSQL server running on the host machine.
# The port 5432 is the default PostgreSQL port, and 3845 is the port on the host that PostgreSQL is listening on.
# The socat command listens on port 5432 inside the container and forwards traffic to the host's PostgreSQL port.
# This is useful for development environments where the database runs on the host
# CMD  socat -v TCP-LISTEN:5432,fork,reuseaddr TCP:host.docker.internal:5432 & node
CMD  node

# 本番用ステージ
FROM base AS prod

CMD  node
