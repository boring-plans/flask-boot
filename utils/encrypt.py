# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/11/16.
"""
# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/6/11.
"""
import hashlib
import random
import jwt
from datetime import datetime, timedelta
from context import use_conf

conf = use_conf()


def md5_encrypt(string) -> str:
    """Encrypt string passed in with md5 algorithm
    :param string: src
    :return: dist
    """
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def sha1_encrypt(string) -> str:
    """Encrypt string passed in with sha-1 algorithm
    :param string: src
    :return: dist
    """
    return hashlib.sha1(string.encode('utf-8')).hexdigest()


def gen_salt() -> str:
    """Generate salt randomly
    :return: salt
    """
    return md5_encrypt(''.join([chr(random.randint(48, 122)) for i in range(32)]))  # 0 - z


def gen_jwt(payload=None, expiry: int = int((datetime.now() + timedelta(hours=3)).timestamp())) -> str:
    """Generate jwt
    :param payload: payload
    :param expiry: the last moment when token is valid
    :return: jwt
    """
    if payload is None:
        payload = {}
    secret = conf['auth']['jwt_secret']
    token = jwt.encode({**payload, 'exp': expiry}, secret, algorithm='HS256')
    return token


def verify_jwt(token) -> str or dict:
    """Verify jwt
    :param token: jwt
    :return: eg. {'name': 'foo', 'id': 1}, 'out of date', 'invalid'
    """
    try:
        secret = conf['auth']['jwt_secret']
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'out of date'
    except jwt.InvalidTokenError:
        return 'invalid'


def gen_password(password_md5, salt) -> str:
    """
    Generate password with salt and ma5(plain password)
    :param salt: salt
    :param password_md5: md5(plain password)
    :return: password will be saved in db
    """
    return sha1_encrypt(password_md5+salt)
