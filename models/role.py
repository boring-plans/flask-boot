# -*- coding: utf-8 -*-
"""
Model role

Created by Kang Tao at 2022/1/12 5:04 PM
"""
from context import use_db

db = use_db()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(128))
    menus = db.Column(db.String(1024))
    permissions = db.Column(db.String(1024))

    def to_vo(self):
        from utils.repository import mo_to_vo
        return mo_to_vo(self)
