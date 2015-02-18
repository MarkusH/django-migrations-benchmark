# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zngxahi', '0006_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qahkfonewx',
            name='slyww',
        ),
        migrations.AddField(
            model_name='orofu',
            name='xewlv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qahkfonewx',
            name='gwrlr',
            field=models.IntegerField(default=0),
        ),
    ]
