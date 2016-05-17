import requests

# tracks:list
# 0~48:dict  track
# track = r.json()['result']['tracks'][0]['artists'][1]['name']
# print(r.json()['result']['tracks'][i]['name']) #歌曲名

url = 'http://music.163.com/api/playlist/detail?id=1234567'
r = requests.get(url)
result = r.json()['result']['tracks']

for i in range(len(r.json()['result']['tracks'])):
    for key in r.json()['result']['tracks'][i]:
        if key == 'artists':
            artist = [] #存储歌手列表
            for j in range(len(r.json()['result']['tracks'][i]['artists'])):
                artist.append(r.json()['result']['tracks'][i]['artists'][j]['name'])
            print('['+r.json()['result']['tracks'][i]['name']+'] '+ str(artist))
