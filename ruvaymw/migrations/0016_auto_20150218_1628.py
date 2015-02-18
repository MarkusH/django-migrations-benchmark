# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0015_ndhcup_buhiucccq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ndhcup',
            name='buhiucccq',
        ),
        migrations.RemoveField(
            model_name='ndhcup',
            name='udvzu',
        ),
        migrations.DeleteModel(
            name='Ndhcup',
        ),
    ]
