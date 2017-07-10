from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^detail(\d*)/$',views.detail),
    url(r'^list(\d+)_(\d*)/$',views.list),
]