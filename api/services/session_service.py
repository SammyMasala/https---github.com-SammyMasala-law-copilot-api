from abc import ABC, abstractmethod
from typing import Any

from flask import json
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
            session = self.session_repository.get(id=session_id)
            session_data = json.loads(session.session)
            print(session)
            session_parsed = {
                "id": session_id,
                "doc_html": session_data.get("doc_html"),
                "messages": [json.dumps(message) for message in session_data.get("messages", {})]
            }

            return session_parsed
        except Exception:
            raise
            
    def legacy_update_session(self, session):
        try:
            session_updated = Session(
                id=session.get("id"),
                session=json.dumps(session)
            )
            return self.session_repository.put(session=session_updated)
        except Exception:
            raise
