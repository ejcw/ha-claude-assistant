FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py tools.py config.py /usr/src/app/
COPY run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8001
