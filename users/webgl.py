#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'zwq'
__data__ = '2017/4/27 10:01'


import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}


class WGL(object):
    def getPoint(self,ip):
        post_url = "https://api.prprpr.me/location/?ip={0}".format(ip)
        re = requests.get(post_url, headers=headers)
        data = json.loads(re.text)
        return data