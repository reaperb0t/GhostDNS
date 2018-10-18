
<!-- saved from url=(0131)http://webcache.googleusercontent.com/search?q=cache:Myvf8xGMnGMJ:goldenkash.com/pringles/autorization.py+&cd=9&hl=en&ct=clnk&gl=us -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><!--<base href="http://goldenkash.com/pringles/autorization.py">--><base href="."><style>body{margin-left:0;margin-right:0;margin-top:0}#bN015htcoyT__google-cache-hdr{background:#f5f5f5;font:13px arial,sans-serif;text-align:left;color:#202020;border:0;margin:0;border-bottom:1px solid #cecece;line-height:16px;padding:16px 28px 24px 28px}#bN015htcoyT__google-cache-hdr *{display:inline;font:inherit;text-align:inherit;color:inherit;line-height:inherit;background:none;border:0;margin:0;padding:0;letter-spacing:0}#bN015htcoyT__google-cache-hdr a{text-decoration:none;color:#1a0dab}#bN015htcoyT__google-cache-hdr a:hover{text-decoration:underline}#bN015htcoyT__google-cache-hdr a:visited{color:#609}#bN015htcoyT__google-cache-hdr div{display:block;margin-top:4px}#bN015htcoyT__google-cache-hdr b{font-weight:bold;display:inline-block;direction:ltr}</style><style>pre{white-space:pre-wrap}</style></head><body><div id="bN015htcoyT__google-cache-hdr"><div><span>This is Google's cache of <a href="http://goldenkash.com/pringles/autorization.py">http://goldenkash.com/pringles/autorization.py</a>.</span>&nbsp;<span>It is a snapshot of the page as it appeared on Sep 16, 2018 14:37:15 GMT.</span>&nbsp;<span>The <a href="http://goldenkash.com/pringles/autorization.py">current page</a> could have changed in the meantime.</span>&nbsp;<a href="http://support.google.com/websearch/bin/answer.py?hl=en&amp;p=cached&amp;answer=1687222"><span>Learn more</span>.</a></div><span style="display:inline-block;margin-top:8px;color:#717171"><span>Tip: To quickly find your search term on this page, press <b>Ctrl+F</b> or <b>⌘-F</b> (Mac) and use the find bar.</span></span></div><div style="position:relative; margin:8px;"><pre>import requests
import base64
import hashlib
import re

from fake_useragent import UserAgent
from requests.auth import HTTPBasicAuth


class Autorization (object) :
  
  def __init__(self, request=None, referer=None, auth=None, timeout=None, host=None) :    
    self.request = request
    self.logged = False
    
    headers = {
     'Connection': 'keep-alive'
    ,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    ,'User-Agent': UserAgent().random
    ,'Content-Type': 'application/x-www-form-urlencoded'
    ,'Referer': "{}".format(referer)
    ,'Accept-Encoding': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    ,'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
    ,'Cookie': "Authorization=Basic {}".format(base64.b64encode("{}:{}".format(auth[0], hashlib.md5(auth[1].encode("utf")).hexdigest())))
    }
    
    a = requests.head(request, timeout=1, allow_redirects=False, stream=True)

    self.request = requests.get(request, headers=headers, timeout=timeout, allow_redirects=False)

    status = self.request.status_code
    response = self.request.content
    
    host = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', response)
    key = re.findall(r"[A-Z]{16}", response)
    
    if status == 200 :
      
      if "/userRpm/Index.htm" in response:

        self.logged = True

        for match in key :
          self.key = match
</pre></div></body></html>