# 项目参考

## 项目环境初始化
```bash
cd {your project workdir}
cp -r {ms-task or ms-without-task}./* ./
mv instance_tpl instance
vim {instance/config.py}
# {put your sample data to instance/data_dir/demo_sample_data}

pip install -r requirements.txt # 安装依赖
# 根据项目需要可不安装 celery 等
# 安装额外需要的包 

# 必须安装 平台公共sdk包,目前最新版本为 1.3.0, 后续会根据需要更新版本
# 安装前需要配置私服
# 1. vim ~/.pypirc ,配置内容参考 pypirc
# 2. vim ~/.config/pip/pip.conf ,配置内容参考 pip.conf

pip install hippo==1.3.0 

# 集成前端项目
# 前端项目待发布,目前还不是最新的代码
cp -r {本项目下}/app/static {your project workdir}/app
cp -r {本项目下}/app/templates {your project workdir}/app


# {开发业务代码}

```
##  



## 注意

1. 项目区分任务和非任务，使用对应的项目进行开发
2. 将 instance_tpl 修改为 instance,并根据需要增减参数配置
3. `app/views/` 目录中第一级的目录和文件名会注册成 url_prefix,并寻找其中的 `bp` 对象自动注册路由
4. api接口需要文件名，函数名，接口名三者一致（不强制）
5. 接口功能中必须实现 `submit` 接口,并调用对象的 `submit_task` 或 `submit` 方法(使用对应项目模板无需任何修改)
6. 开发的接口需要引入到`bp`,以示例为例:
   需要在 `app/views/ms_jk/__init__.py` 文件末尾添加 `from .a_sample_api import a_sample_api`
7. 其他待定