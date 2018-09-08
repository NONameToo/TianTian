# coding:utf-8

from django.http import HttpResponseRedirect

# 登陆验证的装饰器


def login_check(func):
    def login_func(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            # 如果是登陆了的，就继续做他自己的事情
            return func(request, *args, **kwargs)
        else:
            #　如果没有登陆就跳转到登陆页登陆
            red = HttpResponseRedirect('/user/login/')

            #　把跳转之前的url记录下来
            red.set_cookie('url', request.get_full_path())
            return red

    return login_func



