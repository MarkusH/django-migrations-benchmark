# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0009_auto_20150218_1625'),
    ]

    run_before = [
        ('kakry', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gmclwtufhi',
            name='jdwqs',
        ),
        migrations.RemoveField(
            model_name='jkjvvohe',
            name='kjeun',
        ),
    ]
