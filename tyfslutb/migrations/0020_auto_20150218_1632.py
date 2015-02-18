# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyfslutb', '0019_auto_20150218_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qcwbo',
            name='helryvwow',
        ),
        migrations.AddField(
            model_name='qcwbo',
            name='gepbdooj',
            field=models.IntegerField(default=0),
        ),
    ]
