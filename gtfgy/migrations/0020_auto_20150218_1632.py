# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfgy', '0019_auto_20150218_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symqs',
            name='cdcocpyto',
        ),
        migrations.RemoveField(
            model_name='symqs',
            name='cuean',
        ),
        migrations.DeleteModel(
            name='Symqs',
        ),
    ]
