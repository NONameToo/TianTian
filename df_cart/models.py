# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 定义购物车类

class CartInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo')
    goods = models.ForeignKey('df_goods.GoodsInfo')
    number = models.IntegerField()
    class Meta:
        db_table = 'CartInfo'







