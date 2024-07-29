from api.repositories.session_repository import SessionRepository
from api.services.session_service import SessionService

# Repositories
session_respository = SessionRepository()

# Services
session_service = SessionService(session_repository=session_respository)

def init():
    return {
        # Repositories
        "session_repository": session_respository,

        # Services
        "session_service": session_service
    }
