from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.wsconnection_service import ConnectionManager
from app.core.config import ALLOWED_ADMIN_IPS, ADMIN_TOKEN

router = APIRouter(tags=["websockets"])
manager = ConnectionManager()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect_user(client_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_to_admin(client_id, data)
    except WebSocketDisconnect:
        manager.disconnect_user(client_id)

@router.websocket("/ws/admin/")
async def admin_websocket(websocket: WebSocket):
    client_host = websocket.client.host
    protocols = websocket.headers.get("sec-websocket-protocol", "")
    protocol_list = [p.strip() for p in protocols.split(",") if p.strip()]

    if len(protocol_list) < 2:
        await websocket.close(code=1008)
        return

    protocol, admin_token = protocol_list[0], protocol_list[1]

    # IP restriction check
    if client_host not in ALLOWED_ADMIN_IPS:
        await websocket.close(code=1008)
        return

    # Token authentication check
    if admin_token != ADMIN_TOKEN:
        await websocket.close(code=1008)
        return
    
    await manager.connect_admin(websocket, protocol)

    try:
        while True:
            data = await websocket.receive_json()
            client_id = data.get("client_id")
            message = data.get("message")
            if client_id is not None and message:
                await manager.send_to_user(client_id, message)
    except WebSocketDisconnect:
        manager.disconnect_admin()
    except Exception as e:
        print(f"Unexpected error: {e}")
        await websocket.close()