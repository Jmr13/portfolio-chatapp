from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    role: str
    content: str

class ConversationResponse(BaseModel):
    current_time: str

class ConversationRequest(BaseModel):
    messages: list[Message]