import re
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from api import init

app = Flask(__name__)
CORS(app=app, resources={r"/*": {"origins": [
    re.compile(r'https?://.*\.amazonaws\.com'), 
    re.compile(r'https?://.*\.learn-law-copilot\.net'),
    "http://localhost:8080"
    ]}})
blueprints = init()

app.register_blueprint(blueprints["session_bp"].get_blueprint())
app.register_blueprint(blueprints["chat_bp"].get_blueprint())

@app.route("/health-check/liveness", methods=["GET"])
def health_check():
    return make_response(jsonify(message="HEALTH OK!"), 200)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
