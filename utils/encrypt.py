# -*- coding: utf-8 -*-
"""
Created by Kang Tao at 2022/1/12 5:06 PM
"""
import hashlib
import random
import jwt
from datetime import datetime, timedelta
from utils.common import get_conf


def md5_encrypt(string) -> str:
    """Encrypt string passed in with md5 algorithm"""
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def sha1_encrypt(string) -> str:
    """Encrypt string passed in with sha-1 algorithm"""
    return hashlib.sha1(string.encode('utf-8')).hexdigest()


def gen_salt() -> str:
    """Generate salt randomly"""
    return md5_encrypt(''.join([chr(random.randint(48, 122)) for i in range(32)]))  # 0 - z


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


def gen_password(password_md5, salt) -> str:
    """Generate password with salt and ma5(plain password)"""
    return sha1_encrypt(password_md5+salt)
