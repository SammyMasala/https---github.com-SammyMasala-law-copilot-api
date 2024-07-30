from api.repositories import *
from api.services import *


# Repositories
session_respository = SessionRepository()
chat_repository = ChatRepository()

# Services
session_service = SessionService(session_repository=session_respository)
chat_service = ChatService(chat_repository=chat_repository)

def init():
    return {
        # Repositories
        "session_repository": session_respository,
        "chat_repository": chat_repository,

        # Services
        "session_service": session_service,
        "chat_service": chat_service
    }
