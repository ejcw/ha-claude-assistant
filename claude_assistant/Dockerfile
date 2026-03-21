ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

# Installeer Python en pip
RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app

# Python dependencies
COPY requirements.txt ./
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# App code en run script
COPY app.py tools.py config.py run.sh ./
RUN chmod +x run.sh

EXPOSE 8001
