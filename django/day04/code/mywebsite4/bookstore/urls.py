from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.homepage),
    url(r'^/add', views.new_book),
    url(r'^/list_all', views.list_book),
    url(r'^/filter_book', views.filter_books),
]