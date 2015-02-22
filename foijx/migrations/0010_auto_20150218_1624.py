# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0009_auto_20150218_1623'),
    ]

    run_before = [
        ('burhjvc', '0015_auto_20150218_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wrafoshzom',
            name='gzayhaq',
        ),
        migrations.RemoveField(
            model_name='wrafoshzom',
            name='qqpfdtng',
        ),
        migrations.RemoveField(
            model_name='qrwsj',
            name='tbcua',
        ),
        migrations.DeleteModel(
            name='Wrafoshzom',
        ),
    ]
