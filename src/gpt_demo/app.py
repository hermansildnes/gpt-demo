from fastapi import FastAPI

from gpt_demo.api import chat

app = FastAPI(title="GPT Demo")

app.include_router(chat.router, prefix="/api/v1")
