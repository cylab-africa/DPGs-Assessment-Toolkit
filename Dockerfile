FROM ubuntu:20.04
USER root
RUN echo "Built !!!!!"
RUN apt update -y  --fix-missing && apt upgrade -y
RUN apt install -y apt-utils
RUN apt install -y sqlmap
RUN apt install -y net-tools nmap wget curl git sudo
WORKDIR /root/

RUN useradd -ms /bin/bash user
RUN echo 'user ALL=(ALL) NOPASSWD: ALL'>> /etc/sudoers
RUN cat /etc/sudoers
USER user
WORKDIR /home/user

RUN curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
RUN bash install.sh
RUN /home/linuxbrew/.linuxbrew/bin/brew install kubeaudit
#RUN /home/linuxbrew/.linuxbrew/bin/kubeaudit
RUN wget 'https://github.com/aquasecurity/kube-bench/releases/download/v0.6.8/kube-bench_0.6.8_linux_amd64.deb'
RUN sudo dpkg -i 'kube-bench_0.6.8_linux_amd64.deb'
RUN which kube-bench
RUN sudo apt install -y python3 python3-setuptools python3-pip
RUN git clone https://github.com/aquasecurity/kube-hunter
RUN python3 --version
WORKDIR /home/user/kube-hunter
RUN pip3 install -r requirements.txt
#RUN python3 kube-hunter.py --help
RUN wget 'https://github.com/controlplaneio/kubesec/releases/download/v2.11.5/kubesec_linux_amd64.tar.gz'
RUN mkdir ./kubesec
RUN tar -xvf kubesec_linux_amd64.tar.gz -C ./kubesec
RUN chmod +x kubesec/kubesec
#RUN kubesec/kubesec
USER root
ENV TERM=xterm-256color
#ENV DEBIAN_FRONTEND=noninteractive 


ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Africa/Cairo
RUN apt-get install -y tzdata

RUN apt install -y rsync software-properties-common
RUN add-apt-repository ppa:openjdk-r/ppa && apt-get update




RUN apt-get -y install openjdk-8-jre
#RUN apt-get -y install openjdk-8-jre-headless openjdk-8-jre icedtea-8-jre-jamvm icedtea-8-jre-cacao icedtea-8-plugin
USER user
WORKDIR /home/user
RUN mkdir src/
WORKDIR src/
RUN wget https://github.com/zaproxy/zaproxy/releases/download/2.5.0/ZAP_2.5.0_Linux.tar.gz
RUN tar -xzvf ZAP_2.5.0_Linux.tar.gz
RUN sudo rsync -av ZAP_2.5.0/ /opt/zaproxy/
RUN ls -laht /opt/zaproxy/
WORKDIR /opt/zaproxy/
RUN bash zap.sh  -help 
RUN sudo apt-get install -y software-properties-common sqlite3

RUN sudo apt install python3 python3-pip
RUN pip3 install python-gvm paramiko
RUN sudo apt install-y nano
WORKDIR /home/user
RUN mkdir /home/user/output
RUN mkdir /home/user/output/nmap
RUN nmap -sV -sT -A -p- -T4 -Pn $ALL_IP -oG  /home/user/output/nmap/fullscan.txt
