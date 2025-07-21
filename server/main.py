from fastapi import FastAPI

from routers.health_router import health_router
from routers.log_router import log_router

app = FastAPI(
    title="Guri",
    description="Smart Log",
    version="0.0.0",
)

app.include_router(health_router)
app.include_router(log_router)