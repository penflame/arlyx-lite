from fastapi import FastAPI
from .routers import health, core_proxy

app = FastAPI(title="ARLYX Lite v2.1")

app.include_router(health.router)
app.include_router(core_proxy.router)
