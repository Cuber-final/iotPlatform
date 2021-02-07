from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render, HttpResponse
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser
from . import database, models

from .forms import UserLoginForm, UserRegisterForm


# JSonResponse 前端不用反序列化，只能传输字典，不能传输字符串。


# 登录操作
class Login(APIView):
    parser_classes = [JSONParser, FormParser]  # 指定数据解析器
    authentication_classes = []

    def post(self, request):
        # username = request.data.get('username', None)
        # password = request.data.get('password', None)
        user_login_form = UserLoginForm(data=request.POST)

        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据,返回对应模型统一格式的字段
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作并且保持的是非永久登录状态直至网页关闭
                login(request, user)
                return redirect("homepage")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")

    def get(self, request):
        return render(request, 'website/login.html')


# 登出操作
def Logout(request):
    logout(request)
    return redirect('homepage')


# 注册用户
class Register(APIView):
    # 以下通过直接截取POST的数据的方法实现注册
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        password2 = request.data.get('password2', None)
        res = database.register(username, password, password2)
        if res['message'] == 'Succeed':
            # 注册成功则直接跳转至主页并维持登录状态
            user = models.GUser.objects.filter(username=username).first()
            login(request, user)
            return redirect('homepage')
        # 注册失败返回错误提示
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type='application/json', )

    def get(self, request):
        return render(request, 'website/register.html')
