# -*- coding: utf-8 -*-

import requests


class BaseWechat(object):
    def __init__(self):
        self.API_DOMAIN = 'https://api.weixin.qq.com'
        self.OPEN_DOMAIN = 'https://open.weixin.qq.com'
        self.MCH_DOMAIN = 'https://api.mch.weixin.qq.com'

    def get(self, url, verify=False, toencoding=True, tojson=True, res_processor_func=None, **kwargs):
        # When ``verify=True`` and ``cacert.pem`` not match ``https://xxx.weixin.qq.com``, will raise
        # SSLError: [Errno 1] _ssl.c:510: error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed
        res = requests.get(url.format(**kwargs), verify=verify)
        if toencoding:
            res.encoding = 'utf-8'
        if res_processor_func:
            return res_processor_func(res)
        return res.json() if tojson else res

    def post(self, url, verify=False, toencoding=True, tojson=True, res_processor_func=None, **kwargs):
        res = requests.post(url, verify=verify, **kwargs)
        if toencoding:
            res.encoding = 'utf-8'
        if res_processor_func:
            return res_processor_func(res)
        return res.json() if tojson else res
