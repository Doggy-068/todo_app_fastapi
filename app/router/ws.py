from fastapi import APIRouter, WebSocket, Depends, Query, WebSocketException, status
from jose import jwt
from .auth import JWT_SECRET_KEY

router = APIRouter(prefix='/api/ws')


async def verify_token(token: str = Query()):
    try:
        jwt.decode(token, JWT_SECRET_KEY)
    except:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)


@router.websocket('', dependencies=[Depends(verify_token)])
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f'Message text was: {data}')
