#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yunongxin
# @Date: 2019-04-19

from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''} #不生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # 定义一个HTML小部件，提供一个文本区域