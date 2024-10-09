from abc import ABC, abstractmethod
from typing import Any
from api.entities.session_entities import Session
from api.repositories.session_repository import SessionRepository

class ISessionService(ABC):
    @abstractmethod
    def get_session(self, id) -> Any:
        pass
    
    @abstractmethod
    def update_session(self, session:Session) -> Any:
        pass

class SessionService(ISessionService):
    def __init__(self, session_repository):
        self.session_repository: SessionRepository = session_repository

    def get_session(self, id):
        """Get Session

        Args:
            id (str): session id

        Returns:
            session(any): session
        """
        try:
            return self.session_repository.get(id)
        except Exception:
            raise
            
    def update_session(self, session: Session):
        try:
            return self.session_repository.put(session=session)
        except Exception:
            raise

    # DEPRECATED!!
    def legacy_get_session(self, session_id):
        try:
            return self.session_repository.legacy_get(session_id=session_id)
        except Exception:
            raise
            
    def legacy_update_session(self, session):
        try:
            return self.session_repository.legacy_put(session=session)
        except Exception:
            raise
