# -*- coding: utf-8 -*-
"""
Auth related APIs

Created by Kang Tao at 2022/1/12 5:05 PM
"""
from flask import request, Blueprint
from utils.response import make_response
from context import use_app
from services import auth as auth_service

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/token', methods=['GET'])
def get_token():
    """Signing-in is actually to fetch a token, in RESTful concept,
    So return a token
    """
    username, password = request.args['username'], request.args['password']
    captcha, captcha_key = request.args['captcha'], request.args['captchaKey']
    code, res = auth_service.sign_in(username, password, captcha_key, captcha)
    return make_response(res, code)


@blueprint.route('/captcha', methods=['GET'])
def get_captcha():
    """Get a captcha with a random key"""
    captcha_key = request.args['captchaKey']
    return make_response(auth_service.get_captcha(captcha_key))


@blueprint.route('/user', methods=['POST'])
def register_user():
    """Register one user"""
    params = request.get_json()
    username, password = params['username'], params['password']
    captcha, captcha_key = params['captcha'], params['captchaKey']
    code, res = auth_service.sign_up(username, password, captcha_key, captcha)
    return make_response(res, code), 201 if code == 0 else 200


@blueprint.route('/permissions', methods=['GET'])
def get_permissions():
    """Get all accessible menus and permissions"""
    return make_response(auth_service.get_all_permissions())


use_app().register_blueprint(blueprint)
