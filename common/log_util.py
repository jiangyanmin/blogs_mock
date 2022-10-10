#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/10/6 15:53
"""
import logging
from logging.handlers import RotatingFileHandler
import os

path = os.getcwd() + '/logs'   # os.path.dirname(os.path.abspath(__file__)_
print(path)


def log_util(filename):
    # 日志收集器
    logger = logging.getLogger(filename)
    # 日志收集器级别
    logger.setLevel('INFO')

    # 日志输出格式
    fmt = logging.Formatter('%(asctime)s  %(pathname)s  %(module)s  %(lineno)d  %(levelname)s  %(message)s')

    # 文件日志处理器
    file_handler = RotatingFileHandler(os.path.join(path, filename), mode='a', maxBytes=10*1024*1024, backupCount=10, encoding='utf-8')
    # 文件日志处理器级别
    file_handler.setLevel('INFO')
    # 文件处理器日志输出格式
    file_handler.setFormatter(fmt)

    # 控制台日志处理器
    console_handler = logging.StreamHandler()
    # 控制台日志处理器级别
    console_handler.setLevel('INFO')
    # 控制台日志输出格式
    console_handler.setFormatter(fmt)

    # 日志收集器和处理器对接，指定输出渠道
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# if __name__ == '__main__':
#     log = log_util('run.log')
#     log.info('hhhh')
