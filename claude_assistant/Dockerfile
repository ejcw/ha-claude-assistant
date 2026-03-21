FROM ghcr.io/home-assistant/amd64-base:latest

# Basis Python (in dit base-image is Python al aanwezig, we installeren alleen pip/venv tools indien nodig)
RUN apk add --no-cache py3-pip

WORKDIR /usr/src/app

# Python dependencies
COPY requirements.txt ./
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# App code
COPY app.py tools.py config.py run.sh ./
RUN chmod +x run.sh

EXPOSE 8001

CMD ["/usr/src/app/run.sh"]
