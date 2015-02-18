# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0006_auto_20150218_1623'),
        ('qclaxc', '0009_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yiifw',
            name='thlbyuu',
        ),
        migrations.AddField(
            model_name='yiifw',
            name='deekrnqng',
            field=models.OneToOneField(null=True, related_name='+', to='khwbgr.Bwshcnprcg'),
        ),
    ]
