from typing import List
from pydantic import BaseModel

from api.dtos import ApiResponse
from api.entities.chat_entities import Message

# conversation
class ConversationRequest(BaseModel):
    messages: List[Message]

class ConversationResponse(ApiResponse):
    reply: str
    
# ask_law
class AskLawRequest(BaseModel):
    message: Message

class AskLawResponse(ApiResponse):
    reply: str