# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0014_remove_jydvnf_xwilqwztoj'),
    ]

    run_before = [
        ('qclaxc', '0015_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gbmslrhm',
            name='wftcam',
        ),
        migrations.AddField(
            model_name='gbmslrhm',
            name='ezrgxhh',
            field=models.IntegerField(default=0),
        ),
    ]
