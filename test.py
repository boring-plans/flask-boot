# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/11/16.
"""
# - encrpyt
from tests import encrpyt
encrpyt.test_gen_salt()
encrpyt.test_gen_jwt()
encrpyt.test_verify_jwt('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                        '.eyJ1c2VyIjoidGVzdCIsImlkIjoiMTIzIiwiZXhwIjoxNjM3MDYxODA4fQ.hKxW4qkNN4uIWBkG4bRR4qThc731Pd'
                        '-OlfEecWyXmL8')
encrpyt.test_gen_password('123456', '9b4e4debbc5d54761600e2c702417235')

# - auth
from tests import auth
auth.test_sign_in()
