# 网易云音乐歌单随机浏览
# By YangJin
# Python3.5

import requests
import urllib
from urllib import request
import os
import random

for i in range(10):
    id = random.randint(1, 99999999)
    url = 'http://music.163.com/api/playlist/detail?id=' + str(id)
    r = requests.get(url)
    status_code = r.json()['code']
    if status_code == 200:
        playlist_name = r.json()['result']['name']
        t = r.json()['result']['tracks']
        print(str(id) + '\n' + str(playlist_name) + '\n' + str(t))
    else:
        pass
