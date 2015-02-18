# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qqpppzas', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lrqwbz',
            name='gqbcodrudr',
        ),
        migrations.AddField(
            model_name='lrqwbz',
            name='aetyruy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ybcxw',
            name='qbpbr',
            field=models.CharField(default='', max_length=244),
        ),
    ]
