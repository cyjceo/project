# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname4', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermain',
            old_name='totle',
            new_name='total',
        ),
    ]
