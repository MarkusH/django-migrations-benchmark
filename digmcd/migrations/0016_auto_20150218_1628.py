# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0015_auto_20150218_1628'),
        ('digmcd', '0015_auto_20150218_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='krbaxhjpkp',
            name='jqqic',
        ),
        migrations.RemoveField(
            model_name='lemzs',
            name='nvjgsjcee',
        ),
        migrations.RemoveField(
            model_name='mqnavvvb',
            name='cvopda',
        ),
        migrations.AddField(
            model_name='krbaxhjpkp',
            name='rzllxxpr',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='lemzs',
            name='csflnkvdne',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mqnavvvb',
            name='qguzrxggsd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='xmvhvzui',
            name='tffnbk',
            field=models.ForeignKey(null=True, related_name='+', to='uivaguf.Zwjgfcdi'),
        ),
    ]
