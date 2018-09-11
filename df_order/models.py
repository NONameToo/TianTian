# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.

# 订单
class OrderInfo(models.Model):
    #　订单号
    oid = models.CharField(max_length=20, primary_key=True)
    # 用户
    user = models.ForeignKey('df_user.UserInfo')
    odate = models.DateTimeField(auto_now=True)
    # 总金额
    ototal = models.DecimalField(max_digits=6, decimal_places=2)
    # 收货地址
    oaddr = models.CharField(max_length=100)
    # 是否已经支付
    oispay = models.BooleanField(default=False)
    class Meta:
        db_table = 'OrderInfo'



# 订单详情

class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo')

    # 是那个订单的订单详情
    order = models.ForeignKey(OrderInfo)
    # 单价（以购买当时的实际价格为准）
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # 数量
    count = models.IntegerField()
    class Meta:
        db_table = 'OrderDetailInfo'
