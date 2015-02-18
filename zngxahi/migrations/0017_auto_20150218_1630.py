# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0009_auto_20150218_1628'),
        ('zngxahi', '0016_auto_20150218_1628'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Qmhypaufcg',
        ),
        migrations.RemoveField(
            model_name='orofu',
            name='liqkyjd',
        ),
        migrations.AddField(
            model_name='eauslyif',
            name='nteiooiikw',
            field=models.OneToOneField(null=True, related_name='+', to='wulegwfs.Txgqxz'),
        ),
        migrations.AddField(
            model_name='nnkqr',
            name='eczmitq',
            field=models.CharField(default='', max_length=7),
        ),
    ]
