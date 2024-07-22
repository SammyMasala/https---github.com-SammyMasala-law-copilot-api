import os

from flask import Flask, jsonify, make_response, request

from api import init
from api.libs.parse_http import parse_http_get, parse_http_post
from api.services.session_service import SessionService

app = Flask(__name__)

session_service: SessionService = init().session_service

@app.route('/session/<string:session_id>', methods=["GET"])
def get_session(session_id):
    try:
        print("Session id: ", session_id)
        result = session_service.get_session(session_id=session_id)
        print(result)
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
        print(request)
        body = parse_http_post(request)
        session_service.put_session(session=body.get("session"))
        return jsonify(result="success"),200
    except Exception as exc:
        print(exc)
        return jsonify(
            {'result': 'Server Exception'}
        ), 502


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(result='Not found!'), 404)
