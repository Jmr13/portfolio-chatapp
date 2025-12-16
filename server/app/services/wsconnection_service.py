from fastapi import WebSocket
from typing import Dict, Optional

class ConnectionManager:
    def __init__(self):
        self.user_connections: Dict[int, WebSocket] = {}
        self.admin_connection: Optional[WebSocket] = None

    async def connect_user(self, client_id: int, websocket: WebSocket):
        await websocket.accept()
        self.user_connections[client_id] = websocket

    async def connect_admin(self, websocket: WebSocket, subprotocol: str):
        await websocket.accept(subprotocol=subprotocol)
        self.admin_connection = websocket

    def disconnect_user(self, client_id: int):
        if client_id in self.user_connections:
            del self.user_connections[client_id]

    def disconnect_admin(self):
        self.admin_connection = None

    # Send message from user to admin
    async def send_to_admin(self, client_id: int, message: str):
        if self.admin_connection:
            try:
                await self.admin_connection.send_text(f"User #{client_id}: {message}")
            except RuntimeError:
                print("Admin connection closed while sending")

    # Send message from admin to a specific user
    async def send_to_user(self, client_id: int, message: str):
        ws = self.user_connections.get(client_id)
        if ws:
            await ws.send_text(f"[ADMIN] {message}")
