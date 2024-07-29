from unittest.mock import patch

from api.init import init
from api.services.session_service import SessionService

session_service: SessionService = init()["session_service"] 
def test_session_service():
    mock_get_item_return = {}
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