# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nzfoyhj',
            name='hwflnm',
        ),
        migrations.AddField(
            model_name='edynlg',
            name='ghfqson',
            field=models.CharField(default='', max_length=21),
        ),
    ]
