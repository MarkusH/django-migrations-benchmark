# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0005_sehvi_wkpzco'),
    ]

    run_before = [
        ('cuspknbh', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sehvi',
            name='wkpzco',
        ),
        migrations.AddField(
            model_name='sehvi',
            name='ywngrzbcq',
            field=models.CharField(default='', max_length=168),
        ),
    ]
