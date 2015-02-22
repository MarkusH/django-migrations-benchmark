# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0015_auto_20150218_1627'),
    ]

    run_before = [
        ('irmtbds', '0009_delete_bemqls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lqfdippdc',
            name='cjqbkmmoe',
        ),
    ]
