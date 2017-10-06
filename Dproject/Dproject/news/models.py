from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    '''新闻分类表'''
    def __str__(self):
        return self.cag_name
    cag_name = models.CharField(max_length=50) #max_length指定最大长度，id默认自己会添加

class NewsInfo(models.Model):
    '''定义新闻信息类'''
    def __str__(self):
        return self.news_title

    news_title = models.CharField(max_length=50) #定义新闻标题
    news_content = models.TextField(max_length=5000)#定义新闻内容
    news_category = models.ForeignKey(NewsCategory)#定义新闻分类此处使用外键