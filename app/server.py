from fastapi import FastAPI
from app.routers import health_router, log_router

from app.routers.health_router import health_router as health_api_router
from app.routers.log_router import log_router as log_api_router

app = FastAPI(
    title="Guri",
    description="Smart Log",
    version="0.0.0",
)

app.include_router(health_api_router)
app.include_router(log_api_router)