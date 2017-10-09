from django.shortcuts import render
from django.http import HttpResponse # 导入http响应类 用做视图的返回对象
from django.template import loader
from .models import *
# Create your views here.
def index(request): #最简易视图
    #return HttpResponse('hello django!!')
    cags = NewsCategory.objects.all()  #获取所有的分类对象
    title = '新闻首页'  #设置网页标头
    return render(request,'index.html',locals()) #进行替换

def news_detail(request,cag_id):#用来处理新闻详细页的函数
    detail_news = NewsInfo.objects.filter(news_category_id=cag_id) # 获取多条网页新闻
    title = NewsCategory.objects.get(id=cag_id).cag_name #从多条详细新闻获取这个新闻的类型，设置到网页标头
    return render(request,'news.html',locals())

def areas_query(request,aid):  # 用来处理显示城市的网页
    if aid:
        areas_list = areas.objects.filter(pid=aid)  # 如果存在父城市的编号，则获取所有该父城市的子城市
    else:
        areas_list = areas.objects.filter(pid=None) # 如果没有父城市穿过来，则说明访问的是主页
    return render(request,'areas.html',locals())