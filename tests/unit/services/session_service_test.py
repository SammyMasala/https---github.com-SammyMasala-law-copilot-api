from unittest.mock import patch
from api.init import init
from api.services.chat_service import ChatService
from mistralai.models.chat_completion import (ChatCompletionResponse, ChatCompletionResponseChoice, ChatMessage, UsageInfo)

def test_get_session():
    mockResponse = {"session": {
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

    mockMessages = [{"isUser": True, "message": "Test"}]
    chat_service: ChatService = init()["chat_service"]
    with patch("api.clients.mistral.MistralClient.chat_response", return_value=mockResponse):
        assert(chat_service.send_message(mockMessages)) == mockResponse
        pass

# def get_session(self, session_id):
#         return self.repository.get_session(table_name=self.table_name, client=self.client, id=session_id)
    
#     def put_session(self, session):
#         return self.repository.put_session(table_name=self.table_name, client=self.client, session=session)