from unittest.mock import patch

from api.init import init
from api.services.session_service import SessionService

session_service: SessionService = init()["session_service"] 
def test_session_service():
    mock_get_item_return = {"session": {
        "Item": {
            "doc_html": {
                "S": "<p>this is a test doc</p>"
            },
            "id": {
                "S": "test"
            },
            "messages": {
                "SS": [
                    "{'message': 'Hi', 'isUser': false}",
                    "{'message': 'Yo', 'isUser': true}"
                ]
            }
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
    }}
    with patch("api.clients.aws.dynamodb.DynamoDBClient.get_item", return_value=mock_get_item_return):
        assert(session_service.get_session(session_id="test")) == mock_get_item_return

    mock_put_item_return = {}
    with patch("api.clients.aws.dynamodb.DynamoDBClient.put_item", return_value=mock_put_item_return):
        assert(session_service.put_session(session={            
            "id": "test",
            "messages": [
                "{'message': 'Hi', 'isUser': false}",
                "{'message': 'Yo', 'isUser': true}"
            ],
            "doc_html": "<p>this is a test doc</p>"
        })) == mock_put_item_return