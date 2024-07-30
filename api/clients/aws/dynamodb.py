import os
import boto3

class DynamoDBClient:
    def __init__(self, region_name):
        if os.environ.get('IS_OFFLINE'):
            print("WARN: No connection AWS for DynamoDB, using local!")
            self.client = boto3.client(
                'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
            )
        else: 
            self.client = boto3.client("dynamodb", region_name=region_name)

    def get_item(self, key, table_name):
        return self.client.get_item(Key=key, TableName=table_name)

    def put_item(self, item, table_name):
        return self.client.put_item(Item=item, TableName=table_name)

    def delete_item(self, key, table_name):
        return self.client.delete_item(Key=key, TableName=table_name)
