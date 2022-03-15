# -*- coding: utf-8 -*-
"""
User service

Created by Allen Tao at 2022/1/12 5:05 PM
"""
from utils import repository
from models.role import Role
from context import use_db

db = use_db()


def create_one(name, description):
    """Create one role"""
    role = Role.query.filter_by(name=name).first()
    if role:
        return 1, 'Role already exists'
    else:
        return 0, repository.create_one(
            db,
            Role,
            {'name': name, 'description': description}
        ).to_vo()


def list_all():
    """List all"""
    return [r.to_vo() for r in repository.list_all(Role)]


def update_one(role_id, props):
    """Update one certain"""
    repeat = False
    role = Role.query.get(role_id)
    if 'name' in props and role.name != props['name']:
        repeat_role = Role.query.filter_by(name=props['name']).filter(Role.id.isnot(role_id)).first()
        if repeat_role:
            repeat = True

    if repeat:
        return 1, 'Role already exists'
    else:
        repository.update_one(db, Role, role_id, props)
        return 0, ''


def delete_many(role_ids):
    """Delete many roles"""
    repository.delete_many(db, Role, role_ids)
