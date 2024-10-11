from typing import List
from unittest.mock import patch
from mistralai.models.chat_completion import ChatMessage, ChatCompletionResponse, ChatCompletionResponseChoice, UsageInfo

from api import init
from api.entities.chat_entities import Message
from api.services.chat_service import ChatService

chat_service:ChatService = init()["chat_service"]
mock_mistral_return = ChatCompletionResponse(
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

test_messages: List[Message] = [Message(is_user=True, message="Test")]

# LEGACY
test_legacy_messages = [{"isUser": True, "message": "Test"}]

def test_conversation():    
    with patch("api.clients.mistral.MistralChatClient.chat", return_value=mock_mistral_return):
        assert(chat_service.conversation(messages=test_messages)) == "This is a mock response."

def test_ask_law():    
    with patch("api.clients.mistral.MistralChatClient.chat", return_value=mock_mistral_return):
        assert(chat_service.ask_law(message=test_messages[0])) == "This is a mock response."

# LEGACY
def test_legacy_conversation():    
    with patch("api.clients.mistral.MistralChatClient.chat", return_value=mock_mistral_return):
        assert(chat_service.legacy_conversation(messages=test_legacy_messages)) == "This is a mock response."
