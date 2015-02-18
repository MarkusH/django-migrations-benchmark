# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qqpppzas', '0004_auto_20150218_1621'),
        ('joavhqi', '0004_auto_20150218_1621'),
        ('zngxahi', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orofu',
            name='ciuhnrivc',
        ),
        migrations.AddField(
            model_name='nnkqr',
            name='tecbgms',
            field=models.OneToOneField(null=True, related_name='+', to='joavhqi.Lfssmpr'),
        ),
        migrations.AddField(
            model_name='orofu',
            name='liqkyjd',
            field=models.OneToOneField(null=True, related_name='+', to='qqpppzas.Vdscpy'),
        ),
    ]
