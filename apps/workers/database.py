# Author Cuber
# coding=utf-8
# @Time    : 2021/2/3 22:18
# @Site    : 
# @File    : database.py
# @Software: PyCharm
import time

from django.contrib.auth.hashers import make_password
from django.db import transaction
from apps.workers import models


def register(username, password, password2):
    """
    注册用户

    :param username: 用户名（唯一的）
    :param password: 密码
    :param password2: 二次输入的密码
    :return: {'code': 0, 'message': '', 'data': {'username': ""}}
    """
    res = {'code': 0, 'message': '', 'data': {}}
    # 检查参数是否正确
    if not username or not password or not password2:
        res['code'] = 1
        res['message'] = '参数错误'
        return res
    if password != password2:
        res['code'] = 1
        res['message'] = '两次密码输入不一致'
    # 检查用户名是否重复
    if models.GUser.objects.filter(username=username).first():
        res['code'] = 2
        res['message'] = "用户名已存在"
        return res
    try:
        encode_psw = make_password(password)
        # 使用django自带的加密方法make_password对密码加密
        # 并可通过check_password(post_password,database_password)方法，进行校验密码是否与数据库的一致，返回boolean值
        with transaction.atomic():  # 出错回滚
            models.GUser.objects.create(username=username, password=encode_psw)
            res['message'] = 'Succeed'
            res['data']['username'] = username
    except Exception as e:
        res['code'] = 3
        res['message'] = e.__repr__()
    return res
