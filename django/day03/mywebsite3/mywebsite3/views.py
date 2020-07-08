from django.http import HttpResponse
from django.shortcuts import render

def test_form(request):
    '''此视图用于示意form表单的提交'''
    if request.method=='GET':
        dic=dict(request.GET)
        nickname=request.GET.get('nickname','')
        print("dic=",dic)
        print('nickname=',nickname)
        return render(request,'myform.html')
    elif request.method=='POST':

        dic=dict(request.POST)
        print("POST提交的结果是：",dic)
        fav=request.POST.getlist('fav')
        print("fav=",fav)
        return HttpResponse("没有结果")

def page1(request):
    return render(request,'page1.html')