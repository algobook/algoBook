from django.conf.urls import url, include
from django.contrib import admin
from . import regbackend

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'algo/(?P<id>[\w+-]+)/$', views.show, name= "show_algo"),
    # url(r'^search$',views.search, name='index'),
    url(r'^accounts/update_profile/$', views.update_profile, name = 'update_profile'),
    url(r'^accounts/register/$', regbackend.MyRegistrationView.as_view(), name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^(?P<query>[\w+-]+)/$', views.search, name = "search_algo"),
]
