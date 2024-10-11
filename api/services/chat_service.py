from abc import ABC, abstractmethod
from typing import List
from api.clients.mistral import MistralChatClient
from api.config import MISTRAL_API_KEY, MODEL_NAME, SYSTEM_PROMPT_LAW
from api.entities.chat_entities import Message

class IChatService(ABC):
    @abstractmethod
    def conversation(self, messages:List[Message]) -> str:
        pass

    @abstractmethod
    def ask_law(self, message:Message) -> str:
        pass

class ChatService(IChatService):
    def __init__(
            self, 
            client = MistralChatClient(api_key=MISTRAL_API_KEY),
            model_name = MODEL_NAME,
            system_prompt_law = SYSTEM_PROMPT_LAW
        ):
        self.client = client
        self.model_name = model_name
        self.system_prompt_law = system_prompt_law

    def conversation(self, messages: List[Message]) -> str:
        MAX_MESSAGES = 6 # Max number of past messages to control input token cost
        try:
            prompt_messages = [  
                {
                    "role": ("user" if message.is_user is True else "assistant"),
                    "content":message.message
                } for message in messages[max(0, len(messages)-MAX_MESSAGES):len(messages)]
            ]
            reply = self.client.chat(model=self.model_name, messages=prompt_messages)
            return reply.choices[0].message.content
        except Exception:
            raise 

    def ask_law(self, message:Message) -> str:
        try:
            system_message = [{"role": "system", "content": self.system_prompt_law}]
            prompt_message = [  
                {
                    "role": ("user" if message.is_user is True else "assistant"),
                    "content":message.message
                } 
            ]
            reply = self.client.chat(model=self.model_name, messages=system_message + prompt_message)
            return reply.choices[0].message.content
        except Exception:
            raise 

    # Legacy
    def legacy_conversation(self, messages):
        MAX_MESSAGES = 6 # Max number of past messages to control input token cost
        try:
            prompt_messages = [  
                {
                    "role": ("user" if message.get("isUser") is True else "assistant"),
                    "content":message.get("message")
                } for message in messages[max(0, len(messages)-MAX_MESSAGES):len(messages)]
            ]
            reply = self.client.chat(model=self.model_name, messages=prompt_messages)
            return reply.choices[0].message.content
        except Exception:
            raise 