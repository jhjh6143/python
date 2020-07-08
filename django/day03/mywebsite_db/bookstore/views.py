from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homepage(request):
    return HttpResponse("图书列表首页")

def add_book(request):
    if request.method=='GET':
        title=request.GET.get('title','noname')
        publish=request.GET.get('pub','xxx')
        from . import models
        models.Book.objects.create(title=title,
                                   pub=publish)
        return HttpResponse('OK')
