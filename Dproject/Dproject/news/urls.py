#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'index/$',index),#将 访问news/index/ 与 index函数做绑定
]




if __name__ == '__main__':
    pass