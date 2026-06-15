from fastapi import APIRouter
import requests

router = APIRouter()

CORE_URL = "http://arlyx-core:8000"

@router.post("/query")
def proxy_query(q: str):
    r = requests.post(f"{CORE_URL}/query/", json={"q": q})
    return r.json()
