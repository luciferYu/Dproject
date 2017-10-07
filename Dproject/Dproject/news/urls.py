#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'index/$',index),#将 访问news/index/ 与 index函数做绑定
    url(r'news_detail/(\d+).html',news_detail)
]




if __name__ == '__main__':
    pass