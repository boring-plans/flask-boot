# -*- coding: utf-8 -*-
"""
Configure app and run.

by kang1.tao,
on 2021/6/10.
"""
import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from context import use_app, use_db, use_conf, use_env
from utils.guard import before_request

app = use_app()
db = use_db()
conf = use_conf()
env = use_env()

# configure app
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
app.config['SQLALCHEMY_POOL_SIZE'] = conf['db']['pool_size']
app.config['SQLALCHEMY_MAX_OVERFLOW'] = conf['db']['max_overflow']
app.config['SQLALCHEMY_POOL_RECYCLE'] = conf['db']['pool_recycle']
app.config['SQLALCHEMY_DATABASE_URI'] = conf['db']['dev_uri' if env == 'dev' else 'prod_uri']

root_path = Path(os.path.dirname(os.path.abspath(__file__)))
(root_path / conf['app']['static_folder']).mkdir(exist_ok=True)
(root_path / 'logs').mkdir(exist_ok=True)
logger_handler = TimedRotatingFileHandler(
    filename='logs/' + datetime.now().strftime('%Y-%m-%d') + '.flask_boot.log',
    when='D', interval=1, backupCount=15,
    encoding='UTF-8',
    delay=False)
logger_handler.setFormatter(
    logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)d] - [%(levelname)s] - %(message)s'))
app.logger.addHandler(logger_handler)
app.before_request(before_request)

# db initialization
from models import *
db.create_all()

# register routes
from routes import *

if __name__ == '__main__':
    app.run()
