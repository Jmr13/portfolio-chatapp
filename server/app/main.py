from fastapi import FastAPI
from app.routers import conversations
from app.routers import websockets

app = FastAPI()

app.include_router(conversations.router)
app.include_router(websockets.router)