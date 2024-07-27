import boto3

def init_dynamodb_client():
    return boto3.client("dynamodb", region_name="ap-southeast-1")