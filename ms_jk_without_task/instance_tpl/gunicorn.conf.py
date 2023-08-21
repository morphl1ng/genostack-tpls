#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : gunicorn.conf.py.py
@Time       : 2023/03/03
@Version    : 1.0
@Desc       : None
"""
import os
from gevent import monkey

root_dir = os.path.dirname(__file__)

monkey.patch_all()

# 定义同时开启的处理请求的进程数量，根据网站流量适当调整
workers = 5  # multiprocessing.cpu_count() * 2 + 1  # #同时执行的进程数，推荐为当前CPU个数*2+1
# 采用gevent库，支持异步处理请求，提高吞吐量
worker_class = "gevent"  # sync, gevent,meinheld   #工作模式选择，默认为sync，这里设定为gevent异步
timeout = 3600
# 绑定IP和端口
bind = "0.0.0.0:5000"
preload_app = True
# 使用后台守护进程的模式启动,若开启则docker启动时容器会直接退出
# daemon = "true"

# 日志设置
# 设置gunicorn访问日志格式，错误日志无法设置
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# access_log_format = '%(asctime)s,%(msecs)03d [%(name)s:%(lineno)d] [%(levelname)s] %(message)s'
# 访问日志的存储文件, 当前路径的logs目录下
accesslog = os.path.join(root_dir, "log/gunicorn_access.log")
# 错误日志的存储文件, 当前路径的logs目录下
errorlog = os.path.join(root_dir, "log/gunicorn_error.log")
# 设置pid文件的文件名
pidfile = os.path.join(root_dir, "log/gunicorn.pid")
# 日志记录等级
loglevel = 'info'  # debug error warning error critical
worker_tmp_dir = "/dev/shm"  # 该目录共享内存和内存文件系统

# daemon = False  # 在生产环境改为False
# reload = False  # 当代码有修改时，自动重启workers。适用于开发环境。
# x_forwarded_for_header = 'X-FORWARDED-FOR'
backlog = 2048  # 等待服务客户的数量，最大为2048，即最大挂起的连接数
max_requests = 1000  # 默认的最大客户端并发数量