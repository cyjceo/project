#coding=utf-8
from django.shortcuts import render
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from haystack.generic_views import SearchView

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

    content = {'title': '详情', 'top': '1', 'good': good, 'recommendgoods': recommendgoods, 'car_show': '1'}
    responese = render(request, 'appname2/detail.html', content)
    recently = request.COOKIES.get('recently','')
    recentlylist = recently.split(',')
    if id in recentlylist:
        recentlylist.remove(id)
    recentlylist.insert(0,id)
    if len(recentlylist) > 6:
        recentlylist.pop()

    responese.set_cookie('recently',','.join(recentlylist))
    return responese


def list(request,cid,index,orderBy):
    type = TypeInfo.objects.get(id=cid)
    list = []
    desc = '1'
    if orderBy == '1':
        list = type.goodsinfo_set.order_by('-id')
    elif orderBy == '2':
        desc = request.GET.get('desc')
        if desc == '1':
            list = type.goodsinfo_set.order_by('-gprice')
        else:
            list = type.goodsinfo_set.order_by('gprice')
    elif orderBy == '3':
        list = type.goodsinfo_set.order_by('-gclick')

    recommendgoods = type.goodsinfo_set.order_by('-id')[0:2]
    p = Paginator(list,2)
    if index == '':
        index = '1'
    index = int(index)
    if index < 1:
        index = 1
    if index > p.num_pages:
        index = p.num_pages
    page = p.page(index)
    page_range = []
    if page.paginator.num_pages <= 5:
        page_range = range(1,page.paginator.num_pages+1)
    elif page.number <= 2:
        page_range = range(1,6)
    elif page.number >= page.paginator.num_pages-1:
        page_range = range(page.paginator.num_pages-4,page.paginator.num_pages+1)
    else:
        page_range = range(page.number-2,page.number+3)
    content = {'title': '更多', 'top': '1','page':page,'page_range':page_range,'car_show':'1','id':cid,'type':type,'recommendgoods':recommendgoods,'orderBy':orderBy,'desc':desc}
    return render(request,'appname2/list.html',content)


class mysearchview(SearchView):
    def get_context_data(self, *args,**kwargs):
        context = super(mysearchview,self).get_context_data(*args,**kwargs)
        context['car_show'] = '1'
        page = context.get('page_obj')
        page_range =[]
        if page.paginator.num_pages < 5:
            page_range = range(1,page.paginator.num_pages+1)
        elif page.number <= 2:
            page_range = range(1,6)
        elif page.number >= page.paginator.num_pages-1:
            page_range = range(page.paginator.num_pages-4,page.paginator.num_pages+1)
        else:
            page_range = range(page.number-2,page.number+3)
        context['page_range'] = page_range
        return context