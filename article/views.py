from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,Http404
from article.models import Article


# Create your views here.
def article_detail(request,article_id):
    # 方法二
    article=get_object_or_404(Article,pk=article_id)
    context={}
    context['article_obj']=article
    return render_to_response('article_detail.html',context)

    # 方法一：
    # try:
    #     article=Article.objects.get(id=article_id)
    #     context={}
    #     context['article_obj']=article
    #     return render(request,'article_detail.html',context)
    # except Article.DoesNotExist:
    #     # return HttpResponse("你访问的内容不存在")
    #     raise Http404


    # return HttpResponse("<h2>文章标题:%s</h2><br>文章内容是：%s"%(article.title,article.content))


def article_list(request):
    # 筛选出删掉的字段
    articles=Article.objects.filter(is_deleted=False)

    #article获取全部
    # articles=Article.objects.all()

    context={}
    context['articles']=articles
    return render_to_response('article_list.html',context)

