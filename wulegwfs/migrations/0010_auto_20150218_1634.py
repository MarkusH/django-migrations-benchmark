# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0009_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='txgqxz',
            name='mhptuwb',
        ),
        migrations.AddField(
            model_name='txgqxz',
            name='kcqlpb',
            field=models.IntegerField(default=0),
        ),
    ]
