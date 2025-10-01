from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class Message(BaseModel):
    role: str
    content: str

class ConversationRequest(BaseModel):
    messages: list[Message]

class ConversationResponse(BaseModel):
    message: str