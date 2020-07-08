from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def page1_template(request):
    # t=loader.get_template("page1.html")
    # html=t.render()
    # print(html)
    # return HttpResponse(html)
    return render(request,'page1.html')
class Dog:
    def __init__(self,k,c):
        self.kinds=k
        self.color=c

    def info(self):
        return self.color+"的"+self.kinds+"狗"

def page2_render(request):
    d={"name":"魏老师，",
       "age":35,
       "favorite":["看书","看电影"],
       "friend":{'name':"小张","age":25},
       "pet":Dog('京巴','白色')}
    # t=loader.get_template("page2.html")
    # html=t.render(d)
    # return HttpResponse(html)

    return render(request,'page2.html',d)

def test_tag(request):
    dic={
        'name':'魏老师',
        'has_car':True,
        'age':35,
        'fav':['aa','bb','cc','dd'],
    }
    return  render(request,'page3.html',dic)

def page4(request):
    string='welcome to beijing'
    a="<span>hello</span>"
    b=200
    print(locals())
    return render(request,'page4.html',locals())

def homepage(reuqest):
    return render(reuqest,'base.html')

def sport_homepage(reuqest):
    return render(reuqest,'sport.html')

def pages(reuqest):
    return render(reuqest,'pages.html')

def person(reuqest,name):
    return render(reuqest,'person.html',locals())

def info(reuqest,name):
    s=name+"的详细信息"
    return HttpResponse(s)