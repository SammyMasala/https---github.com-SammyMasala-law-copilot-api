from mistralai.client import ChatCompletionResponse
from api.clients.mistral.client import init_mistral_client

class MistralClient:
    def __init__(self, api_key):
        self.client = init_mistral_client(api_key=api_key)
    
    def chat_completion(self, messages):
        try:
            return self.client.chat_completion(messages=messages)
        except:
            raise

