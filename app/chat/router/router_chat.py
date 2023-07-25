from fastapi import APIRouter, Depends, status
from app.utils import AppModel
from pydantic import Field
from typing import Any
from ..service import Service, get_service
import json

router = APIRouter()


class ChatRequest(AppModel):
    prompt: str


class ChatResponse(AppModel):
    response: str


@router.post("/")
def chat_with_ai(
    request: ChatRequest,
    svc: Service = Depends(get_service),
) -> str:
    prompt = request.prompt
    response = svc.chat_service.get_response(prompt)
    
    # Update chat history with user's prompt and AI's response
    svc.chat_service.add_chat("user", prompt)
    svc.chat_service.add_chat("assistant", response)

    # Return AI's response
    return response["content"]