from unittest.mock import patch

from api.init import init
from api.services.chat_service import ChatService


chat_service:ChatService = init()["chat_service"]
def test_chat_service():
    mock_mistral_return = {}
    test_messages = {}
    with patch("api.clients.mistral.MistralChatClient.chat", return_value=mock_mistral_return):
        assert(chat_service.chat_completion(messages=test_messages)) == mock_mistral_return
