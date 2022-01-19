# -*- coding: utf-8 -*-
"""
Random captcha

Created by Kang Tao at 2022/1/18 11:13 AM
"""
from captcha.image import ImageCaptcha
import random


def _gen_random_str():
    """To generate a string whose length is 4 and characters are randomly chosen"""
    chars = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return ''.join(random.choice(chars) for _ in range(4))


def gen_captcha():
    """To generate a captcha in format base64"""
    from io import BytesIO
    import base64
    captcha_str = _gen_random_str()
    captcha = ImageCaptcha().generate_image(captcha_str)
    buffer = BytesIO()
    captcha.save(buffer, format='PNG')
    data = buffer.getvalue()
    return captcha_str, 'data:image/png;base64,' + base64.b64encode(data).decode()
