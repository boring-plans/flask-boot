"""
By Qingqiu
On 2022-02-07
"""
from flask import request, Blueprint
from flask import current_app as app
from utils.permission import decorator_test

blueprint = Blueprint('test', __name__, url_prefix='/test')


@blueprint.route('/auth_decorator_test/<id>', methods=['GET'])
@decorator_test(['user:retrieve', 'user:update'])
def test_decorator(id):
    print(id, request.args['test'])
    return 'success'


app.register_blueprint(blueprint)
