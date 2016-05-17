# -*- coding: utf-8 -*-
import sys
import urllib3
import urllib
import json
from urllib import request

url = 'http://apis.baidu.com/apistore/idservice/id?id=420984198704207896'

req = urllib.request.Request(url)

req.add_header("apikey", "63376bc10da1f338d1a2cc505cceb7ca")


resp = urllib.request.urlopen(req)

content = resp.read()
if(content):
    print(content)



#63376bc10da1f338d1a2cc505cceb7ca

