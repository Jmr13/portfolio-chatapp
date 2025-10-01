from fastapi import APIRouter
from app.services.conversation_service import run_conversation
from app.schemas.conversation import ConversationRequest, ConversationResponse

router = APIRouter(prefix="/conversation", tags=["conversations"])

@router.post("/", response_model=ConversationResponse)
def start_conversation(request: ConversationRequest):
    response = run_conversation(request.messages)
    return ConversationResponse(
        message = response.content
    )