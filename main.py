import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models  import promptRequest
from services.openai_service import call_openai
from services.claude_service import call_claude
from services.gemini_service import call_gemini

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/comparee")
async def compare_llms(data: promptRequest):
    prompt = data.prompt

    results = await asyncio.gather(
        call_openai(prompt),
        call_claude(prompt),
        call_gemini(prompt)
    )

    return {
        "openai_response": results[0],
        "claude_response": results[1],
        "gemini_response": results[2]
    }