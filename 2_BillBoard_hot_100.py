import gzip
import urllib
import urllib.request
import re


def get_song_info(data):
    # 获取_xsrf值
    pattern_ranking = re.compile('class="chart-row chart-row--([0-9]*) js-chart-row"', flags=0)
    pattern_song_name = re.compile('data-hovertracklabel="Song Hover-(.*)" data-songtitle=""', flags=0)
    # pattern_artist_name = re.compile('<a class="chart-row__artist" href="(.*)" data-tracklabel="Artist Name">(.*)',
    #                                  flags=0)

    ranking_list = pattern_ranking.findall(data)
    song_name_list = pattern_song_name.findall(data)
    # artist_name = pattern_artist_name.findall(data)
    return ranking_list, song_name_list


url = 'http://www.billboard.com/charts/hot-100'

urlop = urllib.request.urlopen(url, timeout=10)
data = urlop.read().decode('utf-8')
# print(data)

out_ranking, out_song_name = get_song_info(data)
# print(out_ranking)
# print(out_song_name)
for i in range(len(out_ranking)):
    print(out_ranking[i], out_song_name[i])
