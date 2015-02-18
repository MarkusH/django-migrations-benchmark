# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adlorvp', '0015_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bauxko',
            name='mjgvx',
        ),
        migrations.AddField(
            model_name='bauxko',
            name='wmvyhrhbsm',
            field=models.IntegerField(default=0),
        ),
    ]
