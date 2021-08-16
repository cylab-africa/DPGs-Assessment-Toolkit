# Dockerfile, Image, Container
FROM python:3.8-slim
WORKDIR /app

ADD runtest.py .
ADD kbstuff/kube-bench_0.6.3_linux_amd64.tar.gz .
#ADD kubesec_linux_amd64.tar.gz .

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install nmap
RUN pip install kube-hunter
RUN apt-get update && apt-get install -y procps
RUN mkdir /app/output
#RUN tar -xzf kube-bench_0.6.3_linux_amd64.tar.gz
#RUN tar -xzf kubesec_linux_amd64.tar.gz

#CMD [ "touch", "/app/touch/kh.txt"]
#CMD [ "touch", "/app/dir/kb.txt"]
ENTRYPOINT [ "python", "runtest.py"]
