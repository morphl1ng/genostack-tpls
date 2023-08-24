#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : run_monocle2_task.py
@Time       : 2023/08/18
@Version    : 1.0
@Desc       : None
"""
import os
import time
import yaml
import json
import shutil
import subprocess
from ms_jk_utils.web import SysRequest
from ms_jk_utils.tool import change_path
from celery import shared_task, current_task


@shared_task(ignore_result=False)
def run_monocle2_task(root_path, params, ticket) -> dict:
    current_task_id = current_task.request.id
    sys_req = SysRequest(ticket)

    try:
        # 运行 monocle2 流程
        # 1. 需要按照给定参数修改 config 文件
        # 2. 运行改造后的 snakemake 流程
        # 3. 更新 task 状态
        # note: 因为本地无法运行（资源不够，没有小测试文件），干运行流程，
        # 并 copy 一个流程结果到输出目录中

        # params : = inputs_json
        # root_path : workflow_root

        output = os.path.join(root_path, "output")

        # 将模板代码 copy 到工作根目录中
        # todo 从环境变量或current_app中获取，不存在则异常
        code_tpl_path = os.environ.get("MS_JK_MONOCLE2_CODE_TEMPLATE_PATH")
        if code_tpl_path is None or code_tpl_path == "":
            code_tpl_path = "/home/lx/Documents/jikai/ms_jk_monocle2/instance/data_dir/tpl_code"
        shutil.copytree(code_tpl_path, root_path, dirs_exist_ok=True)

        # todo 将参数从 inputs_json 中更新到 config.yaml 中
        # update {root_path}/config/config.yaml
        with open(os.path.join(root_path, "config/config.yaml"), "r") as fh:
            cfg = yaml.safe_load(fh.read())

        for k, v in params.items():
            if k == "inFile":
                pass
            elif "." in k:
                ks = k.split(".")
                if len(ks) != 2:
                    continue
                k1, k2 = ks
                if k1 not in cfg:
                    continue
                sub_cfg = cfg.get(k1)
                if k2 not in sub_cfg:
                    continue
                cfg[k2] = v
        with open(os.path.join(root_path, "config/config.yaml"), "w") as fh:
            fh.write(yaml.dump(cfg, allow_unicode=True))
        if not os.path.exists(output):
            os.makedirs(output)
        with change_path(output):
            # snakemake -s ../workflow/Snakefile  --configfile ../config/config.yaml --cores 4 --use-singularity
            cmd = "snakemake -s ../workflow/Snakefile all --dag --configfile ../config/config.yaml"
            res = subprocess.run(cmd, shell=True)
            print(res)

            # todo 临时的方案，docker中使用对应目录
            base_dir1 = "/home/lx/Documents/jikai/ms_jk_monocle2"
            # base_dir1 = "/workspace"
            # source_path = f"{base_dir1}/instance/data_dir/trajectory-analysis-monocle2-demo-report"
            source_path = f"{base_dir1}/instance/data_dir/output"
            shutil.copytree(source_path, output, dirs_exist_ok=True)
            time.sleep(120)
            data = {
                "status": "Succeeded",  # 'Submitted','Running','Failed','Aborted','Succeeded'
            }
            # task_param.updateTask(current_task_id, data)
            sys_req.platform_data_analysis_update(current_task_id, data)
            return {"status": "Task success!"}
    except Exception as e:
        # update status
        data = {"status": "Failed"}
        sys_req.platform_data_analysis_update(current_task_id, data)
        return {"status": "Task failed!", "msg": str(e)}
