# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubuhm',
            name='qbjla',
        ),
        migrations.DeleteModel(
            name='Ubuhm',
        ),
    ]
