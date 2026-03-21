ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

# S6 overlay & bashio zijn al aanwezig in het base image

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

# Laat s6 de service starten via run.sh
CMD ["/usr/bin/with-contenv", "/usr/src/app/run.sh"]
