# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bniworfy', '0007_auto_20150218_1622'),
    ]

    run_before = [
        ('ysgxuyu', '0005_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gsmbfohda',
            name='xtcnijqs',
        ),
        migrations.RemoveField(
            model_name='mxfnrc',
            name='ifxub',
        ),
        migrations.RemoveField(
            model_name='sbfynkpvu',
            name='inzqctzh',
        ),
        migrations.AddField(
            model_name='gsmbfohda',
            name='gxvwzvtps',
            field=models.CharField(default='', max_length=90),
        ),
    ]
