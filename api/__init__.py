from api.blueprints import ChatBlueprint
from api.blueprints import SessionBlueprint
from api.repositories import *
from api.services import *

# Repositories
session_respository = SessionRepository()

# Services
session_service = SessionService(session_repository=session_respository)
chat_service = ChatService()

# Blueprints
session_bp = SessionBlueprint(session_service=session_service)
chat_bp = ChatBlueprint(chat_service=chat_service)

def init():
    return {
        # Repositories
        "session_repository": session_respository,

        # Services
        "session_service": session_service,
        "chat_service": chat_service,

        # Blueprints
        "session_bp": session_bp,
        "chat_bp": chat_bp
    }
