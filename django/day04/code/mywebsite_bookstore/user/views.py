from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import models
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.
def mylogin2(request):
    if request.method=='GET':
        return render(request,'user/login.html',locals())
    elif request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')

        try:
            user=models.User.objects.get(username=username,
                                         is_active=True)
            if user.check_passwprd(password):
                login(request,user)
                return HttpResponse("登陆成功")
            else:
                return HttpResponse("密码不正确")
        except:

            return HttpResponse('没有此用户')

def mylogout2(request):
    logout(request)
    return HttpResponse('退出登录')

def myregister2(request):
    if request.method=='GET':
        return render(request,'user/register.html',locals())
    elif request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        password2=request.POST.get('password2','')
        try:
            user=models.User.objects.create_superuser(
                username=username,
                password=password,
                email='weimz@tedu.cn'
            )
            user.save()
            return HttpResponse('注册成功')
        except:
            return HttpResponse('注册失败')