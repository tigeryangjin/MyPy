import urllib.request
from collections import deque

url = "http://baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)

