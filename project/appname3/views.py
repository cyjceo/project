#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import CartInfo
from appname1.Is_Login import isLogin
from appname1.models import UserInfo
from appname2.models import GoodsInfo
from django.db.models import Sum
# Create your views here.
def addcart(request):
    try:
        uid = request.session.get('uid')
        gid = request.GET.get('gid')
        count = int(request.GET.get('count','1'))
        carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
        if len(carts) == 1:
            cart = carts[0]
            cart.count += count
            cart.save()
        else:
            cart = CartInfo()
            cart.user_id = uid
            cart.goods_id = gid
            cart.count = count
            cart.save()
        return JsonResponse({'issuccess':'1'})
    except:
        return JsonResponse({'issuccess':'0'})

def del_cart(request):
    try:
        uid = request.session.get('uid')
        gid = request.GET.get('gid')
        cart = CartInfo.objects.get(user_id=uid,goods_id=gid)
        cart.delete()
        return JsonResponse({'ok':1})
    except:
        return JsonResponse({'ok': 0})

def count(request):
    uid = request.session.get('uid')
    #num = CartInfo.objects.filter(user_id=uid).count()
    num = CartInfo.objects.filter(user_id=uid).aggregate(Sum('count')).get('count__sum')
    return JsonResponse({'count':num})

@isLogin
def cart(request):
    uid = request.session.get('uid')
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'title':'我的购物车','top':'1','carts':carts}
    return render(request,'appname3/cart.html',context)

def edit(request):
    try:
        gid = request.GET.get('gid')
        count = request.GET.get('count')
        uid = request.session.get('uid')
        cart = CartInfo.objects.get(goods_id=gid,user_id=uid)
        cart.count = count
        cart.save()
        return JsonResponse({'ok':1})
    except:
        return JsonResponse({'ok':0})



def place_order(request):
    idlist = request.POST.getlist('cartid')
    cartlist = CartInfo.objects.filter(id__in=idlist)
    user = UserInfo.objects.get(id=request.session.get('uid'))
    idstr = ','.join(idlist)
    context = {'title': '提交订单', 'cartlist': cartlist, 'user': user, 'idstr': idstr}
    return render(request,'appname3/place_order.html',context)


