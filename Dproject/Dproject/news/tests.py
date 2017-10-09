from django.test import TestCase
from .models import * #通过相对路径引入模块
import random
# Create your tests here.

#1.插入数据
# news_cag = NewsCategory() #创建分类对象
# news_cag.cag_name = '军事新闻'
# news_cag.save() #调用模型类的save方法，即可向数据库中添加数据
#
#
# news_info = NewsInfo()# 创建一条新闻信息对象
# news_info.news_title = '中国8艘核动力航母已经部署到太平洋地区'
# news_info.news_content = '据路边社报道，中国8艘核动力航母已部署到太平洋地区，随时准备和美国对抗，将美军赶出亚太地区'
# news_info.news_category = news_cag  # 将news_cag对象作为新闻分类的外键，实际会讲news_cag的id作为值
# news_info.save() #保存记录

#2.修改数据
# news_info = NewsInfo.objects.get(id=1) #取出id为1的记录
# print(news_info)  #打印该对象，可以定义一个__str__方法改变显示
#
# news_info.news_title = '中国航母新标题'  #设置新标题
# news_info.save()  #保存修改

#3.查询数据
# news_list = NewsInfo.objects.all() #获得所有新闻信息数据
# print('获取所有新闻信息数据:'+ str(news_list))
# news_info = NewsInfo.objects.get(pk=1) #获得某条记录
# print('获得一条新闻数据:'+ str(news_info))

#4.删除数据
# news_info = NewsInfo.objects.get(pk=1) #先获取某条记录
# news_info.delete() #调用对象的delete()方法删除

# #图书数据
# book_list = ['射雕英雄传', '天龙八部', '笑傲江湖', '雪山飞狐']
# # 创建测试数据
# for book_name in book_list:
#     # 创建图书对象
#     book = BookInfo()
#     # 字段赋值
#     book.book_title = book_name
#     book.book_comment = random.randint(1, 100)
#     book.book_read = random.randint(1, 100)
#     book.book_delete = False
#     # 保存图书信息
#     book.save()
#
# # 英雄数据
# hero_list = [
#     {'name': '郭靖', 'sex': 1, 'desc': '降龙十八掌', 'book': 1},
#     {'name': '黄蓉', 'sex': 0, 'desc': '打狗棍法', 'book': 1},
#     {'name': '黄药师', 'sex': 1, 'desc': '弹指神通', 'book': 1},
#     {'name': '欧阳锋', 'sex': 1, 'desc': '蛤蟆功', 'book': 1},
#     {'name': '梅超风', 'sex': 0, 'desc': '九阴白骨爪', 'book': 1},
#     {'name': '乔峰', 'sex': 1, 'desc': '降龙十八掌', 'book': 2},
#     {'name': '段誉', 'sex': 1, 'desc': '六脉神剑', 'book': 2},
#     {'name': '虚竹', 'sex': 1, 'desc': '天山六阳掌', 'book': 2},
#     {'name': '王语嫣', 'sex': 0, 'desc': '神仙姐姐', 'book': 2},
#     {'name': '令狐冲', 'sex': 1, 'desc': '独孤九剑', 'book': 3},
#     {'name': '任盈盈', 'sex': 0,'desc': '弹琴', 'book': 3},
#     {'name': '岳不群', 'sex': 1, 'desc': '华山剑法', 'book': 3},
#     {'name': '东方不败', 'sex': 1, 'desc': '葵花宝典', 'book': 3},
#     {'name': '胡斐', 'sex': 1, 'desc': '胡家刀法', 'book': 4},
#     {'name': '苗若兰', 'sex': 0, 'desc': '黄衣', 'book': 4},
#     {'name': '程灵素', 'sex': 0, 'desc': '医术', 'book': 4},
#     {'name': '袁紫衣', 'sex': 0, 'desc': '六合拳', 'book': 4},
# ]
#
# # 创建测试数据
# for hero_info in hero_list:
#     # 创建英雄类
#     hero = HeroInfo()
#     # 字段赋值
#     hero.hero_name = hero_info['name']
#     hero.hero_desc = hero_info['desc']
#     hero.hero_sex = hero_info['sex']
#     hero.hero_delete = False
#     hero.hero_book_id = hero_info['book']
#     # 保存对象
#     hero.save()




