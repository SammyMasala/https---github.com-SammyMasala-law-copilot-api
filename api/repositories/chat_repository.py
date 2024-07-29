

from api.clients.mistral import MistralChatClient
from api.config import MISTRAL_API_KEY, MODEL_NAME


class ChatRepository:
    def __init__(self):
        self.client = MistralChatClient(api_key=MISTRAL_API_KEY)
        self.MODEL_NAME = MODEL_NAME
        
    def chat(self, messages):
        context_messages = [
            {
                "role": ("user" if message.isUser is True else "assistant"),
                "message":message.get("message")
            } for message in messages
        ]
        return self.client.chat(model=self.MODEL_NAME, messages=context_messages)