from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import leads_server as leads
import whatsapp_server as wa

app = FastAPI(title="RC Jiu Jitsu — MCP Gateway", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class ToolCall(BaseModel):
    tool: str
    arguments: dict[str, Any] = {}


@app.get("/")
def root():
    return {
        "status": "ok",
        "tools": ["send_whatsapp", "save_lead"],
        "professors": list(wa.PROFESSORS.keys()),
    }


@app.post("/call")
def call_tool(body: ToolCall):
    if body.tool == "send_whatsapp":
        return wa.send_whatsapp(**body.arguments)

    if body.tool == "save_lead":
        return leads.save_lead(**body.arguments)

    return {"ok": False, "error": f"Herramienta desconocida: '{body.tool}'"}


@app.get("/leads")
def get_leads():
    return leads.list_leads()
