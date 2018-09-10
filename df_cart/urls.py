from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^add(\d+)_(\d+)/$', views.add, name='add'),
    url(r'^cart_count', views.cart_count),
    url(r'^edit(\d+)_(\d+)/$', views.edit),
    url(r'^del(\d+)/$', views.dele),



]