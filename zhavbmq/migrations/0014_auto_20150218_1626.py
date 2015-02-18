# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0013_auto_20150218_1625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Yqtbfv',
        ),
        migrations.RemoveField(
            model_name='rywmfrbmil',
            name='hhpchb',
        ),
        migrations.AddField(
            model_name='murrsbmz',
            name='sivjfg',
            field=models.CharField(default='', max_length=146),
        ),
    ]
