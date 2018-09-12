from app import app
from flask import jsonify, request, abort, make_response
from requests import put, get, post, delete

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'

@app.route('/organizations')
def organizations():
    r = get('http://localhost:5000/api/v1/organizations').json()
    return r[0]['Org_Id']
