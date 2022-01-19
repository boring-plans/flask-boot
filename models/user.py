# -*- coding: utf-8 -*-
"""
Model User

Created by Kang Tao at 2022/1/12 5:04 PM
"""
from context import use_db
from models.user_role import user_role

db = use_db()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))
    salt = db.Column(db.String(64))
    is_admin = db.Column(db.Boolean)
    roles = db.relationship('Role', secondary=user_role, backref=db.backref('users'))

    def to_vo(self):
        from utils.repository import mo_to_vo
        vo = mo_to_vo(self)
        vo.pop('is_admin')
        vo['roles'] = [role.to_vo() for role in self.roles]
        return vo
