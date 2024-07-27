from unittest.mock import patch
from api.init import init
from api.services.chat_service import ChatService
from mistralai.models.chat_completion import (ChatCompletionResponse, ChatCompletionResponseChoice, ChatMessage, UsageInfo)

def test_send_message():
    mockResponse = ChatCompletionResponse(
        id='00ecbb59eb5049ad92c4c0ff2627b06a', 
        object='chat.completion', 
        created=1722004932, 
        model='open-mixtral-8x22b', 
        choices=[ChatCompletionResponseChoice(
            index=0, 
            message=ChatMessage(
                role='assistant', 
                content="This is a mock response.",
                name=None, 
                tool_calls=None, 
                tool_call_id=None
            ),
            finish_reason= None
        )], 
        usage=UsageInfo(
            prompt_tokens=5, 
            total_tokens=42, 
            completion_tokens=37
        )
)

    mockMessages = [{"isUser": True, "message": "Test"}]
    chat_service: ChatService = init()["chat_service"]
    with patch("api.clients.mistral.MistralClient.chat_response", return_value=mockResponse):
        assert(chat_service.send_message(mockMessages)) == mockResponse

