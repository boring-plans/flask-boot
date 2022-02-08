# -*- coding: utf-8 -*-
"""
User management

Created by Kang Tao at 2022/1/21 11:03 AM
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
    username, password = request.args['username'], request.args['password']
    user_service.create_one(username, password)
    return make_response(), 201


@blueprint.route('/users', methods=['GET'])
@require_permission('user:retrieve')
def get_users():
    return make_response(user_service.list_all())


@blueprint.route('/user/<user_id>', methods=['PUT'])
@require_permission('user:update')
def update_user(user_id):
    user_service.update_one(user_id, request.get_json())
    return make_response()


@blueprint.route('/user/<user_id>/status', methods=['PATCH'])
@require_permission('user:update')
def update_user_status(user_id):
    user_service.update_one(user_id, request.get_json())
    return make_response()


app.register_blueprint(blueprint)
