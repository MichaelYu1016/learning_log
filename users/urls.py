#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yunongxin
# @Date: 2019-04-19

from django.urls import path
from django.contrib.auth.views import LoginView # Django2.0登录视图和1.X不一样了

from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(template_name= 'users/login.html'), name = 'login'),
    # 注销页面
    path('logout/', views.logout_view, name = 'logout'),
    # 注册页面
    path('register/', views.register, name = 'register'),
]