from fastapi import FastAPI
from models.conversation import run_conversation
from schemas.conversation import ConversationRequest, ConversationResponse

app = FastAPI()

@app.post("/conversation/", response_model=ConversationResponse)
def start_conversation(request: ConversationRequest):
    """Handle the conversation and return a response."""
    response_content = run_conversation(request.messages)
    return ConversationResponse(current_time=response_content)