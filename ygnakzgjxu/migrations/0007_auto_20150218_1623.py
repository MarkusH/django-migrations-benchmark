# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0006_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xdwhlpqgw',
            name='cepyeeaw',
        ),
        migrations.AddField(
            model_name='xdwhlpqgw',
            name='potlucvgl',
            field=models.IntegerField(default=0),
        ),
    ]
