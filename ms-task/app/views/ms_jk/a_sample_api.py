#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : a_sample_api.py
@Time       : 2023/08/21
@Version    : 1.0
@Desc       : None
"""
import logging
from app.views.ms_jk import bp
from flask import request, jsonify
from app.util.a_common_func_in_pro import a_common_func_in_pro
from ms_jk_utils.web import DataAnalysisTableRecord
from ms_jk_utils.tool import change_path, isEmpty, tobase64


@bp.route("/a_sample_api", methods=['POST'])
def a_sample_api():
    try:
        record = DataAnalysisTableRecord()
        # 获取左侧计算参数
        infile = record.get_input_param("infile")
        # 获取右侧绘图参数
        color = record.get_plot_param("color")
        base_out_dir = record.path_for_output()

        # 切换命令运行的工作目录， 必须在这里运行，且确认脚本输出文件到这个目录下
        # 这个目录位于 {record.workflow_root}/output 下
        base64list = []
        file_list = []
        with change_path(base_out_dir):
            # do something
            a_common_func_in_pro()
            # todo 1.使用参数绘制图片
            # todo 2.验证输出的图片是否存在
            # todo 3.将图片转成base64
            out_img_path = "..."  # 输出的文件路径
            out_img_name = "..."  # 输出的文件名称
            img_base64 = tobase64(out_img_path, out_img_name)
            # 将 img_base64 返回给前台, 返回格式与
            base64list.append(img_base64)
            file_list.append(out_img_name)
            result = {
                "out_dir": out_img_path,
                "file_list": file_list,
                "base64list": base64list
            }
        return result
    except Exception as e:
        logging.exception(e)
        return jsonify(error_code=999, msg=str(e)), 500
