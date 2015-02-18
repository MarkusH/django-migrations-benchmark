# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0017_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myohdht',
            name='vwrrbmxs',
        ),
        migrations.AddField(
            model_name='myohdht',
            name='nrkvvcx',
            field=models.CharField(default='', max_length=170),
        ),
    ]
