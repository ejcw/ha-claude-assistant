FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py tools.py config.py run.sh ./
RUN chmod +x /usr/src/app/run.sh

CMD ["/usr/src/app/run.sh"]
