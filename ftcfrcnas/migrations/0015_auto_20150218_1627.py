# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqwywo', '0010_auto_20150218_1627'),
        ('ftcfrcnas', '0014_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myohdht',
            name='lybemykxx',
        ),
        migrations.AddField(
            model_name='lqfdippdc',
            name='zuydaednz',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myohdht',
            name='vaeutfp',
            field=models.ForeignKey(null=True, related_name='+', to='rqwywo.Xaszfxobvf'),
        ),
    ]
