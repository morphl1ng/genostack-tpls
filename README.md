[![Build Status](https://travis-ci.org/mobidevke/cookiecutter-flask-api-starter.svg?branch=master)](https://travis-ci.org/mobidevke/cookiecutter-flask-api-starter)

# genostack-tpl

`branch: st-1.0.0`
平台项目模板之小工具非任务模式项目模板

## 用法说明

使用本模板创建项目之前，应该先创建python=3.10环境,参考命令如下：

```python
conda create -n ${env_name} python=3.10 -y && conda activate ${env_name}
# 或者
python3 -m venv .${env_name} && python activate .${env_name}/bin/activate
```

下载 cookiecutter:

`pip install --user cookiecutter`
使用本模板创建小工具应用:

`cookiecutter http://192.168.0.135:30080/genostack/genostack-tpls.git -c st-1.0.0`

如果有需要的话可以更新项目配置(instance/config.py)
