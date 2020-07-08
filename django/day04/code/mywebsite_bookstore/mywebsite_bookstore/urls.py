"""mywebsite_bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^bookstore/', include('bookstore.urls')),
    url('^test_cookie',views.test_cookie),
    url('^show_cookie', views.show_cookie),
    url('^userinfo/', include('userinfo.urls')),
    url('^show_session', views.show_session),
    url('^test_session',views.test_session),
    url('^$', views.show_homepage),
    url(r'^user/',include('user.urls'))

]
