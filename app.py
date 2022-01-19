# -*- coding: utf-8 -*-
"""
Register routes,
 and declare models,
 and provide the instance of flask app,
 which can be run directly or by 'gunicorn'

Created by Kang Tao at 2022/1/12 5:06 PM
"""
from context import use_app, use_db


# app
app = use_app()

# db & routes
from models import *
from routes import *


if __name__ == '__main__':
    # initializing
    use_db().create_all()
    from services.user import create_admin
    create_admin()

    from utils.common import get_env
    if get_env() == 'dev':
        app.run()


