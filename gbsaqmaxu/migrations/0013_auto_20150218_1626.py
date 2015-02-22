# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbsaqmaxu', '0012_auto_20150218_1625'),
    ]

    run_before = [
        ('ygnakzgjxu', '0008_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nhlpe',
            name='mcctecfjs',
        ),
        migrations.AddField(
            model_name='nhlpe',
            name='vcwskrliy',
            field=models.CharField(default='', max_length=139),
        ),
    ]
