# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbsaqmaxu', '0014_auto_20150218_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhlpe',
            name='afpyhakre',
            field=models.CharField(default='', max_length=204),
        ),
    ]
