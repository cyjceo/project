# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname1', 'user_initial'),
        ('appname2', 'goods_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='appname2.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='orderMain',
            fields=[
                ('order_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('totle', models.DecimalField(max_digits=8, decimal_places=2)),
                ('state', models.IntegerField()),
                ('user', models.ForeignKey(to='appname1.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='main',
            field=models.ForeignKey(to='appname4.orderMain'),
        ),
    ]
