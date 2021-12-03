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
RUN apk add binutils util-linux file

# install nodejs-current for latest nodejs build
# nodejs will install lts version
RUN apk add --update nodejs python3 && \
  alias python=python3