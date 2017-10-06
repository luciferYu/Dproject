from django.test import TestCase
from .models import * #通过相对路径引入模块
# Create your tests here.

#1.插入数据
news_cag = NewsCategory() #创建分类对象
news_cag.cag_name = '军事新闻'
news_cag.save() #调用模型类的save方法，即可向数据库中添加数据


news_info = NewsInfo()# 创建一条新闻信息对象
news_info.news_title = '中国8艘核动力航母已经部署到太平洋地区'
news_info.news_content = '据路边社报道，中国8艘核动力航母已部署到太平洋地区，随时准备和美国对抗，将美军赶出亚太地区'
news_info.news_category = news_cag  # 将news_cag对象作为新闻分类的外键，实际会讲news_cag的id作为值
news_info.save() #保存记录
