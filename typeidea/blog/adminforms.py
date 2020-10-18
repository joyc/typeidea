#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : adminforms.py
# @Author : Hython
# @Dec    : 自定义 Form，文章描述字段改用 textarea 展示
from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label="是否删除", required=True)  # TODO: 处理布尔类型为需要的字段
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
