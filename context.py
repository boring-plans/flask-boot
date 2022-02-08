# -*- coding: utf-8 -*-
"""
Create and configure instance of Flask and SqlAlchemy,
which compose a context that whole _app works in

Created by Kang Tao at 2022/1/12 5:06 PM
"""
import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.common import get_conf, get_env
from utils.permission import bind_authentication_checker

_app = _db = None


def use_app():
    global _app
    if _app is None:
        _app = Flask(__name__)

        # db
        conf = get_conf('db')
        _app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
        _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to dismiss warning
        _app.config['SQLALCHEMY_POOL_SIZE'] = int(conf['pool_size'])
        _app.config['SQLALCHEMY_MAX_OVERFLOW'] = int(conf['max_overflow'])
        _app.config['SQLALCHEMY_POOL_RECYCLE'] = int(conf['pool_recycle'])
        _app.config['SQLALCHEMY_DATABASE_URI'] = conf[f'{get_env()}_uri']

        # logging
        from pathlib import Path
        app_root = Path(__file__).parent
        (app_root / 'static').mkdir(exist_ok=True)
        (app_root / 'logs').mkdir(exist_ok=True)
        logger_handler = TimedRotatingFileHandler(
            filename=app_root / 'logs' / (datetime.now().strftime('%Y-%m-%d') + '.flask_boot.log'),
            when='D', interval=1, backupCount=15,
            encoding='UTF-8',
            delay=False)
        logger_handler.setFormatter(
            logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)d] - [%(levelname)s] - %(message)s'))
        _app.logger.addHandler(logger_handler)

        # authentication checker
        bind_authentication_checker(_app)
    return _app


def use_db():
    global _db
    if _db is None:
        _db = SQLAlchemy(use_app())

    return _db
