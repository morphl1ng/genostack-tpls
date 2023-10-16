#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : __init__.py
@Time       : 2023/07/11
@Version    : 1.0
@Desc       : None
"""
from flask import Blueprint

bp = Blueprint('views_bp', __name__)

from .submit import submit
from .demo import demo # 开发请删除该示例路由
