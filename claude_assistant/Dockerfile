ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python
RUN apk add --no-cache python3 py3-pip py3-venv

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
