# -*- coding: utf-8 -*-
"""
Functions used to control permissions

Created by Kang Tao at 2022/1/12 5:06 PM
"""
from flask import request, g, make_response
from utils.encrypt import verify_jwt, gen_jwt
from datetime import datetime, timedelta


def guard_route(app):
    """Before request"""
    def is_white(path: str):
        white_list = ['/auth', '/static']
        for w in white_list:
            if path.startswith(w):
                return True
        return False

    def before_request():
        app.logger.info('[E]..' + request.path)
        if is_white(request.path):
            app.logger.info('This is a public route.')
            return
        else:
            token = request.headers.get('Authorization')
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
                app.logger.info('Unauthorized')
                return make_response('Unauthorized', 401)

    def after_request(response):
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

    app.before_request(before_request)
    app.after_request(after_request)


def permission(permissions):
    """Decorator used to check permissions"""
    def decorator(fn):
        from services.auth import get_all_permissions
        permissions_owned = get_all_permissions()['permissions']
        if permissions_owned == 'ALL' or any([p.value in permissions_owned for p in permissions]):
            return fn
        else:
            return lambda *args: make_response('Permission denied', 403)
    return decorator
