# -*- coding: utf-8 -*-
"""
User service

Created by Kang Tao at 2022/1/12 5:05 PM
"""
from utils import repository
from models.user import User
from utils.encrypt import gen_password, gen_salt
from context import use_db
from utils.common import get_conf

db = use_db()


def create_one(username, password, is_admin=False):
    """Create one user"""
    salt = gen_salt()
    return repository.create_one(
        db,
        User,
        {'username': username, 'password': gen_password(password, salt), 'salt': salt, 'is_admin': is_admin}
    )


def create_admin():
    """Create one special user named Admin"""
    admin = User.query.filter(User.is_admin.is_(True)).first()
    if not admin:
        create_one('Admin', get_conf('app')['admin_password'], is_admin=True)


def list_all():
    """List all"""
    return repository.list_all(User)


def update_one(user_id, props):
    """Update one certain"""
    repository.update_one(db, User, user_id, props)


def delete_many(user_ids):
    """Delete many users"""
    repository.delete_many(db, User, user_ids)
