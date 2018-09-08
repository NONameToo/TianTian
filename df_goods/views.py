# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *

from django.core.paginator import Paginator



def index(request):

    # 把每一个分类的最新的和最热的四条拿出来
    typelist = GoodsType.objects.all()

    type1 = typelist[0].goodsinfo_set.order_by('-id')[0: 4]
    type11 = typelist[0].goodsinfo_set.order_by('-gclick')[0: 4]

    type2 = typelist[1].goodsinfo_set.order_by('-id')[0: 4]
    type22 = typelist[1].goodsinfo_set.order_by('-gclick')[0: 4]

    type3 = typelist[2].goodsinfo_set.order_by('-id')[0: 4]
    type33 = typelist[2].goodsinfo_set.order_by('-gclick')[0: 4]

    type4 = typelist[3].goodsinfo_set.order_by('-id')[0: 4]
    type44 = typelist[3].goodsinfo_set.order_by('-gclick')[0: 4]

    type5 = typelist[4].goodsinfo_set.order_by('-id')[0: 4]
    type55 = typelist[4].goodsinfo_set.order_by('-gclick')[0: 4]

    type6 = typelist[5].goodsinfo_set.order_by('-id')[0: 4]
    type66 = typelist[5].goodsinfo_set.order_by('-gclick')[0: 4]

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
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]

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

    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]


    context = {
        'title': goods.gtype.ttitle,
        'page_num': 2,
        'goods': goods,
        'news': news,
        'num': num,
    }

    response = render(requeset, 'df_goods/detail.html', context)

    # 把用户最近的浏览信息记录到cookie中

    goods_ids =  requeset.COOKIES.get('goods_ids', '')

    # 把商品的id转换成字符串
    goods_id = '%d' % goods.id

    # 判断是否有浏览记录
    if goods_ids != '':
        # 把结果拆成一个列表
        goods_ids1 = goods_ids.split(',')
        if goods_ids1.count(goods_id) >= 1:   #如果已经有了记录，就不再记录
            goods_ids1.remove(goods_id)
        else:
            goods_ids1.insert(0, goods_id)


        if len(goods_ids1) >=6:   # 只保留五条浏览记录
            del goods_ids1[5]
        else:
            # 拼接字符串
            goods_ids = ','.join(goods_ids1)


    else:
        # 如果没有浏览记录则直接添加
        goods_ids = goods_id

    # 写到cookie中
    response.set_cookie('goods_ids', goods_ids)

    return response















