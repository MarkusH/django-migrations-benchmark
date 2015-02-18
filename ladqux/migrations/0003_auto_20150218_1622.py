# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladqux', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oeyhu',
            name='yzqcicylut',
        ),
        migrations.AddField(
            model_name='oeyhu',
            name='chhwiag',
            field=models.CharField(default='', max_length=58),
        ),
    ]
