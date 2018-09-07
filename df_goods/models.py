# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


# 商品的分类

class GoodsType(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')


    class Meta:
        db_table = 'GoodsType'






# 商品信息

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    # 售卖的单位
    gunite = models.CharField(max_length=20, default='500g')
    gclick = models.IntegerField()
    # 商品简介
    # 商品简介
    gintroduction = models.CharField(max_length=200)
    # 商品库存
    ginventory = models.IntegerField()

    # 商品详细描述,使用富文本编辑器
    gcontent = HTMLField()

    # 关联的商品种类
    gtype =  models.ForeignKey(GoodsType)


    def __str__(self):
        return self.gtitle.encode('utf-8')



    class Meta:
        db_table = 'GoodsInfo'

