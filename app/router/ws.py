from fastapi import APIRouter, WebSocket

router = APIRouter(prefix='/api/ws')


@router.websocket('')
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f'Message text was: {data}')
