# -*- coding: utf-8 -*-
"""
Authorization and Authentication

Created by Kang Tao at 2022/1/18 12:22 PM
"""
from functools import reduce
from flask import g
from models.user import User
from utils.encrypt import gen_jwt, gen_password
from utils.captcha_util import gen_captcha
from utils.redis_util import set_redis_value, get_redis_value
from services import user as user_service


def sign_up(username, password, captcha_key, captcha):
    """Sign up"""
    valid = validate_captcha(captcha_key, captcha)
    if valid:
        user_service.create_one(username, password)
        _, token = sign_in(username, password, captcha, captcha_key)
        return 0, token
    else:
        return 1, 'Wrong captcha'


def sign_in(username, password, captcha_key, captcha):
    """Sign in"""
    valid = validate_captcha(captcha_key, captcha)
    if valid:
        user = User.query.filter_by(username=username).first()
        if user:
            if gen_password(password, user.salt) != user.password:
                return 1, 'Wrong password'
            else:
                return 0, gen_jwt({'id': user.id})
        else:
            return 2, 'User not found'
    else:
        return 3, 'Wrong captcha'


def get_all_permissions():
    """Get all permissions that current user owns"""
    user = User.query.get(g.current_user['id'])
    permissions = {'menus': [], 'permissions': []}
    if user:
        if user.is_admin:
            permissions = {'menus': 'ALL', 'permissions': 'ALL'}
        else:
            permissions = reduce(
                lambda pre, curr: {
                    'menus': [*{*curr.menus.split(','), *pre["menus"]}],
                    'permissions': [*{*curr.menus.split(','), *pre["permissions"]}]
                }, user.roles, permissions)

    return permissions


def get_captcha(random_key):
    """Get a random captcha with a random key"""
    captcha_str, captcha = gen_captcha()
    set_redis_value(f'captcha-key-{random_key}', captcha_str)
    return captcha


def validate_captcha(random_key, captcha_str):
    """To validate the captcha_str"""
    saved_str = get_redis_value(f'captcha-key-{random_key}')
    return saved_str == captcha_str

