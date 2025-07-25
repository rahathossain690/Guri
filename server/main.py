from fastapi import FastAPI

from routers.health_router import health_router
from routers.log_router import log_router
from raw_log_to_db_consumer import start_raw_log_to_db_consumer, stop_raw_log_to_db_consumer

app = FastAPI(
    title="Guri",
    description="Smart Log",
    version="0.0.0",
)

@app.on_event("startup")
def startup_event():
    start_raw_log_to_db_consumer()

@app.on_event("shutdown")
def shutdown_event():
    stop_raw_log_to_db_consumer()

app.include_router(health_router)
app.include_router(log_router)