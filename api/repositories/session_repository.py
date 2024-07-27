from api.clients.aws.dynamodb import DynamoDBClient
from api.config import AWS_REGION, TABLE_NAME


class SessionRepository:
    def __init__(self):
        self.client = DynamoDBClient(region_name=AWS_REGION)
        self.table_name = TABLE_NAME
    def get_session(self, id):
        try:
            return self.client.get_item(key={ 
                "id": {
                    "S": id 
                }
            }, table_name=self.table_name)
        except:
            raise

    def put_session(self, session):
        try:
            return self.client.put_item(item={
                "id": {
                    "S": session.get("id") 
                },"doc_html": {
                    "S": session.get("doc_html") 
                },"messages": {
                    "SS": session.get("messages") 
                },
            }, table_name=self.table_name)
        except:
            raise

    def delete_session(self, id):
        try: 
            return self.client.delete_item(key={
                "id": {
                    "S": id 
                }
            }, table_name=self.table_name)
        except: 
            raise
        

