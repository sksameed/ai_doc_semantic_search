from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.rag_service import ask_question

router = APIRouter()

@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    return ask_question(request.question)