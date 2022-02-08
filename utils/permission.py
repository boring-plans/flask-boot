# -*- coding: utf-8 -*-
"""
Functions used to control permissions

Created by Kang Tao at 2022/1/12 5:06 PM
"""
from flask import request, g, make_response
from utils.encrypt import verify_jwt, gen_jwt
from datetime import datetime, timedelta
from functools import wraps


def bind_authentication_checker(app):
    """Bind authentication checker"""

    def is_white(path: str):
        white_list = ['/auth', '/static', '/test']
        for w in white_list:
            if path.startswith(w):
                return True
        return False

    def before_checker():
        app.logger.info('[E]..' + request.path)
        if is_white(request.path):
            app.logger.info('This is a public route.')
            return
        else:
            token = request.headers.get('x-access-token')
            if token:
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
                app.logger.info('Unauthenticated')
                return make_response('Unauthorized', 401)

    def after_checker(response):
        """Token updating"""
        app.logger.info('[X]..' + request.path)
        if response.status == 200:
            payload = verify_jwt(request.headers.get('Authorization'))
            valid_delta = datetime.fromtimestamp(payload['exp']) - datetime.now()
            if valid_delta <= timedelta(minutes=5):
                del payload['exp']
                new_token = gen_jwt(payload)
                response.data['token'] = new_token
                return make_response(response.data, 210)
        return response

    app.before_request(before_checker)
    app.after_request(after_checker)


def require_permission(permission):
    """Decorator used to check authorization"""
    def extend_fn(fn):
        @wraps(fn)
        def extended(**kwargs):
            from services.auth import get_all_permissions
            permissions = get_all_permissions()
            if permissions == '*' or permission in permissions:
                return fn(**kwargs)
            else:
                return make_response('Permission denied', 403)

        return extended

    return extend_fn


def decorator_test(test_list):
    def extend_fn(fn):
        def extended(**kwargs):
            print(kwargs)
            if not ('user:create' in test_list):
                return make_response('Permission denied', 403)
            else:
                return fn(**kwargs)
        return extended
    return extend_fn
