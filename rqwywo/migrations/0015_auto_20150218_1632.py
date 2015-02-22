# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqwywo', '0014_auto_20150218_1631'),
    ]

    run_before = [
        ('cohutfvb', '0016_auto_20150218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gkiwtx',
            name='pwsnbpros',
        ),
        migrations.RemoveField(
            model_name='wmvmz',
            name='xpvpigphfl',
        ),
        migrations.AddField(
            model_name='wmvmz',
            name='cakit',
            field=models.CharField(default='', max_length=20),
        ),
    ]
