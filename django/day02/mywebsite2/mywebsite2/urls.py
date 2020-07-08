"""mywebsite2 URL Configuration

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
from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'page1',views.page1_template,name='page1'),
    path(r'page2', views.page2_render),
    path(r'page3', views.test_tag),
    path(r'page4', views.page4),
    path(r'p', views.homepage,name='index'),
    path(r'sport', views.sport_homepage),
    path(r'pages', views.pages),
    path(r"^person/(\w+)", views.person,name='person'),
    path(r"^info/(\w+)", views.info, name='info'),
]
