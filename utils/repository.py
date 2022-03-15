# -*- coding: utf-8 -*-
"""
Model Repository

Created by Allen Tao at 2022/1/17 6:48 PM
"""


def mo_to_vo(mo):
    """Convert model object to view object"""
    vo = {}
    for key in mo.__mapper__.c.keys():
        vo[key] = getattr(mo, key)
    return vo


def create_one(db, model, props):
    """Create one"""
    one = model(**props)
    db.session.add(one)
    db.session.commit()
    return one


def update_one(db, model, one_id, props):
    """Update one"""
    one = model.query.get(one_id)
    for key, value in props.items():
        setattr(one, key, value)
    db.session.commit()


def find_one(model, one_id):
    """Find one"""
    return model.query.get(one_id)


def find_one_by(model, prop_name, prop_value):
    """Find one by a certain prop"""
    return model.query.filter_by(**{prop_name: prop_value}).first()


def find_many(model, many_ids):
    """Find many"""
    return model.query.filter(model.id.in_(many_ids)).all()


def find_many_by(model, prop_name, prop_value):
    """Find many by a certain prop"""
    return model.query.filter_by(**{prop_name: prop_value}).all()


def list_all(model):
    """List all"""
    return model.query.all()


def delete_one(db, model, one_id):
    """Delete one"""
    model.query.get(one_id).delete()
    db.session.commit()


def delete_many(db, model, many_ids):
    """Delete many"""
    model.query.filter(model.id.in_(many_ids)).delete()
    db.session.commit()

