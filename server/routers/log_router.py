from fastapi import APIRouter, HTTPException, Request, Response, status
import datetime
import os
import json
from confluent_kafka import Producer

log_router = APIRouter(
    prefix="/api/v1/log",
    tags=["Log"],
)

KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "kafka:9093")
KAFKA_TOPIC_RAW = os.environ.get("KAFKA_TOPIC_RAW", "raw_logs")

producer = Producer({'bootstrap.servers': KAFKA_BROKER})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record {msg.key()} successfully produced to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

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

        producer.produce(
            KAFKA_TOPIC_RAW,
            key=None,
            value=json.dumps(parsed_data).encode('utf-8'),
            callback=delivery_report
        )
        
        producer.flush()

        return Response(
            status_code=status.HTTP_200_OK,
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))