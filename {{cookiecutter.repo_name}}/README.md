# {{cookiecutter.repo_name}}

## 环境安装
```
# 1. 创建项目环境

# 2. 安装项目依赖
pip install -r requestments.txt

# 3. 更新项目前台代码
cd app
git clone http://192.168.0.135:30080/genostack-app/app-ui-releases.git 
# 目前这里还需要输入用户名密码
mv app-ui-releases/app/* ./ && rm -rf app-ui-releases
cd ..

# 4. 下载项目配置参数模板
git clone -b inst http://192.168.0.135:30080/genostack/genostack-docs.git instance

# 5. 根据需要更新项目项目配置


```