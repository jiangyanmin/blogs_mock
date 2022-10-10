#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/9/25 23:44
"""
# import sys
# sys.path.append(r"D:\PycharmProjects\interface_test_mock")
import yaml
import os


class ExtractUtil:
    def __init__(self, filepath):
        self.filepath = filepath

    # 读取动态参数 os.path.dirname(os.path.abspath(__file__))
    def read_yaml(self):
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            # print(os.getcwd())
            return yaml.load(stream=f, Loader=yaml.FullLoader)

    # 读取测试用例数据
    def read_case_yaml(self):
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            # print(os.getcwd())
            cases = yaml.load_all(stream=f, Loader=yaml.FullLoader)
            for case in cases:
                return case

    # 写入
    def write_yaml(self, data):
        with open(self.filepath, mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, encoding='utf-8')

    # 清除
    def clean_yaml(self):
        with open(self.filepath, mode='w', encoding='utf-8') as f:
            f.truncate()


# if __name__=='__main__':
#     s = ExtractUtil('D:\\PycharmProjects\\blogs_mock\\data\\login_case.yaml')  #/testcase/mock_yamls
#     print(s.read_case_yaml()[0]['res']['status_code'])
#
#

