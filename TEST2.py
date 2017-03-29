

import requests
import json


def test():
    url = "https://www.zhihu.com/topic/19550994/hot"
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '27',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '这里的内容弄你自己的吧，我就不把我的账户cookie信息放上来了',
        'Host': 'www.zhihu.com',
        'Origin': 'https://www.zhihu.com',
        'Referer': 'https://www.zhihu.com/topic/19550994/hot',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrftoken': 'f56ce1182d8e4ada986e83150d131a16'}

    re = requests.post(url, headers=headers, data={'start': 0, 'offset': 3047.3986818})
    return json.loads(re.text)

print(test())