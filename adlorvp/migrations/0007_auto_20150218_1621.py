# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adlorvp', '0006_auto_20150218_1621'),
    ]

    run_before = [
        ('khwbgr', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kmygwyorsi',
            name='shkjv',
        ),
        migrations.RemoveField(
            model_name='kzrfnfxko',
            name='rcqudvnf',
        ),
        migrations.AddField(
            model_name='kmygwyorsi',
            name='zvqajqzsmi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kzrfnfxko',
            name='fmvbwiqgc',
            field=models.CharField(default='', max_length=52),
        ),
    ]
