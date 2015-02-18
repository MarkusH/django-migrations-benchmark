# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0016_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hhnwphllci',
            name='lgfcdtfmmh',
        ),
        migrations.RemoveField(
            model_name='ylhrvymeyk',
            name='qjehrn',
        ),
        migrations.AddField(
            model_name='hhnwphllci',
            name='fbjvih',
            field=models.CharField(default='', max_length=135),
        ),
        migrations.AddField(
            model_name='ylhrvymeyk',
            name='zadqslz',
            field=models.CharField(default='', max_length=240),
        ),
    ]
