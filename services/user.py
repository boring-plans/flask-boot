# -*- coding: utf-8 -*-
"""
API associated with authorization and authentication.

by kang1.tao,
on 2021/6/11.
"""
from models.user import User
from utils.encrypt import gen_password, gen_jwt


def sign_in(username: str, password: str) -> dict or str:
    """Sign in
    :param username: username
    :param password: md5(plain password)
    :return: a jwt or error message
    """
    user = User.query.filter_by(username=username).first()
    if user:
        if gen_password(password, user.salt) != user.password:
            return '密码错误'
        else:
            return gen_jwt(user.to_vo())
    else:
        return '用户不存在！'
