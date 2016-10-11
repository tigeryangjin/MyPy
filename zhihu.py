import gzip
import urllib
import urllib.request
import re


def getXSRF(data):
    # 获取_xsrf值
    cer = re.compile('name="_xsrf" value="(.*)"', flags=0)
    strlist = cer.findall(data)
    return strlist


def ungzip(data):
    # 解压数据
    try:
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


url = 'https://www.zhihu.com'

urlop = urllib.request.urlopen(url, timeout=2)
data = urlop.read().decode('utf-8')
print(getXSRF(data))
print(data)
