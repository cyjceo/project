#coding=utf-8
from django.shortcuts import render,redirect
from django.db import transaction
from models import *
from datetime import datetime
from appname3.models import CartInfo
# Create your views here.

@transaction.atomic
def commit_order(request):
    issuccess = True
    sid = transaction.savepoint()

    try:
        uid = request.session.get('uid')
        orderM = orderMain()
        orderM.user_id = uid
        orderM.order_id = '%s%d'%(datetime.now().strftime('%Y%m%d%H%M%S'),uid)
        orderM.save()
        print 11111
        cart_ids = request.POST.get('idstr').split(',')

        carts = CartInfo.objects.filter(id__in=cart_ids)
        total = 0

        for cart in carts:
            if cart.count <= cart.goods.gkucun:
                orderD = orderDetail()
                orderD.main = orderM
                orderD.count = cart.count
                orderD.price = cart.goods.gprice
                orderD.goods = cart.goods
                orderD.save()

                cart.goods.gkucun-=cart.count
                cart.goods.save()

                total += cart.count*cart.goods.gprice
                orderM.total = total
                orderM.save()

                cart.delete()
            else:
                issuccess = False
                transaction.savepoint_rollback(sid)
                break

        if issuccess:
            transaction.savepoint_commit(sid)

    except:
        transaction.savepoint_rollback(sid)
        issuccess = False
    if issuccess:
        return redirect('/user_center_order/')
    else:
        return redirect('/cart/')

