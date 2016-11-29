import urllib.request
import re

url = 'https://api.douban.com/v2/book/1220562'
url_op = urllib.request.urlopen(url, timeout=10)
data = url_op.read().decode('utf-8')
print(data)