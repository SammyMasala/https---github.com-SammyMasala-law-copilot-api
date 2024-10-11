from unittest.mock import patch

from api import init
from api.entities.session_entities import Session
from api.services.session_service import SessionService

session_service: SessionService = init()["session_service"] 

mock_dynamodb_get_return = {
    "Item": {            
        "id": {
            "S": "test"
        },
        "session": {"S": "{\"messages\": [{\"message\": \"Hi\",\"isUser\": true}],\"doc_html\": \"<p>this is a test doc</p>\"}"}
    },
    "ResponseMetadata": {
        "HTTPHeaders": {
            "connection": "keep-alive",
            "content-length": "166",
            "content-type": "application/x-amz-json-1.0",
            "date": "Fri, 26 Jul 2024 10:22:24 GMT",
            "server": "Server",
            "x-amz-crc32": "4238721578",
            "x-amzn-requestid": "M48B6NKO16JFTSJ4A51RKQ0UDVVV4KQNSO5AEMVJF66Q9ASUAAJG"
        },
        "HTTPStatusCode": 200,
        "RequestId": "M48B6NKO16JFTSJ4A51RKQ0UDVVV4KQNSO5AEMVJF66Q9ASUAAJG",
        "RetryAttempts": 0
    }
}

mock_dynamodb_put_return = {
    "ResponseMetadata": {
        "HTTPHeaders": {
            "connection": "keep-alive",
            "content-length": "2",
            "content-type": "application/x-amz-json-1.0",
            "date": "Sat, 27 Jul 2024 04:23:58 GMT",
            "server": "Server",
            "x-amz-crc32": "2745614147",
            "x-amzn-requestid": "MJAF0PN5G5D3TQFP5VCRF0IMAJVV4KQNSO5AEMVJF66Q9ASUAAJG"
        },
        "HTTPStatusCode": 200,
        "RequestId": "MJAF0PN5G5D3TQFP5VCRF0IMAJVV4KQNSO5AEMVJF66Q9ASUAAJG",
        "RetryAttempts": 0
    }
}

def test_load():
    test_load_response = Session(
        id="test",
        session="{\"messages\": [{\"message\": \"Hi\",\"isUser\": true}],\"doc_html\": \"<p>this is a test doc</p>\"}"
    )

    with patch("api.clients.aws.dynamodb.DynamoDBClient.get_item", return_value=mock_dynamodb_get_return):
        assert(session_service.get_session(id="test")) == test_load_response

def test_save():
    test_session = Session(
        id="test",
        session="{\"messages\": [{\"message\": \"Hi\",\"isUser\": true}],\"doc_html\": \"<p>this is a test doc</p>\"}"
    )
    with patch("api.clients.aws.dynamodb.DynamoDBClient.put_item", return_value=mock_dynamodb_put_return):
        assert(session_service.update_session(session=test_session)) == mock_dynamodb_put_return

# LEGACY
def test_legacy_load():
    test_load_response = {
        "doc_html": "<p>this is a test doc</p>",
        "id": "test",
        "messages": [
            '{"message": "Hi", "isUser": true}',
        ]
    }

    with patch("api.clients.aws.dynamodb.DynamoDBClient.get_item", return_value=mock_dynamodb_get_return):
        assert(session_service.legacy_get_session(id="test")) == test_load_response
