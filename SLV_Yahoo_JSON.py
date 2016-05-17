import requests

url='https://www.ishares.com/us/products/239855/ishares-silver-trust-fund'
r=requests.get(url)
data=r.text
print(type(data))