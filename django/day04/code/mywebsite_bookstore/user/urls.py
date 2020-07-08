from django.conf.urls import  url
from  . import views

urlpatterns=[
    url(r'^login',views.mylogin2),
    url(r'^logout', views.mylogout2),
    url(r'^reg', views.myregister2),
]