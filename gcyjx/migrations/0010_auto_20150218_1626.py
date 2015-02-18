# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0009_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snjsz',
            name='qsntdomu',
        ),
        migrations.DeleteModel(
            name='Snjsz',
        ),
    ]
