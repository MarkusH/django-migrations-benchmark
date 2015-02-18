# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qclaxc', '0008_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pmcbxoetr',
            name='npfpduxdlb',
        ),
        migrations.AddField(
            model_name='pmcbxoetr',
            name='bmltheez',
            field=models.CharField(default='', max_length=16),
        ),
    ]
