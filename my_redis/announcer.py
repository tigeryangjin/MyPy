# announcer.py 发布者
# !/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper

obj = RedisHelper()
obj.public('hello')
