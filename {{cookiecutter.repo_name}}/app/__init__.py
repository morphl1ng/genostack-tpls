#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : __init__.py.py
@Time       : 2022/09/21
@Version    : 1.0
@Desc       : None
"""
import os
from flask_cors import CORS
from flask import Flask, g, render_template
from hippo.cfg import DefaultConfig
from hippo.web import blueprints_dynamic_register
from hippo.web import exception_handle_register

__VERSION = (1, 0, 0)
__VERSION__ = ".".join(map(lambda x: str(x), __VERSION))


def create_app():
    app = Flask(__name__)

    app.config.from_object(DefaultConfig)
    app.config.from_pyfile(os.path.join(app.instance_path, 'config.py'))
    blueprints_dynamic_register(os.path.dirname(__file__), app)

    # r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
    CORS(app, resources=r'/*')

    @app.route('/', methods=['GET'])
    @app.route('/tool_detail', methods=['GET'])
    def index():
        return render_template('index.html')

    exception_handle_register(app)
    return app
