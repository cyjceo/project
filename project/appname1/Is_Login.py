#coding=utf-8
from django.shortcuts import redirect
def isLogin(func):
    def login(request,*args,**kwargs):
        if request.session.has_key('uid'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/login/')
    return login