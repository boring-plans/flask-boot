# -*- coding: utf-8 -*-
"""
User service

Created by Allen Tao at 2022/1/12 5:05 PM
"""
from utils import repository
from models.user import User
from models.role import Role
from context import use_db
from utils.common import get_conf

db = use_db()


def create_one(username, password, is_admin=False):
    """Create one user"""
    user = User.query.filter_by(username=username).first()
    if user:
        return 1, 'User already exists'
    else:
        return 0, repository.create_one(
            db,
            User,
            {'username': username, 'password': password, 'is_admin': is_admin}
        ).to_vo()


def create_admin():
    """Create one special user named Admin"""
    admin = User.query.filter(User.is_admin.is_(True)).first()
    if not admin:
        create_one('Admin', get_conf('app')['admin_password'], is_admin=True)


def list_all():
    """List all"""
    return [u.to_vo() for u in filter(lambda x: not x.is_admin, repository.list_all(User))]


def update_one(user_id, props):
    """Update one certain"""
    repeat = False
    user = User.query.get(user_id)
    if 'username' in props and user.username != props['username']:
        repeat_user = User.query.filter_by(username=props['username']).filter(User.id.isnot(user_id)).first()
        if repeat_user:
            repeat = True
    if repeat:
        return 1, 'User already exists'
    else:
        direct_props = {**props}
        if 'roles' in direct_props:
            del direct_props['roles']
            roles = Role.query.filter(Role.id.in_(props['roles'])).all()
            user.roles = roles
            db.session.commit()
        repository.update_one(db, User, user_id, direct_props)
        return 0, ''


def delete_many(user_ids):
    """Delete many users"""
    repository.delete_many(db, User, user_ids)
