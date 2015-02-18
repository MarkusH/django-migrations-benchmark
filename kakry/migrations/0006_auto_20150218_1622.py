# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etnevwmkj', '0004_auto_20150218_1622'),
        ('kakry', '0005_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wnbhmzvze',
            name='mltbxn',
        ),
        migrations.AddField(
            model_name='ajbkovws',
            name='kmhhp',
            field=models.ForeignKey(null=True, related_name='+', to='etnevwmkj.Ryfwmkefy'),
        ),
        migrations.AddField(
            model_name='wnbhmzvze',
            name='lmtij',
            field=models.IntegerField(default=0),
        ),
    ]
