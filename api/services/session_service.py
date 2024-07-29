from api.repository.session_repository import SessionRepository


class SessionService:
    def __init__(self, session_repository):
        self.session_repository: SessionRepository = session_repository

    def get_session(self, id):
        try: 
            return self.session_repository.get_session(session_id=id)
        except:
            raise

    def put_session(self, session):
        try:
            return self.session_repository.put_session(session=session)
        except:
            raise