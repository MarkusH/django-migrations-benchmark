# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0012_zaganduq_plaqa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zaganduq',
            name='plaqa',
        ),
    ]
