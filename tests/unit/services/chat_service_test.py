from unittest.mock import patch
from mistralai.models.chat_completion import ChatMessage, ChatCompletionResponse, ChatCompletionResponseChoice, UsageInfo

from mistralai.models.chat_completion import ChatMessage, ChatCompletionResponse, ChatCompletionResponseChoice, UsageInfo

from api.init import init
from api.services.chat_service import ChatService

chat_service:ChatService = init()["chat_service"]
def test_chat():
    mock_mistral_return = mockResponse = ChatCompletionResponse(
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
    test_messages = [{"isUser": True, "message": "Test"}]
    with patch("api.clients.mistral.MistralChatClient.chat", return_value=mock_mistral_return):
        assert(chat_service.chat_completion(messages=test_messages)) == mock_mistral_return
