from api.clients.mistral.client import init_mistral_client
from mistral.client import MistralClient

class MistralChatClient:
    def __init__(self, api_key):
        self.client:MistralClient = init_mistral_client(api_key=api_key)
    
    def chat(self, model, messages):
        return self.client.chat(model=model, messages=messages)

