FROM dockerhub.genostack.com:8090/jikai/{{cookiecutter.repo_name}}:base_v01

WORKDIR /workspace

COPY . .

# 这里，需要安装项目依赖的脚本
RUN pip install {{cookiecutter.repo_name}}-script==1.0.0
RUN pip install hippo==1.3.15

EXPOSE 5000
ENTRYPOINT ["supervisord","-c","instance/supervisord.conf"]

# docker build -t dockerhub.genostack.com:8090/jikai/{{cookiecutter.repo_name}}:{{cookiecutter.version}}.alpha.01 .
