# -*- coding: utf-8 -*-
"""
Table role.

by kang1.tao,
on 2021/6/11.
"""
from context import use_db

db = use_db()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(40))
