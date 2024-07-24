from api.repositories.chat_repository import ChatRepository
from api.clients.mistral.client import init_mistral_client
from mistralai.models.chat_completion import ChatMessage


class ChatService:
    def __init__(self, chat_repository: ChatRepository, chat_api_key, chat_model):
        self.chat_repository = chat_repository
        self.client = init_mistral_client(api_key=chat_api_key)
        self.model = chat_model,
    
    def send_message(self, context_messages):
        messages = []
        for message in context_messages:
            messages.append(ChatMessage(role="user", content=message.get("message")))
        return self.chat_repository.chat_response(client=self.client, model=self.model, messages=messages)
