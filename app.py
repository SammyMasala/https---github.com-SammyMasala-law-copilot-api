import os

from flask import Flask, jsonify, make_response, request

from api.init import init
from api.libs.parse_http import parse_http_get, parse_http_post
from api.services.chat_service import ChatService
from api.services.session_service import SessionService

app = Flask(__name__)

init = init()
session_service: SessionService = init["session_service"]
chat_service: ChatService = init["chat_service"]

@app.route('/session', methods=["GET"])
def get_session():
    try:
        params = parse_http_get(request=request)
        print(params)
        result = session_service.get_session(session_id=params.get("session_id"))
        if not result:
            return jsonify({'result': 'session not found', 'session': None}), 404    
        else:
            return jsonify({'result': 'successful', 'session': result}), 200   
    except Exception as exc:
        print(exc)
        return jsonify(
            {'result': 'Server Exception',
             'session': None}
        ), 502

@app.route('/session/save-session', methods=['POST'])
def put_session():
    try: 
        print(request.json)
        body = parse_http_post(request)
        session_service.put_session(session=body.get("session"))
        return jsonify(result="success"),200
    except Exception as exc:
        print(exc)
        return jsonify(
            {'result': 'Server Exception'}
        ), 502
    
@app.route('/chat/conversation', methods=['POST'])
def post_conversation():
    try: 
        body = parse_http_post(request)
        print(f"Request: {body}")
        reply = chat_service.send_message(messages=body.get("messages"))
        print(f"Response: {reply}")
        return jsonify({"result":"success", "reply": reply}),200
    except Exception as exc:
        print(exc)
        return jsonify(
            {'result': 'Server Exception', 'reply': {}}
        ), 502

@app.route("/health-check/liveness", methods=["GET"])
def health_check():
    return jsonify(status="ALL GOOD!")

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(result='Not found!'), 404)

