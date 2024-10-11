from abc import ABC, abstractmethod
from typing import Any

from flask import json
from api.dtos.session_dtos import LoadSessionResponse, SaveSessionRequest
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

    def get_session(self, id) -> Any:
        """Get Session

        Args:
            id (str): session id

        Returns:
            session(any): session
        """
        try:
            session = self.session_repository.get(id)
            return json.loads(session.session)
        except Exception:
            raise
            
    def update_session(self, id: str, session_data: Any):
        try:
            session = Session(
                id=id,
                session=json.dumps(session_data)
            )
            return self.session_repository.put(session=session)
        except Exception:
            raise

    # Legacy Support
    def legacy_get_session(self, id) -> Any:
        session = self.get_session(id=id)
        session_filter_messages = {key:value for key, value in session.items() if key != "messages"}

        return{
            "id": id,
            "messages": [json.dumps(message) for message in session.get("messages", [])],
            **session_filter_messages
        }
    
    def legacy_update_session(self, data: Any):
        try:
            id = data.get("id")
            
            session_data = {
                "doc_html": data.get("doc_html", ""),
                "messages": [json.loads(message) for message in data.get("messages", [])]
            }
            session = Session(
                id=id,
                session=json.dumps(session_data)
            )
            return self.session_repository.put(session=session)
        except Exception:
            raise
