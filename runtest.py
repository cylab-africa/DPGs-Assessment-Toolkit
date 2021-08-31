#!usr/bin/env python3

import os
import sys

def runkh(option, ipadd):
    khcmd = 'kube-hunter ' + option + ' ' + ipadd
    os.system(khcmd + ' > /app/dir/output/kh.txt')
    print('Run Kube-Hunter')

def runkb(target, cfgloc):
    kbcmd = './kube-bench run --targets=' + target + ' --config-dir ' + cfgloc
    os.system(kbcmd + ' > /app/dir/output/kb.txt')
    print('Run Kube-Bench')

def runkadt(pathaudit, auditmode):
    kadtcmd = './kubeaudit all ' + auditmode + ' "' + pathaudit + '"'
    os.system(kadtcmd + ' > /app/dir/output/kadt.txt')
    print('Run Kubeaudit')

def runksec(pathsec):
    f = open("/app/dir/output/ksec.txt", "w")
    kseccmdAPI = 'curl -sSX POST --data-binary @"' + pathsec + '" https://v2.kubesec.io/scan'
#    kseccmdETCD = 'curl -sSX POST --data-binary @"/etc/kubernetes/manifests/etcd.yaml" https://v2.kubesec.io/scan'
#    kseccmdCM = 'curl -sSX POST --data-binary @"/etc/kubernetes/manifests/kube-controller-manager.yaml" https://v2.kubesec.io/scan'
#    kseccmdSCH = 'curl -sSX POST --data-binary @"/etc/kubernetes/manifests/kube-scheduler.yaml" https://v2.kubesec.io/scan'
    writeksec('API', kseccmdAPI, f)
#    writeksec('ETCD', kseccmdETCD, f)
#    writeksec('Controller-Manager', kseccmdCM, f)
#    writeksec('Scheduler', kseccmdSCH, f)
    f.close()
    print('Run Kubesec')

def writeksec(manifest, cmd, f):
    header = "Kubesec " + manifest + " Check:\n-------------------------------------------"
    os.system(cmd + ' >> /app/dir/output/ksec.txt')

def getIPaddress():
    ipcmd =" arp -a | grep 'eth0' | awk '{print $2}' | awk '{print substr ($0,2,length($0) - 2)}' "
    os.system(ipcmd + ' > ipaddress.txt ')
    os.system('cat ipaddress.txt')
    print("In get IP address")

def runnmap():
        nmapcmd = 'nmap -T4 -p- -A -script vuln -iL ipaddress.txt -oN nmapVulnResults'
        os.system(nmapcmd)
        print('inside nmap run ')
        os.system('cat nmapVulnResults')

if __name__ == "__main__":
    import sys
    import json
    path = '/app/dir/' + sys.argv[1]
    f = open(path)
    data = json.load(f)
    print(data['scanopt'])
    print(data['ipadd'])
    print(data['target'])
    print(data['cfgloc'])
    print(data['auditmode'])
    print(data['pathsec'])
    print(data['pathaudit'])
    runkh(data['scanopt'], data['ipadd'])
    runkb(data['target'], data['cfgloc'])
    runksec(data['pathsec'])
    runkadt(data['pathaudit'], data['auditmode'])
#    getIPaddress()
#    runnmap()
#    runksec(1)
