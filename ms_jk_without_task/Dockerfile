FROM dockerhub.genostack.com:8090/jikai/ms_jk_beeswarm:base_v01

WORKDIR /workspace

COPY . .
# RUN mv bin/beeswarm_plot.R /usr/local/envs/py310/bin/
# RUN chmod u+x /usr/local/envs/py310/bin/beeswarm_plot.R
# RUN rm -rf bin
# RUN pip install ms-jk-utils==1.1.6

EXPOSE 5000
ENTRYPOINT ["supervisord","-c","instance/supervisord.conf"]

# docker build -t dockerhub.genostack.com:8090/jikai/ms_jk_monocle2:v02.01_02 .
