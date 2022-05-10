FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/wf-base:fbe8-main

RUN curl -O -L https://github.com/chanzuckerberg/shasta/releases/download/0.10.0/shasta-Linux-0.10.0 &&\ 
    chmod ugo+x shasta-Linux-0.10.0 &&\ 
    mv shasta-Linux-0.10.0 shasta

COPY wf /root/wf

ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
RUN  sed -i 's/latch/wf/g' flytekit.config
RUN python3 -m pip install --upgrade latch
WORKDIR /root
