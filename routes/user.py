# -*- coding: utf-8 -*-
"""
User management

Created by Kang Tao at 2022/1/21 11:03 AM
"""
from flask import request, Blueprint
from utils.response import make_response
from context import use_app
from services import user as user_service
from utils.permission import permission

blueprint = Blueprint('user', __name__, url_prefix='/user-management')


@permission(['user:create'])
@blueprint.route('/user', method=['POST'])
def create_user():
    username, password = request.args['username'], request.args['password']
    user_service.create_one(username, password)
    return make_response(), 201


@blueprint.route('/users', method=['GET'])
def get_users():
    return make_response(user_service.list_all())


@blueprint.route('/user/<user_id>', method=['PUT'])
def update_user(user_id):
    user_service.update_one(user_id, request.get_json())
    return make_response()


@blueprint.route('/user/<user_id>/status', method=['PATCH'])
def update_user_status(user_id):
    user_service.update_one(user_id, request.get_json())
    return make_response()


use_app().register_blueprint(blueprint)
