#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : submit.py
@Time       : 2023/08/12
@Version    : 1.0
@Desc       : None
"""
import logging
from app.views.ms_jk import bp
from flask import request, jsonify
from ms_jk_utils.web import DataAnalysisSubmit


@bp.route("/submit", methods=['POST'])
def submit():
    try:
        das = DataAnalysisSubmit()
        return das.submit()
    except Exception as e:
        logging.exception(e)
        return jsonify(error_code=999, msg=str(e)), 500
