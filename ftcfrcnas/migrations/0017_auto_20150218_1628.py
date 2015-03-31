# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0016_remove_lqfdippdc_cjqbkmmoe'),
    ]

    run_before = [
        ('rqwywo', '0012_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myohdht',
            name='vaeutfp',
        ),
        migrations.RemoveField(
            model_name='qrwqtj',
            name='xoazccbco',
        ),
        migrations.AddField(
            model_name='myohdht',
            name='vwrrbmxs',
            field=models.CharField(default='', max_length=167),
        ),
        migrations.AddField(
            model_name='qrwqtj',
            name='tidplepk',
            field=models.CharField(default='', max_length=28),
        ),
    ]
