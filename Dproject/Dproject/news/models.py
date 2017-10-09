from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    '''新闻分类表'''
    def __str__(self):
        return self.cag_name
    cag_name = models.CharField(max_length=50)  # max_length指定最大长度，id默认自己会添加

class NewsInfo(models.Model):
    '''定义新闻信息类'''
    def __str__(self):
        return self.news_title

    news_title = models.CharField(max_length=50)  # 定义新闻标题
    news_content = models.TextField(max_length=5000)  # 定义新闻内容
    news_category = models.ForeignKey(NewsCategory)  # 定义新闻分类此处使用外键


class BaseModel(models.Model):  # 创建一个基础类
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_time = models.DateTimeField(auto_now=True)  # 最后一次修改的时间

    class Meta:  #声明当前类不是一个模型类，而是作为其他模型类的抽象基类
        abstract = True

class BookInfo(BaseModel):
    '''图书类'''
    book_title = models.CharField(max_length=50)  # 图书标题
    book_comment = models.IntegerField(default=0)  # 图书评论量
    book_read = models.IntegerField(default=0)  # 图书阅读量
    book_delete = models.BooleanField(default=False) #图书是否被逻辑删除

    def __str__(self):
        return self.book_title

class HeroInfoManager(models.Manager):
    '''定义一个新的管理器类'''
    def all(self):
        '''
        定义一个新的all方法，将父类all获取到的结果过滤掉逻辑删除的部分
        :return: 返回过滤完成的结果
        '''
        result = super().all().filter(hero_delete=False)
        return result

    def remove_hero(self,heroname):
        '''
        定义一个逻辑删除英雄的方法
        :param heroname: 传入英雄的方法
        :return:
        '''
        #尝试获取英雄列表
        heros = HeroInfo.objects.filter( models.Q(hero_delete=False) & models.Q(hero_name=heroname))
        if heros:
            for hero in heros:
                hero.hero_delete = True
                hero.save()
                print('删除成功')
                return True
        else:
            print('删除失败2')
            return False

class HeroInfo(BaseModel):
    '''英雄类'''
    hero_name = models.CharField(max_length=50)  # 英雄的名字
    hero_sex = models.BooleanField(default=True)  # 英雄的性别
    hero_desc = models.TextField()  # 英雄的描述
    hero_delete = models.BooleanField(default=False)  # 英雄是否被逻辑删除
    hero_book = models.ForeignKey('BookInfo')  # 英雄属于的书
    #hero_hometown = models.CharField(max_length=70,default='金庸小说') # 英雄也要问出处
    objects = HeroInfoManager()  # 自定义管理器

    def __str__(self):
        return self.hero_name

class areas(models.Model):
    aid = models.IntegerField(primary_key=True)
    atitle = models.CharField(max_length=20)
    pid = models.IntegerField(null=True)

    def __str__(self):
        '''
        定义一个显示的方法
        :return:
        '''
        return self.atitle














