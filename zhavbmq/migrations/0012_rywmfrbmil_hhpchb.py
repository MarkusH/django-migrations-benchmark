# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0006_auto_20150218_1623'),
        ('zhavbmq', '0011_auto_20150218_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='rywmfrbmil',
            name='hhpchb',
            field=models.OneToOneField(null=True, related_name='+', to='khwbgr.Bwshcnprcg'),
        ),
    ]
