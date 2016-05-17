import requests

#tracks:list
#0~48:dict  track
#track = r.json()['result']['tracks'][0]['artists'][1]['name']
url = 'http://music.163.com/api/playlist/detail?id=1234567'
r = requests.get(url)
result=r.json()['result']['tracks'][0]['artists']
print(type(result))
print(result)