from abc import ABC, abstractmethod
from typing import Any
from api.clients.aws.dynamodb import DynamoDBClient
from api.config import AWS_REGION, TABLE_NAME
from api.entities.session_entities import Session

class ISessionRepository(ABC):
    @abstractmethod
    def put(self, session: Session) -> Any:
        pass
    @abstractmethod
    def get(self, id) -> Any:
        pass

class SessionRepository(ISessionRepository):
    def __init__(self):
        self.TABLE_NAME = TABLE_NAME
        self.client = DynamoDBClient(region_name=AWS_REGION)

    def put(self, session:Session):
        try:
            item = {
                "id": {
                    "S": session.id
                }, "session": {
                    "S": session.session
                }
            }
            return self.client.put_item(table_name=self.TABLE_NAME, item=item)        
        except Exception:
            raise

    def get(self, id):
        try:
            key = {
                "id": {
                    "S": id
                }
            }

            response = self.client.get_item(key=key, table_name=self.TABLE_NAME)
            print(response)
            session = response.get("Item")
            if session is None:
                return None
            else: 
                return session
        except Exception:
            raise

    # DEPRECATED!!
    def legacy_put(self, session):
        try:
            item = {
                "id": {
                    "S": session.get("id", {})
                }, "doc_html": {
                    "S": session.get("doc_html", "")
                }, "messages": {
                    "L": [{"S": message} for message in session.get("messages", [])]
                }
            }
            return self.client.put_item(table_name=self.TABLE_NAME, item=item)        
        except Exception:
            raise

    def legacy_get(self, session_id):
        try:
            key = {
                "id": {
                    "S": session_id
                }
            }

            response = self.client.get_item(key=key, table_name=self.TABLE_NAME)
            session = response.get("Item")
            if session is None:
                return None
            else: 
                return {
                    "id": session.get("id").get("S"),
                    "doc_html": session.get("doc_html", {}).get("S"),
                    "messages": [message.get("S", {}) for message in session.get("messages",{}).get("L", [])]
                }
        except Exception:
            raise
