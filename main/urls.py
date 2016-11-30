from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    # url(r'^search$',views.search, name='index'),
    url(r'^(?P<query>[\w+-]+)/$', views.search, name="search_algo")
]
