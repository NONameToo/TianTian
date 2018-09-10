# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'tiantian/index.html')


def cart(request):
    return render(request, 'tiantian/cart.html')


def detail(request):
    return render(request, 'tiantian/detail.html')


def list(request):
    return render(request, 'tiantian/list.html')


def login(request):
    return render(request, 'tiantian/login.html')


def place_order(request):
    return render(request, 'tiantian/order.html')


def register(request):
    return render(request, 'tiantian/register.html')


def user_center_info(request):
    return render(request, 'tiantian/info.html')


def user_center_order(request):
    return render(request, 'tiantian/order.html')


def user_center_site(request):
    return render(request, 'tiantian/site.html')