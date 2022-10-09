nmap -sV -sT -A -F -T4 $ALL_IP --script vuln -oG  /home/user/output/nmap/fullscan.txt | tee /tmp/1
/opt/zaproxy/zap.sh -cmd -quickurl https://$CONSOLE/ -quickout /home/user/output/zap/report.xml | tee /tmp/2
python3 /home/user/kube-hunter/kube-hunter.py --remote $( echo $ALL_IP | sed "s/ /,/g") | tee /home/user/output/kube-hunter/out.txt | tee /tmp/3
cd /home/user/output/gvm/ 
python3 /home/user/pyssh.py | tee /tmp/4
/bin/bash
