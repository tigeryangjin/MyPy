import urllib.request
import re
from collections import deque

url = 'http://news.dbanotes.net'
urlop = urllib.request.urlopen(url)
data = urlop.read().decode('utf-8')
linkre = re.compile(r'class="title".+?href="(.+?)"')
queue=deque()

#for x in linkre.findall(data):
for x in data:
    if 1:
        queue.append(x)
    print(queue)
print(data)
