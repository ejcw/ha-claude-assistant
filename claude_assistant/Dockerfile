FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip

COPY rootfs /
RUN chmod +x /etc/cont-init.d/00-test
RUN chmod +x /etc/services.d/claude/run

EXPOSE 8001
