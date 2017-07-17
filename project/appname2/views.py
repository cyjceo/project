#coding=utf-8
from django.shortcuts import render
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(60,cache='file_cache')
def index(request):
    cList = TypeInfo.objects.all()
    list = []
    print '**************没有缓存*******************'
    for c in cList:
        list1 = c.goodsinfo_set.order_by('-gclick')[0:4]
        list2 = c.goodsinfo_set.order_by('-id')[0:4]
        con = {'c':c,'list1':list1,'list2':list2}
        list.append(con)
    content = {'title':'首页','top':'1','list':list,'car_show':'1'}
    return render(request,'appname2/index.html',content)
def detail(request,id):
    good = GoodsInfo.objects.get(id=id)
    good.gclick+=1
    good.save()
    recommendgoods = good.gtype.goodsinfo_set.order_by('-id')

    content = {'title': '详情', 'top': '1', 'good':good,'recommendgoods':recommendgoods,'car_show':'1'}
    return render(request,'appname2/detail.html',content)

def list(request,cid,index):
    type = TypeInfo.objects.get(id=cid)
    list = type.goodsinfo_set.order_by('-id')
    recommendgoods = type.goodsinfo_set.order_by('-id')[0:2]
    p = Paginator(list,15)
    if index == '':
        index = '1'
    index = int(index)
    if index < 1:
        index = 1
    if index > p.num_pages:
        index = p.num_pages
    page = p.page(index)
    content = {'title': '更多', 'top': '1','page':page,'car_show':'1','id':cid,'recommendgoods':recommendgoods}
    return render(request,'appname2/list.html',content)
