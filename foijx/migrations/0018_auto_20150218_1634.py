# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0017_remove_abmhnczd_nflur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abmhnczd',
            name='wdlblsubi',
        ),
        migrations.DeleteModel(
            name='Abmhnczd',
        ),
    ]
