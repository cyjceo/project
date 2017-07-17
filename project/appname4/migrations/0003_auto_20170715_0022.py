# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname4', '0002_auto_20170714_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermain',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordermain',
            name='total',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
    ]
