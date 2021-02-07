# Author Cuber
# coding=utf-8
# @Time    : 2021/2/2 11:43
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from django.conf.urls import url
from apps.website import views as webViews
from apps.workers import views as userViews

app_name = 'website'  # 指定应用名，在使用{% url ' ' %} 引用链接时就可以套用对应应用名下的模板
urlpatterns = [
    url(r'login', userViews.Login.as_view(), name='login'),  # 登陆验证
    url(r'logout', userViews.Logout, name='logout'),
    url(r'register', userViews.Register.as_view(), name='register'),  # 登陆验证
    # url(r'^dashboard$', webViews.Dashboard.as_view()),  # 登陆验证
    # url(r'^charts$', webViews.Chart.as_view()),  # 登陆验证
    # url(r'^devices', webViews.Device.as_view()),  # 登陆验证
    # url(r'^streams', webViews.Stream.as_view()),  # 登陆验证
    # url(r'^console', webViews.Console.as_view()),  # 登陆验证
    # url(r'^triggers', webViews.Trigger.as_view()),  # 登陆验证
]
