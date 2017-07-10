# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('upassword', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=20)),
                ('uaddress', models.CharField(max_length=100, null=True)),
                ('ureceive', models.CharField(max_length=10, null=True)),
                ('ucode', models.CharField(max_length=6, null=True)),
                ('uphone', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]
