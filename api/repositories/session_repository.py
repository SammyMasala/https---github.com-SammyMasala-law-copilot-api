class SessionRepository:
    def get_session(self, table_name, client, id):
        try:
            return client.get_item(Key={
                "S": id
            }, TableName=self.table_name)
        except:
            raise

    def put_session(self, table_name, client, session):
        try:
            return client.put_item(Item={
                "session_id": {
                    "S": session.get("id") 
                },"doc_html": {
                    "S": session.get("doc_html") 
                },"messages": {
                    "SS": session.get("messages") 
                },
            }, TableName=self.table_name)
        except:
            raise

    def delete_session(self, table_name, client, id):
        try: 
            return client.delete_item(Key={
                "S": id
            }, TableName=self.table_name)
        except: 
            raise
        

