#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

r = redis.Redis(host='192.168.188.128', port=6379, db=0)
r.hset('noset', 'python', '11')
print(r.hget('noset', 'python'))
