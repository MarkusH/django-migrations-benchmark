# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adlorvp', '0012_remove_afyxxcmzds_nfvueppp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afyxxcmzds',
            name='wobjqpykka',
        ),
        migrations.RemoveField(
            model_name='kmygwyorsi',
            name='albva',
        ),
        migrations.AddField(
            model_name='afyxxcmzds',
            name='webvuzv',
            field=models.CharField(default='', max_length=20),
        ),
    ]
