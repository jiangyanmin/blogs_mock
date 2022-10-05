#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/9/24 19:08
"""
import sys
sys.path.append(r"D:\PycharmProjects\interface_test_mock")
import requests


class AllRequestMethod:
    def __init__(self):
        pass

    def request_method(self, method, url, **kwargs):
        print('---------------------------')
        sess = requests.session()
        req = sess.request(method, url, **kwargs)
        return req