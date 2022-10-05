#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/9/24 19:04
"""
# import sys
# sys.path.append(r"D:\PycharmProjects\interface_test_mock")
import hashlib
import pytest
import os
import json

from common.request_util import AllRequestMethod as qm
from common.extract_util import ExtractUtil

yaml_extract = ExtractUtil(os.getcwd() + '/common/extract_dynamic_util.yaml')  # 获取动态参数
login_cases = ExtractUtil(os.getcwd() + '/data/login_case.yaml').read_case_yaml()  # 获取登录接口测试用例数据


class TestCnblogs:
    def setup_class(self):
        print('测试用例开始执行')

    @pytest.fixture()
    def send(self, request):   # request.param是pytest内request传参固定用法，用于接收传入的值并调用
        method = request.param[0]
        url = request.param[1]
        data = request.param[2]
        headers = request.param[3]
        # print(method)  # post
        res = qm().request_method(method=method, url=url, json=data, headers=headers)  #
        # return json.loads(json.dumps(res).replace(r'\\', '\\'))  #, data, headers
        return res

    @pytest.mark.smoke
    @pytest.mark.parametrize('send',
                             [(login_cases[0]["method"], login_cases[0]["url"],
                               login_cases[0]["data"], login_cases[0]["headers"])],
                             ids=[login_cases[0]["describe"]],
                             indirect=True)
    def test_01_login(self, send):
        res = send
        # 获取access_token
        access_token = res.json().get("access_token")
        # 将access_token写入yaml文件
        yaml_extract.write_yaml({"access_token": access_token})
        assert res.status_code == login_cases[0]['res']['status_code']
        assert res.json().get("name") == login_cases[0]['res']['name']
        assert res.json().get("password") == hashlib.sha256(login_cases[0]['res']['password'].encode('utf-8')).hexdigest()

    @pytest.mark.smoke
    @pytest.mark.parametrize('send',
                             [(login_cases[1]["method"], login_cases[1]["url"],
                               login_cases[1]["data"], login_cases[1]["headers"])],
                             ids=[login_cases[1]["describe"]],
                             indirect=True)
    def test_02_login(self, send):
        res = send
        # print(res.json())
        assert res.status_code == login_cases[1]["res"]["status_code"]
        assert res.json()['msg'] == login_cases[1]["res"]['msg']

    @pytest.mark.smoke
    @pytest.mark.parametrize('send',
                             [(login_cases[2]["method"], login_cases[2]["url"],
                               login_cases[2]["data"], login_cases[2]["headers"])],
                             ids=[login_cases[2]["describe"]],
                             indirect=True)
    def test_03_login(self, send):
        res = send
        # print(res.json())
        assert res.status_code == login_cases[2]["res"]["status_code"]
        assert res.json()['msg'] == login_cases[2]["res"]['msg']

    @pytest.mark.smoke
    @pytest.mark.parametrize('send',
                             [(login_cases[3]["method"], login_cases[3]["url"],
                               login_cases[3]["data"], login_cases[3]["headers"])],
                             ids=[login_cases[3]["describe"]],
                             indirect=True)
    def test_04_login(self, send):
        res = send
        print(res.status_code)
        assert res.status_code == login_cases[3]["res"]["status_code"]
        # assert res.json() == {'msg': '找不到资源！'}11

    # @pytest.mark.smoke
    # @pytest.mark.parametrize("send",
    #                          [("post", "http://127.0.0.1:8888/blogs/edit",
    #                            {"title":"this is a test case for success!", "content":"this is a test case for success!"},
    #                            {'access_token': yaml_extract.read_yaml()['access_token'], 'content-type': 'application/json'}),
    #                           ("post", "http://127.0.0.1:8888/blogs/edit",
    #                            {"title":"this is a test case for failure!", "content":"this is a test case for failure!"},
    #                            {'access_token': '123456', 'content-type': 'application/json'}),
    #                           ("post", "http://127.0.0.1:8888/blogs/edit",
    #                            {"title": "",
    #                             "content": "this is a test case for failure!"},
    #                            {'access_token': yaml_extract.read_yaml()['access_token'], 'content-type': 'application/json'})
    #                           ],
    #                          ids=['保存博客成功', '鉴权失败，保存博客失败', '未写标题，保存博客失败'],
    #                          indirect=True)
    # def test_11_edit(self, send):
    #     res = send
    #     data = send
    #     headers = send
    #     access_token = headers['access_token']
    #     if access_token == yaml_extract.read_yaml()['access_token'] and data['title']:
    #         assert res.status_code == 200
    #         assert res.json() == {"response": "save succeed"}
    #     elif access_token != yaml_extract.read_yaml()['access_token']:
    #         assert res.status_code == 401
    #         assert res.json() == {'msg': '鉴权失败！'}
    #     elif data['title'] is None:
    #         assert res.status_code == 400
    #         assert res.json() == {'msg': '参数异常！'}
    #     else:
    #         assert res.status_code == 500
    #         assert res.json() == {'msg': '未知异常！'}

    def teardown_class(self):
        print('测试用例全部执行结束')


