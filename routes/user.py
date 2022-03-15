# -*- coding: utf-8 -*-
"""
User management

Created by Allen Tao at 2022/1/21 11:03 AM
"""
from flask import request, Blueprint
from flask import current_app as app
from utils.response import make_response
from services import user as user_service
from utils.permission import require_permission

blueprint = Blueprint('user', __name__, url_prefix='/user-management')


@blueprint.route('/user', methods=['POST'])
@require_permission('user:create')
def create_user():
    params = request.get_json()
    username, password = params['username'], params['password']
    code, res = user_service.create_one(username, password)
    return make_response(res, code), 201 if code == 0 else 200


@blueprint.route('/users', methods=['GET'])
@require_permission('user:retrieve')
def get_users():
    return make_response(user_service.list_all())


@blueprint.route('/user/<user_id>', methods=['PUT'])
@require_permission('user:update')
def update_user(user_id):
    code, res = user_service.update_one(user_id, request.get_json())
    return make_response(res, code)


@blueprint.route('/users', methods=['DELETE'])
@require_permission('user:delete')
def delete_users():
    user_service.delete_many(request.get_json()['ids'])
    return make_response(), 204


app.register_blueprint(blueprint)
