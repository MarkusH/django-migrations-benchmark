# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0009_auto_20150218_1631'),
        ('pnxyvqx', '0013_auto_20150218_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rwrraj',
            name='qcbtpghkq',
        ),
        migrations.AddField(
            model_name='aehywz',
            name='nzufecwivy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nenfvguk',
            name='mpogohi',
            field=models.ForeignKey(null=True, related_name='+', to='ygnakzgjxu.Xdwhlpqgw'),
        ),
    ]
