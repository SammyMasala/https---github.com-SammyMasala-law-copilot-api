from api.clients.mistral import MistralClient
from api.config import CHAT_API_KEY, MODEL_NAME

class ChatRepository:
    def __init__(self):
        self.client = MistralClient(api_key=CHAT_API_KEY)
        self.model_name = MODEL_NAME
    def chat(self, messages):
        response = self.client.chat_response(model=self.model_name, messages=messages)
        return response
