# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/11/16.
"""
from utils import encrypt


def test_gen_salt():
    print(encrypt.gen_salt())


def test_gen_jwt():
    print(encrypt.gen_jwt({'user': 'test', 'id': '123'}))


def test_verify_jwt(token):
    print(encrypt.verify_jwt(token))


def test_gen_password(password, salt):
    print(encrypt.gen_password(encrypt.md5_encrypt(password), salt))
