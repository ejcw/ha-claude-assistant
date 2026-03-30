#!/usr/bin/with-contenv bashio
echo "RUN.SH STARTED" >&2

export ANTHROPIC_API_KEY=$(bashio::config 'anthropic_api_key')
export HA_TOKEN=$(bashio::config 'ha_token')
export HA_URL="http://supervisor/core"

cd /usr/src/app
exec python3 -m uvicorn app:app --host 0.0.0.0 --port 8001
