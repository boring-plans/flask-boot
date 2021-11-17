# -*- coding: utf-8 -*-
"""
Table user.

by kang1.tao,
on 2021/6/11.
"""
from models import user_role
from context import use_db
from flask import jsonify

db = use_db()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))
    salt = db.Column(db.String(64))
    roles = db.relationship('Role', secondary=user_role, lazy='subquery', backref=db.backref('users', lazy=True))

    def to_vo(self):
        return jsonify({
            'id': self.id,
            'username': self.username,
            'roles': self.roles
        })
