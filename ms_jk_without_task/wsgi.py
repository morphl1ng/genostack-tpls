#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : wsgi.py
@Time       : 2023/05/25
@Version    : 1.0
@Desc       : None
"""
import logging
from app import create_app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(
        host=flask_app.config.get("HOST"),
        port=flask_app.config.get("PORT"),
        debug=flask_app.config.get("DEBUG")
    )
else:
    # 使用gunicorn启动时, 将flask应用中的日志绑定到 gunicorn 的日志配置中
    gunicorn_logger = logging.getLogger('gunicorn.error')
    flask_app.logger.handlers = gunicorn_logger.handlers
    flask_app.logger.setLevel(gunicorn_logger.level)
