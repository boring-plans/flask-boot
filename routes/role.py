# -*- coding: utf-8 -*-
"""
Role management

Created by Allen Tao at 2022/3/14 2:44 PM
"""
from flask import request, Blueprint
from flask import current_app as app
from utils.response import make_response
from services import role as role_service
from utils.permission import require_permission

blueprint = Blueprint('role', __name__, url_prefix='/role-management')


@blueprint.route('/role', methods=['POST'])
@require_permission('role:create')
def create_role():
    params = request.get_json()
    name, description = params['name'], params['description']
    code, res = role_service.create_one(name, description)
    return make_response(res, code), 201 if code == 0 else 200


@blueprint.route('/roles', methods=['GET'])
@require_permission('role:retrieve')
def get_roles():
    return make_response(role_service.list_all())


@blueprint.route('/role/<role_id>', methods=['PUT'])
@require_permission('role:update')
def update_role(role_id):
    code, res = role_service.update_one(role_id, request.get_json())
    return make_response(res, code)


@blueprint.route('/roles', methods=['DELETE'])
@require_permission('role:delete')
def delete_roles():
    role_service.delete_many(request.get_json()['ids'])
    return make_response(), 204


app.register_blueprint(blueprint)
