from api.blueprints.session_blueprint import SessionBlueprint
from api.repositories import *
from api.services import *

# Repositories
session_respository = SessionRepository()
chat_repository = ChatRepository()

# Services
session_service = SessionService(session_repository=session_respository)
chat_service = ChatService(chat_repository=chat_repository)

# Blueprints
session_bp = SessionBlueprint(session_service=session_service)

def init():
    return {
        # Repositories
        "session_repository": session_respository,
        "chat_repository": chat_repository,

        # Services
        "session_service": session_service,
        "chat_service": chat_service,

        # Blueprints
        "session_bp": session_bp
    }
