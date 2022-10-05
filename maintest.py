#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/9/22 15:24
"""
# import sys
# sys.path.append(r"D:\PycharmProjects\interface_test_mock")
import pytest
import time
import os
import re

if __name__ == '__main__':
    pytest.main()
    time.sleep(10)
    os.system("allure generate ./temps -o ./reports --clean")

