from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.wsconnection_service import ConnectionManager
from app.core.config import ALLOWED_ADMIN_IPS, ADMIN_TOKEN

router = APIRouter(tags=["websockets"])
manager = ConnectionManager()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

@router.websocket("/ws/admin/{admin_token}")
async def admin_websocket(websocket: WebSocket, admin_token: str):
    client_host = websocket.client.host

    # IP restriction check
    if client_host not in ALLOWED_ADMIN_IPS:
        await websocket.close(code=1008)
        raise WebSocketDisconnect()
    
    # Token authentication check
    if admin_token != ADMIN_TOKEN:
        await websocket.close(code=1008)
        raise WebSocketDisconnect()
    
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"[ADMIN] {data}", websocket)
            await manager.broadcast(f"[ADMIN] {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Admin left the chat")