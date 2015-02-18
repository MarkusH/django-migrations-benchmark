# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epbbfwihj', '0007_auto_20150218_1622'),
        ('digmcd', '0008_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='untgafvod',
            name='upmuq',
        ),
        migrations.AddField(
            model_name='lemzs',
            name='nvjgsjcee',
            field=models.ForeignKey(null=True, related_name='+', to='epbbfwihj.Zfpgchkbaz'),
        ),
        migrations.AddField(
            model_name='rdfrrg',
            name='nkkfvqupui',
            field=models.CharField(default='', max_length=180),
        ),
    ]
