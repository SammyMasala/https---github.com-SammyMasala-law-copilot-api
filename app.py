import re
from flask import Flask, jsonify, make_response, request
from api.init import init
from api.libs.parse_http import parse_http_get, parse_http_post
from api.services.chat_service import ChatService
from api.services.session_service import SessionService
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app, resources={r"/*": {"origins": [re.compile(r'https?://.*\.amazonaws\.com'), "http://localhost:8080"]}})
init = init()

session_service: SessionService = init["session_service"]
chat_service: ChatService = init["chat_service"]

def create_response(status, message, payload=None):
    return {
        "status": status,
        "message": message,
        "payload": payload
    }

@app.route('/session/get-session', methods=["GET"])
def get_session():
    try:
        params = parse_http_get(request)
        print(f"Request: {params}")
        result = session_service.get_session(session_id=params.get("session_id"))
        print(f"Result: {result}")
        item = result.get('Item')
        if not item:
            return jsonify(create_response(status="not found", message="session was not found")), 404
        else:
            return jsonify(create_response(status="success", message="retrieved session", payload=result)), 200
    except Exception as exc:
        print(exc)
        return jsonify(create_response(status="operation error", message=str(exc))), 502
    
@app.route('/session/save-session', methods=["POST"])
def save_session():
    try:
        body = parse_http_post(request)
        print(f"Request: {body}")
        result = session_service.put_session(session=body.get("session"))
        print(f"Result: {result}")
        return jsonify(create_response(status="success", message="session saved", payload=result)), 200
    except Exception as exc:
        print(exc)
        return jsonify(create_response(status="operation error", message=str(exc))), 502

@app.route('/chat/conversation', methods=["POST"])
def chat_conversation():
    try:
        body = parse_http_post(request)
        print(f"Request: {body}")
        result = chat_service.chat_completion(messages=body.get("messages"))
        print(f"Result: {result}")
        return jsonify(create_response(status="success", message="received chat esponse", payload=result)), 200
    except Exception as exc:
        print(exc)
        return jsonify(create_response(status="operation error", message=str(exc))), 502

@app.route("/health-check/liveness", methods=["GET"])
def health_check():
    return jsonify(create_response(status="success", message="ALL GOOD!")), 200

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
