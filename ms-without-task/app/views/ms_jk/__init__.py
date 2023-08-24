#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : __init__.py.py
@Time       : 2023/07/11
@Version    : 1.0
@Desc       : None
"""
from flask import Blueprint

bp = Blueprint('views_bp', __name__)

from .submit import submit
# 需要将开发的接口导入
from .a_sample_api import a_sample_api