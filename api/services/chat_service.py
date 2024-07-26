from api.repositories.chat_repository import ChatRepository
from mistralai.models.chat_completion import ChatMessage


class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository
    
    def send_message(self, messages):
        response = self.chat_repository.chat(messages=messages)
        return response
