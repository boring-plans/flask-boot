# -*- coding: utf-8 -*-
"""
Auth related

Created by Allen Tao at 2022/1/12 5:05 PM
"""
from flask import request, Blueprint, g
from utils.response import make_response
from flask import current_app as app
from services import auth as auth_service

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/token', methods=['GET'])
def get_token():
    """Signing-in is actually to fetch a token, in RESTful concept,
    so return a token
    """
    username, password = request.args['username'], request.args['password']
    code, res = auth_service.sign_in(username, password)
    return make_response(res, code)


@blueprint.route('/user', methods=['POST'])
def register_user():
    """Register one user"""
    params = request.get_json()
    username, password = params['username'], params['password']
    code, res = auth_service.sign_up(username, password)
    return make_response(res, code), 201 if code == 0 else 200


@blueprint.route('/permissions', methods=['GET'])
def get_permissions():
    """Get all accessible permissions"""
    return make_response(auth_service.get_all_permissions())


@blueprint.route('/user-info', methods=['GET'])
def get_user_info():
    """Get info of user signed in"""
    return make_response(g.current_user['username'])


app.register_blueprint(blueprint)
