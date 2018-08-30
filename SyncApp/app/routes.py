from app import app
from flask import jsonify, request, abort, make_response

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'
