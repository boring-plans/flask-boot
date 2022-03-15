# -*- coding: utf-8 -*-
"""
Authorization and Authentication

Created by Allen Tao at 2022/1/18 12:22 PM
"""
from functools import reduce
from flask import g
from models.user import User
from utils.encrypt import gen_jwt
from services import user as user_service


def sign_up(username, password):
    """Sign up"""
    user = User.query.filter_by(username=username).first()
    if user:
        return 1, 'User already exists'
    else:
        user_service.create_one(username, password)
        _, token = sign_in(username, password)
        return 0, token


def sign_in(username, password):
    """Sign in"""
    user = User.query.filter_by(username=username).first()
    if user:
        if user.state == 1:
            if password == user.password:
                return 0, gen_jwt({'id': user.id, 'username': username})
            else:
                return 1, 'Wrong password'
        else:
            # frozen or soft deleted and so on
            return 2, 'User has been frozen'
    else:
        return 3, 'User not found'


def get_all_permissions():
    """Get all permissions that current user owns"""
    user = User.query.get(g.current_user['id'])
    permissions = []
    if user:
        if user.is_admin:
            permissions = '*'
        else:
            permissions = reduce(lambda pre, curr: [*pre, *curr.permissions.split(',')], user.roles, [])

    return permissions

