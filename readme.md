# PoC: Streaming API Response (Server and Client)

![](.readme/preview.gif)

## Details

||| |
| - | - | - |
| server | python | (Starlette/ FastAPI) https://pypi.org/project/sse-starlette |
| client| cURL, python, | https://pypi.org/project/sseclient-py/ |
| |*CAUTION*: [POSTMAN is not supported for streaming](https://github.com/postmanlabs/postman-app-support/issues/5040), however, **response will return JSON of all the words** instead of streaming. As there's a delay embedded in generating response you will observe a lag DONT attribute the lag as program being slow) ||

## Bare Minimum Code
Checkout `server/p1.py` and `client/p1.py`

## Playground

1. Install deps.
    ```python
    pip install -r requirements.txt
    ```

2. Run server
    ```python
    python server/p2.py
    ```

3. Call GET Endpoint
    - **Using cURL**
        ```sh
        curl localhost:8000/get_words
        ```
    - **Using Python**
        ```python
        python client/p2.py
        ```


