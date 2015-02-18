# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qclaxc', '0012_auto_20150218_1626'),
        ('geemkrwi', '0011_delete_howsauugrt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hxkigetost',
            name='wnrwf',
        ),
        migrations.RemoveField(
            model_name='meymafbbi',
            name='lovxtxvw',
        ),
        migrations.AddField(
            model_name='hxkigetost',
            name='ycqitjgln',
            field=models.ForeignKey(null=True, related_name='+', to='qclaxc.Yswziiulyl'),
        ),
        migrations.AddField(
            model_name='mxvtxbqsa',
            name='vlarip',
            field=models.CharField(default='', max_length=198),
        ),
    ]
