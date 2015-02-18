# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkfudme', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hcblxrqme',
            name='ztqdo',
        ),
        migrations.RemoveField(
            model_name='jrppdzds',
            name='ttzww',
        ),
        migrations.RemoveField(
            model_name='osyzmgmbo',
            name='rzhpdh',
        ),
        migrations.AddField(
            model_name='jrppdzds',
            name='pwslpi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='osyzmgmbo',
            name='tlzwts',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Hcblxrqme',
        ),
    ]
