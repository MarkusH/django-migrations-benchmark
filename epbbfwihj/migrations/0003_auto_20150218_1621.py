# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrmdjc', '0002_guhhjm_ixxlcmb'),
        ('epbbfwihj', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gejrsf',
            name='zyxxzvs',
        ),
        migrations.AddField(
            model_name='gejrsf',
            name='wnttrpau',
            field=models.OneToOneField(null=True, related_name='+', to='rrmdjc.Rtbkg'),
        ),
        migrations.AddField(
            model_name='zfpgchkbaz',
            name='zgdobd',
            field=models.IntegerField(default=0),
        ),
    ]
