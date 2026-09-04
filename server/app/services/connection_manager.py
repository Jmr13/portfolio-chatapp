from typing import Optional

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.user_connections: dict[int, WebSocket] = {}
        self.admin_connection: Optional[WebSocket] = None

    async def connect_user(self, client_id: int, websocket: WebSocket):
        await websocket.accept()
        self.user_connections[client_id] = websocket

    async def connect_admin(self, websocket: WebSocket, subprotocol: str):
        await websocket.accept(subprotocol=subprotocol)
        self.admin_connection = websocket

    def disconnect_user(self, client_id: int):
        self.user_connections.pop(client_id, None)

    def disconnect_admin(self):
        self.admin_connection = None

    async def send_to_admin(self, client_id: int, message: str):
        if self.admin_connection:
            try:
                await self.admin_connection.send_text(f"User #{client_id}: {message}")
            except RuntimeError:
                self.disconnect_admin()

    async def send_to_user(self, client_id: int, message: str):
        websocket = self.user_connections.get(client_id)
        if websocket:
            await websocket.send_text(f"[ADMIN] {message}")