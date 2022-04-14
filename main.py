import sys
import time

import pyautogui

from fastapi.applications import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware
from starlette import status

app = FastAPI(title='Some app')
'http://192.168.31.88:8000/connect_socket'

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/connect_socket')
async def echo(request: Request) -> Response:
    print(f'Client connected from: "{request.client.host}"')
    return Response(
        headers={'location': '/ws'},
        status_code=status.HTTP_308_PERMANENT_REDIRECT,
    )


@app.websocket('/ws')
async def web_socket_endpoint(websocket: WebSocket):
    print('Socket connection')
    try:
        await websocket.accept()
    except Exception as err:
        print(err)
    while True:
        try:
            data = await websocket.receive()
            print(data)
        except Exception as err:
            print(err)
            break
    print('Connection failed')