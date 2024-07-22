import boto3
from api.repositories.session_repository import SessionRepository


class SessionService:
    def __init__(self, table_name, session_repository: SessionRepository):
        self.repository = session_repository
        self.table_name = table_name
        self.client = boto3.client("dynamodb", region="ap-southeast-1")

    def get_session(self, session_id):
        return self.repository.get_session(table_name=self.table_name, client=self.client, id=session_id)
    
    def put_session(self, session):
        return self.repository.put_session(table_name=self.table_name, client=self.client, session=session)

