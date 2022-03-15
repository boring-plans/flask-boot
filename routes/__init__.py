# -*- coding: utf-8 -*-
"""
Created by Allen Tao at 2022/1/12 5:05 PM
"""
from pathlib import Path
__all__ = [p.stem for p in Path(__file__).parent.glob('[!_]*.py')]


def register_all():
    """Register all"""
    import importlib
    for route in __all__:
        importlib.import_module(f'routes.{route}')
