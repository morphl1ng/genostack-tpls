FROM dockerhub.genostack.com:8090/jikai/ms_jk_base:v04

WORKDIR /workspace

RUN mamba install r-optparse r-beeswarm -c conda-forge -y && \
  conda clean --all -f -y

# docker build -t dockerhub.genostack.com:8090/jikai/ms_jk_beeswarm:base_v01 .
