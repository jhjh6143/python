from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("这是新闻首页")

def page(request,number):
    return HttpResponse("这是page"+number)
