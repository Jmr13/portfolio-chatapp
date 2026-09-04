from fastapi import APIRouter
from app.schemas.conversation import ConversationRequest, ConversationResponse
from app.services.conversation_service import run_conversation

router = APIRouter(prefix="/conversation", tags=["conversations"])

@router.post("/", response_model=ConversationResponse)
def process_conversation(request: ConversationRequest):
    response = run_conversation(request.messages)
    return ConversationResponse(
        message = response.content
    )