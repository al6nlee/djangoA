#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/7
# @Author  : alan
# @File    : views.py
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
