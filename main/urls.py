from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from . import regbackend
from . import views
from algoSitemap import CodeSitemap

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'algo/(?P<slug>[\w+-]+)/$', views.show, name= "show_algo"),
    # url(r'^search$',views.search, name='index'),
    # url(r'^accounts/update_profile/$', views.update_profile, name = 'update_profile'),
    url(r'^accounts/register/$', regbackend.MyRegistrationView.as_view(), name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^algos/create', views.create_algo),
    url(r'^algos/addcode', views.add_code_to_algo, name="add_code"),
    url(r'^algos/adddesc', views.add_description_to_algo , name="add_desc"),
    url(r'^algos/search/(?P<query>.*)/$', views.api_search, name = "api_search"),

    url(r'^algos/codes/(?P<code_id>[\w+-]+)/votes', views.add_vote_to_code),

    url(r'^codes/sitemap\.xml$', sitemap,
        {'sitemaps': {'algos': CodeSitemap}},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'codes/(?P<code_id>[\w+-]+)/delete', views.delete_code),

    url(r'user/(?P<name>[\w+-]+)/$', views.user_profile),
    url(r'^(?P<query>.*)/$', views.search, name = "search_algo"),
]
