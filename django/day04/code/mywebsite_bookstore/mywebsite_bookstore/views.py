from django.http import  HttpResponse
from django.shortcuts import  render

def test_cookie(request):
    resp=HttpResponse("OK")
    # resp.set_cookie('myschool','abcd',max_age=7*24*60*60)
    resp.delete_cookie('myschool')
    return resp

def show_cookie(request):
    dic=request.COOKIES
    return HttpResponse(str(dic))

def test_session(request):
    del request.session['mykey']
    resp=HttpResponse("设置成功")
    return resp

def show_session(request):
    value=request.session.get('mykey','mykey没有对应的值')
    s=str(value)
    return HttpResponse(s)

def show_homepage(request):
    return render(request,'homepage.html',locals())