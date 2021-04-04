from django.urls import path
from . import views


# app中的路由
urlpatterns = [
    # localhost:8000/article/ 文章列表
    path('', views.article_list, name="article_list"),
    # localhost:8000/article/1 文章内容
    path('<int:article_id>', views.article_detail, name="article_detail"),

]
