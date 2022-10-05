#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/9/28 21:52
"""
import sys
sys.path.append(r"D:\PycharmProjects\interface_test_mock")
import pymysql
import pytest


class SqlUtil:
    def connect_(self, user, password, host, database, port, func):
        conn = pymysql.connect(user=user,
                               password=password,
                               host=host,
                               database=database,
                               port=port,
                               charset="utf-8")
        cur = conn.cursor()
        cur.execute(func)
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return data

    def search_(self):
        sql = 'select c.score from student s, course c where s.studentid = c.studentid group by studentid'
        return sql

    def insert_(self):
        pass

    def update_(self):
        pass

    def delete_(self):
        pass

    def user(self):
        user = {
            'Millie': '123456',
            'Jordan': '123456',
            'Lemon': '123456',
            'Adreona': '123456'
        }
        return user
