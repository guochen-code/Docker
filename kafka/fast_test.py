from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

@app.get("/stream")
async def endless_stream():
    async def stream_data():
        while True:
            # Simulate streaming data
            data = b"This is an endless stream...\n\n"
            yield data
            await asyncio.sleep(1)

    return StreamingResponse(stream_data(), media_type="text/event-stream")

