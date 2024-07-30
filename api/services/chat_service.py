from api.repositories.chat_repository import ChatRepository


class ChatService:
    def __init__(self, chat_repository):
        self.chat_repository:ChatRepository = chat_repository

    def chat_completion(self, messages):
        return self.chat_repository.chat(messages=messages)