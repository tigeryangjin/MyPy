import requests

u = 'http://music.163.com/api/playlist/detail?id='
validID = []
data = []
for i in range(1000000, 1000009):
    url = u + str(i)
    r = requests.get(url)
    status_code = r.json()['code']
    if status_code != 200:
        pass
    else:
        playListName = r.json()['result']['name']
        validID.append(i)
        validID.append(playListName)
        data.append(validID)

print(data)
