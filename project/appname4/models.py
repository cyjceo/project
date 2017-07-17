from django.db import models
from appname1.models import UserInfo
from appname2.models import GoodsInfo
# Create your models here.
class orderMain(models.Model):
    order_id = models.CharField(max_length=20,primary_key=True)
    user = models.ForeignKey(UserInfo)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    state = models.IntegerField(default=0)

class orderDetail(models.Model):
    main = models.ForeignKey(orderMain)
    goods = models.ForeignKey(GoodsInfo)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    count = models.IntegerField()
