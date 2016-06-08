import requests

url = 'https://www.ishares.com/us/products/239855/ishares-silver-trust-fund'
# 10，491.18
# 308774
r = requests.get(url)
data = r.text
i = data.index('Tonnes in Trust')
i += 215
print('SLV持仓数量（吨）：', data[i: i + 9])
price = data.index('Mid-Point Price')
price += 320
print('中间价（美元/盎司）：', data[price:price + 5])
rmb_price = float(data[price:price + 5]) / 28.3495231 * 6.5690
print('中间价（元/克）', rmb_price)
input()
