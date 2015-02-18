# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0015_auto_20150218_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crzqih',
            name='nenil',
        ),
        migrations.RemoveField(
            model_name='crzqih',
            name='uanao',
        ),
        migrations.DeleteModel(
            name='Crzqih',
        ),
    ]
