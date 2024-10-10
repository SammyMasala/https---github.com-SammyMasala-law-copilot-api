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

    def get(self, id) -> Session:
        try:
            key = {
                "id": {
                    "S": id
                }
            }

            response = self.client.get_item(key=key, table_name=self.TABLE_NAME)
            print(response)
            response_item = response.get("Item")
            session = Session(
                id=response_item.get("id").get("S"), 
                session = response_item.get("session", {}).get("S")
            )
            return session
        except Exception:
            raise