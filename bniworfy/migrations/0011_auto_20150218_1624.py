# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bniworfy', '0010_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mxfnrc',
            name='vwngisguf',
        ),
        migrations.DeleteModel(
            name='Mxfnrc',
        ),
    ]
