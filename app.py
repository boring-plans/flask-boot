# -*- coding: utf-8 -*-
"""
Configure app and run.

by kang1.tao,
on 2021/6/10.
"""
from context import use_app, use_db

app = use_app()
db = use_db()

from models import *
db.create_all()

from routes import *

if __name__ == '__main__':
    app.run()
