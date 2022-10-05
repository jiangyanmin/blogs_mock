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

from common.extract_util import ExtractUtil


@pytest.fixture(scope='class',  autouse=True)  # params=['a'],
def clear():
    """清除所有类执行之前先清空yaml文件内容"""
    # print(os.getcwd())
    # print(os.path.dirname(os.path.abspath(__file__)))
    # print('hhhhhhh')
    ExtractUtil(os.getcwd()+'/common/extract_dynamic_util.yaml').clean_yaml()
