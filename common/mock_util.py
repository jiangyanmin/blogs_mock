#! \usr\bin\python
# -*-coding:utf-8 -*-
"""
# Author : jiangym
# Time : 2022/9/29 23:31
"""
# import sys
# sys.path.append(r"D:\PycharmProjects\interface_test_mock")
import json
import flask
import hashlib

from sql_util import SqlUtil


server = flask.Flask(__name__)   # 创建一个服务，把当前这个python文件当做一个服务


@server.route('/login', methods=['post'])
def login_server():   # 登录接口
    if flask.request.is_json:
        name = flask.request.json.get('name')  # 获取json请求的参数值name
        password = flask.request.json.get('password')  # 获取json请求的参数值password
        path = flask.request.path
        print(path)
        method = flask.request.method
        print(method)
        if name in SqlUtil().user() and SqlUtil().user()[name] == password:  # 用户名和密码正确
            data = {'name': name,
                    'password': hashlib.sha256(password.encode('utf-8')).hexdigest(),
                    'access_token': hashlib.md5('12345678'.encode('utf-8')).hexdigest()
                    }
            res = flask.make_response(json.dumps(data, ensure_ascii=False))  # 构造接口响应体
            res.headers = {'content-length': res.content_length}  # 构造接口响应头
            res.status_code = '200'  # 构造接口状态码
        else:
            data = {'msg': '用户名或密码错误！'}
            res = flask.make_response(json.dumps(data, ensure_ascii=False))
            res.status_code = '400'
        if path != '/login' or method not in ['POST', 'post']:  # 接口路径错误，返回404
            data = json.dumps({'msg': '找不到资源！'}, ensure_ascii=False)
            res = flask.make_response(data)
            res.status_code = '404'

        return res
    else:
        return json.dumps({"msg": '请传json格式参数！'}, ensure_ascii=False)


@server.route('/blogs/edit', methods=['post'])
def edit_server():   # 编辑博客接口
    if flask.request.json:  # 规定请求体必须为json格式
        path = flask.request.path
        method = flask.request.method
        access_token = flask.request.headers.get('access_token')
        title = flask.request.json.get('title')
        if access_token == hashlib.md5('12345678'.encode('utf-8')).hexdigest() and title:  # 规定请求头必须带上access_token
            data = json.dumps({"response": "save succeed"}, ensure_ascii=False)
            res = flask.make_response(data)
            res.headers = {'content-length': res.content_length}
            res.status_code = '200'
        elif access_token != hashlib.md5('12345678'.encode('utf-8')).hexdigest():
            res = flask.make_response(json.dumps({'msg': '鉴权失败！'}, ensure_ascii=False))
            res.status_code = '401'
        elif title is None:  # 规定博客标题不能为空
            data = json.dumps({'msg': '参数异常！'}, ensure_ascii=False)
            res = flask.make_response(data)
            res.status_code = '400'
        else:
            data = json.dumps({'msg': '未知异常！'}, ensure_ascii=False)
            res = flask.make_response(data)
            res.status_code = '500'

        return res
    else:
        return json.dumps({'msg': '请传json格式参数！'}, ensure_ascii=False)


if __name__ == '__main__':
    server.run(host='127.0.0.1', port=8888, debug=True)  # 执行响应端口、host

