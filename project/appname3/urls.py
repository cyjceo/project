from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^addcart/$',views.addcart),
    url(r'^cart/$',views.cart),
    url(r'^count/$',views.count),
    url(r'^del/$',views.del_cart),
    url(r'^place_order/$',views.place_order),
    url(r'^edit/$',views.edit),
]