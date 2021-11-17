# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/11/13.
"""
import configparser
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

env = conf = app = db = None


def use_env():
    global env
    if not env:
        env = os.environ['ENV']
    return env


def use_conf():
    global conf
    if not conf:
        conf = configparser.ConfigParser()
        conf.read(Path(os.path.dirname(os.path.abspath(__file__))) / 'config.ini')
    return conf


def use_app():
    global app
    if not app:
        app = Flask(__name__)
        inner_conf = use_conf()
        inner_env = use_env()
        app.config['SQLALCHEMY_DATABASE_URI'] = inner_conf['db']['dev_uri' if inner_env == 'dev' else 'prod_uri']
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to dismiss unimportant warning
    return app


def use_db():
    global db
    if not db:
        db = SQLAlchemy(app)
    return db
