# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladqux', '0001_initial'),
        ('gtfgy', '0001_initial'),
        ('khwbgr', '0001_initial'),
        ('rrmdjc', '0001_initial'),
    ]

    run_before = [
        ('khwbgr', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='xqcngusl',
            name='vgeuicxo',
            field=models.OneToOneField(null=True, related_name='+', to='khwbgr.Qsqcspjrgx'),
        ),
        migrations.AddField(
            model_name='xlaxaa',
            name='etvtohrz',
            field=models.OneToOneField(null=True, related_name='+', to='rrmdjc.Gxoqulk'),
        ),
        migrations.AddField(
            model_name='rykamine',
            name='ofjjiorcjg',
            field=models.OneToOneField(null=True, related_name='+', to='ladqux.Yxjjlex'),
        ),
    ]
