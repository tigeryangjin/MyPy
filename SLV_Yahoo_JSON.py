import requests

url = 'https://www.ishares.com/us/products/239855/ishares-silver-trust-fund'
# 10，491.18
# 308774
r = requests.get(url)
data = r.text
# i = data.index('10,491.18')
i = 308774
print('SLV持仓数量：', data[i: i + 9])
input()
