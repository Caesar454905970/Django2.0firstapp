from django.contrib import admin
from .models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","content","created_time","last_updated_time","author","is_deleted","readed_num")
    # 通过Id正序排序
    ordering = ("id",)
    # 通过ID倒序排序
    # ordering = ("-id",)


# admin.site.register(Article,ArticleAdmin)
