#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/10/5 23:02
"""
from common.extract_util import ExtractUtil as eu


class CaseUtil:
    """获取测试用例测试数据"""
    def case_util(self, filepath):
        cases = eu(filepath).read_case_yaml()
        pass