import redis

r = redis.Redis(host='192.168.188.128', port=6379)
r.mset(k1='v1', k2='v2')
print(r.get('k1'))
