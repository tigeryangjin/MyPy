"""
#1
import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
#print(data)
a = urllib.request.urlopen(url)
#print(type(a))
#print(a.geturl())
print(type(data))
print(len(data))
"""

# import urllib
import urllib.request
import urllib.parse

data = {}
data['word'] = 'python'

url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)
