from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chatbot.engine import process_message

router = APIRouter(prefix="/api/v1/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
    response_text = process_message(payload.message)
    return ChatResponse(response = response_text)
