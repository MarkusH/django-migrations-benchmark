# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0018_auto_20150218_1630'),
        ('rrmdjc', '0009_remove_guhhjm_ehzyfcfm'),
        ('pnxyvqx', '0012_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aehywz',
            name='znmxhx',
        ),
        migrations.RemoveField(
            model_name='ecatm',
            name='kbkjjed',
        ),
        migrations.AddField(
            model_name='aehywz',
            name='ujiftttgv',
            field=models.OneToOneField(null=True, related_name='+', to='burhjvc.Pdzdhpq'),
        ),
        migrations.AddField(
            model_name='ecatm',
            name='qqhiw',
            field=models.OneToOneField(null=True, related_name='+', to='rrmdjc.Gxoqulk'),
        ),
    ]
