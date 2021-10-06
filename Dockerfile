# Dockerfile, Image, Container
FROM python:3.8-slim
WORKDIR /app

ADD runtest.py .
ADD kbstuff/kube-bench_0.6.3_linux_amd64.tar.gz .
ADD kauditstuff/kubeaudit_0.14.2_linux_amd64.tar.gz .

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install curl
RUN pip install kube-hunter
RUN apt-get update && apt-get install -y procps
RUN mkdir /app/output

ENTRYPOINT [ "python", "runtest.py"]
