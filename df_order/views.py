# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from df_user.login import *

from df_user.models import *
from df_cart.models import *
from .models import *
from datetime import datetime
from decimal import Decimal

# 导入事物模块
from django.db import transaction


@login_check
def order(request):

    # 查询出是谁的订单
    user = UserInfo.objects.get(id=request.session['user_id'])



    # 根据用户查询出他的购物车信息

        #　从请求中把所有的提交了的购物车的id拿出来

    carts_id = request.GET.getlist('cart_id')

        # 转换成int类型存成一个列表

    carts_ids = [int(item) for item in carts_id]

    carts = CartInfo.objects.filter(id__in=carts_ids)




    context = {
        'page_num': 4,
        'title': '提交订单',
        'user': user,
        'carts': carts,
        'carts_ids': carts_ids,


    }
    return render(request, 'df_order/order.html', context)



@transaction.atomic()
@login_check
def order_handle(request):

    # #　保存一个点，以便于回滚
    #
    # tran_id = transaction.savepoint()
    # # 接收购物车的编号
    cart_ids = request.POST.get('cart_ids', 'dashuaige')
    print(cart_ids)
    #
    # try:
    #     # 创建订单对象
    #     order = OrderInfo()
    #     now = datetime.now()
    #     uid= request.session['user_id']
    #     order.oid = '%s%d' % (now.strftime('%Y%M%D%H%M%S'),uid )
    #     order.user_id = uid
    #     order.odate = now
    #     order.ototal = Decimal(request.POST.get('total'))
    #     order.save()
    #
    #     # 创建详单对象
    #
    #     cart_ids2 = [int(item) for item in cart_ids.split(',')]
    #     for id in cart_ids2:
    #         order_detail = OrderDetailInfo()
    #         order_detail.order = order
    #         #查询购物车信息
    #         cart = CartInfo.objects.get(id=id)
    #         # 判断商品库存
    #         goods = cart.goods
    #         if goods.ginventory >= order_detail.count:
    #             #减少库存的商品
    #             goods.ginventory -= order_detail.count
    #             goods.save()
    #
    #             #完善详单信息
    #             order_detail.goods_id = goods.id
    #             order_detail.price = goods.gprice
    #             order_detail.count = cart.number
    #             order_detail.save()
    #
    #             #删除购物车数据
    #             cart.delete()
    #         else:
    #             # 如果库存不足
    #
    #             transaction.savepoint_rollback(tran_id)
    #             return redirect('/cart/')
    #
    #
    #     transaction.savepoint_commit(tran_id)
    # except Exception as e:
    #     # 如果中途发生错误
    #     transaction.savepoint_rollback(tran_id)

    return HttpResponse('dashuaige')
    # return redirect('/user/order/')