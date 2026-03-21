import os

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
HA_URL = os.getenv("HA_URL", "http://supervisor/core")
HA_TOKEN = os.getenv("HA_TOKEN")

if not ANTHROPIC_API_KEY:
    raise RuntimeError("ANTHROPIC_API_KEY not set")
if not HA_TOKEN:
    raise RuntimeError("HA_TOKEN not set")
