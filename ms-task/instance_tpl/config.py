#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : config.py.py
@Time       : 2023/05/25
@Version    : 1.0
@Desc       : None
"""

PORT = 5000
UPLOAD_API_URL = f"http://192.168.0.150:5041/api_upload"
COLOR_API_URL = f"http://192.168.0.150:5041/api_upload"
PLATFORM_API_VERSION = "v3"

PLATFORM_URL = f"http://192.168.0.147:8005/platform/{PLATFORM_API_VERSION}"
PLATFORM_DATA_DIR = "/home/lx/pub/platform_data_dir"

REDIS_HOST = "192.168.0.147"
REDIS_PORT = 6379
REDIS_DB = 3
REDIS_EXPIRE = 24 * 60 * 60  # redis 过期时间60秒

# Celery configuration
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

