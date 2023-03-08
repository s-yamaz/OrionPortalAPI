from fastapi import APIRouter
from functions import conversations

router = APIRouter(tags=["conversations"], prefix="/conversations")


@router.get("/{channel_id}")
def get_conversations(channel_id: str):
    return conversations.get_conversations(channel_id)
