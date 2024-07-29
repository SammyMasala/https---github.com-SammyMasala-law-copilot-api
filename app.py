from flask import Flask, jsonify, make_response, request
from api.init import init
from api.libs.parse_http import parse_http_get
from api.services.session_service import SessionService

app = Flask(__name__)
init = init()

session_service: SessionService = init["session_repository"]

def create_response(status, message, session=None):
    return {
        "status": status,
        "message": message,
        "payload": session
    }

@app.route('/session/get-session', methods=["GET"])
def get_session():
    try:
        body = parse_http_get(request)
        print(f"Request: {body}")
        result = session_service.get_session()
        item = result.get('Item')
        if not item:
            return jsonify(create_response(status="not found", message="session was not found")), 404
    except Exception as exc:
        print(exc)
        return jsonify(create_response(status="operation error", message=exc)), 502

@app.route("health-check/liveness", methods=["GET"])
def health_check():
    return jsonify(create_response(status="success", message="ALL GOOD!")), 200

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
