# subscriber.py 订阅者
# !/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)
