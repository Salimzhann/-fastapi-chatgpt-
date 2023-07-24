from fastapi import APIRouter, Depends
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


@router.post("/", response_model=ChatResponse)
def chat_with_ai(
    request: ChatRequest,
    svc: Service = Depends(get_service),
) -> ChatResponse:
    prompt = request.prompt
    response = svc.chat_service.get_response(prompt)
    print(response)
    return ChatResponse(response=response["content"])
