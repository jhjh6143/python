from django.http import HttpResponse
from django.shortcuts import render

def shebao(request):
    if request.method=="GET":
        return render(request,'shebao.html')
    elif request.method=='POST':
        base=request.POST.get('income',0)
        base=base if base else '0'
        base=float(base)
        is_city=request.POST.get('is_city')
        yl_gr=base*0.08
        yl_dw=base*0.19
        return render(request,'shebao.html',locals())
