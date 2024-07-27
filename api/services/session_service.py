from api.clients.aws.dynamodb import init_dynamodb_client
from api.config import TABLE_NAME
from api.repositories.session_repository import SessionRepository

class SessionService:
    def __init__(self, session_repository: SessionRepository):
        self.repository = session_repository
        self.table_name = TABLE_NAME
        self.client = init_dynamodb_client()

    def get_session(self, session_id):
        return self.repository.get_session(table_name=self.table_name, client=self.client, id=session_id)
    
    def put_session(self, session):
        return self.repository.put_session(table_name=self.table_name, client=self.client, session=session)

