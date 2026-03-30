FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY app.py tools.py config.py ./
COPY rootfs /
RUN chmod +x /etc/services.d/claude/run

EXPOSE 8001
