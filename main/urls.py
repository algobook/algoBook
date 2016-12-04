from django.conf.urls import url, include
from django.contrib import admin
from . import regbackend
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'algo/(?P<slug>[\w+-]+)/$', views.show, name= "show_algo"),
    # url(r'^search$',views.search, name='index'),
    # url(r'^accounts/update_profile/$', views.update_profile, name = 'update_profile'),
    url(r'^accounts/register/$', regbackend.MyRegistrationView.as_view(), name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^algos/create', views.create_algo),
    url(r'^algos/addcode', views.add_code_to_algo, name="add_code"),
    url(r'^algos/search/(?P<query>[\w+-]+)/$', views.api_search, name = "api_search"),

    url(r'^(?P<query>[\w+-]+)/$', views.search, name = "search_algo"),
]
