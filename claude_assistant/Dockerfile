FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app

COPY rootfs /
RUN chmod +x /etc/services.d/claude/run

EXPOSE 8001
