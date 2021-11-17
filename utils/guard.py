# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/11/17.
"""
from flask import request, g, make_response

from context import use_conf, use_app
from utils.encrypt import verify_jwt


def is_white(path: str, white_list: list[str]):
    for w in white_list:
        if path.startswith(w):
            return True
    return False


def before_request():
    """Before request
        - logging
        - auth validating
    :return:
    """
    app = use_app()
    conf = use_conf()
    app.logger.info('[E]..' + request.path)
    if is_white(request.path, conf['app']['public_routes'].split(',')):
        app.logger.info('This is a public route.')
        return
    else:
        token = request.headers.get(conf['app']['auth_token_key'])
        if token:
            # 首先校验 jwt 有效性
            res = verify_jwt(token)
            if type(res) == str:
                app.logger.info('Invalid token' + res)
                return make_response(res, 400)
            else:
                app.logger.info('current_user:')
                app.logger.info(res)
                g.current_user = res
                return
        else:
            app.logger.info('Unauthorized')
            return make_response('Unauthorized', 401)
