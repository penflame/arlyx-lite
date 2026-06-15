from fastapi import APIRouter
from pydantic import BaseModel
import httpx
from app.config import config

router = APIRouter()
CORE_URL = config["core"]["url"]

class Query(BaseModel):
    query: str
    user: str | None = None

@router.post("/query", tags=["core"])
async def query_core(payload: Query):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CORE_URL}/rag/query", json=payload.dict())
        return resp.json()
