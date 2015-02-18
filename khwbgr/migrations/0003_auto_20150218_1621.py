# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0002_fetzvwamur_zcpwhzgg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fetzvwamur',
            name='zcpwhzgg',
        ),
        migrations.DeleteModel(
            name='Fetzvwamur',
        ),
    ]
