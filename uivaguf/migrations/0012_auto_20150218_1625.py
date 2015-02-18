# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0011_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onmti',
            name='emaio',
        ),
        migrations.RemoveField(
            model_name='onmti',
            name='vcevpdll',
        ),
        migrations.AddField(
            model_name='ubuhm',
            name='lnfxbtie',
            field=models.IntegerField(default=0),
        ),
    ]
