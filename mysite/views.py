from django.http import HttpResponse
######视图
def index(request):
    return HttpResponse("世界你好")
