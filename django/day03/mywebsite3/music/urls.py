from  django.conf.urls import url

from . import views

urlpatterns=[
    url(r"^list.html",views.list),
    url(r'page1',views.list),
    url(r'^index',views.index)
]