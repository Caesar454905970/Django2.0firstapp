from django.db import models
from  django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    # 文本型字段(属性：标题)
    title=models.CharField(max_length=30)
    # 文本型字段(属性）
    content=models.TextField()
    # 创建日期字段
    created_time=models.DateTimeField(default=timezone.now)
    # 创建更新日期字段
    last_updated_time=models.DateTimeField(auto_now=True)
    #作者字段
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)
    # 是否删除字段
    is_deleted=models.BooleanField(default=False)
    # 数值类型：阅读数量
    readed_num=models.IntegerField(default=0)


# 标注文章标题
    def __str__(self):
        return "<Article: %s>" %self.title