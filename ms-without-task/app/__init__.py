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
from ms_jk_utils.cfg import DefaultConfig
from ms_jk_utils.web import blueprints_dynamic_register

__VERSION = (1, 0, 0)
__VERSION__ = ".".join(map(lambda x: str(x), __VERSION))


def create_app():
    app = Flask(__name__)
    #
    #             static_folder="../dist/static",
    #             template_folder="../dist",
    #             instance_path=Paths.instance_path

    # r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
    CORS(app, resources=r'/*')

    app.config.from_object(DefaultConfig)
    app.config.from_pyfile(os.path.join(app.instance_path, 'config.py'))

    blueprints_dynamic_register(os.path.dirname(__file__), app)

    @app.route('/', methods=['GET'])
    @app.route('/tool_detail', methods=['GET'])
    def index():
        return render_template('index.html')

    return app
