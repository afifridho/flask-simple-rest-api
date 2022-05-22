from flask import request, jsonify
from app import app
import pendulum

from .const import HttpStatus
from .const import Core

now = pendulum.now(tz=Core.Timezone)

@app.route('/', methods=['GET'])
def home():
    construct = {
        'success': True,
        'message': 'Welcome to simple flask REST API'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.OK
    return response

@app.route('/ping', methods=['GET'])
def ping():
    construct = {
        'success': True,
        'message': 'ok'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.OK
    return response

@app.route('/datetime', methods=['GET'])
def datetime():
    construct = {
        'success': True,
        'message': now.to_cookie_string()
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.OK
    return response