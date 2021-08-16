#!usr/bin/env python3

import os
import sys

def runkh(option, ipadd):
    khcmd = 'kube-hunter ' + option + ' ' + ipadd
    os.system(khcmd + ' > /app/dir/output/kh.txt')
    print('Hello World')

def runkb(target, cfgloc):
    kbcmd = './kube-bench run --targets=' + target + ' --config-dir ' + cfgloc
    os.system(kbcmd + ' > /app/dir/output/kb.txt')
    print('Hello World 2')

def runkadt(cmmd):
    pass

def runksec(cmmd):
    os.system('kubesec scan k8s-deployment.yml')

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
    runkh(data['scanopt'], data['ipadd'])
    runkb(data['target'], data['cfgloc'])
    getIPaddress()
    runnmap()
#    runksec(1)
