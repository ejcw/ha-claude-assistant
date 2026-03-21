from typing import Dict, Any
import httpx

from config import HA_URL, HA_TOKEN

headers = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

async def call_ha_service(domain: str, service: str, data: Dict[str, Any]):
    url = f"{HA_URL}/api/services/{domain}/{service}"
    async with httpx.AsyncClient() as client:
        r = await client.post(url, json=data, headers=headers, timeout=15)
        r.raise_for_status()
        return r.json()

async def get_states():
    url = f"{HA_URL}/api/states"
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        return r.json()

async def create_persistent_notification(title: str, message: str):
    return await call_ha_service(
        "persistent_notification",
        "create",
        {"title": title, "message": message},
    )

async def create_calendar_event(calendar_entity: str, summary: str, start: str, end: str):
    return await call_ha_service(
        "calendar",
        "create_event",
        {
            "entity_id": calendar_entity,
            "summary": summary,
            "start_date_time": start,
            "end_date_time": end,
        },
    )
