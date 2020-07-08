from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models

# Create your views here.



def mylogin(request):
    if request.method=='GET':
        username=request.COOKIES.get('username','')
        return render(request,'login.html',locals())
    elif request.method=='POST':
        remember=request.POST.get('remember','')
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        try:
            user=models.User.objects.get(name=username,
                                         password=password)
            request.session['userinfo']={
                "username":user.name,
                'id':user.id
            }
        except:
            return HttpResponse('登录失败')
        resp=HttpResponse('登陆成功')
        if remember:
            resp.set_cookie('username',username,7*24*60*60)
        else:
            resp.delete_cookie('username')
        return resp

def myregister(request):
    if request.method=='GET':
        return render(request,'userinfo/register.html')
    elif request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        password2=request.POST.get('password2','')

        if username=='':
            username_error="用户名不能为空"
            return render(request,'userinfo/register.html',locals())
        if password=='':
            return HttpResponse('密码不能为空')
        if password!=password2:
            return HttpResponse('两次密码不一致！')

        #开始注册功能
        try:
            from . import models
            user=models.User.objects.create(
                name=username,
                password=password
            )
            return HttpResponse("注册成功")
        except:
            return HttpResponse("注册失败")

def mylogout(request):
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect('/')