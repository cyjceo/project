from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    upassword = models.CharField(max_length=40)
    uemail = models.CharField(max_length=20)
    uaddress = models.CharField(max_length=100,null=True)
    ureceive = models.CharField(max_length=10,null=True)
    ucode = models.CharField(max_length=6,null=True)
    uphone = models.CharField(max_length=11,null=True)