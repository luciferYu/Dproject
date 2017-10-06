from django.shortcuts import render
from django.http import HttpResponse # 导入http响应类 用做视图的返回对象
from django.template import loader
from .models import *
# Create your views here.
def index(request): #最简易视图
    #return HttpResponse('hello django!!')
    cags = NewsCategory.objects.all()
    html = ''
    for cag in cags:
        html = html + '<li><a href="">' + cag.cag_name + '</a></li>'
    data = {'title':'新闻首页','content':html}
    return render(request,'index.html',data)

