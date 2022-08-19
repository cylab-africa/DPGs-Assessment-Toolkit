import paramiko
import time
import os
from scp import SCPClient



ALL_IP=os.getenv("ALL_IP")
iplist=ALL_IP.split()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("172.50.0.3", username="gvmuser", password="gvmpass")

for IP in iplist:
        print("Scanning: " + IP)
        cmd="gvm-script --gmp-username $GVM_USER --gmp-password $GVM_PASSWORD socket --socketpath=/usr/local/var/run/gvmd.sock /scripts/scan-new-system.gmp.py " + IP + " 730ef368-57e2-11e1-a90f-406186ea4fc5 | awk -F 'report ID is' '{print $2}' | tee /home/gvmuser/report-id; sleep 300; gvm-script --gmp-username $GVM_USER --gmp-password $GVM_PASSWORD socket --socketpath=/usr/local/var/run/gvmd.sock /scripts/export-pdf-report.gmp.py $(cat /home/gvmuser/report-id) /home/gvmuser/report-" + IP +".pdf"
        #print(cmd)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
        for line in iter(ssh_stdout.readline, ""):
                print(line, end="")

        for line in iter(ssh_stderr.readline, ""):
                print(line, end="")

        ssh_stdin.close()

for IP in iplist:
        print("downloading: report-" + IP + ".pdf")
        with SCPClient(ssh.get_transport()) as scp:
            scp.get("/home/gvmuser/report-" + IP + ".pdf")

