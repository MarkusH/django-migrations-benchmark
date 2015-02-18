# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0002_ivcsuscyb_zdkop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ivcsuscyb',
            name='lypce',
        ),
        migrations.DeleteModel(
            name='Ivcsuscyb',
        ),
    ]
