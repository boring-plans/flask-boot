# -*- coding: utf-8 -*-
"""
Created by Kang Tao at 2022/1/12 5:04 PM
"""
from pathlib import Path
__all__ = [p.stem for p in Path(__file__).parent.glob('[!_]*.py')]


def register_all():
    """Register all"""
    import importlib
    for model in __all__:
        importlib.import_module(f'models.{model}')
