from fastapi import FastAPI
from arlyx_lite.router_core_proxy import router as proxy_router
from arlyx_lite.router_health import router as health_router

app = FastAPI(title="ARLYX Lite")

app.include_router(proxy_router, prefix="/core")
app.include_router(health_router, prefix="/health")
