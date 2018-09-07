# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *
from hashlib import sha1

def register(request):
    title = '天天生鲜-注册页'
    context = {'title': title}
    return render(request, 'df_user/register.html', context)

# def check_name(request, name):
#     list = UserInfo.objects.filter(uname=name)
#     list2 = []
#     for a in list:
#         list2.append({'uname':a.uname})
#
#     return JsonResponse({'date': list2})


def check_name(request):
    # 推荐用这种方式，检查用户名是否存在只需要知道查询结果有几个就可以了
    # ajx 提交过来的方式通过参数传过来
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})




def register_handle(request):
    # 获取用户输入
    uname = request.POST['user_name']
    upwd = request.POST['pwd']
    ucpwd = request.POST['cpwd']
    uemail = request.POST['email']

    # 判断两次的密码是否一致

    if upwd != ucpwd:
        return redirect('/user/register/')

    # 判断用户名是否已经存在
    # result = UserInfo.objects.filter(uname=uname)
    # if result != '':
    #     return HttpResponse(result.uname)
    #     # return redirect('/user/register/')
    # else:
    #     return HttpResponse('为空')


    # 对用户密码进行加密
    s1 = sha1()
    s1.update(upwd)
    pwd = s1.hexdigest()


    # 把数据存入数据库
    user = UserInfo()
    user.uname = uname
    user.upwd = pwd
    user.uemail = uemail
    user.save()

    # 跳转到登录页
    return redirect('/user/login/')

def login(request):
    title = '天天生鲜-登陆'

    # 把cookie中的用户名取出来

    uname = request.COOKIES.get('uname', '')

    # 在通过context 传回去，就能实现记住用户名

    # 加上后面那一堆东西的原因是防止什么都没填的情况下，js报错
    context = {'title': title, 'error_name': '0', 'error_pwd': '0', 'uname': uname}
    return render(request, 'df_user/login.html', context)



def login_handle(request):
    uname = request.POST.get('username')
    pwd = request.POST.get('pwd')

    # 判断用户是否选择了记住用户名
    remember = request.POST.get('remember', 0)


    # 根据用户名取密码

    list = UserInfo.objects.filter(uname=uname)
    if len(list) == 1:                # 如果查询到了结果

        #对密码进行加密
        s1 = sha1()
        s1.update(pwd)
        pwd2 = s1.hexdigest()

        if pwd2 == list[0].upwd:
            # return HttpResponse('登陆成功')
            # 构造一个HttpResponseRedirect对象
            red = HttpResponseRedirect('/user/info/')

            #记住用户名
            if remember != 0:
                # red.set_cookie = ('uname', uname)
                pass
            else:
                # red.set_cookie = ('uname', '', -1)
                pass
            request.session['user_id'] = list[0].id
            request.session['uname'] = uname

            return red

        else:
            # 表明密码错误
            context = {'title': '天天生鲜-登陆', 'error_name': '0', 'error_pwd': '1', 'uname': uname, 'upwd': pwd}
            return render(request, 'df_user/login.html', context)


    else:
        # 表明用户名错误
        context = {'title': '天天生鲜-登陆', 'error_name': '1', 'error_pwd': '0', 'uname': uname, 'upwd': pwd}
        return render(request, 'df_user/login.html', context)



# 用户信息页面

def info(request):

    uname = request.session.get('uname')
    list = UserInfo.objects.filter(uname=uname)

    context = {'title': '个人中心', 'user': list[0], 'page_num':1}
    return render(request, 'df_user/info.html', context)

# 用户订单页面

def order(request):

    # uname = request.session.get('uname')
    # list = UserInfo.objects.filter(uname=uname)
    # if len(list) == 1:  # 如果查询到了结果
    #     context = {'title': '我的订单', 'uname': uname, 'uphone': list[0].uphone, 'uaddr': list[0].uaddr}
    context = {'title': '我的订单', 'page_num':1}
    return render(request, 'df_user/order.html', context)

def site(request):

    # 根据id把那一条数据对象找出来
    user = UserInfo.objects.get(id=request.session['user_id'])

    if request.method == 'POST':
        user.ureceive = request.POST.get('ureceive')
        user.uaddr = request.POST.get('uaddr')
        user.upostcode = request.POST.get('upostcode')
        user.uphone = request.POST.get('uphone')
        user.save()


    context = {'title': '地址管理', 'user': user, 'page_num':1}

    return render(request, 'df_user/site.html', context)



