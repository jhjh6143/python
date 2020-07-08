from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def new_book(request):
    if request.method=='GET':
        return render(request,'new_book.html')
    elif request.method=='POST':
        t=request.POST.get('title','PYTHON')
        pub=request.POST.get('pub','清华大学出版社')
        price=request.POST.get('price','50')
        m_price=request.POST.get('market_price','60')
        # 方法1
        # abook=models.Book.objects.create(
        #     title=t,
        #     pub=pub,
        #     price=price,
        #     market_price=m_price
        # )
        # 方法2
        abook=models.Book(price=price)
        abook.title=t
        abook.pub=pub
        abook.market_price=m_price
        abook.save()
        return HttpResponse('添加成功')

def list_book(request):
    # books=models.Book.objects.all()
    books=models.Book.objects.order_by('-price')
    return render(request,'book_list.html',locals())

def filter_books(request):
    books=models.Book.objects.filter(pub='清华大学出版社')
    # books=models.Book.objects.filter(pub='清华大学出版社',id=6)
    # books=models.Book.objects.filter(price__gte=50)
    return render(request,'book_list.html',locals())