from django.shortcuts import render
from django.http import HttpResponse,JsonResponse # 导入http响应类 用做视图的返回对象
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

def areas_query(request,**kwargs):  # 用来处理显示城市的网页
    if kwargs['aid']:
        areas_list = areas.objects.filter(pid=kwargs['aid'])  # 如果存在父城市的编号，则获取所有该父城市的子城市
        ptitle = areas.objects.get(aid=kwargs['aid']).atitle
    else:
        areas_list = areas.objects.filter(pid=None) # 如果没有父城市穿过来，则说明访问的是主页
        ptitle = '首页'
    return render(request,'areas.html',locals())


def hero_all(request):
    '''显示所有逻辑未删除的英雄'''
    hero_list = HeroInfo.objects.logical_all()
    return render(request,'hero_all.html',locals())

def hero_delete(request):
    '''逻辑删除某个用户'''
    hero_id = request.GET.get('id')
    HeroInfo.objects.remove_hero(hero_id)
    return render(request,'hero_delete.html')

def calc(request):  # 返回简易计算机页面
    return render(request,'简易计算器.html')

def ajax(request):  # 处理简易计算机传来的ajax请求
    num1 = int(request.GET.get('num1',''))
    num2 = int(request.GET.get('num2',''))
    method = request.GET.get('method','')
    result = 0
    if method == '1':  # 加法
        result = num1 + num2
    elif method == '2':  # 减法
        result = num1 - num2
    elif method == '3':  # 乘法
        result = num1 * num2
    elif method == '4':  # 除法
        result = num1 / num2
    return JsonResponse({'result':result})  # 返回json响应

def post(request):
    return render(request,'mypost.html')

def posted(request):
    if request.method == 'POST':
        name = request.POST['username']
        content = '姓名:' + name + '  '
        if request.POST['sex'] == '0':
            content += '性别：男 '
        elif request.POST['sex'] == '1':
            content += '性别：女 '
        hobby_list = request.POST.getlist('hobby')
        if hobby_list:
            content += '爱好：'
        for hobby in hobby_list:
            if hobby == '1':
                content += ' 胸口碎大石'
            if hobby == '2':
                content += ' 脚踩电灯泡'
            if hobby == '3':
                content += ' 口吐火'
    return render(request, 'mypost.html',locals())