# hero =  HeroInfo.objects.get(pk=1)
# print(hero, hero.hero_book)
#
#
# book = BookInfo.objects.get(pk=1)
#
# hero_list = book.heroinfo_set.all()
# print(hero_list)


# book = BookInfo.objects.get(pk=3)  # 获得一本书
# book.delete()  # 级联删除
#
#以下进行查询集测试
#查询方法如下
# (Dproject) C:\Users\lucifer\Desktop\learnpython\python_advan\stage04\作业\day01\Dproject>Scripts\python.exe Dproject\manage.py test news
# <QuerySet [<HeroInfo: 郭靖>, <HeroInfo: 乔峰>]>
# Creating test database for alias 'default'...
# System check identified no issues (0 silenced).



#exact
# hero_list = HeroInfo.objects.filter(hero_sex__exact=True)  # 查询所有性别为男性的对象
# print(hero_list)

#contains
# hero_list = HeroInfo.objects.filter(hero_desc__contains='八') #查询描述中带有8的英雄
# print(hero_list)

#startswith endswith
# hero_list = HeroInfo.objects.filter(hero_desc__startswith='六')  # 查询以六开头的英雄描述
# print([ hero.hero_desc for hero in hero_list])

#in
# hero_list = HeroInfo.objects.filter(pk__in=[1,3,5])
# print(hero_list)

# gt gte lt lte
# hero_list = HeroInfo.objects.filter(pk__gt=3)
# print(hero_list)

# exclude　按照条件反方向查找
# hero_list = HeroInfo.objects.exclude(pk__gt=3)
# print(hero_list)

# get
# try:
#     book = BookInfo.objects.get(pk=20)
# except BookInfo.DoesNotExist:
#     book = BookInfo()
#     book.id = 20
#     book.book_read = random.randint(1, 100)
#     book.book_comment = random.randint(1, 100)
#     book.book_title = '大话西游'
#     book.save()


# F对象
# book_list = BookInfo.objects.filter(book_comment__gte=models.F('book_read'))
# print(book_list) # 查询评论数比阅读量大的书
#
#
# book_list = BookInfo.objects.filter(book_comment__gte=models.F('book_read')*2)
# print(book_list) # 查询评论数大于阅读量两倍书

# Q对象
# book_list = BookInfo.objects.filter(book_read__gt=20).filter(pk__gt=2)
# print(book_list)  #查询阅读量大于20且主键大于2的书

# Ｑ对象支持　&(与) |(或)
# book_list = BookInfo.objects.filter( models.Q(book_read__gt=20) & models.Q(pk__gt=2) )
# print(book_list) #查询图书的阅读量大于20并且id大于2的书
#
# book_list = BookInfo.objects.filter( models.Q(book_read__gt=20) | models.Q(pk__gt=2) )
# print(book_list) #查询图书的阅读量大于20或者id大于2的书

# 通过模型类实现关联查询
# book_list = BookInfo.objects.filter(heroinfo__hero_desc__contains='八')
# print(book_list)  # 查询英雄的描述中含有八的图书记录

# book_list = HeroInfo.objects.filter(hero_book__book_title='天龙八部')
# print(book_list) #查询属于天龙八部这本书的所有英雄


# 结果集排序
# hero_list = HeroInfo.objects.order_by('-id')
# print(hero_list)  # 按照ID倒序排列结果


# hero_list = HeroInfo.objects.filter(id__gt=2).order_by('-id')
# print(hero_list)  #设置筛选条件的倒序


#测试自定义管理器
# hero_list = HeroInfo.objects.all()
# print(hero_list)
# try:
#     guojing = HeroInfo.objects.get(hero_name='郭靖')
#     guojing.hero_delete = True
#     guojing.save()
# except:
#     print('删除失败')
#hero_list = HeroInfo.objects.all()
# print()
#print(hero_list)

# hero_list = HeroInfo.objects.all()
# print(hero_list)
# #HeroInfo.objects.remove_hero('黄蓉')
# HeroInfo.objects.remove_hero('无名氏为了触发失败')
# print()
# hero_list = HeroInfo.objects.all()
# print(hero_list)

areas_list = areas.objects.all()
print(areas_list)