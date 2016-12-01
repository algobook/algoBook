from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'algo/(?P<id>[\w+-]+)/$', views.show, name= "show_algo"),
    # url(r'^search$',views.search, name='index'),
    url(r'^(?P<query>[\w+-]+)/$', views.search, name = "search_algo"),
]
