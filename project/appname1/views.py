#coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render,redirect
from hashlib import sha1
from models import *
from Is_Login import isLogin
from appname2.models import GoodsInfo
from appname4.models import orderMain,orderDetail
from django.core.paginator import Paginator

# Create your views here.
def login(request):
    name = request.COOKIES.get('username','')
    content = {'title':'登录','username':name,'top':'0'}
    return render(request,'appname1/login.html',content)

def login_handle(request):
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    jizhu = request.POST.get('jizhu')

    user = UserInfo.objects.filter(username=username)
    s1 = sha1()
    s1.update(password)
    sha1_pwd = s1.hexdigest()
    if user.count() == 1:
        if user[0].upassword == sha1_pwd:
            request.session['uid'] = user[0].id
            request.session['uname'] = user[0].username
            path = request.session.get('urlpath','/')
            print path
            response = redirect(path)
            if jizhu == '1':
                response.set_cookie('username',username)
            else:
                response.set_cookie('username','',max_age=-1)
            return response
        else:
            return render(request,'appname1/login.html',{'pwd_error':'1'})
    else:
        return render(request,'appname1/login.html',{'name_error':'1'})



def register(request):
    content = {'title': '注册','top':'0'}
    return render(request,'appname1/register.html',content)

def register_handle(request):
    if request.method == 'POST':
        req=request.POST
        user_name = req.get('user_name')
        pwd = req.get('pwd')
        email = req.get('email')
        s1 = sha1()
        s1.update(pwd)
        spwd = s1.hexdigest()
        user = UserInfo()
        user.username = user_name
        user.upassword = spwd
        user.uemail = email
        user.save()
        return redirect('/login/')
    elif request.method == 'GET':
        req = request.GET
        user_name = req.get('user_name')
        user = UserInfo.objects.filter(username=user_name)
        if user.count() == 1:
            return JsonResponse({'exist':'1'})
        else:
            return JsonResponse({'exist':'0'})

'''
def index(request):
    content = {'title':'首页','top':'1'}
    return render(request,'appname2/index.html',content)
'''
@isLogin
def user_center_info(request):
    user = UserInfo.objects.get(id=request.session['uid'])
    recentlystr = request.COOKIES.get('recently','')
    list = []
    recentlylist = recentlystr.split(',')
    recentlylist.pop()
    for i in recentlylist:
        good = GoodsInfo.objects.get(id=i)
        list.append(good)
    return render(request,'appname1/user_center_info.html',{'user':user,'title':'用户中心','top':'1','list':list})
@isLogin
def user_center_site(request):
    user = UserInfo.objects.get(id=request.session['uid'])
    return render(request,'appname1/user_center_site.html',{'user': user,'title':'收货地址','top':'1'})
@isLogin
def user_center_order(request):
    index = request.GET.get('index',1)
    print index
    order = orderMain.objects.filter(user_id=request.session['uid']).order_by('-order_date')
    paginator = Paginator(order,5)
    page = paginator.page(index)
    pagenum = []
    if page.paginator.num_pages<5:
        pagenum = range(1,page.paginator.num_pages+1)
    elif page.number <=2:
        pagenum = range(1,6)
    elif page.number>=page.paginator.num_pages-1:
        pagenum = range(page.paginator.num_pages-4,page.paginator.num_pages+1)
    else:
        pagenum = range(page.number-2,page.number+3)

    return render(request,'appname1/user_center_order.html',{'title':'全部订单','top':'1','page':page,'pagenum':pagenum})
@isLogin
def userinfo_handle(request):
    post = request.POST
    user = UserInfo.objects.get(id=request.session['uid'])
    user.ureceive = post.get('ureceive')
    user.uaddress = post.get('address')
    user.ucode = post.get('code')
    user.uphone = post.get('phone')
    user.save()
    return render(request, 'appname1/user_center_site.html', {'user': user,'top':'1'})

def exit(request):
    request.session.flush()
    return redirect('/')

def isLogin(reuqest):
    if reuqest.session.has_key('uid'):
        return JsonResponse({'islogin':'1'})
    else:
        return JsonResponse({'islogin':'0'})