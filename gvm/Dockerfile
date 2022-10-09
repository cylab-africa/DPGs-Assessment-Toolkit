FROM isaudits/gvm:gvm-21.4
USER root
RUN useradd -rm -d /home/gvmuser -s /bin/bash -g root -G sudo -u 1001 gvmuser
RUN echo "gvmuser:gvmpass" | chpasswd
RUN apt update
RUN apt install -y openssh-server sudo
RUN echo 'gvmuser ALL=(ALL) NOPASSWD: ALL'>> /etc/sudoers
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config
RUN service ssh start
RUN pip3 install gvm-tools
RUN sleep 600
RUN chmod 777 /usr/local/var/run/gvmd.sock
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
# create user and install ssh
# expose ssh port ?

