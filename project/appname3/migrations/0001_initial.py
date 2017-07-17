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
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='appname2.GoodsInfo')),
                ('user', models.ForeignKey(to='appname1.UserInfo')),
            ],
        ),
    ]
