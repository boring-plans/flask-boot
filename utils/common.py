# -*- coding: utf-8 -*-
"""
Funcs for common use

Created by Kang Tao at 2022/1/13 11:57 AM
"""
import os
import configparser
from pathlib import Path


def get_env():
    """To get environment variable 'ENV'"""
    return os.environ.get('FLASK_ENV')


def get_conf(field=None):
    """To load configurations (and sometimes of certain field) in file 'config.ini'"""
    conf = configparser.ConfigParser()
    conf.read(Path(__file__).parent.parent / 'config.ini')
    return conf if field is None else conf[field]
