# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0009_auto_20150218_1623'),
        ('gtfgy', '0008_auto_20150218_1622'),
    ]

    run_before = [
        ('khwbgr', '0006_auto_20150218_1623'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Zbbwyog',
        ),
        migrations.RemoveField(
            model_name='yrekcfrkl',
            name='vgwig',
        ),
        migrations.AddField(
            model_name='rykamine',
            name='ueuzllk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='yrekcfrkl',
            name='tidjkv',
            field=models.ForeignKey(null=True, related_name='+', to='ftcfrcnas.Myohdht'),
        ),
    ]
