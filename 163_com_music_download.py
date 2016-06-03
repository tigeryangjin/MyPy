# 网易云音乐批量下载
# By YangJin
# Python3.5

import requests
import urllib
from urllib import request
import os

# 榜单歌曲批量下载
# r = requests.get('http://music.163.com/api/playlist/detail?id=2884035')	# 网易原创歌曲榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=19723756')	# 云音乐飙升榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')  # 云音乐热歌榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')	# 云音乐新歌榜
r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')

arr = r.json()['result']['tracks']  # 共有100首歌
play_list_name = r.json()['result']['name']
download_path = 'G:/Music/Music/' + play_list_name + '/'  # 下载目录:每个歌单创建新的文件夹，文件名为歌单名

if os.path.exists(download_path) == False:
    os.makedirs(download_path)
else:
    pass

for i in range(len(arr)):  # 输入要下载音乐的数量，1到100。
    s_name = arr[i]['name']
    music_name = s_name.strip('\/:*?"<>|')  # 剔除歌曲名字中的特殊字符，这些特殊字符不能做文件名
    name = str(i + 1) + '_' + music_name + '.mp3'
    link = arr[i]['mp3Url']
    try:
        urllib.request.urlretrieve(link, download_path + name)  # 提前要创建文件夹
        print(name + link + ' 下载完成')
    except:
        print(name + link + ' 无法下载')
