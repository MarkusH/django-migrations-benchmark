# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0010_remove_owamswc_owxxem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owamswc',
        ),
    ]
