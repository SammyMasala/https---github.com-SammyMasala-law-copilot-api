class SessionRepository:
    def get_session(self, table_name, client, id):
        try:
            return client.get_item(Key={ 
                "id": {
                    "S": id 
                }
            }, TableName=table_name)
        except:
            raise

    def put_session(self, table_name, client, session):
        try:
            return client.put_item(Item={
                "id": {
                    "S": session.get("id") 
                },"doc_html": {
                    "S": session.get("doc_html") 
                },"messages": {
                    "SS": session.get("messages") 
                },
            }, TableName=table_name)
        except:
            raise

    def delete_session(self, table_name, client, id):
        try: 
            return client.delete_item(Key={
                "id": {
                    "S": id 
                }
            }, TableName=table_name)
        except: 
            raise
        

