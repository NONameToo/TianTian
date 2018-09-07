# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *

from django.core.paginator import Paginator



def index(request):

    # 把每一个分类的最新的和最热的四条拿出来
    typelist = GoodsType.objects.all()

    type1 = typelist[0].goodsinfo_set.order_by('-id')
    type11 = typelist[0].goodsinfo_set.order_by('-gclick')

    type2 = typelist[1].goodsinfo_set.order_by('-id')
    type22 = typelist[1].goodsinfo_set.order_by('-gclick')

    type3 = typelist[2].goodsinfo_set.order_by('-id')
    type33 = typelist[2].goodsinfo_set.order_by('-gclick')

    type4 = typelist[3].goodsinfo_set.order_by('-id')
    type44 = typelist[3].goodsinfo_set.order_by('-gclick')

    type5 = typelist[4].goodsinfo_set.order_by('-id')
    type55 = typelist[4].goodsinfo_set.order_by('-gclick')

    type6 = typelist[5].goodsinfo_set.order_by('-id')
    type66 = typelist[5].goodsinfo_set.order_by('-gclick')

    context = {
        'title': '首页',
        'page_num': 2,
        'type1': type1,
        'type11': type11,
        'type2': type2,
        'type22': type22,
        'type3': type3,
        'type33': type33,
        'type4': type4,
        'type44': type44,
        'type5': type5,
        'type55': type55,
        'type6': type6,
        'type66': type66,
    }
    # context = {'page_num': 2}
    return render(request, 'df_goods/index.html', context)



# 列表页

def list(request, pid, pindex, sort):
    # 更具pid查询上级
    typeinfo = GoodsType.objects.get(pk=int(pid))

    # 根据时间id查处最新的两条放在左边的新品推荐里面
    news = typeinfo.goodsinfo_set.order_by('-id')

    # 根据不同的排序方式查询数据
    if sort == '1':   # 默认方式
        goods_list = GoodsInfo.objects.filter(gtype_id=int(pid)).order_by('-id')

    elif sort == '2':  # 按照价格排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(pid)).order_by('-gprice')

    elif sort == '3':  # 按照人气进行排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(pid)).order_by('-gclick')


    # 创建paginator对象

    paginator = Paginator(goods_list, 10)   #每页取出十个数据

    # 创建page对象

    page = paginator.page(int(pindex))  # 显示第几页

    context = {
        'title': typeinfo.ttitle,
        'page_num': 2,
        'page': page,
        'paginator': paginator,
        'typeinfo': typeinfo,
        'sort': sort,
        'news': news
    }


    return render(request, 'df_goods/list.html', context)


def detail(requeset, num):
    goods = GoodsInfo.objects.get(id=int(num))

    # 每点击一次，点击量加一

    goods.gclick += 1
    goods.save()


    # 左边那两个推荐商品

    # 通过子 找 父 再 通过父找出所有的子

    news = goods.gtype.goodsinfo_set.order_by('-id')

    context = {
        'title': goods.gtype.ttitle,
        'page_num': 2,
        'goods': goods,
        'news': news,
        'num': num
    }




    return render(requeset, 'df_goods/detail.html', context)




















