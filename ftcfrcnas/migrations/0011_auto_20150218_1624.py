# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0007_auto_20150218_1624'),
        ('ftcfrcnas', '0010_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrwqtj',
            name='ssdfr',
        ),
        migrations.RemoveField(
            model_name='wjxepwd',
            name='grpthucwr',
        ),
        migrations.AddField(
            model_name='qrwqtj',
            name='xoazccbco',
            field=models.ForeignKey(null=True, related_name='+', to='gcyjx.Nmbztrlh'),
        ),
        migrations.AddField(
            model_name='wjxepwd',
            name='nridz',
            field=models.CharField(default='', max_length=134),
        ),
    ]
