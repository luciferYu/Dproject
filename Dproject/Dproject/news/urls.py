#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index.html$',index,name='index'),#将 访问news/index/ 与 index函数做绑定
    url(r'detail_(\d+).html',news_detail,name='detail'), #新闻详细页url
    url(r'^areas/(?P<aid>\d{6})?$',areas_query,name='areas_query'), #地区自关联查询url
    url(r'^hero/index.html$',hero_all,name='hero_all'), #英雄首页
    url(r'^hero/delete.html$',hero_delete,name='hero_delete'), #英雄删除页
    url(r'^calc/$',calc),#计算器页面
    url(r'ajax/result.json$',ajax), #计算器ajax请求页面
    url(r'^post/$',post), # 提交前
    url(r'^posted/$',posted), # 提交后
    url(r'^upload/$',upload), #上传文件
    url(r'^upload_handle/',upload_handle)
]




if __name__ == '__main__':
    pass