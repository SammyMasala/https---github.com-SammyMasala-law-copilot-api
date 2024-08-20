from api.clients.aws.dynamodb import DynamoDBClient
from api.config import AWS_REGION, TABLE_NAME


class SessionRepository:
    def __init__(self):
        self.TABLE_NAME = TABLE_NAME
        self.client = DynamoDBClient(region_name=AWS_REGION)

    def put_session(self, session):
        item = {
            "id": {
                "S": session.get("id")
            }, "doc_html": {
                "S": session.get("doc_html")
            }, "messages": {
                "L": [{"S": message} for message in session.get("messages")]
            }
        }
        return self.client.put_item(table_name=self.TABLE_NAME, item=item)

    def get_session(self, session_id):
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
                "doc_html": session.get("doc_html").get("S"),
                "messages": [message.get("S") for message in session.get("messages").get("L")]
            }
