#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import string
import random


def write_hash_redis(key, field, value):
    # 写入redis（hash数据类型）
    r = redis.Redis(host='192.168.188.128', port=6379, db=0)
    r.hset(key, field, value)  # 写入


def random_str(n):
    # 生成制定长度的字符串：大小写字母+数字
    str_a = ''
    for i in range(n):
        str_a = str_a + str(random.choice(string.ascii_letters + string.digits))
    return str_a


for i in range(10):
    write_hash_redis('row_' + str(i), 'col_a', random_str(10))
