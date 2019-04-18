#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yunongxin
# @Date: 2019-04-18

"""定义learning_logs的url模式"""

from django.urls import path
from . import views #导入视图

app_name = 'learning_logs' #必须包含该app的命名空间，否则会报错

urlpatterns = [
    #主页
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics'),
    #特定主页的详细页面
    path('topics/<int:topic_id>/', views.topic, name = 'topic')
]