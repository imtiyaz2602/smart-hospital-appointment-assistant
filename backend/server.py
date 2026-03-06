import sys
import os

from fastapi import FastAPI
from pydantic import BaseModel

# allow project imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.voice_agent import agent_response

app = FastAPI()


class Query(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Voice AI Agent API running"}


@app.post("/voice-agent")
def voice_agent(query: Query):

    user_message = query.message

    response = agent_response(user_message)

    return {
        "user_message": user_message,
        "ai_response": response
    }