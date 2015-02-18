# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0004_mfivvxhds_erclh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mfivvxhds',
            name='erclh',
        ),
        migrations.DeleteModel(
            name='Mfivvxhds',
        ),
    ]
