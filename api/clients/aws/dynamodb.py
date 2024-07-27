import boto3

class DynamoDBClient:
    def __init__(self, region_name):
        self.client =  boto3.client("dynamodb", region_name=region_name)

    def get_item(self, table_name, key):
        try:
            return self.client.get_item(Key=key, TableName=table_name)
        except:
            raise

    def put_item(self, table_name, item):
        try:
            return self.client.put_item(Item=item,
             TableName=table_name)
        except:
            raise

    def delete_item(self, table_name, key):
        try: 
            return self.client.delete_item(Key=key, TableName=table_name)
        except: 
            raise
