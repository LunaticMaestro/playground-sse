# Reference Code: https://github.com/sysid/sse-starlette

import asyncio
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI, Request
import json

# generated from https://randomwordgenerator.com/
words = ['salmon', 'intention', 'pipe', 'beat', 'crosswalk', 'nail', 'hardware', 'snow', 'panic', 'diameter', 'dozen', 'pop', 'gallery', 'rest', 'silk', 'terms', 'load', 'tough', 'module', 'slap']

async def some_processing(equest=None):
    try: 
        for word in words:
            await asyncio.sleep(0.9)  # simulate some background processing
            yield dict(data=json.dumps(# simulate JSON response
                {
                    'word': word,
                    'length': len(word)
                }
            ))
    except asyncio.CancelledError as e:
        print(f"Disconnected from client (via refresh/close) {request.client}")
        # Clean up
        raise e

async def sse(request):
    handler = some_processing(request)
    return EventSourceResponse(handler)

routes = [
    Route("/get_words", endpoint=sse)
]


# Both below lines are smae
app = Starlette(debug=True, routes=routes)
# app = FastAPI(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level='info')