# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiupu', '0002_delete_jpmwh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fzmiecxuo',
            name='wpvqrrkg',
        ),
        migrations.DeleteModel(
            name='Fzmiecxuo',
        ),
    ]
