#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LoveNight

import requests
import time
import json
import os
import re
import sys
import subprocess
from bs4 import BeautifulSoup as BS


class ZhiHuClient(object):
    """连接知乎的工具类，维护一个Session
    2015.11.11

    用法：

    client = ZhiHuClient()

    # 第一次使用时需要调用此方法登录一次，生成cookie文件
    # 以后可以跳过这一步
    client.login("username", "password")

    # 用这个session进行其他网络操作，详见requests库
    session = client.getSession()
    """

    # 网址参数是账号类型
    TYPE_PHONE_NUM = "phone_num"
    TYPE_EMAIL = "email"
    loginURL = r"http://www.zhihu.com/login/{0}"
    homeURL = r"http://www.zhihu.com"
    captchaURL = r"http://www.zhihu.com/captcha.gif"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.zhihu.com",
        "Upgrade-Insecure-Requests": "1",
    }

    captchaFile = os.path.join(sys.path[0], "captcha.gif")
    cookieFile = os.path.join(sys.path[0], "cookie")

    def __int__(self):
        os.chdir(sys.path[0])
