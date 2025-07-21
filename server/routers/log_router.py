from fastapi import APIRouter, HTTPException, Request, Response, status
import datetime

log_router = APIRouter(
    prefix="/log",
    tags=["Log"],
)

@log_router.post("/", summary="Add Logs")
async def add_single_log(request: Request):
    try:
        # TODO: parse log data properly

        body = await request.body()
        body_str = body.decode('utf-8')

        parsed_data = dict()
        parsed_data["provider"] = "guri" # TODO: Replace with actual provider logic
        parsed_data["data"] = body_str
        parsed_data["timestamp"] = datetime.datetime.now()

        print(parsed_data)

        return Response(
            status_code=status.HTTP_200_OK,
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))