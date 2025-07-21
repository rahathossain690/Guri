from fastapi import APIRouter

health_router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

@health_router.get("/", summary="Health Check")
async def health_check():
    # todo: Implement actual health check logic
    return {"status": "healthy"}