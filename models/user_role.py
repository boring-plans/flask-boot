# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/6/11.
"""
from context import use_db

db = use_db()


class UserRole(db.Model):
    __tablename__ = 'user_role'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)
