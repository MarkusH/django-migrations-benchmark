# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bniworfy', '0006_sbfynkpvu_txgmuotqrn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hqjqgiq',
            name='rzndbtb',
        ),
        migrations.AddField(
            model_name='hqjqgiq',
            name='uloiryanki',
            field=models.IntegerField(default=0),
        ),
    ]
