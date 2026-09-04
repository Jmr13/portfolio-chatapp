from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.admin_auth_service import is_authorized_admin, parse_admin_protocols
from app.services.connection_manager import ConnectionManager

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
    credentials = parse_admin_protocols(
        websocket.headers.get("sec-websocket-protocol", "")
    )
    if credentials is None:
        await websocket.close(code=1008)
        return

    protocol, admin_token = credentials

    if not is_authorized_admin(client_host, admin_token):
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