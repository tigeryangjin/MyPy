import requests
import re

url = 'http://live.sina.com.cn/zt/app_zt/f/v/finance/globalnews1/?page=1'
html_source = requests.get(url).text
time = re.findall(r'<p class="bd_i_time_c">(.*?)</p>', html_source)
messages = re.findall(r'<p class="bd_i_txt_c">(.*?)</p>', html_source)
for i in range(len(messages)):
    print(time[i],messages[i])
