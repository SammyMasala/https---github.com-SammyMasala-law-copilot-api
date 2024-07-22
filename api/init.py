from api.config import TABLE_NAME
from api.repositories.chat_repository import ChatRepository
from api.repositories.session_repository import SessionRepository
from api.services.chat_service import ChatService
from api.services.session_service import SessionService


def init():
    # Repositories
    session_repository = SessionRepository()
    chat_repository = ChatRepository()

    # Services
    session_service = SessionService(table_name=TABLE_NAME, session_repository=session_repository)
    chat_service = ChatService(chat_repository)
    return {
        # Repositories
        session_repository,
        chat_repository,

        # Services
        session_service,
        chat_service
    }