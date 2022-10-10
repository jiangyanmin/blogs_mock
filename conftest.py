#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/9/25 16:33
"""
# import sys
# sys.path.append(r"D:\PycharmProjects\interface_test_mock")
import os
import pytest

from common.request_util import AllRequestMethod as qm
from common.extract_util import ExtractUtil


@pytest.fixture(scope='class', autouse=True)
def send(request):   # request.param是pytest内request传参固定用法，用于接收传入的值并调用
    method = request.param[0]
    url = request.param[1]
    data = request.param[2]
    headers = request.param[3]
    # print(method)  # post
    res = qm().request_method(method=method, url=url, json=data, headers=headers)  #
    # return json.loads(json.dumps(res).replace(r'\\', '\\'))  #, data, headers
    return res


@pytest.fixture(scope='class',  autouse=True)  # params=['a'],
def clear():
    """清除所有类执行之前先清空yaml文件内容"""
    # print(os.getcwd())
    # print(os.path.dirname(os.path.abspath(__file__)))
    # print('hhhhhhh')
    ExtractUtil(os.getcwd()+'/common/extract_dynamic_util.yaml').clean_yaml()
