FROM alpine:3.15.0

# Setup vscode user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN apk add sudo && \
  addgroup $USERNAME && \
  adduser -u $USER_UID -G $USERNAME -s /bin/sh -D $USERNAME && \
  echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
  chmod 0440 /etc/sudoers.d/$USERNAME

# Install dependencies
RUN apk add curl wget git nano file binutils util-linux

# install nodejs-current for latest nodejs build
# nodejs will install lts version
RUN apk add --update nodejs npm python3 && \
  cd /usr/bin && \
  ln -s python3 python

# Install other langauges
RUN apk add openjdk11-jdk gcc g++
  # Install rust 
  # curl -sSf https://sh.rustup.rs | sh -s -- -y && \
  # source $HOME/.cargo/env && \
  # Install dotnet
  # apk add bash icu-libs krb5-libs libgcc libintl libssl1.1 libstdc++ zlib && \
  # apk add libgdiplus --repository https://dl-cdn.alpinelinux.org/alpine/edge/testing && \
  # mkdir -p /usr/share/dotnet && \
  # ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet && \
  # wget https://dot.net/v1/dotnet-install.sh && \
  # chmod +x dotnet-install.sh && \
  # ./dotnet-install.sh -c 6.0 --install-dir /usr/share/dotnet

# https://stackoverflow.com/questions/52056387/how-to-install-go-in-alpine-linux
# https://stackoverflow.com/a/59485924
COPY --from=golang:1.17-alpine /usr/local/go/ /usr/local/go/