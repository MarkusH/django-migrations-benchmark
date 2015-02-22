# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adlorvp', '0004_afyxxcmzds_wobjqpykka'),
    ]

    run_before = [
        ('kfapsax', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kzrfnfxko',
            name='rfezjxndz',
        ),
        migrations.AddField(
            model_name='kzrfnfxko',
            name='rcqudvnf',
            field=models.IntegerField(default=0),
        ),
    ]
