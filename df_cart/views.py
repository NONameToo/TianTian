# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import JsonResponse


from df_user.login import login_check
from .models import *

@login_check
def cart(request):
    carts = CartInfo.objects.filter(user_id=request.session['user_id'])


    context = {
        'title': '购物车',
        'page_num': 3,
        'carts': carts,
    }

    return render(request, 'df_cart/cart.html', context)


# @login_check
# def order(requeset):
#     context = {
#         'page_num': 4,
#     }
#
#     return render(requeset, 'df_cart/order.html', context)

def cart_count(request):
    count = CartInfo.objects.filter(user_id=request.session.get('user_id')).count()
    return JsonResponse({'count': count})




def add(request, gid, count):

    # 把数据写到数据库中，并返回购物车商品栏数
    uid = request.session.get('user_id', '')
    gid = int(gid)
    count = int(count)


    # 在数据库中查询是否有这条数据存在
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)

    # 如果有这条数据存在，就只是增加数量
    if len(carts)>=1:
        cart = carts[0]
        cart.number += count
    # 如果没有这条数据存在，就新增一条数据
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.number = count


    # 保存到数据库
    cart.save()

    # 判断请求的方式
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session.get('user_id')).count()
        return JsonResponse({'count': count})

    else:
        return  redirect('/cart/')




def  edit(request, cart_id, value):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count = cart.number
        cart.number = value
        cart.save()
        data = {'back': 0}

    except Exception as e:
        data = {'back': count}
        return JsonResponse(data)

    else:
        return JsonResponse(data)


def dele(request, cart_id):
    try:
        cart = CartInfo.objects.get(pk=cart_id)
        cart.delete()
        data = {'back': 0}

    except Exception as e:
        data = {'back': 1}

    else:
        return JsonResponse(data)






















