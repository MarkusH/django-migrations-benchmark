# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0008_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='murrsbmz',
            name='lsdctjp',
        ),
        migrations.AddField(
            model_name='murrsbmz',
            name='guuexjxd',
            field=models.IntegerField(default=0),
        ),
    ]
