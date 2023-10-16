#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : query_repo_info.py
@Time       : 2023/05/24
@Version    : 1.0
@Desc       : None
"""
import os
from app.views.ms_jk import bp
from flask import request, jsonify, current_app
from hippo.exception import JobNotCompleteError
from hippo.web import DataAnalysisTableRecord
from hippo.tool import change_path, isEmpty, run_shell
from hippo.tool import trans_to_json


@bp.route("/demo", methods=['POST'])
def demo():
    record = DataAnalysisTableRecord(__file__)

    # 界面左侧参数获取
    infile = record.get_input_param("infile")  # -i ,--input

    # 界面右侧绘图参数获取
    width = record.get_plot_param("width", None)
    height = record.get_plot_param("height", None)
    
    basedir = record.path_for_output()

    with change_path(basedir):
        record.cmd_cache.add(scripts="demo.R")
        record.cmd_cache.add(key="-i", value=infile)
        record.cmd_cache.add(key="-w", value=width, ignore_default=8)
        record.cmd_cache.add(key="-h", value=height, ignore_default=6)
        record.cmd_cache.run()

        # 文件流返回
        generate_file_by_script = "demo.png"
        record.stream_return_add(generate_file_by_script)
        return jsonify(record.stream_return_get())
