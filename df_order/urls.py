# coding:utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.order),
    url(r'^handle/$', views.order_handle),




]