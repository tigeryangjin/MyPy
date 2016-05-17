import requests

'''
a = requests.get('https://github.com/timeline.json')
b = requests.post('http://httpbin.org/post')
c = requests.put("http://httpbin.org/put")
d = requests.delete("http://httpbin.org/delete")
e = requests.head("http://httpbin.org/get")
f = requests.options("http://httpbin.org/get")
print(a,b,c,d,e,f)


payload = {'key1': 'value1', 'key2': 'value2'}
g = requests.get("http://httpbin.org/get", params=payload)
print(g.url)
'''

a = requests.get('https://github.com/timeline.json')
print(a.encoding)
print(a.text)
a.encoding='ISO-8859-1'
print(a.text)