# 网易云音乐批量下载
# By YangJin
# Python3.5

import requests
import urllib
from urllib import request
import os


def mp3_download():
    # 榜单歌曲批量下载
    print('2884035:网易原创歌曲榜')
    print('19723756:云音乐飙升榜')
    print('3778678:云音乐热歌榜')
    print('3779629:云音乐新歌榜')
    play_list = input('请输入playlistID：')

    url = 'http://music.163.com/api/playlist/detail?id=' + play_list
    r = requests.get(url)
    status_code = r.json()['code']

    while status_code != 200:  # 如果输入的ID不存在，则要求重新输入ID,当status['code']==200则表示ID存在。
        print('输入的ID不存在！')
        play_list = input('请重新输入playlistID：')
        url = 'http://music.163.com/api/playlist/detail?id=' + play_list
        r = requests.get(url)
        status_code = r.json()['code']
    else:
        arr = r.json()['result']['tracks']
        play_list_name = r.json()['result']['name']  # 歌单名
        download_path = 'G:/Music/Music/' + play_list_name + '/'  # 下载目录:每个歌单创建新的文件夹，文件名为歌单名

        # 如果目录不存在这创建目录
        if os.path.exists(download_path) == False:
            os.makedirs(download_path)
        else:
            pass

        # 下载playlist的歌曲
        for i in range(len(arr)):
            s_name = arr[i]['name']  # 歌曲名
            music_name = s_name.strip('\/:*?"<>|')  # 剔除歌曲名字中的特殊字符，这些特殊字符不能做文件名
            artists = []  # 演唱者
            for j in range(len(r.json()['result']['tracks'][i]['artists'])):
                artists.append(r.json()['result']['tracks'][i]['artists'][j]['name'])
            name = str(i + 1) + '[' + music_name + ']'
            link = arr[i]['mp3Url']
            try:
                urllib.request.urlretrieve(link, download_path + name)  # 提前要创建文件夹
                print(name + str(artists) + link + ' 下载完成')
            except:
                print(name + str(artists) + link + ' 无法下载')


def playlist_search():
    key_word = input('请输入搜索关键词：')
    u = 'http://music.163.com/api/playlist/detail?id='
    play_list = []
    for i in range(99999):
        url = u + str(i)
        r = requests.get(url)
        status_code = r.json()['code']
        if status_code != 200:
            pass
        else:
            arr = r.json()['result']['tracks']
            play_list_name = r.json()['result']['name']  # 歌单名
            if play_list_name.find(key_word) == -1:
                pass
            else:
                play_list.append(play_list_name)
    print(play_list)


playlist_search()
