import redis

r = redis.Redis(host='192.168.188.128', port=6379)
r.set('guo', 'shuai')
print(r.get('guo'))
