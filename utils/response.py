# -*- coding: utf-8 -*-
"""
Used to create unified response
by kang1.tao,
on 2021/6/10.
"""
from flask import jsonify, Response
import datetime


def positive(msg: str = 'success', data: object = None) -> Response:
    """Positive
    :param msg: message
    :param data: whatever kind of data you want
    :return: an object will transferred to frontend
    """
    return jsonify({
        "code": 200,
        "message": msg,
        "data": data,
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


def negative(msg: str = 'failed', data: object = None) -> Response:
    """Negative
    :param msg: message
    :param data: maybe always None
    :return: an object will transferred to frontend
    """
    return jsonify({
        "code": 444,
        "message": msg,
        "data": data,
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


def make_response(code: int, msg: str, data: object) -> Response:
    """Manually appoint response status code
    :param code: status code
    :param msg: message in response
    :param data: data in response
    :return: also an object
    """
    return jsonify({
        "code": code,
        "message": msg,
        "data": data,
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
