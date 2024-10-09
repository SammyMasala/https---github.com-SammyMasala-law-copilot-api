
from abc import ABC, abstractmethod
from flask import Blueprint, jsonify, request

from api.dtos import ApiResponse
from api.dtos.session_dtos import LoadSessionRequest, LoadSessionResponse, SaveSessionRequest, SaveSessionResponse
from api.entities.session_entities import Session
from api.services.session_service import SessionService

class ISessionBlueprint(ABC):
    @abstractmethod
    def load(self, id) -> LoadSessionResponse:
        pass

    @abstractmethod
    def save(self, id) -> SaveSessionResponse:
        pass

class SessionBlueprint(ISessionBlueprint):
    blueprint: Blueprint
    session_service: SessionService

    def __init__(self, session_service: SessionService):
        self.session_service = session_service

        self.blueprint = Blueprint(name="session", import_name="__name__", url_prefix="/session")

        self.blueprint.add_url_rule(rule="/<string:id>", methods=["GET"], view_func=self.load)
        self.blueprint.add_url_rule(rule="/<string:id>", methods=["PATCH"], view_func=self.save)

        # Legacy
        self.blueprint.add_url_rule(rule="/get-session", methods=["GET"], view_func=self.legacy_load)
        self.blueprint.add_url_rule(rule="/save-session", methods=["POST"], view_func=self.legacy_save)

    def get_blueprint(self):
        return self.blueprint
    

    def load(self, id):
        """
        GET /session/:id - Get Session
        """

        try:
            print(f"GET SESSION REQUEST: {id}")
            data = LoadSessionRequest.model_validate({
                "id": id
            })
            result: Session = self.session_service.get_session(id=data.id)

            if result is None:
                response = LoadSessionResponse.model_validate({
                    "is_success": False,
                    "failed_message": f"session {id} not found"
                })
                return jsonify(response.model_dump()), 404
            else:
                response = LoadSessionResponse.model_validate({
                    "is_success": True,
                    "session": result
                })
                return jsonify(response.model_dump()), 200
        except Exception as exc:
            response = ApiResponse.model_validate({
                    "is_success": False,
                    "failed_message": str(exc)
                })
            return jsonify(response.model_dump()), 502
        
    def save(self, id):
        """
        PATCH /session/:id - Save Session
        """
        try:
            body = request.json
            print(body)
            session = SaveSessionRequest.model_validate({
                "id": id,
                "session": body.get("session", "")
            })
            print(f"Request: {body}")
            
            result = self.session_service.update_session(session=session)

            response = SaveSessionResponse.model_validate({
                "is_success": True,
                "session": result
            })
            return jsonify(response.model_dump()), 200
        except Exception as exc:
            response = ApiResponse.model_validate({
                    "is_success": False,
                    "failed_message": str(exc)
                })
            return jsonify(response.model_dump()), 502
 

    # LEGACY: DEPRECATED!!
    def _legacy_create_response(self, status, message, payload=None):
        return {
            "status": status,
            "message": message,
            "payload": payload
        }

    def legacy_load(self):
        try:
            params = request.args
            print(f"Request: {params}")
            result = self.session_service.legacy_get_session(session_id=params.get("session_id"))
            print(f"Result: {result}")
            if result is None:
                return jsonify(self._legacy_create_response(status="not found", message="session was not found")), 404
            else:
                return jsonify(self._legacy_create_response(status="success", message="retrieved session", payload=result)), 200
        except Exception as exc:
            print(exc)
            return jsonify(self._legacy_create_response(status="operation error", message=str(exc))), 502
        
    def legacy_save(self):
        try:
            body = request.json
            print(f"Request: {body}")
            result = self.session_service.legacy_update_session(session=body.get("session"))
            print(f"Result: {result}")
            return jsonify(self._legacy_create_response(status="success", message="saved session", payload=result)), 200
        except Exception as exc:
            print(exc)
            return jsonify(self._legacy_create_response(status="operation error", message=str(exc))), 502
