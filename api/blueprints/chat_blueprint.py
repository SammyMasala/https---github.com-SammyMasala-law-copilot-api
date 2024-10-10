
from abc import ABC, abstractmethod
from flask import Blueprint, jsonify, make_response, request

from api.dtos import ApiResponse
from api.dtos.chat_dtos import AskLawRequest, AskLawResponse, ConversationRequest, ConversationResponse
from api.services.chat_service import ChatService

class IChatBlueprint(ABC):
    @abstractmethod
    def conversation(self, id) -> ConversationResponse:
        pass

    @abstractmethod
    def ask_law(self, id) -> AskLawResponse:
        pass

class ChatBlueprint(IChatBlueprint):
    blueprint: Blueprint
    chat_service: ChatService

    def __init__(self, chat_service: ChatService):
        self.chat_service = chat_service

        self.blueprint = Blueprint(name="chat", import_name="__name__", url_prefix="/chat")

        self.blueprint.add_url_rule(rule="", methods=["POST"], view_func=self.conversation)
        self.blueprint.add_url_rule(rule="/law", methods=["POST"], view_func=self.ask_law)

        # Legacy
        self.blueprint.add_url_rule(rule="/conversation", methods=["POST"], view_func=self.legacy_conversation)

    def get_blueprint(self):
        return self.blueprint
    

    def conversation(self):
        """
        POST /chat - Conversation
        """

        try:
            conversation_request = ConversationRequest(
                **request.json
            )
            reply_message: str = self.chat_service.conversation(messages=conversation_request.messages)

            response = ConversationResponse(
                reply=reply_message
            )
            return make_response(jsonify(response.model_dump()), 200)
        except Exception as exc:
            response = ApiResponse(
                    is_success=False,
                    failed_message=str(exc)
                )
            return make_response(jsonify(response.model_dump()), 502)
        
    def ask_law(self):
        """
        POST /chat/law - Ask about law
        """
        try:
            body = request.json
            ask_law_request = AskLawRequest.model_validate({
                "message": body.get("message")
            })
            print(f"Request: {body}")
            
            reply_message: str = self.chat_service.ask_law(message=ask_law_request.message)

            response = AskLawResponse(
                reply=reply_message
            )
            return make_response(jsonify(response.model_dump()), 200)
        except Exception as exc:
            response = ApiResponse(
                    is_success=False,
                    failed_message=str(exc)
                )
            return make_response(jsonify(response.model_dump()), 502)
 

    # LEGACY: DEPRECATED!!
    def _legacy_create_response(self, status, message, payload=None):
        return {
            "status": status,
            "message": message,
            "payload": payload
        }

    def legacy_conversation(self):
        try:
            body = request.json
            print(f"Request: {body}")
            result = self.chat_service.legacy_ask_law(messages=body.get("messages"))
            print(f"Result: {result}")
            return jsonify(self._legacy_create_response(status="success", message="received chat esponse", payload=result)), 200
        except Exception as exc:
            print(exc)
            return jsonify(self._legacy_create_response(status="operation error", message=str(exc))), 502