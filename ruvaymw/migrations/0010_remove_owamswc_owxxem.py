# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0009_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owamswc',
            name='owxxem',
        ),
    ]
