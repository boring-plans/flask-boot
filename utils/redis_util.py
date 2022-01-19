# -*- coding: utf-8 -*-
"""
Redis Util

Created by Kang Tao at 2022/1/18 11:17 AM
"""
import redis
from utils.common import get_conf, get_env

conf = get_conf('redis')
env = get_env()
host = conf[f'{env}_host']
port = int(conf[f'{env}_port'])


def set_redis_value(key: str, value: str, exp: int = 3600 * 3):
    """Set value, default exp is 3 hrs"""
    with redis.Redis(host, port) as r:
        if exp == -1:
            # always valid
            r.set(key, value)
        else:
            r.set(key, value, ex=exp)


def get_redis_value(key: str):
    """Get value"""
    with redis.Redis(host, port, decode_responses=True) as r:
        return r.get(key)


def delete_redis_value(key: str):
    """Delete value"""
    with redis.Redis(host, port) as r:
        (key in r) and r.delete(key)
