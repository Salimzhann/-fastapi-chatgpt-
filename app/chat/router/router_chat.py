from fastapi import APIRouter, Depends
from app.utils import AppModel
from ..service import ChatService, get_service
import openai

router = APIRouter()


class ChatRequest(AppModel):
    prompt: str


class ChatResponse(AppModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
def chat_with_ai(
    request: ChatRequest,
    svc: ChatService = Depends(get_service),
) -> ChatResponse:
    prompt = request.prompt
    response = svc.get_response(prompt)
    return ChatResponse(response=response)
