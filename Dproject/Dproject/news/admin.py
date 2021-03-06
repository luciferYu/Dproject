from django.contrib import admin
from .models import * #导入模型类

class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','news_title','news_content','news_category'] #显示的内容
    list_filter = ['news_title']#过滤字段
    search_fields = ['news_content']#搜索字段 搜索会出现在左上侧
    list_per_page = 10 #分页


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cag_name'] #显示的内容

@admin.register(HeroInfo)  #另一种注册方法使用装饰器注册
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hero_name','hero_desc']

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['book_title','book_comment','book_read']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','news_title','news_content']


# Register your models here.
admin.site.register(NewsInfo,NewsInfoAdmin)#注册新闻分类
admin.site.register(NewsCategory,NewsCategoryAdmin) #注册新闻信息类
