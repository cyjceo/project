from django.db import models
from appname1.models import UserInfo
from appname2.models import GoodsInfo
# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    