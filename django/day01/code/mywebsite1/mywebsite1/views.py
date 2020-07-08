from  django.http import HttpResponse
def pagel(request):
    print("Page被调用！")

def page_year(request,y):
    html="参数是："+y
    return HttpResponse(html)

def birthday(request,y,m,d):
    html="生日是："+y+m+d
    return HttpResponse(html)
