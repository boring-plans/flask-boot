# -*- coding: utf-8 -*-
"""
Import app from context,
which can be run directly or by 'gunicorn'

Created by Allen Tao at 2022/1/12 5:06 PM
"""
from context import use_app

app = use_app()

# register models and routes
with app.app_context():
    from models import register_all as register_models
    from routes import register_all as register_routes
    register_models()
    register_routes()

if __name__ == '__main__':
    from context import use_db
    use_db().create_all()
    from services.user import create_admin
    create_admin()

    from utils.common import get_env
    (get_env() == 'dev') and app.run()
