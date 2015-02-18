# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0007_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yxsnty',
            name='bcknzwc',
        ),
        migrations.AddField(
            model_name='yxsnty',
            name='hytuumyfek',
            field=models.CharField(default='', max_length=33),
        ),
    ]
