from flask import request, make_response, jsonify
from app import app
from controller import handle_new_visitor, get_visitor_welcome_back_message, get_app_version

@app.route('/')
def index():
    visitor_id = request.cookies.get('visitor_id')
    if not visitor_id:
        response, visitor_id = handle_new_visitor()
    else:
        response = get_visitor_welcome_back_message(visitor_id)

    resp = make_response(response)
    resp.set_cookie('visitor_id', visitor_id, max_age=365*24*60*60)  # Cookie expires in one year
    return resp

@app.route('/version')
def version():
    return jsonify(get_app_version())
