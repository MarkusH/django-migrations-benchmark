# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyfslutb', '0015_auto_20150218_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfdhb',
            name='jhuhmbj',
        ),
        migrations.AddField(
            model_name='qhzppcqwku',
            name='ikycuom',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rfdhb',
            name='pcnnq',
            field=models.IntegerField(default=0),
        ),
    ]
