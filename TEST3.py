import requests
from time import time


def playlist_to_file():
    t = time()
    u = 'http://music.163.com/api/playlist/detail?id='
    valid_id = []
    r_get = requests.get
    fp = open('output2.txt', 'w', encoding="utf8")
    fp_write = fp.write
    stri = str
    c = range(1000000, 1009999)
    for i in c:
        t1 = time()
        url = u + str(i)
        try:
            r = r_get(url)
        except:
            pass
        status_code = r.json()['code']
        if status_code != 200:
            pass
        else:
            play_list_name = r.json()['result']['name']
            valid_id.append(i)
            valid_id.append(play_list_name)
            fp_write(stri(valid_id) + '\n')
            valid_id = []
            print(i, time() - t1)
    fp.close()
    print(time() - t)


playlist_to_file()
