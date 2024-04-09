from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from kafka import KafkaConsumer
from anyio.lowlevel import RunVar
from anyio import CapacityLimiter


app = FastAPI()

def kafka_event_stream():
    consumer = KafkaConsumer('sample', bootstrap_servers='localhost:9092,localhost:9093,localhost:9094')
    for message in consumer:
        yield f"data: {message.value.decode('utf-8')}\n\n"

@app.get('/stream')
async def stream():
    return StreamingResponse(kafka_event_stream(), media_type="text/event-stream")


@app.on_event("startup")
def startup():
    print("start")
    RunVar("_default_thread_limiter").set(CapacityLimiter(200))
