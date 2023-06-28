# Reference: https://pypi.org/project/sseclient-py/

import json 
import sseclient # pip install sseclient-py
import pprint

def with_requests(url, headers):
    """Get a streaming response for the given event feed using requests."""
    import requests
    return requests.get(url, stream=True, headers=headers)


url = 'http://localhost:8000'
headers = {'Accept': 'text/event-stream'}
response = with_requests(url, headers) 
client = sseclient.SSEClient(response)
for event in client.events():
    pprint.pprint(json.loads(event.data))