# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/11/16.
"""
from utils.encrypt import gen_password, md5_encrypt


def test_sign_in():
    assert gen_password(md5_encrypt('123456'), '9b4e4debbc5d54761600e2c702417235') == \
        'e8637949388ce977ed52ee63ba71b71bb6c01f7a'
