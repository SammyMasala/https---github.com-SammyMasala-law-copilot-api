

from api.clients.mistral import MistralChatClient
from api.config import MISTRAL_API_KEY, MODEL_NAME, SYSTEM_PROMPT


class ChatRepository:
    def __init__(self):
        self.client = MistralChatClient(api_key=MISTRAL_API_KEY)
        self.MODEL_NAME = MODEL_NAME
        self.SYSTEM_PROMPT = SYSTEM_PROMPT
        
    def chat(self, messages):
        try:
            system_message = [{"role": "system", "content": SYSTEM_PROMPT}]
            prompt_messages = [  
                {
                    "role": ("user" if message.get("isUser") is True else "assistant"),
                    "content":message.get("message")
                } for message in messages
            ]
            reply = self.client.chat(model=self.MODEL_NAME, messages=system_message + prompt_messages)
            return reply.choices[0].message.content
        except Exception:
            print("test")
            raise 
        