# Author Cuber
# coding=utf-8
# @Time    : 2021/2/6 16:43
# @Site    : 
# @File    : forms.py
# @Software: PyCharm


from django import forms

from .models import GUser


# 对于与用户而非管理的这类对象，不需要对数据库进行交互改动的，通过集成forms.Form来自行配置字段信息
# 对于管理员则通过继承forms.ModelForm

# 登录表单
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 注册表单
class UserRegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()

    # 定义校验方法
    def clean_password(self):
        # 校验密码的合法性，不能为纯数据
        password = self.cleaned_data.get("password")
        if password.isdecimal():
            raise forms.ValidationError("密码不能为纯数字！")
        return password

    def clean_r_password(self):
        # 校验密码的合法性，不能为纯数据
        r_password = self.cleaned_data.get("password2")
        if r_password.isdecimal():
            raise forms.ValidationError("密码不能为纯数字！")
        return r_password

    # 定义全局钩子
    def clean(self):
        # 校验两次密码输入是否一致
        if self.cleaned_data.get("password") != self.cleaned_data.get("password2"):
            self.add_error("password2", "两次密码输入不一致！")
        else:
            return self.cleaned_data

