# Reference Code: https://github.com/sysid/sse-starlette

import asyncio
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI, Request

async def numbers(minimum, maximum, request=None):
    try: 
        for i in range(minimum, maximum + 1):
            await asyncio.sleep(0.9)
            yield dict(data=i)
    except asyncio.CancelledError as e:
        print(f"Disconnected from client (via refresh/close) {request.client}")
        # Clean up
        raise e

async def sse(request):
    generator = numbers(1, 5, request)
    return EventSourceResponse(generator)

routes = [
    Route("/", endpoint=sse)
]


# Both below lines are smae
app = Starlette(debug=True, routes=routes)
# app = FastAPI(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level='info')