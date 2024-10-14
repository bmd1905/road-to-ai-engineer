import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI
from pydantic import BaseModel


class ChatRequest(BaseModel):
    model: str = "gpt-4o-mini"
    message: str
    history: Any = []


class ChatResponse(BaseModel):
    message: str | None = None


load_dotenv()

app = FastAPI()

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(inputs: ChatRequest):
    openai_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        *inputs.history,
        {"role": "user", "content": inputs.message},
    ]
    response = await client.chat.completions.create(
        model=inputs.model,
        messages=openai_messages,
        stream=True,
    )

    async def stream():
        async for chunk in response:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content

    return StreamingResponse(stream(), media_type="text/event-stream")
