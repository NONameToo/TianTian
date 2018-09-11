# coding:utf-8

from django.conf.urls import url
from . import views
from .views import *


urlpatterns = [

    url(r'^goods/$', views.index, name='index'),
    url(r'^goods/list(\d+)_(\d+)_(\d+)/$', views.list, name='list'),

    url(r'^goods/(\d+)/$', views.detail, name='detail'),
    url(r'^search/$', MySearchView())
]