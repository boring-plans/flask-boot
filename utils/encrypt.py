# -*- coding: utf-8 -*-
"""
Created by Allen Tao at 2022/1/12 5:06 PM
"""
import jwt
from datetime import datetime, timedelta
from utils.common import get_conf


def gen_jwt(payload=None, expiry=None) -> str:
    """Generate jwt"""
    if payload is None:
        payload = {}
    if expiry is None:
        expiry = (datetime.now() + timedelta(hours=3)).timestamp()
    conf = get_conf('app')
    secret = conf['jwt_secret']
    token = jwt.encode({**payload, 'exp': expiry}, secret, algorithm='HS256')
    return token


def verify_jwt(token) -> str or dict:
    """Verify jwt"""
    try:
        conf = get_conf('app')
        secret = conf['jwt_secret']
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Out of date'
    except jwt.InvalidTokenError:
        return 'Invalid'
