from api.repository.session_repository import SessionRepository


class SessionService:
    def __init__(self, session_repository):
        self.session_repository: SessionRepository = session_repository

    def get_session(self, session_id):
        return self.repository.get_session(id=session_id)
    
    def put_session(self, session):
        return self.repository.put_session(session=session)

