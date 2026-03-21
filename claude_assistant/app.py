from fastapi import FastAPI
from pydantic import BaseModel
import anthropic

from config import ANTHROPIC_API_KEY
import tools

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str | None = None
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    tool_defs = [
        {
            "name": "create_ha_notification",
            "description": "Maak een Home Assistant notificatie",
            "input_schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "message": {"type": "string"},
                },
                "required": ["title", "message"],
            },
        },
        {
            "name": "create_calendar_event",
            "description": "Maak een kalenderafspraak in Home Assistant",
            "input_schema": {
                "type": "object",
                "properties": {
                    "calendar_entity": {"type": "string"},
                    "summary": {"type": "string"},
                    "start": {"type": "string"},
                    "end": {"type": "string"},
                },
                "required": ["calendar_entity", "summary", "start", "end"],
            },
        },
    ]

    messages = [
        {
            "role": "system",
            "content": (
                "Je bent een persoonlijke assistent geïntegreerd met Home Assistant. "
                "Je mag tools gebruiken om notificaties en agenda-afspraken te beheren. "
                "Vraag door als iets onduidelijk is (bijvoorbeeld datum/tijd of welke kalender)."
            ),
        },
        {"role": "user", "content": req.message},
    ]

    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=500,
        tools=tool_defs,
        messages=messages,
    )

    tool_calls = [c for c in response.content if c.type == "tool_use"]
    tool_results = []

    for call in tool_calls:
        if call.name == "create_ha_notification":
            args = call.input
            res = await tools.create_persistent_notification(
                title=args["title"],
                message=args["message"],
            )
            tool_results.append(
                {"tool_use_id": call.id, "output": str(res)}
            )
        elif call.name == "create_calendar_event":
            args = call.input
            res = await tools.create_calendar_event(
                calendar_entity=args["calendar_entity"],
                summary=args["summary"],
                start=args["start"],
                end=args["end"],
            )
            tool_results.append(
                {"tool_use_id": call.id, "output": str(res)}
            )

    if tool_results:
        followup = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=500,
            messages=[
                *messages,
                response,
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tr["tool_use_id"],
                            "content": tr["output"],
                        }
                        for tr in tool_results
                    ],
                },
            ],
        )
        final_text = "".join(
            part.text for part in followup.content if part.type == "text"
        )
    else:
        final_text = "".join(
            part.text for part in response.content if part.type == "text"
        )

    return {"reply": final_text}
