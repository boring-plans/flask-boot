# -*- coding: utf-8 -*-
"""
by kang1.tao,
on 2021/11/13.
"""
import configparser
import os
from flask import Flask
from flask import g, request, make_response
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
        inner_conf = use_conf()
        app = Flask(__name__, static_folder=inner_conf['app']['static_folder'])
    return app


def use_db():
    global db
    if not db:
        db = SQLAlchemy(app)
    return db
