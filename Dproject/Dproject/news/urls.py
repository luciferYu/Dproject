#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'index.html$',index,name='index'),#将 访问news/index/ 与 index函数做绑定
    url(r'detail_(\d+).html',news_detail,name='detail'),
    url(r'^areas/(?P<aid>\d{6})?$',areas_query,name='areas_query')
]




if __name__ == '__main__':
    pass