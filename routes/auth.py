# -*- coding: utf-8 -*-
"""
API associated with authorization and authentication.

by kang1.tao,
on 2021/6/10.
"""
from flask import request, Blueprint, Response
from utils.response import positive, negative
from context import use_app
from services import user

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')
app = use_app()
app.register_blueprint(auth_blueprint)


@auth_blueprint.route('/token', methods=['GET'])
def get_token() -> Response:
    """Signing-in is actually to fetch a token in REST-ful concept
    :return: so return a token
    """
    username, password = request.args['username'], request.args['password']
    res = user.sign_in(username, password)
    if type(res) == str:
        return negative(res)
    else:
        return positive(res)
