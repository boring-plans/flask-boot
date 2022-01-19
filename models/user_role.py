# -*- coding: utf-8 -*-
"""
User <-> Role

Created by Kang Tao at 2022/1/17 6:27 PM
"""
from context import use_db

db = use_db()


user_role = db.Table(
    'user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)
