# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice', 'gunite', 'gclick', 'gintroduction', 'ginventory', 'gcontent']



admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)