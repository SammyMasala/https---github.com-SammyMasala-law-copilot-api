

from api.clients.mistral import MistralChatClient
from api.config import MISTRAL_API_KEY, MODEL_NAME


class ChatRepository:
    def __init__(self):
        self.client = MistralChatClient(api_key=MISTRAL_API_KEY)
        self.MODEL_NAME = MODEL_NAME
        
    def chat(self, messages):
        context_messages = [
            {
                "role": ("user" if message.get("isUser") is True else "assistant"),
                "content":message.get("message")
            } for message in messages
        ]
        reply = self.client.chat(model=self.MODEL_NAME, messages=context_messages)
        return reply.choices[0].message.content