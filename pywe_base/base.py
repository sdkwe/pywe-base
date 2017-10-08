# -*- coding: utf-8 -*-

import json

import requests
from pywe_xml import dict_to_xml


class BaseWechat(object):
    def __init__(self):
        self.API_DOMAIN = 'https://api.weixin.qq.com'
        self.OPEN_DOMAIN = 'https://open.weixin.qq.com'
        self.MCH_DOMAIN = 'https://api.mch.weixin.qq.com'

    def get(self, url, verify=False, encoding='utf-8', res_to_encoding=True, res_to_json=True, res_processor_func=None, resjson_processor_func=None, **kwargs):
        # When ``verify=True`` and ``cacert.pem`` not match ``https://xxx.weixin.qq.com``, will raise
        # SSLError: [Errno 1] _ssl.c:510: error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed
        res = requests.get(url.format(**kwargs), verify=verify)
        if res_to_encoding:
            res.encoding = encoding
        if res_processor_func:
            return res_processor_func(res)
        if not res_to_json:
            return res
        resjson = res.json()
        return resjson_processor_func(resjson) if resjson_processor_func else resjson

    def post(self, url, verify=False, encoding='utf-8', data_to_json_str=True, data_to_xml_str=False, res_to_encoding=True, res_to_json=True, res_processor_func=None, resjson_processor_func=None, **kwargs):
        if data_to_json_str:
            data = kwargs.get('data', {})
            if isinstance(data, dict):
                kwargs['data'] = json.dumps(data)
        if data_to_xml_str:
            data = kwargs.get('data', {})
            if isinstance(data, dict):
                kwargs['data'] = dict_to_xml(data)
        res = requests.post(url, verify=verify, **kwargs)
        if res_to_encoding:
            res.encoding = encoding
        if res_processor_func:
            return res_processor_func(res)
        if not res_to_json:
            return res
        resjson = res.json()
        return resjson_processor_func(resjson) if resjson_processor_func else resjson
