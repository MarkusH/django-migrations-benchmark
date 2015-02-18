# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zngxahi', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qahkfonewx',
            name='sdxgci',
        ),
        migrations.AddField(
            model_name='qahkfonewx',
            name='slyww',
            field=models.IntegerField(default=0),
        ),
    ]
