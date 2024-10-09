from flask import Flask, jsonify, make_response, request
from api.init import init
from api.services.chat_service import ChatService

app = Flask(__name__)
init = init()

app.register_blueprint(init["session_bp"].get_blueprint())

chat_service: ChatService = init["chat_service"]

def create_response(status, message, payload=None):
    return {
        "status": status,
        "message": message,
        "payload": payload
    }

@app.route('/chat/conversation', methods=["POST"])
def chat_conversation():
    try:
        body = request.json
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
