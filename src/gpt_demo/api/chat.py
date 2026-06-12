from fastapi import APIRouter
from pydantic import BaseModel
from openai import AsyncOpenAI

from gpt_demo.config import settings

router = APIRouter(prefix="/chat", tags=["chat"])
client = AsyncOpenAI(api_key=settings.openai_api_key)


class ChatRequest(BaseModel):
    message: str
    model: str = settings.openai_model


class ChatResponse(BaseModel):
    reply: str


@router.post("/prompt", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    response = await client.chat.completions.create(
        model=request.model,
        messages=[{"role": "user", "content": request.message}],
    )
    return ChatResponse(reply=response.choices[0].message.content)


@router.get("/health")
async def health():
    return {"healthy": "True"}