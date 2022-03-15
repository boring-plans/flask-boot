# -*- coding: utf-8 -*-
"""
Used to generate unified response

Created by Allen Tao at 2022/1/12 5:06 PM
"""
from flask import jsonify, Response
import datetime


def make_response(result=None, code=0) -> Response:
    """To make response, and the default code 0 means a success
    Called like this:
        - make_response([{"id":1, "name": "foo"}])
        - make_response('Permission denied', 1)
    """
    return jsonify({
        "code": code,
        "result": result,
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
